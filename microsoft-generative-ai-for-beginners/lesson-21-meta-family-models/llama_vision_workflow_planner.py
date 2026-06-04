from pathlib import Path
import json
from datetime import datetime


# --------------------------------------------------
# Lesson 21 Build 3: Llama Vision Workflow Planner
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Plan Llama 3.2 Vision workflows for ResearchLab,
# Business Ops, and scientific visual analysis tasks.
# --------------------------------------------------


def safe_file_name(text):
    cleaned = "".join(
        char if char.isalnum() or char in (" ", "-", "_") else ""
        for char in text
    )
    cleaned = "_".join(cleaned.strip().split())
    return cleaned[:70] if cleaned else "llama_vision_workflow_plan"


def recommend_vision_model(
    visual_task_type,
    complexity_level,
    image_count,
    scientific_risk,
    cost_sensitivity,
    latency_sensitivity,
    human_review_need,
    deployment_preference
):
    llama_32_11b_score = 0
    llama_32_90b_score = 0
    vision_fallback_score = 0
    human_review_score = 0
    hybrid_score = 0

    task = visual_task_type.lower().strip()
    complexity = complexity_level.lower().strip()
    risk = scientific_risk.lower().strip()
    cost = cost_sensitivity.lower().strip()
    latency = latency_sensitivity.lower().strip()
    review = human_review_need.lower().strip()
    deployment = deployment_preference.lower().strip()

    try:
        count = int(image_count)
    except ValueError:
        count = 1

    # Task type
    if any(keyword in task for keyword in ["screenshot", "thumbnail", "simple image", "basic description"]):
        llama_32_11b_score += 4

    if any(keyword in task for keyword in ["scientific figure", "diagram", "table", "chart", "postharvest image", "visual evidence"]):
        llama_32_90b_score += 5
        hybrid_score += 2

    if any(keyword in task for keyword in ["ocr", "table", "chart", "complex figure"]):
        llama_32_90b_score += 4
        vision_fallback_score += 2

    # Complexity
    if complexity == "low":
        llama_32_11b_score += 4
    elif complexity == "medium":
        llama_32_11b_score += 2
        llama_32_90b_score += 3
        hybrid_score += 2
    else:
        llama_32_90b_score += 5
        vision_fallback_score += 3
        hybrid_score += 3

    # Image count
    if count <= 1:
        llama_32_11b_score += 1
        llama_32_90b_score += 1
    elif 2 <= count <= 5:
        llama_32_90b_score += 3
        hybrid_score += 2
    else:
        vision_fallback_score += 3
        hybrid_score += 3

    # Risk
    if risk in ["high", "very high"]:
        llama_32_90b_score += 2
        vision_fallback_score += 4
        human_review_score += 5
        hybrid_score += 3
    elif risk == "medium":
        llama_32_90b_score += 2
        human_review_score += 2
        hybrid_score += 2
    else:
        llama_32_11b_score += 2

    # Cost
    if cost in ["high", "very high"]:
        llama_32_11b_score += 4
        hybrid_score += 2
    elif cost == "medium":
        llama_32_11b_score += 2
        llama_32_90b_score += 1
    else:
        llama_32_90b_score += 2
        vision_fallback_score += 1

    # Latency
    if latency in ["high", "very high"]:
        llama_32_11b_score += 4
    elif latency == "medium":
        llama_32_11b_score += 1
        llama_32_90b_score += 1

    # Human review
    if review in ["yes", "y", "high", "always"]:
        human_review_score += 4
        hybrid_score += 2

    # Deployment
    if "github" in deployment:
        llama_32_11b_score += 2
        llama_32_90b_score += 2
    elif "cloud" in deployment or "azure" in deployment:
        llama_32_90b_score += 3
        vision_fallback_score += 1
    elif "hybrid" in deployment:
        hybrid_score += 5
    elif "local" in deployment:
        llama_32_11b_score += 2

    scores = {
        "Llama 3.2 11B Vision": llama_32_11b_score,
        "Llama 3.2 90B Vision": llama_32_90b_score,
        "Claude/GPT Vision fallback": vision_fallback_score,
        "Human expert review": human_review_score,
        "Hybrid vision workflow": hybrid_score
    }

    recommended_option = max(scores, key=scores.get)

    if human_review_score >= 7 and risk in ["high", "very high"]:
        recommended_option = "Human expert review"

    return recommended_option, scores


