from pathlib import Path
import json
from datetime import datetime


# --------------------------------------------------
# Lesson 18 Build 3: Fine-Tuning Example Formatter
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Create JSONL-style supervised fine-tuning examples from
# structured user-assistant training pairs.
# --------------------------------------------------


def safe_file_name(text):
    cleaned = "".join(char if char.isalnum() or char in (" ", "-", "_") else "" for char in text)
    cleaned = "_".join(cleaned.strip().split())
    return cleaned[:70] if cleaned else "fine_tuning_examples"


def create_fine_tuning_example(system_message, user_message, assistant_response):
    """
    Create one chat-style fine-tuning example.
    """

    return {
        "messages": [
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": user_message
            },
            {
                "role": "assistant",
                "content": assistant_response
            }
        ]
    }


def validate_example(example):
    """
    Validate that one example has the expected structure.
    """

    if "messages" not in example:
        return False, "Missing messages key."

    messages = example["messages"]

    if not isinstance(messages, list):
        return False, "Messages must be a list."

    if len(messages) != 3:
        return False, "Each example must contain system, user, and assistant messages."

    expected_roles = ["system", "user", "assistant"]

    for message, expected_role in zip(messages, expected_roles):
        if message.get("role") != expected_role:
            return False, f"Expected role {expected_role}."

        if not message.get("content", "").strip():
            return False, f"Empty content found for role {expected_role}."

    return True, "Valid example."


def save_jsonl_examples(examples, output_path):
    """
    Save examples as JSONL.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        for example in examples:
            file.write(json.dumps(example, ensure_ascii=False) + "\n")


def save_readable_json(examples, output_path):
    """
    Save examples as readable JSON for review.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(examples, file, indent=2, ensure_ascii=False)


def generate_sample_examples():
    """
    Generate sample fine-tuning examples for ResearchLab.
    These are examples only and should be human-reviewed before real fine-tuning.
    """

    system_message = (
        "You are ResearchLab Assistant. Produce concise, academically useful, "
        "grounded responses for postharvest research. Do not invent citations, "
        "statistics, or claims. Mention limitations when evidence is incomplete."
    )

    examples = [
        create_fine_tuning_example(
            system_message=system_message,
            user_message=(
                "Generate a research question on AI-enabled harvest maturity "
                "assessment for tomatoes in LMIC warm-chain systems."
            ),
            assistant_response=(
                "How can AI-enabled harvest maturity assessment improve harvest "
                "timing, postharvest quality, and loss reduction for tomatoes in "
                "LMIC warm-chain systems? This question is suitable because it links "
                "AI decision support to crop quality, practical harvest timing, and "
                "resource-constrained value-chain conditions."
            )
        ),
        create_fine_tuning_example(
            system_message=system_message,
            user_message=(
                "Explain why RAG is useful for a postharvest literature assistant."
            ),
            assistant_response=(
                "RAG is useful because it allows the assistant to retrieve relevant "
                "context from a trusted postharvest knowledge base before generating "
                "an answer. This can improve groundedness and reduce unsupported claims. "
                "However, the quality of the answer still depends on the quality, coverage, "
                "and relevance of the retrieved documents."
            )
        ),
        create_fine_tuning_example(
            system_message=system_message,
            user_message=(
                "Give a limitation statement for an AI-generated answer about "
                "computer vision for fruit maturity detection."
            ),
            assistant_response=(
                "Limitation: This answer should be interpreted cautiously because "
                "computer vision often captures external maturity features such as "
                "colour, size, texture, and visible defects, but may not fully reflect "
                "internal quality attributes such as soluble solids, firmness, dry matter, "
                "or acidity without additional validation."
            )
        ),
        create_fine_tuning_example(
            system_message=system_message,
            user_message=(
                "Draft a concise academic answer on barriers to AI adoption in "
                "smallholder farming systems."
            ),
            assistant_response=(
                "AI adoption in smallholder farming systems may be constrained by "
                "limited connectivity, high technology costs, weak extension support, "
                "low technical capacity, limited access to quality data, and poor fit "
                "between advanced tools and local production realities. Any AI solution "
                "for these contexts should therefore be low-cost, explainable, locally "
                "validated, and linked to practical decisions."
            )
        ),
        create_fine_tuning_example(
            system_message=system_message,
            user_message=(
                "Convert this idea into a structured research title: AI helps farmers "
                "know when to harvest fruit."
            ),
            assistant_response=(
                "AI-Enabled Harvest Maturity Assessment for Improved Fruit Quality "
                "and Postharvest Decision-Making in Resource-Constrained Horticultural "
                "Systems"
            )
        )
    ]

    return examples


def create_custom_example():
    """
    Let the user manually create one example.
    """

    print("\nCreate a custom fine-tuning example.\n")

    system_message = input("System message: ")
    user_message = input("User message: ")
    assistant_response = input("Ideal assistant response: ")

    example = create_fine_tuning_example(
        system_message=system_message,
        user_message=user_message,
        assistant_response=assistant_response
    )

    is_valid, message = validate_example(example)

    return example, is_valid, message


print("\nFine-Tuning Example Formatter")
print("Lesson 18: Build 3")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "formatted_fine_tuning_examples"
output_dir.mkdir(parents=True, exist_ok=True)

while True:
    print("Choose an option:")
    print("1. Generate sample ResearchLab examples")
    print("2. Create one custom example")
    print("3. Exit")

    choice = input("\nEnter choice 1, 2, or 3: ").strip()

    if choice.lower() in ["exit", "quit", "stop", "3"]:
        print("Fine-tuning example formatter ended.")
        break

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if choice == "1":
        examples = generate_sample_examples()

        validation_results = []

        for i, example in enumerate(examples, start=1):
            is_valid, message = validate_example(example)
            validation_results.append({
                "example_number": i,
                "is_valid": is_valid,
                "message": message
            })

        jsonl_path = output_dir / f"researchlab_sample_fine_tuning_examples_{timestamp}.jsonl"
        json_path = output_dir / f"researchlab_sample_fine_tuning_examples_{timestamp}.json"

        save_jsonl_examples(examples, jsonl_path)
        save_readable_json(examples, json_path)

        print("\nSample fine-tuning examples generated.")
        print("\nValidation results:")
        for result in validation_results:
            print(
                f"Example {result['example_number']}: "
                f"{result['is_valid']} - {result['message']}"
            )

        print("\nSaved files:")
        print(jsonl_path)
        print(json_path)

        print("\nWarning:")
        print("These examples are templates. Do not use for real fine-tuning without expert review.")

    elif choice == "2":
        example, is_valid, message = create_custom_example()

        if not is_valid:
            print(f"\nExample is invalid: {message}")
            continue

        file_stem = safe_file_name(example["messages"][1]["content"])
        jsonl_path = output_dir / f"{file_stem}_{timestamp}.jsonl"
        json_path = output_dir / f"{file_stem}_{timestamp}.json"

        save_jsonl_examples([example], jsonl_path)
        save_readable_json([example], json_path)

        print("\nCustom fine-tuning example generated.")
        print(f"Validation: {message}")
        print("\nSaved files:")
        print(jsonl_path)
        print(json_path)

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    print("\n" + "=" * 100 + "\n")