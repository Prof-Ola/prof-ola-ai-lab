import json
import os
from datetime import datetime
from anthropic import Anthropic
from dotenv import load_dotenv


# --------------------------------------------------
# Lesson 11 Build 3: Claude-Assisted Function Calling Router
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Use Claude to extract function intent and arguments as JSON,
# then let Python execute the actual local function.
# --------------------------------------------------

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5")

if not ANTHROPIC_API_KEY:
    print("ERROR: ANTHROPIC_API_KEY was not found. Check your .env file.")
    exit()

client = Anthropic(api_key=ANTHROPIC_API_KEY)


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

        if not query_terms or all(term in searchable_text for term in query_terms):
    results.append(record)

    return {
        "matches_found": len(results),
        "records": results
    }


def generate_research_question(topic="", crop="", context=""):
    if not topic:
        topic = "AI-enabled agricultural decision support"

if "harvest maturity" in topic.lower() and "ai" not in topic.lower():
    topic = "AI-enabled harvest maturity assessment"

    if not crop:
        crop = "horticultural crops"

    if not context:
        context = "resource-constrained LMIC systems"

    return {
        "research_question": f"How can {topic} improve postharvest decision-making for {crop} in {context}?",
        "working_title": f"{topic} for {crop} in {context}",
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


AVAILABLE_FUNCTIONS = {
    "search_research_records": search_research_records,
    "generate_research_question": generate_research_question,
    "draft_deadline_reminder": draft_deadline_reminder
}


FUNCTION_SCHEMAS = {
    "search_research_records": {
        "description": "Search local research records using topic, crop, method, and context.",
        "arguments": {
            "topic": "string",
            "crop": "string",
            "method": "string",
            "context": "string"
        }
    },
    "generate_research_question": {
        "description": "Generate a research question, working title, and possible contribution.",
        "arguments": {
            "topic": "string",
            "crop": "string",
            "context": "string"
        }
    },
    "draft_deadline_reminder": {
        "description": "Draft a deadline reminder message.",
        "arguments": {
            "project": "string",
            "deadline": "string",
            "next_action": "string"
        }
    }
}


def extract_function_call_with_claude(user_message):
    """
    Ask Claude to return JSON describing the intended function call.
    Cleans Markdown code fences if Claude wraps the JSON in ```json.
    """

    prompt = f"""
You are a function-calling router.

Your task is to read the user's message and choose the best function to call.

Available functions:
{json.dumps(FUNCTION_SCHEMAS, indent=2)}

Return only valid JSON in this exact format:
{{
  "function_name": "one of: search_research_records, generate_research_question, draft_deadline_reminder, general_response",
  "arguments": {{
    "topic": "",
    "crop": "",
    "method": "",
    "context": "",
    "project": "",
    "deadline": "",
    "next_action": ""
  }},
  "reason": "brief explanation of why this function was selected"
}}

Rules:
- Choose search_research_records when the user asks to find, search, locate, retrieve, or list records, literature, studies, or papers.
- Choose generate_research_question when the user asks to generate, refine, create, or develop a research question, title, concept, or review question.
- Choose draft_deadline_reminder when the user asks to draft a reminder, email, message, notification, or deadline update.
- Choose general_response if no function fits.
- Extract only information present or strongly implied by the user message.
- Do not invent dates, crops, methods, or project names.
- Use empty strings for missing arguments.
- Return JSON only. No markdown. No explanation outside JSON.

User message:
{user_message}
"""

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=700,
        temperature=0,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    raw_text = response.content[0].text.strip()

    def clean_json_response(text):
        """
        Clean common non-JSON wrappers such as Markdown code fences.
        """

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "", 1).strip()

        if text.startswith("```"):
            text = text.replace("```", "", 1).strip()

        if text.endswith("```"):
            text = text[:-3].strip()

        return text

    cleaned_text = clean_json_response(raw_text)

    try:
        parsed = json.loads(cleaned_text)

        default_arguments = {
            "topic": "",
            "crop": "",
            "method": "",
            "context": "",
            "project": "",
            "deadline": "",
            "next_action": ""
        }

        parsed_arguments = parsed.get("arguments", {})
        default_arguments.update(parsed_arguments)
        parsed["arguments"] = default_arguments

        return parsed

    except json.JSONDecodeError:
        return {
            "function_name": "general_response",
            "arguments": {
                "topic": "",
                "crop": "",
                "method": "",
                "context": "",
                "project": "",
                "deadline": "",
                "next_action": ""
            },
            "reason": "Claude returned invalid JSON.",
            "raw_response": raw_text,
            "cleaned_response": cleaned_text
        }

def execute_function_call(function_call):
    function_name = function_call.get("function_name", "general_response")
    arguments = function_call.get("arguments", {})

    if function_name not in AVAILABLE_FUNCTIONS:
        return {
            "message": "No valid function was selected.",
            "available_functions": list(AVAILABLE_FUNCTIONS.keys())
        }

    if function_name == "search_research_records":
        used_arguments = {
            "topic": arguments.get("topic", ""),
            "crop": arguments.get("crop", ""),
            "method": arguments.get("method", ""),
            "context": arguments.get("context", "")
        }

    elif function_name == "generate_research_question":
        used_arguments = {
            "topic": arguments.get("topic", ""),
            "crop": arguments.get("crop", ""),
            "context": arguments.get("context", "")
        }

    elif function_name == "draft_deadline_reminder":
        used_arguments = {
            "project": arguments.get("project", ""),
            "deadline": arguments.get("deadline", ""),
            "next_action": arguments.get("next_action", "")
        }

    else:
        used_arguments = {}

    result = AVAILABLE_FUNCTIONS[function_name](**used_arguments)

    return {
        "used_arguments": used_arguments,
        "result": result
    }


def route_user_message(user_message):
    function_call = extract_function_call_with_claude(user_message)
    execution = execute_function_call(function_call)

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "user_message": user_message,
        "function_call": function_call,
        "execution": execution
    }


print("\nClaude-Assisted Function Calling Router")
print("Lesson 11: Build 3")
print("Type 'exit' anytime to stop.\n")

while True:
    user_message = input("You: ")

    if user_message.lower().strip() in ["exit", "quit", "stop"]:
        print("Claude-assisted function calling router ended.")
        break

    try:
        output = route_user_message(user_message)

        print("\nStructured Function Calling Output:\n")
        print(json.dumps(output, indent=2))

    except Exception as e:
        print("\nSomething went wrong:")
        print(e)

    print("\n" + "=" * 100 + "\n")