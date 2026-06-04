from pathlib import Path
import json
from datetime import datetime


# --------------------------------------------------
# Lesson 21 Build 2: Llama Function Calling Planner
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Plan function-calling architectures using Llama 3.1
# for ResearchLab, Business Ops, and Trading Lab workflows.
# --------------------------------------------------


def safe_file_name(text):
    cleaned = "".join(
        char if char.isalnum() or char in (" ", "-", "_") else ""
        for char in text
    )
    cleaned = "_".join(cleaned.strip().split())
    return cleaned[:70] if cleaned else "llama_function_calling_plan"


def recommend_llama_function_model(
    complexity_level,
    rag_need,
    synthetic_data_need,
    multilingual_need,
    risk_level,
    cost_sensitivity,
    deployment_preference
):
    llama_31_70b_score = 0
    llama_31_405b_score = 0
    hybrid_score = 0
    fallback_score = 0

    complexity = complexity_level.lower().strip()
    rag = rag_need.lower().strip()
    synthetic = synthetic_data_need.lower().strip()
    multilingual = multilingual_need.lower().strip()
    risk = risk_level.lower().strip()
    cost = cost_sensitivity.lower().strip()
    deployment = deployment_preference.lower().strip()

    if complexity == "low":
        llama_31_70b_score += 3
    elif complexity == "medium":
        llama_31_70b_score += 4
        llama_31_405b_score += 2
        hybrid_score += 2
    else:
        llama_31_405b_score += 5
        hybrid_score += 3
        fallback_score += 2

    if rag in ["yes", "y", "high"]:
        llama_31_70b_score += 3
        llama_31_405b_score += 4
        hybrid_score += 2

    if synthetic in ["yes", "y", "high"]:
        llama_31_405b_score += 5
        llama_31_70b_score += 2
        hybrid_score += 2

    if multilingual in ["yes", "y", "high"]:
        llama_31_405b_score += 4
        llama_31_70b_score += 2
        hybrid_score += 1

    if risk in ["high", "very high"]:
        llama_31_405b_score += 2
        fallback_score += 4
        hybrid_score += 3
    elif risk == "medium":
        llama_31_70b_score += 1
        llama_31_405b_score += 1
        hybrid_score += 2
    else:
        llama_31_70b_score += 1

    if cost in ["high", "very high"]:
        llama_31_70b_score += 3
        hybrid_score += 3
    elif cost == "medium":
        llama_31_70b_score += 2
        hybrid_score += 1
    else:
        llama_31_405b_score += 2

    if "github" in deployment:
        llama_31_70b_score += 2
        llama_31_405b_score += 2
    elif "cloud" in deployment or "azure" in deployment:
        llama_31_405b_score += 3
    elif "hybrid" in deployment:
        hybrid_score += 5
    elif "local" in deployment:
        llama_31_70b_score += 1
        hybrid_score += 1

    scores = {
        "Llama 3.1 70B function calling": llama_31_70b_score,
        "Llama 3.1 405B function calling": llama_31_405b_score,
        "Hybrid Llama function calling": hybrid_score,
        "Claude/GPT fallback for tool reasoning": fallback_score
    }

    recommended_model = max(scores, key=scores.get)

    return recommended_model, scores


