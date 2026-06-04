# --------------------------------------------------
# Lesson 19 Build 2: Phi Model Deployment Planner
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Recommend a Phi-3 / Phi-3.5 model and deployment route
# based on task type, modality, hardware, privacy, cost,
# latency, and experimentation needs.
# --------------------------------------------------


def generate_phi_deployment_plan(
    use_case,
    task_type,
    modality,
    complexity_level,
    hardware_available,
    privacy_requirement,
    cost_sensitivity,
    latency_requirement,
    offline_need,
    multilingual_need,
    vision_need,
    scale_need,
    preferred_platform
):
    """
    Generate Phi model and deployment route recommendation.
    """

    phi_mini_score = 0
    phi_35_mini_score = 0
    phi_vision_score = 0
    phi_moe_score = 0

    ollama_score = 0
    onnx_score = 0
    huggingface_score = 0
    github_models_score = 0
    azure_ai_score = 0
    nvidia_nim_score = 0

    task = task_type.lower().strip()
    mode = modality.lower().strip()
    complexity = complexity_level.lower().strip()
    hardware = hardware_available.lower().strip()
    privacy = privacy_requirement.lower().strip()
    cost = cost_sensitivity.lower().strip()
    latency = latency_requirement.lower().strip()
    offline = offline_need.lower().strip()
    multilingual = multilingual_need.lower().strip()
    vision = vision_need.lower().strip()
    scale = scale_need.lower().strip()
    platform = preferred_platform.lower().strip()

    # Model scoring
    if mode in ["text", "chat", "language"]:
        phi_mini_score += 2
        phi_35_mini_score += 3

    if "classification" in task or "extraction" in task or "summarization" in task:
        phi_mini_score += 3
        phi_35_mini_score += 3

    if "chat" in task or "qa" in task or "rag" in task:
        phi_35_mini_score += 3
        phi_mini_score += 2

    if vision in ["yes", "y", "high"] or mode in ["image", "vision", "multimodal"]:
        phi_vision_score += 6

    if multilingual in ["yes", "y", "high"]:
        phi_35_mini_score += 4

    if complexity == "low":
        phi_mini_score += 3
        phi_35_mini_score += 2
    elif complexity == "medium":
        phi_35_mini_score += 3
        phi_moe_score += 1
    else:
        phi_moe_score += 4
        phi_35_mini_score += 1

    if scale in ["high", "very high"]:
        phi_moe_score += 3
        azure_ai_score += 2
        nvidia_nim_score += 2

    # Deployment scoring
    if offline in ["yes", "y", "high"]:
        ollama_score += 4
        onnx_score += 3
        huggingface_score += 1

    if privacy in ["high", "very high"]:
        ollama_score += 4
        onnx_score += 3
        huggingface_score += 1

    if cost in ["high", "very high"]:
        ollama_score += 3
        onnx_score += 2
        huggingface_score += 2
        github_models_score += 1

    if latency in ["high", "very high"]:
        onnx_score += 4
        nvidia_nim_score += 3
        ollama_score += 2

    if "basic" in hardware or "cpu" in hardware or "laptop" in hardware:
        ollama_score += 3
        onnx_score += 2
        phi_mini_score += 2
        phi_35_mini_score += 1

    if "gpu" in hardware or "strong" in hardware:
        huggingface_score += 2
        onnx_score += 3
        nvidia_nim_score += 2
        phi_vision_score += 1
        phi_moe_score += 1

    if "cloud" in hardware:
        azure_ai_score += 3
        github_models_score += 2
        nvidia_nim_score += 2

    if "ollama" in platform:
        ollama_score += 5
    elif "onnx" in platform:
        onnx_score += 5
    elif "hugging" in platform:
        huggingface_score += 5
    elif "github" in platform:
        github_models_score += 5
    elif "azure" in platform:
        azure_ai_score += 5
    elif "nvidia" in platform or "nim" in platform:
        nvidia_nim_score += 5

    model_scores = {
        "Phi-3 mini": phi_mini_score,
        "Phi-3.5 mini": phi_35_mini_score,
        "Phi-3 / Phi-3.5 Vision": phi_vision_score,
        "Phi-3.5 MoE": phi_moe_score
    }

    deployment_scores = {
        "Ollama local deployment": ollama_score,
        "ONNX Runtime local / edge deployment": onnx_score,
        "Hugging Face Transformers": huggingface_score,
        "GitHub Models": github_models_score,
        "Azure AI Studio": azure_ai_score,
        "NVIDIA NIM": nvidia_nim_score
    }

    recommended_model = max(model_scores, key=model_scores.get)
    recommended_deployment = max(deployment_scores, key=deployment_scores.get)

    model_explanations = {
        "Phi-3 mini": """
Best when:
- You need a lightweight text model.
- The task is simple or repetitive.
- You want low-cost local inference.
- You are doing classification, extraction, tagging, or short summarization.
""",
        "Phi-3.5 mini": """
Best when:
- You need a stronger small text model.
- You need better multilingual support.
- You want chat, RAG, summarization, extraction, or research note support.
- You want a good balance between size and capability.
""",
        "Phi-3 / Phi-3.5 Vision": """
Best when:
- The task involves images, diagrams, figures, tables, screenshots, or visual reasoning.
- You need multimodal understanding.
- You are analyzing scientific figures or visual data.
""",
        "Phi-3.5 MoE": """
Best when:
- The task needs stronger reasoning than a mini model.
- You want better capability while keeping active parameters efficient.
- You are testing more advanced SLM deployment patterns.
"""
    }

    deployment_explanations = {
        "Ollama local deployment": """
Best when:
- You want the easiest local setup.
- You want privacy and offline experimentation.
- You are testing SLMs on a laptop.
- You want quick local chat or research workflows.
""",
        "ONNX Runtime local / edge deployment": """
Best when:
- You need optimized local or edge inference.
- You care about speed, portability, and deployment efficiency.
- You may later deploy to Windows, Linux, mobile, or edge environments.
""",
        "Hugging Face Transformers": """
Best when:
- You want maximum flexibility.
- You want to experiment with model loading, tokenizers, pipelines, or fine-tuning.
- You have enough hardware or cloud compute.
""",
        "GitHub Models": """
Best when:
- You want quick cloud-based testing.
- You want to compare models without local installation complexity.
- You are comfortable using API-based inference.
""",
        "Azure AI Studio": """
Best when:
- You want enterprise cloud deployment.
- You need model catalog access, deployment, monitoring, and Azure integration.
- You may later build production workflows.
""",
        "NVIDIA NIM": """
Best when:
- You need optimized inference on NVIDIA infrastructure.
- You care about performance, scalability, and enterprise deployment.
- You have access to NVIDIA GPUs or managed infrastructure.
"""
    }

    plan = f"""
# Phi Model Deployment Plan

## 1. Use Case

{use_case}

## 2. Task Type

{task_type}

## 3. Modality

{modality}

---

# 4. Inputs Reviewed

Complexity level:
{complexity_level}

Hardware available:
{hardware_available}

Privacy requirement:
{privacy_requirement}

Cost sensitivity:
{cost_sensitivity}

Latency requirement:
{latency_requirement}

Offline need:
{offline_need}

Multilingual need:
{multilingual_need}

Vision need:
{vision_need}

Scale need:
{scale_need}

Preferred platform:
{preferred_platform}

---

# 5. Phi Model Scores

| Model Option | Score |
|---|---:|
| Phi-3 mini | {phi_mini_score} |
| Phi-3.5 mini | {phi_35_mini_score} |
| Phi-3 / Phi-3.5 Vision | {phi_vision_score} |
| Phi-3.5 MoE | {phi_moe_score} |

## Recommended Phi Model

{recommended_model}

{model_explanations[recommended_model]}

---

# 6. Deployment Route Scores

| Deployment Route | Score |
|---|---:|
| Ollama local deployment | {ollama_score} |
| ONNX Runtime local / edge deployment | {onnx_score} |
| Hugging Face Transformers | {huggingface_score} |
| GitHub Models | {github_models_score} |
| Azure AI Studio | {azure_ai_score} |
| NVIDIA NIM | {nvidia_nim_score} |

## Recommended Deployment Route

{recommended_deployment}

{deployment_explanations[recommended_deployment]}

---

# 7. ResearchLab Guidance

For ResearchLab:

- Use Phi-3.5 mini or Phi-3 mini for tagging, extraction, classification, short summaries, and routing.
- Use Phi + RAG for grounded local Q&A where privacy and cost matter.
- Use Phi Vision only when figures, screenshots, diagrams, tables, or image-based reasoning are involved.
- Use Claude, GPT, or another stronger LLM as fallback for complex manuscript reasoning, grant strategy, or high-stakes synthesis.
- Always evaluate Phi outputs before trusting them in academic workflows.

Suggested architecture:

SLM local task handler
+
RAG context retrieval
+
LLM fallback for complex reasoning
+
Human review for important outputs
"""
    return plan.strip()


