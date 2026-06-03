from datetime import datetime
from pathlib import Path
import json


# --------------------------------------------------
# Lesson 17 Build 3: Multi-Agent Research Meeting Simulator
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Simulate a research meeting with multiple specialist agents.
# Each agent reviews a pitch from its own role and produces
# questions, concerns, recommendations, and next actions.
# --------------------------------------------------


def research_director_agent(pitch, context):
    return {
        "agent": "Research Director",
        "role_focus": "Strategic direction, academic positioning, originality, and publication potential.",
        "key_questions": [
            "What is the central research problem?",
            "What is the unique contribution compared with existing literature?",
            "Which journal, grant, or institutional priority does this align with?",
            "What would make this work internationally relevant?"
        ],
        "concerns": [
            "The idea may become too broad if the scope is not tightly defined.",
            "The novelty must be clearly separated from general AI-in-agriculture discussions.",
            "The expected academic output should be defined early."
        ],
        "recommendations": [
            "Frame the idea around one strong research gap.",
            "Define the target output, such as article, grant concept, prototype, or policy brief.",
            "Connect the work to food security, postharvest loss reduction, climate resilience, or LMIC systems.",
            "Develop a clear conceptual framework before expanding the evidence base."
        ],
        "next_actions": [
            "Write a one-sentence problem statement.",
            "Define the intended academic contribution.",
            "Identify the top three target journals or funding calls."
        ]
    }


def postharvest_scientist_agent(pitch, context):
    return {
        "agent": "Postharvest Scientist",
        "role_focus": "Scientific validity, crop physiology, quality indicators, storage, and value-chain relevance.",
        "key_questions": [
            "Which crop or crop group is the priority?",
            "Which maturity or quality indicators will be measured?",
            "How does the idea reduce postharvest loss or improve shelf life?",
            "What happens under warm-chain or resource-constrained conditions?"
        ],
        "concerns": [
            "AI outputs may be weak if physiological maturity indicators are poorly defined.",
            "External visual features alone may not represent internal fruit quality.",
            "Smallholder contexts require practical, low-cost, and robust methods."
        ],
        "recommendations": [
            "Link AI predictions to measurable postharvest quality indicators.",
            "Include both external and internal maturity parameters where possible.",
            "Consider warm-chain stress, cold storage limitations, and handling practices.",
            "Prioritize crops with high postharvest loss and strong local relevance."
        ],
        "next_actions": [
            "List the maturity indicators relevant to the selected crop.",
            "Identify practical measurement methods for each indicator.",
            "Map how harvest timing affects shelf life and market quality."
        ]
    }


def ai_engineer_agent(pitch, context):
    return {
        "agent": "AI Engineer",
        "role_focus": "Technical feasibility, data, model choice, RAG, function calling, agents, and deployment.",
        "key_questions": [
            "What data will the AI system use?",
            "Is the task better solved by RAG, classification, computer vision, function calling, or an agent?",
            "Will the system run locally, through an API, or as a hybrid stack?",
            "How will outputs be evaluated?"
        ],
        "concerns": [
            "The project may fail if data quality and data structure are weak.",
            "A chatbot alone is not enough if the workflow needs retrieval, tools, or memory.",
            "Uncontrolled agents can choose wrong tools or generate unsupported answers."
        ],
        "recommendations": [
            "Start with a narrow prototype before adding agent complexity.",
            "Use RAG where answers must be grounded in documents.",
            "Use function calling where the system must choose tools or structured actions.",
            "Use persistent state only after defining what should and should not be stored.",
            "Add evaluation logs for quality, groundedness, safety, cost, and latency."
        ],
        "next_actions": [
            "Define the minimum viable AI workflow.",
            "Identify required tools and data sources.",
            "Create test prompts and scoring criteria before expanding the app."
        ]
    }


def grant_strategist_agent(pitch, context):
    return {
        "agent": "Grant Strategist",
        "role_focus": "Funding alignment, impact story, stakeholders, scalability, and implementation pathway.",
        "key_questions": [
            "Who benefits directly from this project?",
            "What funder priority does this address?",
            "What is the measurable outcome?",
            "How can the idea scale beyond one study or one app?"
        ],
        "concerns": [
            "Funders may not support the idea if the impact pathway is vague.",
            "Technical novelty alone is not enough without community, food security, or value-chain relevance.",
            "The proposal needs measurable outputs, milestones, and beneficiaries."
        ],
        "recommendations": [
            "Frame the project as a solution to postharvest loss, food security, and climate-resilient value chains.",
            "Identify beneficiaries such as smallholder farmers, extension workers, students, researchers, and agribusinesses.",
            "Include capacity building, knowledge transfer, and low-cost implementation.",
            "Develop a phased plan from prototype to field validation."
        ],
        "next_actions": [
            "Draft a short impact statement.",
            "Identify potential funders or institutional partners.",
            "Define outputs, outcomes, and indicators."
        ]
    }


