# --------------------------------------------------
# Lesson 09 Build 1: Research Image Prompt Builder
# Microsoft Generative AI for Beginners adaptation
# Focus: image generation prompts + meta prompt boundaries
# --------------------------------------------------

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


print("\nResearch Image Prompt Builder")
print("Lesson 09: Building Image Generation Applications")
print("Type 'exit' anytime to stop.\n")

while True:
    topic = input("Enter image topic: ")

    if topic.lower().strip() in ["exit", "quit", "stop"]:
        print("Prompt builder ended.")
        break

    purpose = input("Enter image purpose, for example LinkedIn post, journal figure, grant proposal visual: ")
    key_elements = input("Enter key visual elements to include: ")
    image_type = input("Enter image type, for example scientific diagram, thumbnail, poster, concept art: ")
    audience = input("Enter target audience, for example researchers, students, farmers, funders: ")
    style = input("Enter preferred style, for example minimalist, realistic, cinematic, BioRender-style: ")
    orientation = input("Enter orientation, for example square, landscape 16:9, portrait: ")

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
    print("\n" + "=" * 100 + "\n")