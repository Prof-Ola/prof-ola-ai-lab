from pathlib import Path
import json
from datetime import datetime


# --------------------------------------------------
# Lesson 20 Build 3: Mistral Function Calling Planner
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Plan function-calling architectures using Mistral Large
# or Mistral NeMo for ResearchLab, Business Ops, and Trading Lab.
# --------------------------------------------------


def safe_file_name(text):
    cleaned = "".join(
        char if char.isalnum() or char in (" ", "-", "_") else ""
        for char in text
    )
    cleaned = "_".join(cleaned.strip().split())
    return cleaned[:70] if cleaned else "mistral_function_calling_plan"


def recommend_mistral_function_model(
    complexity_level,
    license_flexibility_need,
    local_or_open_model_need,
    risk_level,
    cost_sensitivity,
    deployment_preference
):
    mistral_large_score = 0
    mistral_nemo_score = 0
    hybrid_score = 0

    complexity = complexity_level.lower().strip()
    license_need = license_flexibility_need.lower().strip()
    open_need = local_or_open_model_need.lower().strip()
    risk = risk_level.lower().strip()
    cost = cost_sensitivity.lower().strip()
    deployment = deployment_preference.lower().strip()

    if complexity == "high":
        mistral_large_score += 4
        hybrid_score += 2
    elif complexity == "medium":
        mistral_large_score += 2
        mistral_nemo_score += 2
        hybrid_score += 2
    else:
        mistral_nemo_score += 3

    if license_need in ["yes", "y", "high"]:
        mistral_nemo_score += 5

    if open_need in ["yes", "y", "high"]:
        mistral_nemo_score += 5

    if risk in ["high", "very high"]:
        mistral_large_score += 3
        hybrid_score += 4
    elif risk == "medium":
        mistral_large_score += 1
        hybrid_score += 2
        mistral_nemo_score += 1
    else:
        mistral_nemo_score += 2

    if cost in ["high", "very high"]:
        mistral_nemo_score += 3
        hybrid_score += 2
    elif cost == "medium":
        mistral_nemo_score += 2
        hybrid_score += 1
    else:
        mistral_large_score += 2

    if "local" in deployment or "open" in deployment:
        mistral_nemo_score += 3
    elif "cloud" in deployment or "azure" in deployment or "github" in deployment:
        mistral_large_score += 2
    elif "hybrid" in deployment:
        hybrid_score += 4

    scores = {
        "Mistral Large function calling": mistral_large_score,
        "Mistral NeMo function calling": mistral_nemo_score,
        "Hybrid Mistral function calling": hybrid_score
    }

    recommended_model = max(scores, key=scores.get)

    return recommended_model, scores


def build_default_tools(lab_context):
    """
    Return suggested tools based on AI Lab context.
    """

    lab = lab_context.lower().strip()

    common_tools = [
        {
            "name": "create_next_action_plan",
            "purpose": "Create a structured next-action plan for a user goal.",
            "risk_level": "low",
            "human_review_required": "No, unless used for high-impact decisions."
        },
        {
            "name": "draft_deadline_reminder",
            "purpose": "Draft a professional reminder for upcoming deadlines.",
            "risk_level": "low",
            "human_review_required": "Yes before sending externally."
        }
    ]

    research_tools = [
        {
            "name": "search_research_records",
            "purpose": "Search structured research records by topic, crop, method, and context.",
            "risk_level": "medium",
            "human_review_required": "Yes before citing or using in manuscripts."
        },
        {
            "name": "generate_research_question",
            "purpose": "Generate focused research questions and working titles.",
            "risk_level": "medium",
            "human_review_required": "Yes before academic use."
        },
        {
            "name": "retrieve_rag_context",
            "purpose": "Retrieve relevant chunks from the ResearchLab knowledge base.",
            "risk_level": "medium",
            "human_review_required": "Yes for publication-level outputs."
        },
        {
            "name": "log_rag_evaluation",
            "purpose": "Log query, retrieved chunks, model answer, and evaluation scores.",
            "risk_level": "low",
            "human_review_required": "No."
        }
    ]

    business_tools = [
        {
            "name": "create_project_tracker",
            "purpose": "Generate a table or workflow structure for business operations.",
            "risk_level": "low",
            "human_review_required": "Yes before operational use."
        },
        {
            "name": "draft_client_message",
            "purpose": "Draft professional business communication.",
            "risk_level": "medium",
            "human_review_required": "Yes before sending."
        }
    ]

    trading_tools = [
        {
            "name": "paper_trade_risk_check",
            "purpose": "Check whether a paper-trading idea respects predefined risk controls.",
            "risk_level": "high",
            "human_review_required": "Always."
        },
        {
            "name": "log_paper_trade_decision",
            "purpose": "Record a paper-trading decision for audit and learning.",
            "risk_level": "medium",
            "human_review_required": "Yes."
        }
    ]

    if "research" in lab:
        return research_tools + common_tools

    if "business" in lab:
        return business_tools + common_tools

    if "trading" in lab:
        return trading_tools + common_tools

    return research_tools + business_tools + trading_tools + common_tools


