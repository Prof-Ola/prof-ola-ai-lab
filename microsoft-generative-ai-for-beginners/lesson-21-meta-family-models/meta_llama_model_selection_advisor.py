# --------------------------------------------------
# Lesson 21 Build 1: Meta Llama Model Selection Advisor
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Help choose between Llama 3.1, Llama 3.2 Vision,
# small/edge Llama options, Claude/GPT fallback,
# or a hybrid Meta model strategy.
# --------------------------------------------------


def generate_meta_llama_advice(
    use_case,
    task_type,
    modality,
    complexity_level,
    rag_need,
    function_calling_need,
    vision_need,
    synthetic_data_need,
    multilingual_need,
    cost_sensitivity,
    latency_sensitivity,
    local_or_edge_need,
    risk_level,
    deployment_preference
):
    """
    Generate a Meta Llama model selection recommendation.
    """

    llama_31_70b_score = 0
    llama_31_405b_score = 0
    llama_32_11b_vision_score = 0
    llama_32_90b_vision_score = 0
    small_llama_edge_score = 0
    llm_fallback_score = 0
    hybrid_score = 0

    task = task_type.lower().strip()
    mode = modality.lower().strip()
    complexity = complexity_level.lower().strip()
    rag = rag_need.lower().strip()
    function_calling = function_calling_need.lower().strip()
    vision = vision_need.lower().strip()
    synthetic = synthetic_data_need.lower().strip()
    multilingual = multilingual_need.lower().strip()
    cost = cost_sensitivity.lower().strip()
    latency = latency_sensitivity.lower().strip()
    edge = local_or_edge_need.lower().strip()
    risk = risk_level.lower().strip()
    deployment = deployment_preference.lower().strip()

    # Modality and vision
    if mode in ["vision", "image", "multimodal"] or vision in ["yes", "y", "high"]:
        llama_32_11b_vision_score += 4
        llama_32_90b_vision_score += 6
        hybrid_score += 2

    if mode in ["text", "chat", "language"]:
        llama_31_70b_score += 3
        llama_31_405b_score += 4
        small_llama_edge_score += 1

    # Complexity
    if complexity == "low":
        small_llama_edge_score += 4
        llama_31_70b_score += 1
    elif complexity == "medium":
        llama_31_70b_score += 4
        llama_32_11b_vision_score += 2
        hybrid_score += 2
    else:
        llama_31_405b_score += 5
        llama_32_90b_vision_score += 3
        llm_fallback_score += 2
        hybrid_score += 3

    # RAG
    if "rag" in task or rag in ["yes", "y", "high"]:
        llama_31_70b_score += 3
        llama_31_405b_score += 5
        hybrid_score += 2

    # Function calling
    if function_calling in ["yes", "y", "high"]:
        llama_31_70b_score += 3
        llama_31_405b_score += 4
        hybrid_score += 2

    # Synthetic data
    if synthetic in ["yes", "y", "high"]:
        llama_31_405b_score += 4
        llama_31_70b_score += 2
        hybrid_score += 2

    # Multilingual
    if multilingual in ["yes", "y", "high"]:
        llama_31_405b_score += 4
        llama_31_70b_score += 3
        hybrid_score += 1

    # Cost
    if cost in ["high", "very high"]:
        small_llama_edge_score += 4
        llama_31_70b_score += 2
        hybrid_score += 3
    elif cost == "medium":
        llama_31_70b_score += 2
        hybrid_score += 1
    else:
        llama_31_405b_score += 2
        llama_32_90b_vision_score += 1

    # Latency
    if latency in ["high", "very high"]:
        small_llama_edge_score += 4
        llama_32_11b_vision_score += 2
        llama_31_70b_score += 1
    elif latency == "medium":
        llama_31_70b_score += 1
        hybrid_score += 1

    # Local or edge
    if edge in ["yes", "y", "high"]:
        small_llama_edge_score += 5
        llama_32_11b_vision_score += 2
        hybrid_score += 1

    # Risk
    if risk in ["high", "very high"]:
        llama_31_405b_score += 2
        llama_32_90b_vision_score += 1
        llm_fallback_score += 4
        hybrid_score += 3
    elif risk == "medium":
        llama_31_70b_score += 1
        llama_31_405b_score += 1
        hybrid_score += 2
    else:
        small_llama_edge_score += 1

    # Deployment
    if "local" in deployment or "edge" in deployment:
        small_llama_edge_score += 4
    elif "github" in deployment:
        llama_31_70b_score += 2
        llama_31_405b_score += 2
        llama_32_90b_vision_score += 2
    elif "cloud" in deployment or "azure" in deployment:
        llama_31_405b_score += 3
        llama_32_90b_vision_score += 2
    elif "hybrid" in deployment:
        hybrid_score += 5

    scores = {
        "Llama 3.1 70B Instruct": llama_31_70b_score,
        "Llama 3.1 405B Instruct": llama_31_405b_score,
        "Llama 3.2 11B Vision": llama_32_11b_vision_score,
        "Llama 3.2 90B Vision": llama_32_90b_vision_score,
        "Small Llama edge model": small_llama_edge_score,
        "Claude/GPT fallback": llm_fallback_score,
        "Hybrid Meta strategy": hybrid_score
    }

    recommended_option = max(scores, key=scores.get)

    explanations = {
        "Llama 3.1 70B Instruct": """
Recommended model:
Llama 3.1 70B Instruct.

Best fit when:
- You need strong text reasoning.
- You need RAG support.
- You need function calling.
- You want a capable open model without jumping to the largest model.

AI Lab fit:
Use for ResearchLab RAG, function calling prototypes, grounded answers, and medium-complexity academic workflows.
""",
        "Llama 3.1 405B Instruct": """
Recommended model:
Llama 3.1 405B Instruct.

Best fit when:
- You need the strongest Meta text model option.
- You need advanced RAG.
- You need native function calling.
- You need multilingual capability.
- You want synthetic data generation support.
- Complexity is high and quality matters.

AI Lab fit:
Use for advanced ResearchLab synthesis, synthetic data generation, high-complexity RAG, and serious function-calling experiments.
""",
        "Llama 3.2 11B Vision": """
Recommended model:
Llama 3.2 11B Vision.

Best fit when:
- You need vision capability but want a smaller model.
- You are testing image understanding.
- You want flexible deployment for multimodal prototypes.

AI Lab fit:
Use for early visual analysis of scientific figures, screenshots, diagrams, and postharvest image workflows.
""",
        "Llama 3.2 90B Vision": """
Recommended model:
Llama 3.2 90B Vision.

Best fit when:
- Vision reasoning quality matters.
- You need stronger multimodal analysis.
- You are working with scientific figures, images, tables, screenshots, or diagrams.
- You need deeper interpretation of visual material.

AI Lab fit:
Use for advanced visual analysis, figure interpretation, and multimodal ResearchLab workflows.
""",
        "Small Llama edge model": """
Recommended model:
Small Llama edge model.

Best fit when:
- Local or edge deployment matters.
- Low latency matters.
- The task is simple.
- Cost control matters.
- You need lightweight classification, extraction, or short summarization.

AI Lab fit:
Use for tagging notes, local preprocessing, simple Business Ops tasks, and low-risk routing.
""",
        "Claude/GPT fallback": """
Recommended route:
Use Claude or GPT fallback.

Best fit when:
- The task is high-stakes.
- The output requires careful judgement.
- Publication, grant, legal, financial, or farmer-facing consequences may follow.
- You need maximum reasoning quality and human review.

AI Lab fit:
Use for final manuscript critique, grant strategy, and sensitive decision support.
""",
        "Hybrid Meta strategy": """
Recommended strategy:
Use a hybrid Meta model workflow.

Best fit when:
- Different subtasks require different models.
- You need local/edge capability for simple work.
- You need Llama 3.1 for RAG or function calling.
- You need Llama 3.2 for vision.
- You need Claude/GPT fallback for final high-stakes review.

Suggested pattern:
Small Llama for tagging and extraction.
Llama 3.1 for RAG and function calling.
Llama 3.2 Vision for image/figure understanding.
Claude/GPT fallback for final judgement.
"""
    }

    advice = f"""
# Meta Llama Model Selection Advice

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

RAG need:
{rag_need}

Function calling need:
{function_calling_need}

Vision need:
{vision_need}

Synthetic data need:
{synthetic_data_need}

Multilingual need:
{multilingual_need}

Cost sensitivity:
{cost_sensitivity}

Latency sensitivity:
{latency_sensitivity}

Local or edge need:
{local_or_edge_need}

Risk level:
{risk_level}

Deployment preference:
{deployment_preference}

---

# 5. Strategy Scores

| Model / Strategy | Score |
|---|---:|
| Llama 3.1 70B Instruct | {llama_31_70b_score} |
| Llama 3.1 405B Instruct | {llama_31_405b_score} |
| Llama 3.2 11B Vision | {llama_32_11b_vision_score} |
| Llama 3.2 90B Vision | {llama_32_90b_vision_score} |
| Small Llama edge model | {small_llama_edge_score} |
| Claude/GPT fallback | {llm_fallback_score} |
| Hybrid Meta strategy | {hybrid_score} |

---

# 6. Recommended Option

{recommended_option}

{explanations[recommended_option]}

---

# 7. ResearchLab Guidance

For ResearchLab:

1. Use Llama 3.1 70B for capable RAG and function-calling workflows.
2. Use Llama 3.1 405B for complex reasoning, multilingual work, and synthetic data generation experiments.
3. Use Llama 3.2 Vision for scientific figures, screenshots, diagrams, and postharvest image workflows.
4. Use smaller Llama variants for local tagging, extraction, and lightweight routing.
5. Use Claude/GPT fallback for final manuscript critique, grant strategy, or high-risk decisions.
6. Keep human review for publication-level and practitioner-facing outputs.

Operating rule:
Match the model to the task. Do not use a 405B model to do the work of a clipboard.
"""
    return advice.strip()