def ethics_risk_reviewer_agent(pitch, context):
    return {
        "agent": "Ethics and Risk Reviewer",
        "role_focus": "Responsible AI, bias, privacy, security, overreliance, and human review.",
        "key_questions": [
            "What data could be sensitive?",
            "Could the system give misleading or overconfident recommendations?",
            "Who is responsible if the AI advice causes poor decisions?",
            "How will users know the AI output needs human review?"
        ],
        "concerns": [
            "AI systems may overstate certainty when evidence is limited.",
            "Smallholder users may overtrust AI recommendations if limitations are not clearly shown.",
            "Private research notes, collaborator details, and unpublished data should not be exposed.",
            "Agent memory may store sensitive information if not controlled."
        ],
        "recommendations": [
            "Add human review warnings to all high-impact outputs.",
            "Avoid storing sensitive information in persistent state unless necessary.",
            "Add prompt injection tests before connecting tools to real data.",
            "Use evidence limitation statements in research and RAG outputs.",
            "Keep API keys and private files out of GitHub."
        ],
        "next_actions": [
            "Classify data sensitivity before deployment.",
            "Add AI-generated output notices.",
            "Create a risk register and test unsafe prompts."
        ]
    }


AGENTS = [
    research_director_agent,
    postharvest_scientist_agent,
    ai_engineer_agent,
    grant_strategist_agent,
    ethics_risk_reviewer_agent
]


def generate_integrated_recommendation(agent_outputs, pitch):
    all_next_actions = []

    for output in agent_outputs:
        all_next_actions.extend(output["next_actions"])

    priority_actions = all_next_actions[:8]

    return {
        "meeting_summary": (
            "The multi-agent panel agrees that the idea has strong potential if it is "
            "narrowed into a clear research problem, grounded in postharvest science, "
            "supported by a feasible AI workflow, aligned with funder priorities, "
            "and protected by responsible AI safeguards."
        ),
        "highest_priority_recommendations": [
            "Clarify the exact research problem and intended output.",
            "Define the crop, context, users, and measurable postharvest outcome.",
            "Decide whether the technical approach needs RAG, function calling, agents, or computer vision.",
            "Create evaluation metrics before expanding the prototype.",
            "Add human review, privacy safeguards, and prompt injection testing."
        ],
        "suggested_next_actions": priority_actions,
        "decision": (
            "Proceed to concept refinement before full implementation. "
            "Do not scale until the problem statement, data sources, evaluation criteria, "
            "and risk controls are clear."
        )
    }


def run_multi_agent_meeting(pitch, context):
    agent_outputs = []

    for agent in AGENTS:
        output = agent(pitch, context)
        agent_outputs.append(output)

    integrated_recommendation = generate_integrated_recommendation(agent_outputs, pitch)

    meeting_record = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "pitch": pitch,
        "context": context,
        "agent_outputs": agent_outputs,
        "integrated_recommendation": integrated_recommendation
    }

    return meeting_record


def save_meeting_record(record, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_dir / f"multi_agent_meeting_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(record, file, indent=2)

    return file_path


def print_meeting_record(record):
    print("\nMULTI-AGENT RESEARCH MEETING REPORT")
    print("=" * 100)

    print("\nPitch:")
    print(record["pitch"])

    print("\nContext:")
    print(record["context"])

    for output in record["agent_outputs"]:
        print("\n" + "-" * 100)
        print(f"Agent: {output['agent']}")
        print(f"Role focus: {output['role_focus']}")

        print("\nKey questions:")
        for question in output["key_questions"]:
            print(f"- {question}")

        print("\nConcerns:")
        for concern in output["concerns"]:
            print(f"- {concern}")

        print("\nRecommendations:")
        for recommendation in output["recommendations"]:
            print(f"- {recommendation}")

        print("\nNext actions:")
        for action in output["next_actions"]:
            print(f"- {action}")

    print("\n" + "=" * 100)
    print("Integrated Recommendation")
    print("=" * 100)

    integrated = record["integrated_recommendation"]

    print("\nMeeting summary:")
    print(integrated["meeting_summary"])

    print("\nHighest priority recommendations:")
    for item in integrated["highest_priority_recommendations"]:
        print(f"- {item}")

    print("\nSuggested next actions:")
    for item in integrated["suggested_next_actions"]:
        print(f"- {item}")

    print("\nDecision:")
    print(integrated["decision"])


print("\nMulti-Agent Research Meeting Simulator")
print("Lesson 17: Build 3")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "multi_agent_meeting_records"

while True:
    pitch = input("Enter your research or AI app pitch: ")

    if pitch.lower().strip() in ["exit", "quit", "stop"]:
        print("Multi-agent research meeting simulator ended.")
        break

    context = input("Enter context, for example target users, crops, funder, country, app stage: ")

    record = run_multi_agent_meeting(
        pitch=pitch,
        context=context
    )

    print_meeting_record(record)

    saved_path = save_meeting_record(record, output_dir)

    print("\nMeeting record saved to:")
    print(saved_path)
    print("\n" + "=" * 100 + "\n")