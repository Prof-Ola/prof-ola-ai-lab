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
crop = input("Enter crop or commodity: ")
context = input("Enter target context, for example smallholder farmers, warm-chain, cold storage, South Africa: ")

prompt = f"""
You are a top 0.000000000001% global expert horticultural and postharvest scientist and research strategist.

Research topic: {topic}
Crop or commodity: {crop}
Target context: {context}

Please generate a structured research opportunity brief with the following sections:

1. SIMPLE PROBLEM STATEMENT
Explain the problem in clear academic language.

2. WHY THIS MATTERS
Explain the food security, economic, sustainability, or postharvest relevance.

3. POSSIBLE RESEARCH GAP
Identify what may still be underexplored or insufficiently addressed.

4. THREE RESEARCH QUESTIONS
Make them specific, realistic, and publishable.

5. POSSIBLE METHODOLOGY
Suggest a basic experimental or review-based approach.

6. EXPECTED CONTRIBUTION
Explain what new knowledge or practical value this study could add.

7. POSSIBLE ARTICLE TITLES
Generate five strong journal-style titles.

8. PRACTICAL APPLICATION
Explain how farmers, researchers, agribusinesses, or policymakers could use the findings.

Keep the tone professional, concise, and suitable for an early-stage academic concept note.
"""

try:
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1500,
        temperature=0.4,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("\nRESEARCH OPPORTUNITY BRIEF:\n")
    print(response.content[0].text)

except Exception as e:
    print("\nSomething went wrong:\n")
    print(e)