print("\nMeta Llama Model Selection Advisor")
print("Lesson 21: Building With the Meta Family Models")
print("Type 'exit' anytime to stop.\n")

while True:
    use_case = input("Enter use case: ")

    if use_case.lower().strip() in ["exit", "quit", "stop"]:
        print("Meta Llama model selection advisor ended.")
        break

    task_type = input("Task type, for example RAG, function calling, vision, synthetic data, summarization: ")
    modality = input("Modality, text / vision / multimodal / chat: ")
    complexity_level = input("Complexity level, low / medium / high: ")
    rag_need = input("RAG need, yes / no / high: ")
    function_calling_need = input("Function calling need, yes / no / high: ")
    vision_need = input("Vision need, yes / no / high: ")
    synthetic_data_need = input("Synthetic data need, yes / no / high: ")
    multilingual_need = input("Multilingual need, yes / no / high: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    latency_sensitivity = input("Latency sensitivity, low / medium / high / very high: ")
    local_or_edge_need = input("Local or edge need, yes / no / high: ")
    risk_level = input("Risk level, low / medium / high / very high: ")
    deployment_preference = input("Deployment preference, local / edge / GitHub Models / cloud / Azure / hybrid / unsure: ")

    advice = generate_meta_llama_advice(
        use_case=use_case,
        task_type=task_type,
        modality=modality,
        complexity_level=complexity_level,
        rag_need=rag_need,
        function_calling_need=function_calling_need,
        vision_need=vision_need,
        synthetic_data_need=synthetic_data_need,
        multilingual_need=multilingual_need,
        cost_sensitivity=cost_sensitivity,
        latency_sensitivity=latency_sensitivity,
        local_or_edge_need=local_or_edge_need,
        risk_level=risk_level,
        deployment_preference=deployment_preference
    )

    print("\nGenerated Meta Llama Model Selection Advice:\n")
    print(advice)
    print("\n" + "=" * 100 + "\n")