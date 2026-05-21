from pathlib import Path
from datetime import datetime


def build_meta_prompt(image_type, audience, style, orientation):
    """
    Create a meta prompt that defines boundaries for the image generation task.
    """

    disallow_list = [
        "violence",
        "blood",
        "gore",
        "nudity",
        "sexual content",
        "adult content",
        "hate symbols",
        "misleading scientific claims",
        "fake logos",
        "unreadable text",
        "distorted human anatomy",
        "cluttered layout"
    ]

    meta_prompt = f"""
You are an expert visual designer creating images for academic, educational, and professional communication.

Image type: {image_type}
Target audience: {audience}
Preferred style: {style}
Orientation: {orientation}

The image must:
- Be safe for professional and educational use.
- Be visually clear and not cluttered.
- Avoid fake logos, unreadable text, and misleading scientific claims.
- Use clean composition and strong visual hierarchy.
- Match the intended audience and communication purpose.
- Avoid the following: {", ".join(disallow_list)}.
"""
    return meta_prompt.strip()


def build_research_prompt(topic, purpose, key_elements, image_type, audience, style, orientation):
    """
    Build a complete image generation prompt from user inputs.
    """

    meta_prompt = build_meta_prompt(image_type, audience, style, orientation)

    final_prompt = f"""
{meta_prompt}

Create an image about:

Topic:
{topic}

Purpose:
{purpose}

Key visual elements to include:
{key_elements}

Final image requirements:
- Make the image suitable for academic, research, or professional communication.
- Use a clean, polished, high-quality composition.
- Use realistic and scientifically respectful visual logic.
- Avoid unnecessary decorative elements.
- If text is needed, keep it minimal and readable.
- Do not include fake references, fake journal names, or fake institutional logos.

Write the final image as a detailed image generation prompt.
"""
    return final_prompt.strip()


def safe_filename(text):
    """
    Convert text into a simple safe filename.
    """
    cleaned = "".join(char if char.isalnum() or char in (" ", "-", "_") else "" for char in text)
    cleaned = "_".join(cleaned.strip().split())
    return cleaned[:60] if cleaned else "image_prompt"


print("\nResearch Image Prompt Saver")
print("Lesson 09: Build 2")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "saved_prompts"
output_dir.mkdir(exist_ok=True)

while True:
    topic = input("Enter image topic: ")

    if topic.lower().strip() in ["exit", "quit", "stop"]:
        print("Prompt saver ended.")
        break

    purpose = input("Enter image purpose: ")
    key_elements = input("Enter key visual elements to include: ")
    image_type = input("Enter image type: ")
    audience = input("Enter target audience: ")
    style = input("Enter preferred style: ")
    orientation = input("Enter orientation: ")

    prompt = build_research_prompt(
        topic=topic,
        purpose=purpose,
        key_elements=key_elements,
        image_type=image_type,
        audience=audience,
        style=style,
        orientation=orientation
    )

    print("\nGenerated Image Prompt:\n")
    print(prompt)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{safe_filename(topic)}.txt"
    file_path = output_dir / filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(prompt)

    print(f"\nPrompt saved to:\n{file_path}")
    print("\n" + "=" * 100 + "\n")