def generate_tool_schema(tool):
    """
    Generate a simple JSON schema-style structure for a tool.
    """

    name = tool["name"]

    if name == "search_research_records":
        parameters = {
            "topic": "string",
            "crop": "string",
            "method": "string",
            "context": "string"
        }

    elif name == "generate_research_question":
        parameters = {
            "topic": "string",
            "crop": "string",
            "context": "string"
        }

    elif name == "draft_deadline_reminder":
        parameters = {
            "project": "string",
            "deadline": "string",
            "next_action": "string"
        }

    elif name == "create_next_action_plan":
        parameters = {
            "goal": "string"
        }

    elif name == "retrieve_rag_context":
        parameters = {
            "query": "string",
            "top_k": "integer",
            "metadata_filter": "object"
        }

    elif name == "log_rag_evaluation":
        parameters = {
            "question": "string",
            "retrieved_chunks": "array",
            "answer": "string",
            "scores": "object",
            "notes": "string"
        }

    elif name == "create_project_tracker":
        parameters = {
            "project_name": "string",
            "fields_needed": "array",
            "workflow_stage": "string"
        }

    elif name == "draft_client_message":
        parameters = {
            "recipient_type": "string",
            "purpose": "string",
            "tone": "string",
            "key_points": "array"
        }

    elif name == "paper_trade_risk_check":
        parameters = {
            "strategy_name": "string",
            "risk_per_trade": "number",
            "max_daily_loss": "number",
            "paper_trade_only": "boolean"
        }

    elif name == "log_paper_trade_decision":
        parameters = {
            "strategy_name": "string",
            "entry_reason": "string",
            "risk_controls": "array",
            "decision": "string"
        }

    else:
        parameters = {
            "input": "string"
        }

    return {
        "name": name,
        "description": tool["purpose"],
        "parameters": parameters,
        "risk_level": tool["risk_level"],
        "human_review_required": tool["human_review_required"]
    }


def decide_call_pattern(task_type, tool_count, risk_level):
    """
    Decide whether tool calls should be sequential, parallel, or gated.
    """

    task = task_type.lower().strip()
    risk = risk_level.lower().strip()

    if risk in ["high", "very high"]:
        return {
            "pattern": "Human-gated sequential calls",
            "reason": "High-risk workflows should require validation before and after tool use."
        }

    if "rag" in task or "research" in task or "manuscript" in task:
        return {
            "pattern": "Sequential calls",
            "reason": "Research workflows usually require retrieval before generation, then evaluation after generation."
        }

    if tool_count >= 3 and risk == "low":
        return {
            "pattern": "Parallel calls allowed for independent tools",
            "reason": "Low-risk independent tools can be called in parallel to reduce latency."
        }

    return {
        "pattern": "Sequential calls",
        "reason": "Sequential calls are safer and easier to debug for early prototypes."
    }


