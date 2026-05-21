import json
from datetime import datetime


# --------------------------------------------------
# Lesson 11 Build 2: Function Calling Router with JSON Output
# Microsoft Generative AI for Beginners adaptation
# Purpose: Return structured, machine-readable function call outputs.
# --------------------------------------------------


def search_research_records(topic="", crop="", method="", context=""):
    records = [
        {
            "title": "AI for tomato harvest maturity detection",
            "topic": "harvest maturity",
            "crop": "tomato",
            "method": "computer vision",
            "context": "warm-chain horticultural systems",
            "finding": "Computer vision can classify tomato maturity stages using colour and surface features."
        },
        {
            "title": "NIR spectroscopy for avocado maturity",
            "topic": "internal quality",
            "crop": "avocado",
            "method": "near-infrared spectroscopy",
            "context": "non-destructive maturity testing",
            "finding": "NIR can estimate dry matter and oil content as indicators of harvest maturity."
        },
        {
            "title": "AI adoption barriers in LMIC agriculture",
            "topic": "AI adoption",
            "crop": "smallholder systems",
            "method": "literature review",
            "context": "LMIC agriculture",
            "finding": "High cost, limited connectivity, weak extension support, and low technical capacity reduce AI adoption."
        },
        {
            "title": "Smartphone AI tools for harvest timing",
            "topic": "decision support",
            "crop": "horticultural crops",
            "method": "mobile AI",
            "context": "resource-constrained farming systems",
            "finding": "Smartphone-based AI tools can support harvest timing, grading, disease diagnosis, and market readiness."
        }
    ]

    query_terms = [topic.lower(), crop.lower(), method.lower(), context.lower()]
    query_terms = [term for term in query_terms if term]

    results = []

    for record in records:
        searchable_text = " ".join([
            record["title"],
            record["topic"],
            record["crop"],
            record["method"],
            record["context"],
            record["finding"]
        ]).lower()

        if not query_terms or any(term in searchable_text for term in query_terms):
            results.append(record)

    return {
        "matches_found": len(results),
        "records": results
    }


def generate_research_question(topic="", crop="", context=""):
    if not topic:
        topic = "AI-enabled agricultural decision support"

    if not crop:
        crop = "horticultural crops"

    if not context:
        context = "resource-constrained LMIC systems"

    crop_for_title = crop.title()
    context_for_title = context.replace("LMIC", "LMIC").title()

    return {
        "research_question": f"How can {topic} improve postharvest decision-making for {crop} in {context}?",
        "working_title": f"{topic.title()} for {crop_for_title} in {context_for_title}",
        "possible_contribution": "This study could clarify the technical and implementation pathways for using AI to reduce postharvest losses and improve value-chain decisions."
    }


def draft_deadline_reminder(project="", deadline="", next_action=""):
    if not project:
        project = "the project"

    if not deadline:
        deadline_phrase = "soon"
    elif deadline.lower() == "next week":
        deadline_phrase = "next week"
    else:
        deadline_phrase = f"on {deadline}"

    if not next_action:
        next_action = "review the project and update the status"

    return {
        "subject": f"Deadline Reminder: {project}",
        "message": f"Hello, this is a reminder that '{project}' has an upcoming deadline {deadline_phrase}. Next action required: {next_action}. Please review and update the project status."
    }


def detect_function(user_message):
    text = user_message.lower()

    if (
        "generate a research question" in text
        or "research question" in text
        or "create a research question" in text
        or "develop a research question" in text
        or "generate a title" in text
        or "working title" in text
    ):
        return "generate_research_question"

    if (
        "reminder" in text
        or "deadline" in text
        or "email" in text
        or "draft a message" in text
        or "notify" in text
    ):
        return "draft_deadline_reminder"

    if (
        "search" in text
        or "find" in text
        or "record" in text
        or "records" in text
        or "literature" in text
        or "papers" in text
        or "studies" in text
    ):
        return "search_research_records"

    return "general_response"


def extract_arguments(user_message):
    text = user_message.lower()

    args = {
        "topic": "",
        "crop": "",
        "method": "",
        "context": "",
        "project": "",
        "deadline": "",
        "next_action": ""
    }

    if "tomato" in text or "tomatoes" in text:
        args["crop"] = "tomato"

    if "avocado" in text:
        args["crop"] = "avocado"

    if "computer vision" in text:
        args["method"] = "computer vision"

    if "nir" in text or "near-infrared" in text:
        args["method"] = "near-infrared spectroscopy"

    if "lmic" in text or "resource-constrained" in text:
        args["context"] = "resource-constrained LMIC systems"

    if "harvest maturity" in text:
        args["topic"] = "AI-enabled harvest maturity assessment"

    if "postharvest" in text:
        args["topic"] = "postharvest loss reduction"

    if "manuscript" in text:
        args["project"] = "manuscript project"

    if "review" in text:
        args["project"] = "literature review project"

    if "next week" in text:
        args["deadline"] = "next week"

    if "outline" in text:
        args["next_action"] = "complete the outline"

    return args


def route_function_call(user_message):
    function_name = detect_function(user_message)
    args = extract_arguments(user_message)

    if function_name == "search_research_records":
        used_arguments = {
            "topic": args["topic"],
            "crop": args["crop"],
            "method": args["method"],
            "context": args["context"]
        }

        result = search_research_records(**used_arguments)

    elif function_name == "generate_research_question":
        used_arguments = {
            "topic": args["topic"],
            "crop": args["crop"],
            "context": args["context"]
        }

        result = generate_research_question(**used_arguments)

    elif function_name == "draft_deadline_reminder":
        used_arguments = {
            "project": args["project"],
            "deadline": args["deadline"],
            "next_action": args["next_action"]
        }

        result = draft_deadline_reminder(**used_arguments)

    else:
        used_arguments = {}
        result = {
            "message": "No specific function was selected. Try asking to search records, generate a research question, or draft a reminder."
        }

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "user_message": user_message,
        "function_name": function_name,
        "arguments": used_arguments,
        "result": result
    }


print("\nFunction Calling JSON Router")
print("Lesson 11: Build 2")
print("Type 'exit' anytime to stop.\n")

while True:
    user_message = input("You: ")

    if user_message.lower().strip() in ["exit", "quit", "stop"]:
        print("Function calling JSON router ended.")
        break

    output = route_function_call(user_message)

    print("\nStructured Function Call Output:\n")
    print(json.dumps(output, indent=2))
    print("\n" + "=" * 100 + "\n")