def generate_vision_workflow_plan(
    project_name,
    lab_context,
    use_case,
    visual_task_type,
    image_source,
    expected_outputs,
    complexity_level,
    image_count,
    scientific_risk,
    cost_sensitivity,
    latency_sensitivity,
    human_review_need,
    deployment_preference
):
    recommended_option, scores = recommend_vision_model(
        visual_task_type=visual_task_type,
        complexity_level=complexity_level,
        image_count=image_count,
        scientific_risk=scientific_risk,
        cost_sensitivity=cost_sensitivity,
        latency_sensitivity=latency_sensitivity,
        human_review_need=human_review_need,
        deployment_preference=deployment_preference
    )

    workflow_steps = [
        "Define the visual question before sending the image to the model.",
        "Check whether the image contains sensitive, unpublished, or identifying information.",
        "Provide context such as crop, figure type, experiment, or manuscript section.",
        "Ask the model to describe visible evidence before interpreting it.",
        "Separate observation from interpretation.",
        "Require uncertainty statements when the image is unclear.",
        "Use human expert review before using outputs in manuscripts, grants, reports, or farmer-facing advice.",
        "Log the prompt, model used, image type, output, and reviewer notes."
    ]

    if "figure" in visual_task_type.lower() or "diagram" in visual_task_type.lower():
        workflow_steps.extend([
            "Ask the model to identify figure components, arrows, labels, variables, and relationships.",
            "Check whether the model misreads labels or invents missing information.",
            "Use the output to improve clarity, not as final scientific validation."
        ])

    if "postharvest" in visual_task_type.lower() or "crop" in visual_task_type.lower():
        workflow_steps.extend([
            "Ask the model to describe visible maturity, colour, defects, bruising, or handling features.",
            "Do not allow the model to infer internal quality without supporting measurements.",
            "Require expert validation for maturity or quality interpretation."
        ])

    if "table" in visual_task_type.lower() or "chart" in visual_task_type.lower():
        workflow_steps.extend([
            "Ask the model to extract visible trends only.",
            "Verify all numbers manually before use.",
            "Do not trust OCR or chart reading without human checking."
        ])

    safety_rules = [
        "Do not treat image interpretation as scientific proof.",
        "Do not infer internal quality from external images without validation.",
        "Do not invent labels, values, methods, or experimental details.",
        "Do not use visual outputs directly in manuscripts without expert review.",
        "Do not expose confidential manuscript figures, student work, or unpublished data to external APIs unless approved.",
        "For farmer-facing recommendations, require human expert validation.",
        "For screenshots, avoid exposing emails, API keys, private names, or credentials.",
        "Always distinguish visible observation from interpretation."
    ]

    model_guidance = {
        "Llama 3.2 11B Vision": (
            "Use for low to medium complexity image description, screenshot review, simple figure checks, "
            "and low-cost visual preprocessing."
        ),
        "Llama 3.2 90B Vision": (
            "Use for more complex scientific figures, diagrams, tables, charts, and deeper visual reasoning."
        ),
        "Claude/GPT Vision fallback": (
            "Use when the visual task is complex, high-stakes, or requires stronger reasoning and careful explanation."
        ),
        "Human expert review": (
            "Use when the image output can affect scientific claims, manuscript decisions, grant strategy, "
            "farmer-facing guidance, or institutional decisions."
        ),
        "Hybrid vision workflow": (
            "Use Llama 3.2 Vision for first-pass observation, then Claude/GPT or human expert review for final interpretation."
        )
    }

    plan = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "project_name": project_name,
        "lab_context": lab_context,
        "use_case": use_case,
        "visual_task_type": visual_task_type,
        "image_source": image_source,
        "expected_outputs": expected_outputs,
        "inputs_reviewed": {
            "complexity_level": complexity_level,
            "image_count": image_count,
            "scientific_risk": scientific_risk,
            "cost_sensitivity": cost_sensitivity,
            "latency_sensitivity": latency_sensitivity,
            "human_review_need": human_review_need,
            "deployment_preference": deployment_preference
        },
        "recommended_option": recommended_option,
        "scores": scores,
        "model_guidance": model_guidance[recommended_option],
        "workflow_steps": workflow_steps,
        "safety_rules": safety_rules,
        "researchlab_guidance": [
            "Use Llama 3.2 Vision for first-pass visual inspection of figures, screenshots, diagrams, and crop images.",
            "Use stronger vision fallback for complex figure interpretation.",
            "Use human expert review for manuscript, grant, or farmer-facing conclusions.",
            "Use visual AI to support observation and clarity, not to replace postharvest expertise.",
            "Pair image interpretation with measured data wherever possible."
        ]
    }

    return plan