def generate_function_calling_plan(
    project_name,
    lab_context,
    use_case,
    task_type,
    complexity_level,
    license_flexibility_need,
    local_or_open_model_need,
    risk_level,
    cost_sensitivity,
    deployment_preference,
    tools_to_include
):
    recommended_model, model_scores = recommend_mistral_function_model(
        complexity_level=complexity_level,
        license_flexibility_need=license_flexibility_need,
        local_or_open_model_need=local_or_open_model_need,
        risk_level=risk_level,
        cost_sensitivity=cost_sensitivity,
        deployment_preference=deployment_preference
    )

    suggested_tools = build_default_tools(lab_context)

    if tools_to_include.strip():
        requested_tool_names = [
            item.strip()
            for item in tools_to_include.split(",")
            if item.strip()
        ]

        existing_names = {tool["name"] for tool in suggested_tools}

        for name in requested_tool_names:
            if name not in existing_names:
                suggested_tools.append({
                    "name": name,
                    "purpose": "User-defined tool. Add purpose and schema before implementation.",
                    "risk_level": "medium",
                    "human_review_required": "Yes until validated."
                })

    tool_schemas = [
        generate_tool_schema(tool)
        for tool in suggested_tools
    ]

    call_pattern = decide_call_pattern(
        task_type=task_type,
        tool_count=len(tool_schemas),
        risk_level=risk_level
    )

    plan = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "project_name": project_name,
        "lab_context": lab_context,
        "use_case": use_case,
        "task_type": task_type,
        "recommended_model": recommended_model,
        "model_scores": model_scores,
        "call_pattern": call_pattern,
        "tool_schemas": tool_schemas,
        "safety_rules": [
            "Validate all function arguments before execution.",
            "Reject unknown tools.",
            "Do not allow the model to execute shell commands directly.",
            "Log every selected tool, arguments, result, and timestamp.",
            "Use human approval for high-risk or external-facing actions.",
            "Never expose API keys, private files, unpublished data, or credentials.",
            "Use allowlisted tools only.",
            "Add fallback responses when the selected tool fails.",
            "Separate retrieval, reasoning, and action steps.",
            "Require source attribution for research outputs."
        ],
        "implementation_steps": [
            "Define the allowed tool list.",
            "Create JSON schemas for each tool.",
            "Build a router that asks Mistral to select a tool and arguments.",
            "Parse and validate the tool call.",
            "Execute only approved tools.",
            "Store tool results in state.",
            "Generate a final response using tool results.",
            "Log all tool calls for evaluation.",
            "Add human review gates for high-risk outputs.",
            "Test prompt injection attempts before deployment."
        ]
    }

    return plan


def print_plan(plan):
    print("\nMISTRAL FUNCTION CALLING PLAN")
    print("=" * 100)

    print("\nProject:")
    print(plan["project_name"])

    print("\nLab context:")
    print(plan["lab_context"])

    print("\nUse case:")
    print(plan["use_case"])

    print("\nTask type:")
    print(plan["task_type"])

    print("\nRecommended model:")
    print(plan["recommended_model"])

    print("\nModel scores:")
    for model, score in plan["model_scores"].items():
        print(f"- {model}: {score}")

    print("\nRecommended call pattern:")
    print(f"- Pattern: {plan['call_pattern']['pattern']}")
    print(f"- Reason: {plan['call_pattern']['reason']}")

    print("\nTools:")
    for tool in plan["tool_schemas"]:
        print(f"\n- {tool['name']}")
        print(f"  Purpose: {tool['description']}")
        print(f"  Risk level: {tool['risk_level']}")
        print(f"  Human review: {tool['human_review_required']}")
        print(f"  Parameters: {tool['parameters']}")

    print("\nSafety rules:")
    for rule in plan["safety_rules"]:
        print(f"- {rule}")

    print("\nImplementation steps:")
    for step in plan["implementation_steps"]:
        print(f"- {step}")


def save_plan(plan, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    file_name = safe_file_name(plan["project_name"]) + "_function_calling_plan.json"
    file_path = output_dir / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(plan, file, indent=2)

    return file_path


print("\nMistral Function Calling Planner")
print("Lesson 20: Build 3")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "mistral_function_calling_plans"

while True:
    project_name = input("Enter project name: ")

    if project_name.lower().strip() in ["exit", "quit", "stop"]:
        print("Mistral function calling planner ended.")
        break

    lab_context = input("Lab context, ResearchLab / Business Ops / Trading Lab / Mixed: ")
    use_case = input("Use case: ")
    task_type = input("Task type, for example RAG, research planning, business workflow, paper trading: ")
    complexity_level = input("Complexity level, low / medium / high: ")
    license_flexibility_need = input("License flexibility need, yes / no / high: ")
    local_or_open_model_need = input("Local or open model need, yes / no / high: ")
    risk_level = input("Risk level, low / medium / high / very high: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    deployment_preference = input("Deployment preference, local / GitHub Models / cloud / hybrid / unsure: ")
    tools_to_include = input("Extra tools to include, comma-separated, or press Enter: ")

    plan = generate_function_calling_plan(
        project_name=project_name,
        lab_context=lab_context,
        use_case=use_case,
        task_type=task_type,
        complexity_level=complexity_level,
        license_flexibility_need=license_flexibility_need,
        local_or_open_model_need=local_or_open_model_need,
        risk_level=risk_level,
        cost_sensitivity=cost_sensitivity,
        deployment_preference=deployment_preference,
        tools_to_include=tools_to_include
    )

    print_plan(plan)

    saved_path = save_plan(plan, output_dir)

    print("\nPlan saved to:")
    print(saved_path)
    print("\n" + "=" * 100 + "\n")