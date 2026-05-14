from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

topic = input("Enter your research topic: ")

prompt = f"""
You are a helpful academic research assistant.

Topic: {topic}

Please produce:
1. A simple explanation of the topic.
2. Three possible research questions.
3. Three possible journal article titles.
4. One practical application for agriculture, food security, or postharvest systems.

Keep the response clear and beginner-friendly.
"""

response = client.responses.create(
    model="gpt-5.5",
    input=prompt
)

print(response.output_text)