def build_default_tools(lab_context):
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
        },
        {
            "name": "generate_synthetic_eval_questions",
            "purpose": "Generate synthetic evaluation questions for testing RAG, function calling, or model behavior.",
            "risk_level": "medium",
            "human_review_required": "Yes before using in formal evaluation."
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

    external_tools = [
        {
            "name": "brave_search",
            "purpose": "Search the web for current information when up-to-date data is required.",
            "risk_level": "medium",
            "human_review_required": "Yes before citing or using externally."
        },
        {
            "name": "wolfram_alpha",
            "purpose": "Run structured mathematical or computational queries.",
            "risk_level": "medium",
            "human_review_required": "Yes for high-impact calculations."
        }
    ]

    if "research" in lab:
        return research_tools + common_tools + external_tools

    if "business" in lab:
        return business_tools + common_tools + external_tools

    if "trading" in lab:
        return trading_tools + common_tools

    return research_tools + business_tools + trading_tools + common_tools + external_tools


def generate_tool_schema(tool):
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

    elif name == "generate_synthetic_eval_questions":
        parameters = {
            "topic": "string",
            "number_of_questions": "integer",
            "difficulty_level": "string",
            "target_task": "string"
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

    elif name == "brave_search":
        parameters = {
            "query": "string",
            "recency": "string",
            "source_preference": "string"
        }

    elif name == "wolfram_alpha":
        parameters = {
            "query": "string",
            "calculation_type": "string"
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
    task = task_type.lower().strip()
    risk = risk_level.lower().strip()

    if risk in ["high", "very high"]:
        return {
            "pattern": "Human-gated sequential calls",
            "reason": "High-risk workflows require human validation before and after tool use."
        }

    if "research" in task or "rag" in task or "manuscript" in task:
        return {
            "pattern": "Sequential calls",
            "reason": "Research workflows usually need retrieval before generation and evaluation after generation."
        }

    if "synthetic" in task:
        return {
            "pattern": "Sequential calls with review",
            "reason": "Synthetic data should be generated, reviewed, filtered, and validated before use."
        }

    if tool_count >= 3 and risk == "low":
        return {
            "pattern": "Parallel calls allowed for independent low-risk tools",
            "reason": "Independent low-risk tools may run in parallel to reduce latency."
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
    rag_need,
    synthetic_data_need,
    multilingual_need,
    risk_level,
    cost_sensitivity,
    deployment_preference,
    tools_to_include
):
    recommended_model, model_scores = recommend_llama_function_model(
        complexity_level=complexity_level,
        rag_need=rag_need,
        synthetic_data_need=synthetic_data_need,
        multilingual_need=multilingual_need,
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
            "Use allowlisted tools only.",
            "Reject unknown or malformed tool calls.",
            "Validate all arguments before execution.",
            "Do not allow the model to execute shell commands directly.",
            "Separate tool selection, execution, and final response generation.",
            "Log every tool call, arguments, result, timestamp, and user goal.",
            "Require human review for manuscript, grant, farmer-facing, legal, financial, or live-trading outputs.",
            "For web search, cite sources and check recency.",
            "For mathematical outputs, verify calculations.",
            "For synthetic data, label it clearly as synthetic and review before training or evaluation use.",
            "Do not expose API keys, credentials, private files, student data, or unpublished research notes.",
            "Add prompt injection tests before connecting real tools."
        ],
        "implementation_steps": [
            "Define the allowed tool list.",
            "Write JSON schemas for each tool.",
            "Create a prompt that asks Llama to choose exactly one valid tool or no tool.",
            "Parse the model output safely.",
            "Validate arguments against the expected schema.",
            "Execute only approved tools.",
            "Store tool result in state.",
            "Generate a final response based only on tool result and allowed context.",
            "Log the full interaction for evaluation.",
            "Add human approval gates for high-risk outputs.",
            "Test malformed tool calls and prompt injection attempts.",
            "Compare Llama 3.1 70B and 405B on the same function-calling test set."
        ]
    }

    return plan


def print_plan(plan):
    print("\nLLAMA FUNCTION CALLING PLAN")
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

    file_name = safe_file_name(plan["project_name"]) + "_llama_function_calling_plan.json"
    file_path = output_dir / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(plan, file, indent=2)

    return file_path


print("\nLlama Function Calling Planner")
print("Lesson 21: Build 2")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "llama_function_calling_plans"

while True:
    project_name = input("Enter project name: ")

    if project_name.lower().strip() in ["exit", "quit", "stop"]:
        print("Llama function calling planner ended.")
        break

    lab_context = input("Lab context, ResearchLab / Business Ops / Trading Lab / Mixed: ")
    use_case = input("Use case: ")
    task_type = input("Task type, for example RAG, research planning, synthetic data, business workflow: ")
    complexity_level = input("Complexity level, low / medium / high: ")
    rag_need = input("RAG need, yes / no / high: ")
    synthetic_data_need = input("Synthetic data need, yes / no / high: ")
    multilingual_need = input("Multilingual need, yes / no / high: ")
    risk_level = input("Risk level, low / medium / high / very high: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    deployment_preference = input("Deployment preference, GitHub Models / cloud / Azure / local / hybrid / unsure: ")
    tools_to_include = input("Extra tools to include, comma-separated, or press Enter: ")

    plan = generate_function_calling_plan(
        project_name=project_name,
        lab_context=lab_context,
        use_case=use_case,
        task_type=task_type,
        complexity_level=complexity_level,
        rag_need=rag_need,
        synthetic_data_need=synthetic_data_need,
        multilingual_need=multilingual_need,
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