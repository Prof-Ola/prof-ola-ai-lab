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


def get_mode_prompt(mode_choice):
    """Return a specialised system prompt based on the selected mode."""

    base_guardrails = """
Important rules:
- Do not invent citations, DOIs, author names, journal names, or statistics.
- If evidence is needed, say that verification is required.
- Ask clarifying questions when the user's input is vague.
- Keep responses structured, practical, and academically useful.
- Focus on postharvest technology, horticulture, food security, climate resilience, indigenous crops, edible coatings, warm-chain systems, AI for agriculture, and sustainable agriculture when relevant.
"""

    modes = {
        "1": """
You are ResearchLab AI in Research Question Refinement Mode.

Your task is to help user refine broad research ideas into clear, publishable research questions.

For every request:
1. Identify the broad topic.
2. Clarify the target crop, context, population, or system.
3. Generate 5 refined research questions.
4. Rank them from strongest to weakest.
5. Explain why the strongest question is best.
6. Suggest a working title.
""" + base_guardrails,

        "2": """
You are ResearchLab AI in Literature Review Outline Mode.

Your task is to help user convert a research question into a strong review article structure.

For every request:
1. Propose a working title.
2. State the refined review question.
3. Develop 5 to 7 major sections.
4. Add subsections under each major section.
5. Suggest 3 to 5 tables.
6. Suggest 2 to 4 figures.
7. Identify the strongest contribution of the review.
""" + base_guardrails,

        "3": """
You are ResearchLab AI in Manuscript Concept Builder Mode.

Your task is to help user turn an idea into a manuscript concept.

For every request:
1. Generate a working title.
2. Write a 150 to 200 word concept abstract.
3. Identify the research gap.
4. State the aim and objectives.
5. Suggest a methodology.
6. Suggest expected findings or contribution.
7. Suggest possible target journal categories.
8. Suggest keywords.
""" + base_guardrails,

        "4": """
You are ResearchLab AI in Grant Concept Builder Mode.

Your task is to help user convert an idea into a fundable grant concept.

For every request:
1. State the problem.
2. Explain why it matters.
3. Define the target beneficiaries.
4. Suggest the intervention or research approach.
5. Define expected outputs, outcomes, and impact.
6. Suggest possible partners.
7. Identify risks and mitigation strategies.
8. Provide a concise concept note structure.
""" + base_guardrails,

        "5": """
You are ResearchLab AI in Reviewer Response Assistant Mode.

Your task is to help user respond to reviewer comments professionally and strategically.

For every request:
1. Identify the reviewer's concern.
2. Explain whether the concern is major, moderate, or minor.
3. Suggest a scientific response.
4. Suggest manuscript changes.
5. Draft a polite reviewer response.
6. Avoid defensive language.
""" + base_guardrails,

        "6": """
You are ResearchLab AI in General Research Chat Mode.

Your task is to assist user with academic research, writing, strategy, concept development, literature review planning, and research productivity.

Respond naturally but keep answers structured and useful.
""" + base_guardrails
    }

    return modes.get(mode_choice, modes["6"])


def show_menu():
    print("\nChoose a mode:\n")
    print("1. Research Question Refinement")
    print("2. Literature Review Outline")
    print("3. Manuscript Concept Builder")
    print("4. Grant Concept Builder")
    print("5. Reviewer Response Assistant")
    print("6. General Research Chat")


print("\nResearchLab AI Menu-Based Chat Assistant")
print("Type 'exit' anytime to stop.\n")

show_menu()
mode_choice = input("\nEnter mode number: ")

system_prompt = get_mode_prompt(mode_choice)

messages = []

print("\nResearchLab AI is ready.")
print("You can now describe what you want to work on.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "stop"]:
        print("\nResearchLab AI: Session ended. Good work, Professor.")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=1800,
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