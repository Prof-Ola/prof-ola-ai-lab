from pathlib import Path
from datetime import datetime


def safe_filename(text):
    cleaned = "".join(char if char.isalnum() or char in (" ", "-", "_") else "" for char in text)
    cleaned = "_".join(cleaned.strip().split())
    return cleaned[:70] if cleaned else "scientific_figure_prompt"


def build_scientific_meta_prompt(figure_type, target_style, orientation):
    disallow_list = [
        "decorative clutter",
        "fake data",
        "fake references",
        "fake logos",
        "unreadable labels",
        "misleading scientific claims",
        "exaggerated effects",
        "messy layout",
        "low-resolution style",
        "photorealistic human faces unless requested"
    ]

    meta_prompt = f"""
You are an expert scientific illustrator and academic figure designer.

Figure type: {figure_type}
Target visual style: {target_style}
Orientation: {orientation}

The figure must:
- Be suitable for a peer-reviewed academic journal.
- Use a clean white background unless another background is explicitly requested.
- Use a clear visual hierarchy.
- Use minimal, readable text labels.
- Avoid unnecessary icons and decorative elements.
- Represent scientific relationships accurately and cautiously.
- Avoid fake data, fake references, fake journal names, and fake institutional logos.
- Avoid the following: {", ".join(disallow_list)}.
"""
    return meta_prompt.strip()


def build_scientific_figure_prompt(
    topic,
    figure_type,
    main_message,
    components,
    layout,
    target_style,
    colour_preference,
    labels,
    orientation
):
    meta_prompt = build_scientific_meta_prompt(
        figure_type=figure_type,
        target_style=target_style,
        orientation=orientation
    )

    final_prompt = f"""
{meta_prompt}

Create a scientific figure about:

Topic:
{topic}

Main scientific message:
{main_message}

Key components or processes to show:
{components}

Preferred layout:
{layout}

Colour preference:
{colour_preference}

Text labels to include:
{labels}

Detailed figure requirements:
- Make the design publication-ready.
- Use clean lines, balanced spacing, and logical flow.
- Make relationships between components visually clear.
- Use arrows only where they clarify direction, cause, sequence, or flow.
- Do not overcrowd the figure.
- Do not use decorative shadows, textures, gradients, or unnecessary 3D effects.
- Keep all labels concise and readable.
- Use a professional scientific illustration style.
- The output should be written as a detailed image generation prompt.
"""
    return final_prompt.strip()


print("\nScientific Figure Prompt Generator")
print("Lesson 09: Build 3")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "saved_figure_prompts"
output_dir.mkdir(exist_ok=True)

while True:
    topic = input("Enter figure topic: ")

    if topic.lower().strip() in ["exit", "quit", "stop"]:
        print("Scientific figure prompt generator ended.")
        break

    figure_type = input("Enter figure type, for example conceptual diagram, graphical abstract, workflow diagram: ")
    main_message = input("Enter main scientific message: ")
    components = input("Enter key components or processes to show: ")
    layout = input("Enter preferred layout, for example left-to-right flow, layered pyramid, circular system: ")
    target_style = input("Enter target style, for example Q1 journal minimalist, BioRender-style, Elsevier-style: ")
    colour_preference = input("Enter colour preference, for example teal and gold, neutral grey, colour-blind safe palette: ")
    labels = input("Enter text labels to include: ")
    orientation = input("Enter orientation, for example landscape 16:9, square, portrait: ")

    prompt = build_scientific_figure_prompt(
        topic=topic,
        figure_type=figure_type,
        main_message=main_message,
        components=components,
        layout=layout,
        target_style=target_style,
        colour_preference=colour_preference,
        labels=labels,
        orientation=orientation
    )

    print("\nGenerated Scientific Figure Prompt:\n")
    print(prompt)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{safe_filename(topic)}.txt"
    file_path = output_dir / filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(prompt)

    print(f"\nScientific figure prompt saved to:\n{file_path}")
    print("\n" + "=" * 100 + "\n")