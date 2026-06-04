# --------------------------------------------------
# Lesson 20 Build 1: Mistral Model Selection Advisor
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Help choose between Mistral Large, Mistral Small,
# Mistral NeMo, external LLM fallback, or hybrid strategy.
# --------------------------------------------------


def generate_mistral_model_advice(
    use_case,
    task_type,
    complexity_level,
    rag_need,
    function_calling_need,
    coding_need,
    multilingual_need,
    cost_sensitivity,
    latency_sensitivity,
    fine_tuning_need,
    license_flexibility_need,
    risk_level,
    deployment_preference
):
    """
    Generate a Mistral model selection recommendation.
    """

    mistral_large_score = 0
    mistral_small_score = 0
    mistral_nemo_score = 0
    llm_fallback_score = 0
    hybrid_score = 0

    task = task_type.lower().strip()
    complexity = complexity_level.lower().strip()
    rag = rag_need.lower().strip()
    function_calling = function_calling_need.lower().strip()
    coding = coding_need.lower().strip()
    multilingual = multilingual_need.lower().strip()
    cost = cost_sensitivity.lower().strip()
    latency = latency_sensitivity.lower().strip()
    fine_tuning = fine_tuning_need.lower().strip()
    license_need = license_flexibility_need.lower().strip()
    risk = risk_level.lower().strip()
    deployment = deployment_preference.lower().strip()

    # Complexity
    if complexity == "low":
        mistral_small_score += 4
        mistral_nemo_score += 2
    elif complexity == "medium":
        mistral_nemo_score += 3
        mistral_large_score += 2
        hybrid_score += 2
    else:
        mistral_large_score += 4
        llm_fallback_score += 2
        hybrid_score += 3

    # Task type
    if "summarization" in task or "summarisation" in task or "classification" in task or "sentiment" in task or "translation" in task:
        mistral_small_score += 4
        mistral_nemo_score += 2

    if "rag" in task or rag in ["yes", "y", "high"]:
        mistral_large_score += 4
        mistral_nemo_score += 2
        hybrid_score += 2

    if function_calling in ["yes", "y", "high"]:
        mistral_large_score += 3
        mistral_nemo_score += 4
        hybrid_score += 2

    if coding in ["yes", "y", "high"]:
        mistral_large_score += 4
        mistral_small_score += 1
        mistral_nemo_score += 2

    if multilingual in ["yes", "y", "high"]:
        mistral_large_score += 3
        mistral_nemo_score += 3
        mistral_small_score += 1

    # Cost
    if cost in ["high", "very high"]:
        mistral_small_score += 4
        mistral_nemo_score += 3
        hybrid_score += 2
    elif cost == "medium":
        mistral_nemo_score += 2
        mistral_small_score += 2
    else:
        mistral_large_score += 2

    # Latency
    if latency in ["high", "very high"]:
        mistral_small_score += 4
        mistral_nemo_score += 2
    elif latency == "medium":
        mistral_nemo_score += 2
        hybrid_score += 1

    # Fine-tuning
    if fine_tuning in ["yes", "y", "high"]:
        mistral_nemo_score += 5
        hybrid_score += 2

    # License flexibility
    if license_need in ["yes", "y", "high"]:
        mistral_nemo_score += 5

    # Risk
    if risk in ["high", "very high"]:
        mistral_large_score += 2
        llm_fallback_score += 4
        hybrid_score += 3
    elif risk == "medium":
        mistral_large_score += 1
        hybrid_score += 2
    else:
        mistral_small_score += 1

    # Deployment
    if "local" in deployment:
        mistral_nemo_score += 3
        mistral_small_score += 2
    elif "github" in deployment:
        mistral_large_score += 1
        mistral_small_score += 1
        mistral_nemo_score += 1
    elif "cloud" in deployment or "azure" in deployment:
        mistral_large_score += 3
        hybrid_score += 1
    elif "hybrid" in deployment:
        hybrid_score += 4

    scores = {
        "Mistral Large": mistral_large_score,
        "Mistral Small": mistral_small_score,
        "Mistral NeMo": mistral_nemo_score,
        "Claude/GPT fallback": llm_fallback_score,
        "Hybrid Mistral strategy": hybrid_score
    }

    recommended_model = max(scores, key=scores.get)

    explanations = {
        "Mistral Large": """
Recommended model:
Mistral Large.

Best fit when:
- The task needs stronger reasoning.
- RAG needs a larger context window.
- Function calling is important.
- Coding or multilingual performance matters.
- Enterprise-style reliability is needed.

AI Lab fit:
Use for advanced RAG, function calling, code generation, multilingual academic workflows, and complex synthesis.
""",
        "Mistral Small": """
Recommended model:
Mistral Small.

Best fit when:
- Cost saving matters.
- Low latency matters.
- The task is frequent and text-based.
- The task involves summarization, sentiment analysis, translation, or simple code suggestions.

AI Lab fit:
Use for Business Ops, short summaries, note classification, quick drafting, and lightweight ResearchLab tasks.
""",
        "Mistral NeMo": """
Recommended model:
Mistral NeMo.

Best fit when:
- Open licensing matters.
- Fine-tuning may be needed.
- Function calling is needed in an open model.
- Multilingual and code tokenization efficiency matters.
- You want flexibility for experimentation.

AI Lab fit:
Use for open-model experiments, function calling prototypes, local/hybrid workflows, and possible future fine-tuning tests.
""",
        "Claude/GPT fallback": """
Recommended route:
Use a stronger fallback model such as Claude or GPT.

Best fit when:
- The task is high-stakes.
- Quality matters more than cost.
- Deep reasoning or careful judgement is required.
- Human-facing or publication-level outputs need stronger review.

AI Lab fit:
Use as fallback for manuscript critique, grant strategy, final synthesis, and sensitive decisions.
""",
        "Hybrid Mistral strategy": """
Recommended strategy:
Use a hybrid Mistral workflow.

Best fit when:
- Different parts of the task need different model strengths.
- Cost matters, but some tasks need stronger reasoning.
- You want Mistral Small or NeMo for routine tasks and Mistral Large or Claude/GPT for complex tasks.

Suggested pattern:
- Mistral Small for quick summaries and classification.
- Mistral NeMo for open function calling and fine-tuning experiments.
- Mistral Large for advanced RAG and coding.
- Claude/GPT fallback for high-stakes final review.
"""
    }

    advice = f"""
# Mistral Model Selection Advice

## 1. Use Case

{use_case}

## 2. Task Type

{task_type}

---

# 3. Inputs Reviewed

Complexity level:
{complexity_level}

RAG need:
{rag_need}

Function calling need:
{function_calling_need}

Coding need:
{coding_need}

Multilingual need:
{multilingual_need}

Cost sensitivity:
{cost_sensitivity}

Latency sensitivity:
{latency_sensitivity}

Fine-tuning need:
{fine_tuning_need}

License flexibility need:
{license_flexibility_need}

Risk level:
{risk_level}

Deployment preference:
{deployment_preference}

---

# 4. Strategy Scores

| Model / Strategy | Score |
|---|---:|
| Mistral Large | {mistral_large_score} |
| Mistral Small | {mistral_small_score} |
| Mistral NeMo | {mistral_nemo_score} |
| Claude/GPT fallback | {llm_fallback_score} |
| Hybrid Mistral strategy | {hybrid_score} |

---

# 5. Recommended Option

{recommended_model}

{explanations[recommended_model]}

---

# 6. ResearchLab Guidance

For ResearchLab:

1. Use Mistral Small for lightweight tasks such as tagging, short summaries, and simple extraction.
2. Use Mistral Large for RAG, coding, multilingual workflows, and stronger reasoning.
3. Use Mistral NeMo for open-model function calling and future fine-tuning experiments.
4. Use Claude or GPT as fallback for final manuscript critique, grant strategy, or high-risk interpretation.
5. Keep human review for publication-level or practitioner-facing outputs.

Operating rule:
Use the smallest safe model that performs well enough.
"""
    return advice.strip()


