from pathlib import Path
from datetime import datetime
import json
import os
from anthropic import Anthropic
from dotenv import load_dotenv


# --------------------------------------------------
# Lesson 17 Build 4: Claude-Assisted Multi-Agent Research Meeting
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Use Claude to simulate multiple specialist research agents
# reviewing a pitch from different professional perspectives.
# --------------------------------------------------

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5")

if not ANTHROPIC_API_KEY:
    print("ERROR: ANTHROPIC_API_KEY was not found. Check your .env file.")
    exit()

client = Anthropic(api_key=ANTHROPIC_API_KEY)


AGENT_ROLES = [
    {
        "agent_name": "Research Director",
        "role_focus": (
            "Strategic direction, academic positioning, originality, "
            "publication potential, and research contribution."
        )
    },
    {
        "agent_name": "Postharvest Scientist",
        "role_focus": (
            "Scientific validity, crop physiology, maturity indices, quality indicators, "
            "storage, shelf life, warm-chain systems, and postharvest loss reduction."
        )
    },
    {
        "agent_name": "AI Engineer",
        "role_focus": (
            "Technical feasibility, data architecture, RAG, embeddings, vector search, "
            "function calling, agents, model selection, deployment, and evaluation."
        )
    },
    {
        "agent_name": "Grant Strategist",
        "role_focus": (
            "Funding alignment, funder priorities, impact story, stakeholders, "
            "scalability, implementation pathway, outputs, outcomes, and indicators."
        )
    },
    {
        "agent_name": "Ethics and Risk Reviewer",
        "role_focus": (
            "Responsible AI, privacy, security, prompt injection, bias, overreliance, "
            "human review, data governance, and risk controls."
        )
    }
]


def extract_json_from_text(text):
    """
    Clean Claude output and parse JSON.
    Handles cases where Claude wraps JSON in markdown fences.
    """

    cleaned = text.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned.replace("```json", "", 1).strip()

    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```", "", 1).strip()

    if cleaned.endswith("```"):
        cleaned = cleaned[:-3].strip()

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError:
        return {
            "agent": "Parsing Error",
            "role_focus": "JSON parsing",
            "key_questions": [],
            "concerns": [
                "Claude did not return valid JSON."
            ],
            "recommendations": [
                "Try running the request again or simplify the pitch."
            ],
            "next_actions": [
                "Review the raw response and update the prompt if needed."
            ],
            "raw_response": text
        }


def call_claude_agent(agent_name, role_focus, pitch, context):
    """
    Ask Claude to act as a specialist agent and return structured JSON feedback.
    """

    prompt = f"""
You are acting as a specialist agent in a multi-agent research meeting.

Agent name:
{agent_name}

Role focus:
{role_focus}

Research or AI app pitch:
{pitch}

Context:
{context}

Your task:
Review the pitch only from your specialist role.

Return only valid JSON in this exact format:
{{
  "agent": "{agent_name}",
  "role_focus": "{role_focus}",
  "key_questions": [
    "question 1",
    "question 2",
    "question 3",
    "question 4"
  ],
  "concerns": [
    "concern 1",
    "concern 2",
    "concern 3"
  ],
  "recommendations": [
    "recommendation 1",
    "recommendation 2",
    "recommendation 3",
    "recommendation 4"
  ],
  "next_actions": [
    "next action 1",
    "next action 2",
    "next action 3"
  ]
}}

Rules:
- Stay within your assigned role.
- Be specific to the pitch and context.
- Do not invent citations, funders, journals, or data.
- Be constructive and practical.
- Keep each item concise.
- Return JSON only. No markdown.
"""

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=1200,
        temperature=0.3,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw_text = response.content[0].text
    return extract_json_from_text(raw_text)


