from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    print("ERROR: ANTHROPIC_API_KEY was not found. Check your .env file.")
    exit()

client = Anthropic(api_key=api_key)

topic = input("Enter your research topic: ")

prompt = f"""
You are a helpful academic research assistant.

Topic: {topic}

Please produce:
1. A simple explanation of the topic.
2. Three possible research questions.
3. Three possible journal article titles.
4. One practical application for agriculture, food security, or postharvest systems.

Keep the response clear, practical, and beginner-friendly.
"""

try:
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        temperature=0.3,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("\nCLAUDE RESPONSE:\n")
    print(response.content[0].text)

except Exception as e:
    print("\nSomething went wrong:\n")
    print(e)