print("\nPhi Model Deployment Planner")
print("Lesson 19: Build 2")
print("Type 'exit' anytime to stop.\n")

while True:
    use_case = input("Enter use case: ")

    if use_case.lower().strip() in ["exit", "quit", "stop"]:
        print("Phi model deployment planner ended.")
        break

    task_type = input("Task type, for example classification, extraction, RAG, chat, vision, summarization: ")
    modality = input("Modality, text / vision / multimodal / chat: ")
    complexity_level = input("Complexity level, low / medium / high: ")
    hardware_available = input("Hardware available, for example basic CPU laptop, strong GPU, cloud only: ")
    privacy_requirement = input("Privacy requirement, low / medium / high / very high: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    latency_requirement = input("Latency requirement, low / medium / high / very high: ")
    offline_need = input("Offline need, yes / no / high: ")
    multilingual_need = input("Multilingual need, yes / no / high: ")
    vision_need = input("Vision need, yes / no / high: ")
    scale_need = input("Scale need, low / medium / high / very high: ")
    preferred_platform = input("Preferred platform, Ollama / ONNX / Hugging Face / GitHub Models / Azure / NVIDIA NIM / unsure: ")

    plan = generate_phi_deployment_plan(
        use_case=use_case,
        task_type=task_type,
        modality=modality,
        complexity_level=complexity_level,
        hardware_available=hardware_available,
        privacy_requirement=privacy_requirement,
        cost_sensitivity=cost_sensitivity,
        latency_requirement=latency_requirement,
        offline_need=offline_need,
        multilingual_need=multilingual_need,
        vision_need=vision_need,
        scale_need=scale_need,
        preferred_platform=preferred_platform
    )

    print("\nGenerated Phi Model Deployment Plan:\n")
    print(plan)
    print("\n" + "=" * 100 + "\n")