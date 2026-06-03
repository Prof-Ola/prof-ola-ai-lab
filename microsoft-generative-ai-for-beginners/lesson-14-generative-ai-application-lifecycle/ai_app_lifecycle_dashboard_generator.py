from pathlib import Path
import csv
from datetime import datetime


# --------------------------------------------------
# Lesson 14 Build 4: AI App Lifecycle Dashboard Data Generator
# Microsoft Generative AI for Beginners adaptation
# Purpose: Generate a portfolio dashboard CSV for tracking AI apps
# across lifecycle stage, version, risks, metrics, UX, security, and next actions.
# --------------------------------------------------


def create_csv(file_path, headers, rows):
    """
    Create a CSV file with headers and rows.
    """

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            writer.writerow(row)


def generate_dashboard_data(output_dir):
    """
    Generate a master AI app lifecycle dashboard CSV.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    headers = [
        "AppID",
        "AppName",
        "LessonNumber",
        "CurrentVersion",
        "LifecycleStage",
        "PrimaryPurpose",
        "MainUsers",
        "KeyAIFeatures",
        "DataSources",
        "MetricsTracked",
        "KeyRisks",
        "SecurityStatus",
        "UXStatus",
        "NextAction",
        "Owner",
        "Priority",
        "LastReviewed",
        "Notes"
    ]

    rows = [
        [
            "APP001",
            "Research Idea Generator",
            "Lesson 06",
            "v0.1",
            "Prototype",
            "Generate research ideas, research questions, titles, and practical applications.",
            "Professor Ola, researchers, students",
            "Text generation, prompt engineering",
            "User-provided research topic",
            "Output relevance, clarity, usefulness",
            "Generic output, weak evidence grounding",
            "Basic",
            "Basic",
            "Add structured output saving and evaluation test cases",
            "Professor Ola",
            "Medium",
            today,
            "Early text generation app."
        ],
        [
            "APP002",
            "ResearchLab AI Chat Assistant",
            "Lesson 07",
            "v0.2",
            "Prototype testing",
            "Support research conversations, manuscript concepts, review outlines, and academic planning.",
            "Researchers, postgraduate students, collaborators",
            "Chat loop, conversation memory, system prompt, workflow modes",
            "User prompts and session conversation",
            "Response usefulness, context retention, format consistency",
            "Hallucination, overreliance, no persistent memory controls",
            "Basic",
            "Moderate",
            "Add feedback capture and human review warnings",
            "Professor Ola",
            "High",
            today,
            "Important core ResearchLab assistant."
        ],
        [
            "APP003",
            "Research CSV RAG App",
            "Lesson 08",
            "v0.2",
            "Prototype testing",
            "Search structured research records and generate grounded answers from retrieved evidence.",
            "Researchers, postgraduate students, lecturers",
            "Local embeddings, semantic search, CSV retrieval, Claude grounded answer generation",
            "CSV literature records, user questions, retrieved records",
            "Groundedness, relevance, usefulness, latency, cost, evidence limitations",
            "Small database, prompt injection, unsupported claims, API cost",
            "Moderate",
            "Moderate",
            "Add logging, feedback, prompt injection hardening, and larger literature database",
            "Professor Ola",
            "High",
            today,
            "Strong candidate for future ResearchLab tool."
        ],
        [
            "APP004",
            "Research Image Prompt Builder",
            "Lesson 09",
            "v0.1",
            "Prototype",
            "Generate safe, structured image generation prompts for research communication.",
            "Researchers, content creators, educators",
            "Meta prompts, image prompt generation, safety boundaries",
            "User-provided visual concept details",
            "Prompt quality, visual clarity, safety, usefulness",
            "Poor prompt specificity, image model misinterpretation",
            "Basic",
            "Moderate",
            "Add examples and prompt quality scoring",
            "Professor Ola",
            "Medium",
            today,
            "Useful for LinkedIn and scientific visuals."
        ],
        [
            "APP005",
            "Scientific Figure Prompt Generator",
            "Lesson 09",
            "v0.1",
            "Prototype",
            "Generate prompts for journal figures, workflows, graphical abstracts, and conceptual diagrams.",
            "Researchers, manuscript authors",
            "Scientific meta prompts, figure layout design, prompt archiving",
            "User-provided figure concept details",
            "Scientific clarity, layout quality, label readability",
            "Misleading visuals, clutter, poor scientific accuracy",
            "Basic",
            "Moderate",
            "Add figure review checklist and output examples",
            "Professor Ola",
            "High",
            today,
            "High academic value."
        ],
        [
            "APP006",
            "AppSheet Solution Blueprint Builder",
            "Lesson 10",
            "v0.1",
            "Prototype",
            "Generate low-code solution blueprints for AppSheet, Google Sheets, automation, and AI helper tools.",
            "Researchers, business users, administrators",
            "Low-code planning, data model planning, automation prompt generation",
            "User-provided solution requirements",
            "Blueprint completeness, usability, implementation clarity",
            "Incomplete requirements, poor data model design",
            "Basic",
            "Moderate",
            "Connect to generated table templates and workflow prompts",
            "Professor Ola",
            "Medium",
            today,
            "Paywall-safe low-code adaptation."
        ],
        [
            "APP007",
            "Claude-Assisted Function Calling Router",
            "Lesson 11",
            "v0.3",
            "Prototype testing",
            "Use Claude to extract function intent and arguments, then execute validated local functions.",
            "Researchers, developers, workflow builders",
            "Function routing, JSON extraction, validated local function execution",
            "User prompts, local function schemas, local research records",
            "Routing accuracy, JSON validity, function safety, error rate",
            "Wrong function selection, invalid JSON, unsafe function execution",
            "Moderate",
            "Basic",
            "Connect to CSV search and add stronger validation",
            "Professor Ola",
            "High",
            today,
            "Bridge toward agentic ResearchLab tools."
        ],
        [
            "APP008",
            "AI UX Message Framework Generator",
            "Lesson 12",
            "v0.1",
            "Prototype",
            "Generate UX messages for transparency, user control, human review, feedback, and data use.",
            "AI app builders, researchers, students",
            "UX message generation, trust notices, feedback prompts",
            "User-provided app details",
            "UX completeness, clarity, trust support",
            "Generic UX messages, lack of actual app integration",
            "Basic",
            "Strong",
            "Integrate UX messages into core apps",
            "Professor Ola",
            "Medium",
            today,
            "Useful across all AI Lab tools."
        ],
        [
            "APP009",
            "AI Security Risk Assessment Generator",
            "Lesson 13",
            "v0.1",
            "Prototype",
            "Assess security risks and recommend controls for AI applications.",
            "AI app builders, researchers, administrators",
            "Security risk assessment, prompt injection awareness, control recommendations",
            "User-provided app risk details",
            "Risk coverage, control quality, security readiness",
            "Checklist only, no automated testing yet",
            "Strong",
            "Moderate",
            "Link with prompt injection harness and checklist scorer",
            "Professor Ola",
            "High",
            today,
            "Important governance tool."
        ],
        [
            "APP010",
            "AI App Lifecycle Planner",
            "Lesson 14",
            "v0.1",
            "Prototype",
            "Generate lifecycle plans for AI apps from ideation to operationalization.",
            "AI app builders, researchers, project managers",
            "Lifecycle planning, metrics planning, monitoring planning",
            "User-provided app lifecycle details",
            "Plan quality, completeness, implementation usefulness",
            "Manual inputs, no automated dashboard yet",
            "Moderate",
            "Moderate",
            "Use this dashboard generator for portfolio tracking",
            "Professor Ola",
            "High",
            today,
            "Core LLMOps planning tool."
        ]
    ]

    create_csv(output_dir / "ai_app_lifecycle_dashboard.csv", headers, rows)


print("\nAI App Lifecycle Dashboard Data Generator")
print("Lesson 14: Build 4")
print("Type 'exit' anytime to stop.\n")

choice = input("Generate dashboard data now? Type yes or exit: ")

if choice.lower().strip() in ["exit", "quit", "stop"]:
    print("Dashboard generator ended.")
else:
    base_dir = Path(__file__).parent
    output_dir = base_dir / "generated_lifecycle_dashboard"

    generate_dashboard_data(output_dir)

    print("\nGenerated AI App Lifecycle Dashboard CSV:\n")
    print(output_dir / "ai_app_lifecycle_dashboard.csv")

    print("\nNext step:")
    print("1. Open the CSV in Excel or Google Sheets.")
    print("2. Review each app's lifecycle stage, risks, UX status, security status, and next action.")
    print("3. Use this file as the command-center tracker for your AI Lab.")