def generate_integrated_recommendation_with_claude(pitch, context, agent_outputs):
    """
    Ask Claude to synthesize all specialist agent outputs into one integrated recommendation.
    """

    prompt = f"""
You are the chair of a multi-agent research meeting.

You must synthesize the feedback from all specialist agents into one integrated recommendation.

Research or AI app pitch:
{pitch}

Context:
{context}

Agent outputs:
{json.dumps(agent_outputs, indent=2)}

Return only valid JSON in this exact format:
{{
  "meeting_summary": "short summary of the panel's overall view",
  "highest_priority_recommendations": [
    "priority recommendation 1",
    "priority recommendation 2",
    "priority recommendation 3",
    "priority recommendation 4",
    "priority recommendation 5"
  ],
  "suggested_next_actions": [
    "next action 1",
    "next action 2",
    "next action 3",
    "next action 4",
    "next action 5",
    "next action 6"
  ],
  "decision": "clear decision on whether to proceed, refine, pause, or reject",
  "risk_warning": "short warning about the most important risk"
}}

Rules:
- Do not invent facts, citations, funders, or data.
- Make the recommendation practical.
- Balance research value, technical feasibility, funding potential, and responsible AI.
- Return JSON only. No markdown.
"""

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=1200,
        temperature=0.2,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw_text = response.content[0].text
    return extract_json_from_text(raw_text)


def run_multi_agent_meeting(pitch, context):
    """
    Run all specialist agents and generate an integrated recommendation.
    """

    agent_outputs = []

    for role in AGENT_ROLES:
        print(f"\nRunning agent: {role['agent_name']}...")

        agent_output = call_claude_agent(
            agent_name=role["agent_name"],
            role_focus=role["role_focus"],
            pitch=pitch,
            context=context
        )

        agent_outputs.append(agent_output)

    print("\nGenerating integrated recommendation...")

    integrated_recommendation = generate_integrated_recommendation_with_claude(
        pitch=pitch,
        context=context,
        agent_outputs=agent_outputs
    )

    meeting_record = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "model": ANTHROPIC_MODEL,
        "pitch": pitch,
        "context": context,
        "agent_outputs": agent_outputs,
        "integrated_recommendation": integrated_recommendation
    }

    return meeting_record


def save_meeting_record(record, output_dir):
    """
    Save meeting record to JSON.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_file_name = f"claude_multi_agent_meeting_{timestamp}.json"

    file_path = output_dir / safe_file_name

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(record, file, indent=2)

    return file_path


def print_list(title, items):
    print(f"\n{title}:")

    if not items:
        print("- None provided.")
        return

    for item in items:
        print(f"- {item}")


def print_meeting_record(record):
    """
    Print meeting record in readable format.
    """

    print("\nCLAUDE-ASSISTED MULTI-AGENT RESEARCH MEETING REPORT")
    print("=" * 100)

    print("\nPitch:")
    print(record["pitch"])

    print("\nContext:")
    print(record["context"])

    print("\nModel:")
    print(record["model"])

    for output in record["agent_outputs"]:
        print("\n" + "-" * 100)
        print(f"Agent: {output.get('agent', 'Unknown Agent')}")
        print(f"Role focus: {output.get('role_focus', 'Not provided')}")

        print_list("Key questions", output.get("key_questions", []))
        print_list("Concerns", output.get("concerns", []))
        print_list("Recommendations", output.get("recommendations", []))
        print_list("Next actions", output.get("next_actions", []))

        if output.get("raw_response"):
            print("\nRaw response:")
            print(output["raw_response"])

    print("\n" + "=" * 100)
    print("Integrated Recommendation")
    print("=" * 100)

    integrated = record["integrated_recommendation"]

    print("\nMeeting summary:")
    print(integrated.get("meeting_summary", "No summary provided."))

    print_list(
        "Highest priority recommendations",
        integrated.get("highest_priority_recommendations", [])
    )

    print_list(
        "Suggested next actions",
        integrated.get("suggested_next_actions", [])
    )

    print("\nDecision:")
    print(integrated.get("decision", "No decision provided."))

    print("\nRisk warning:")
    print(integrated.get("risk_warning", "No risk warning provided."))


print("\nClaude-Assisted Multi-Agent Research Meeting")
print("Lesson 17: Build 4")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "claude_multi_agent_meeting_records"

while True:
    pitch = input("Enter your research or AI app pitch: ")

    if pitch.lower().strip() in ["exit", "quit", "stop"]:
        print("Claude-assisted multi-agent meeting ended.")
        break

    context = input("Enter context, for example target users, crops, funder, country, app stage: ")

    try:
        record = run_multi_agent_meeting(
            pitch=pitch,
            context=context
        )

        print_meeting_record(record)

        saved_path = save_meeting_record(record, output_dir)

        print("\nMeeting record saved to:")
        print(saved_path)

    except Exception as e:
        print("\nSomething went wrong:")
        print(e)

    print("\n" + "=" * 100 + "\n")