from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    print("ERROR: ANTHROPIC_API_KEY was not found. Check your .env file.")
    exit()

client = Anthropic(api_key=api_key)

MODEL_NAME = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5")

system_prompt = """
You are ResearchLab AI, a helpful academic research assistant for Professor Ola.

Your role:
- Help develop research ideas, manuscripts, concept notes, grant ideas, and research strategies.
- Focus especially on postharvest technology, horticulture, food security, climate resilience, indigenous crops, edible coatings, warm-chain systems, and sustainable agriculture.
- Ask clarifying questions when the user is vague.
- Keep responses practical, structured, and academically useful.
- Do not invent citations or fake references.
- If evidence is needed, say that verification is required.
- Avoid overclaiming.
"""

messages = []

print("\nResearchLab AI Chat Assistant")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "stop"]:
        print("ResearchLab AI: Session ended. Good work, Professor.")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=1200,
            temperature=0.4,
            system=system_prompt,
            messages=messages
        )

        assistant_reply = response.content[0].text

        print("\nResearchLab AI:")
        print(assistant_reply)
        print()

        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

    except Exception as e:
        print("\nSomething went wrong:")
        print(e)
        print()