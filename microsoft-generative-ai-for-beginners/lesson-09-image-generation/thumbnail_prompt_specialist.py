from pathlib import Path
from datetime import datetime


# --------------------------------------------------
# Lesson 09 Build 4: Thumbnail Prompt Specialist
# Purpose: Generate polished thumbnail prompts for LinkedIn,
# FRIN, Future-Ready Weekly, research communication, and academic branding.
# --------------------------------------------------


def safe_filename(text):
    cleaned = "".join(char if char.isalnum() or char in (" ", "-", "_") else "" for char in text)
    cleaned = "_".join(cleaned.strip().split())
    return cleaned[:70] if cleaned else "thumbnail_prompt"


def build_thumbnail_meta_prompt(platform, brand_style, orientation):
    disallow_list = [
        "cluttered composition",
        "fake logos",
        "fake institutional emblems",
        "unreadable text",
        "random letters",
        "misleading scientific claims",
        "excessive decoration",
        "low-resolution look",
        "distorted faces",
        "visual noise",
        "violence",
        "nudity",
        "adult content",
        "hate symbols"
    ]

    meta_prompt = f"""
You are an expert editorial art director and thumbnail designer for academic, professional, and educational communication.

Platform or use case: {platform}
Brand style: {brand_style}
Orientation: {orientation}

The thumbnail must:
- Be professional, clean, and visually striking.
- Use strong hierarchy with one clear focal idea.
- Use minimal readable text only if needed.
- Avoid clutter and unnecessary decoration.
- Avoid fake logos, fake institutional emblems, fake journal names, and fake references.
- Avoid unreadable or gibberish text.
- Be suitable for LinkedIn, newsletters, academic communication, or professional education.
- Avoid the following: {", ".join(disallow_list)}.
"""
    return meta_prompt.strip()


def build_thumbnail_prompt(
    topic,
    headline,
    audience,
    purpose,
    key_visuals,
    platform,
    brand_style,
    colour_palette,
    mood,
    orientation
):
    meta_prompt = build_thumbnail_meta_prompt(
        platform=platform,
        brand_style=brand_style,
        orientation=orientation
    )

    final_prompt = f"""
{meta_prompt}

Create a premium thumbnail image about:

Topic:
{topic}

Main headline or text:
{headline}

Purpose:
{purpose}

Target audience:
{audience}

Key visual elements:
{key_visuals}

Colour palette:
{colour_palette}

Mood or emotional tone:
{mood}

Detailed thumbnail requirements:
- Make the image suitable for high-performing educational and professional content.
- Use a clean editorial layout with strong contrast and clear visual direction.
- Use one dominant focal point and avoid overcrowding.
- If text is included, keep it short, bold, and readable.
- Use modern academic/professional design language.
- Use polished lighting, balanced spacing, and premium composition.
- Avoid cartoonish effects unless explicitly requested.
- Avoid fake logos, fake text, and misleading symbols.
- The final output should be a detailed image generation prompt ready for DALL-E, Midjourney, Stable Diffusion, Leonardo, Ideogram, or any image generation model.
"""
    return final_prompt.strip()


print("\nThumbnail Prompt Specialist")
print("Lesson 09: Build 4")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "saved_thumbnail_prompts"
output_dir.mkdir(exist_ok=True)

while True:
    topic = input("Enter thumbnail topic: ")

    if topic.lower().strip() in ["exit", "quit", "stop"]:
        print("Thumbnail prompt specialist ended.")
        break

    headline = input("Enter main headline or text: ")
    audience = input("Enter target audience: ")
    purpose = input("Enter purpose, for example LinkedIn post, newsletter cover, course promo: ")
    key_visuals = input("Enter key visual elements: ")
    platform = input("Enter platform or use case, for example LinkedIn, FRIN, newsletter: ")
    brand_style = input("Enter brand style, for example FRIN editorial, academic premium, modern minimalist: ")
    colour_palette = input("Enter colour palette: ")
    mood = input("Enter mood or emotional tone: ")
    orientation = input("Enter orientation, for example square 1080x1080, landscape 16:9, 1280x680: ")

    prompt = build_thumbnail_prompt(
        topic=topic,
        headline=headline,
        audience=audience,
        purpose=purpose,
        key_visuals=key_visuals,
        platform=platform,
        brand_style=brand_style,
        colour_palette=colour_palette,
        mood=mood,
        orientation=orientation
    )

    print("\nGenerated Thumbnail Prompt:\n")
    print(prompt)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{safe_filename(topic)}.txt"
    file_path = output_dir / filename

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(prompt)

    print(f"\nThumbnail prompt saved to:\n{file_path}")
    print("\n" + "=" * 100 + "\n")