def print_plan(plan):
    print("\nLLAMA VISION WORKFLOW PLAN")
    print("=" * 100)

    print("\nProject:")
    print(plan["project_name"])

    print("\nLab context:")
    print(plan["lab_context"])

    print("\nUse case:")
    print(plan["use_case"])

    print("\nVisual task type:")
    print(plan["visual_task_type"])

    print("\nImage source:")
    print(plan["image_source"])

    print("\nExpected outputs:")
    print(plan["expected_outputs"])

    print("\nRecommended option:")
    print(plan["recommended_option"])

    print("\nScores:")
    for option, score in plan["scores"].items():
        print(f"- {option}: {score}")

    print("\nModel guidance:")
    print(plan["model_guidance"])

    print("\nWorkflow steps:")
    for step in plan["workflow_steps"]:
        print(f"- {step}")

    print("\nSafety rules:")
    for rule in plan["safety_rules"]:
        print(f"- {rule}")

    print("\nResearchLab guidance:")
    for item in plan["researchlab_guidance"]:
        print(f"- {item}")


def save_plan(plan, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)

    file_name = safe_file_name(plan["project_name"]) + "_llama_vision_workflow_plan.json"
    file_path = output_dir / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(plan, file, indent=2)

    return file_path


print("\nLlama Vision Workflow Planner")
print("Lesson 21: Build 3")
print("Type 'exit' anytime to stop.\n")

base_dir = Path(__file__).parent
output_dir = base_dir / "llama_vision_workflow_plans"

while True:
    project_name = input("Enter project name: ")

    if project_name.lower().strip() in ["exit", "quit", "stop"]:
        print("Llama vision workflow planner ended.")
        break

    lab_context = input("Lab context, ResearchLab / Business Ops / Trading Lab / Mixed: ")
    use_case = input("Use case: ")
    visual_task_type = input("Visual task type, for example scientific figure, screenshot, crop image, chart, table: ")
    image_source = input("Image source, for example manuscript figure, field photo, screenshot, chart, thumbnail: ")
    expected_outputs = input("Expected outputs, for example description, critique, extraction, interpretation: ")
    complexity_level = input("Complexity level, low / medium / high: ")
    image_count = input("Number of images: ")
    scientific_risk = input("Scientific or decision risk, low / medium / high / very high: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    latency_sensitivity = input("Latency sensitivity, low / medium / high / very high: ")
    human_review_need = input("Human review need, yes / no / high / always: ")
    deployment_preference = input("Deployment preference, GitHub Models / cloud / Azure / local / hybrid / unsure: ")

    plan = generate_vision_workflow_plan(
        project_name=project_name,
        lab_context=lab_context,
        use_case=use_case,
        visual_task_type=visual_task_type,
        image_source=image_source,
        expected_outputs=expected_outputs,
        complexity_level=complexity_level,
        image_count=image_count,
        scientific_risk=scientific_risk,
        cost_sensitivity=cost_sensitivity,
        latency_sensitivity=latency_sensitivity,
        human_review_need=human_review_need,
        deployment_preference=deployment_preference
    )

    print_plan(plan)

    saved_path = save_plan(plan, output_dir)

    print("\nPlan saved to:")
    print(saved_path)
    print("\n" + "=" * 100 + "\n")