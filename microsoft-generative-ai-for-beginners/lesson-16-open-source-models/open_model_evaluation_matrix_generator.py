from pathlib import Path
import csv
from datetime import datetime


# --------------------------------------------------
# Lesson 16 Build 2: Open Model Evaluation Matrix Generator
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Generate a CSV template for comparing proprietary and open models
# across cost, quality, privacy, latency, local deployment,
# fine-tuning potential, licensing, and AI Lab fit.
# --------------------------------------------------


def create_csv(file_path, headers, rows):
    """
    Create a CSV file with headers and sample rows.
    """

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            writer.writerow(row)


def generate_model_matrix(output_dir):
    """
    Generate open/proprietary model evaluation matrix.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    headers = [
        "ModelID",
        "ModelName",
        "ModelFamily",
        "ProviderOrHost",
        "ModelStatus",
        "AccessRoute",
        "EstimatedCostRating_1to5",
        "QualityRating_1to5",
        "PrivacyRating_1to5",
        "LatencyRating_1to5",
        "LocalDeploymentPossible",
        "FineTuningPotential",
        "LicenseConcern",
        "BestFor",
        "ResearchLabFit_1to5",
        "BusinessOpsFit_1to5",
        "TradingLabFit_1to5",
        "RecommendedUse",
        "MainRisk",
        "TestPriority",
        "LastReviewed",
        "Notes"
    ]

    rows = [
        [
            "M001",
            "Claude Sonnet",
            "Claude",
            "Anthropic API",
            "Proprietary",
            "Hosted API",
            "2",
            "5",
            "3",
            "4",
            "No",
            "Limited",
            "Provider terms apply",
            "Research reasoning, manuscript support, structured writing, complex synthesis",
            "5",
            "4",
            "3",
            "Use for high-value research reasoning, grant development, manuscript refinement, and grounded synthesis.",
            "API cost, privacy concerns, external dependency",
            "High",
            today,
            "Strong quality model for ResearchLab final synthesis."
        ],
        [
            "M002",
            "GPT-4 / GPT-4 Turbo",
            "GPT",
            "OpenAI API",
            "Proprietary",
            "Hosted API",
            "2",
            "5",
            "3",
            "4",
            "No",
            "Limited",
            "Provider terms apply",
            "General reasoning, coding, writing, structured outputs",
            "5",
            "4",
            "3",
            "Use for high-value reasoning, coding support, and structured app development tasks.",
            "API cost, quota limits, external dependency",
            "High",
            today,
            "Useful benchmark model if access and billing are available."
        ],
        [
            "M003",
            "Gemini Pro",
            "Gemini",
            "Google",
            "Proprietary",
            "Hosted API / Google ecosystem",
            "4",
            "4",
            "3",
            "4",
            "No",
            "Limited",
            "Provider terms apply",
            "Google ecosystem workflows, multimodal tasks, general reasoning",
            "4",
            "4",
            "3",
            "Use where Google ecosystem integration is useful.",
            "Provider dependency, variable model behavior",
            "Medium",
            today,
            "Good candidate for AppSheet and Google-side workflows."
        ],
        [
            "M004",
            "Llama 3 / Llama family",
            "Llama",
            "Meta / Hugging Face / Ollama / OpenRouter",
            "Open model",
            "Local or hosted",
            "5",
            "4",
            "5",
            "3",
            "Yes",
            "Strong",
            "Check license and use restrictions",
            "Local chat, private workflows, classification, summarization, RAG prototypes",
            "4",
            "4",
            "3",
            "Use for local/private experiments and cost-controlled workflows.",
            "Hardware limits, lower quality than frontier proprietary models",
            "High",
            today,
            "Important open model family to test locally."
        ],
        [
            "M005",
            "Mistral / Mixtral",
            "Mistral",
            "Mistral AI / Hugging Face / Ollama / OpenRouter",
            "Open model / hosted options",
            "Local or hosted",
            "5",
            "4",
            "5",
            "4",
            "Yes",
            "Strong",
            "Check model-specific license",
            "Efficient RAG, classification, summarization, cost-sensitive workflows",
            "4",
            "4",
            "3",
            "Use for efficient open model experimentation and hosted open model APIs.",
            "Model selection complexity, license variation",
            "High",
            today,
            "Good cost-quality balance."
        ],
        [
            "M006",
            "Qwen",
            "Qwen",
            "Alibaba / Hugging Face / Ollama / OpenRouter",
            "Open model / hosted options",
            "Local or hosted",
            "5",
            "4",
            "5",
            "4",
            "Yes",
            "Strong",
            "Check license and regional/platform terms",
            "Multilingual tasks, local workflows, coding, RAG experiments",
            "4",
            "4",
            "3",
            "Use for multilingual and local open model testing.",
            "License and deployment uncertainty, model behavior testing required",
            "Medium",
            today,
            "Strong candidate for open model experimentation."
        ],
        [
            "M007",
            "DeepSeek",
            "DeepSeek",
            "DeepSeek / Hugging Face / OpenRouter",
            "Open model / hosted options",
            "Hosted or local depending on model",
            "5",
            "4",
            "4",
            "4",
            "Yes, depending on model size",
            "Strong",
            "Check license and provider terms",
            "Coding, reasoning, cost-sensitive experiments",
            "4",
            "4",
            "4",
            "Use for coding and lower-cost reasoning tests.",
            "Provider/model availability changes, need careful validation",
            "Medium",
            today,
            "Worth testing for coding and agentic workflows."
        ],
        [
            "M008",
            "Falcon",
            "Falcon",
            "Technology Innovation Institute / Hugging Face",
            "Open model",
            "Local or hosted",
            "4",
            "3",
            "5",
            "3",
            "Yes",
            "Moderate",
            "Check license",
            "Open model learning, experimentation, comparison baseline",
            "3",
            "3",
            "2",
            "Use as comparison model, not necessarily first production choice.",
            "May underperform newer models for complex tasks",
            "Low",
            today,
            "Useful historically and for open model comparison."
        ],
        [
            "M009",
            "Phi",
            "Phi",
            "Microsoft / Hugging Face / Ollama",
            "Open model / small model family",
            "Local or hosted",
            "5",
            "3",
            "5",
            "5",
            "Yes",
            "Moderate",
            "Check license",
            "Small local tasks, classification, simple summaries, edge use",
            "3",
            "4",
            "3",
            "Use for lightweight local tasks where speed and cost matter.",
            "Lower capability on complex reasoning",
            "Medium",
            today,
            "Good small-model candidate."
        ],
        [
            "M010",
            "Mixtral 8x7B",
            "Mixtral",
            "Mistral AI / Hugging Face / OpenRouter",
            "Open model / hosted options",
            "Local or hosted",
            "5",
            "4",
            "4",
            "4",
            "Possible with strong hardware",
            "Strong",
            "Check license",
            "Efficient reasoning, RAG, cost-controlled hosted workflows",
            "4",
            "4",
            "3",
            "Use for hosted open model comparison against premium APIs.",
            "Hardware demand for local use",
            "High",
            today,
            "Good candidate for quality-cost testing."
        ]
    ]

    create_csv(output_dir / "open_model_evaluation_matrix.csv", headers, rows)


print("\nOpen Model Evaluation Matrix Generator")
print("Lesson 16: Build 2")
print("Type 'exit' anytime to stop.\n")

choice = input("Generate open model evaluation matrix now? Type yes or exit: ")

if choice.lower().strip() in ["exit", "quit", "stop"]:
    print("Open model matrix generator ended.")
else:
    base_dir = Path(__file__).parent
    output_dir = base_dir / "generated_model_evaluation_matrix"

    generate_model_matrix(output_dir)

    print("\nGenerated Open Model Evaluation Matrix CSV:\n")
    print(output_dir / "open_model_evaluation_matrix.csv")

    print("\nNext step:")
    print("1. Open the CSV in Excel or Google Sheets.")
    print("2. Adjust scores after testing models on your own tasks.")
    print("3. Use it to decide which models fit ResearchLab, Business Ops, and Trading Lab.")