print("\nMistral Model Selection Advisor")
print("Lesson 20: Building with Mistral Models")
print("Type 'exit' anytime to stop.\n")

while True:
    use_case = input("Enter use case: ")

    if use_case.lower().strip() in ["exit", "quit", "stop"]:
        print("Mistral model selection advisor ended.")
        break

    task_type = input("Task type, for example RAG, summarization, function calling, coding, translation: ")
    complexity_level = input("Complexity level, low / medium / high: ")
    rag_need = input("RAG need, yes / no / high: ")
    function_calling_need = input("Function calling need, yes / no / high: ")
    coding_need = input("Coding need, yes / no / high: ")
    multilingual_need = input("Multilingual need, yes / no / high: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    latency_sensitivity = input("Latency sensitivity, low / medium / high / very high: ")
    fine_tuning_need = input("Fine-tuning need, yes / no / high: ")
    license_flexibility_need = input("License flexibility need, yes / no / high: ")
    risk_level = input("Risk level, low / medium / high / very high: ")
    deployment_preference = input("Deployment preference, local / GitHub Models / cloud / Azure / hybrid / unsure: ")

    advice = generate_mistral_model_advice(
        use_case=use_case,
        task_type=task_type,
        complexity_level=complexity_level,
        rag_need=rag_need,
        function_calling_need=function_calling_need,
        coding_need=coding_need,
        multilingual_need=multilingual_need,
        cost_sensitivity=cost_sensitivity,
        latency_sensitivity=latency_sensitivity,
        fine_tuning_need=fine_tuning_need,
        license_flexibility_need=license_flexibility_need,
        risk_level=risk_level,
        deployment_preference=deployment_preference
    )

    print("\nGenerated Mistral Model Selection Advice:\n")
    print(advice)
    print("\n" + "=" * 100 + "\n")