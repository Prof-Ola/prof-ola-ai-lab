# --------------------------------------------------
# Lesson 19 Build 1: SLM Use-Case Fit Advisor
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Help decide whether a task should use a Small Language Model,
# Large Language Model, RAG + SLM, LLM fallback, or hybrid strategy.
# --------------------------------------------------


def generate_slm_fit_advice(
    use_case,
    task_type,
    complexity_level,
    privacy_requirement,
    cost_sensitivity,
    latency_requirement,
    offline_need,
    hardware_available,
    domain_specificity,
    reasoning_depth,
    output_risk,
    rag_available
):
    """
    Generate an SLM suitability recommendation.
    """

    slm_score = 0
    llm_score = 0
    rag_slm_score = 0
    hybrid_score = 0

    complexity = complexity_level.lower().strip()
    privacy = privacy_requirement.lower().strip()
    cost = cost_sensitivity.lower().strip()
    latency = latency_requirement.lower().strip()
    offline = offline_need.lower().strip()
    hardware = hardware_available.lower().strip()
    domain = domain_specificity.lower().strip()
    reasoning = reasoning_depth.lower().strip()
    risk = output_risk.lower().strip()
    rag = rag_available.lower().strip()

    # Complexity
    if complexity in ["low", "simple"]:
        slm_score += 3
        rag_slm_score += 1
    elif complexity == "medium":
        hybrid_score += 2
        rag_slm_score += 2
    else:
        llm_score += 3
        hybrid_score += 2

    # Privacy
    if privacy in ["high", "very high"]:
        slm_score += 3
        rag_slm_score += 2
        hybrid_score += 1
    elif privacy == "medium":
        hybrid_score += 1
        rag_slm_score += 1
    else:
        llm_score += 1

    # Cost
    if cost in ["high", "very high"]:
        slm_score += 3
        rag_slm_score += 2
        hybrid_score += 2
    elif cost == "medium":
        slm_score += 1
        hybrid_score += 1
    else:
        llm_score += 2

    # Latency
    if latency in ["high", "very high"]:
        slm_score += 3
        rag_slm_score += 2
    elif latency == "medium":
        hybrid_score += 1

    # Offline
    if offline in ["yes", "y", "high"]:
        slm_score += 4
        rag_slm_score += 2

    # Hardware
    if "basic" in hardware or "cpu" in hardware or "laptop" in hardware:
        slm_score += 2
        rag_slm_score += 1
    elif "gpu" in hardware or "strong" in hardware:
        slm_score += 2
        rag_slm_score += 2
        hybrid_score += 1
    elif "cloud" in hardware:
        llm_score += 1
        hybrid_score += 1

    # Domain specificity
    if domain in ["high", "very high"]:
        if rag in ["yes", "y", "available"]:
            rag_slm_score += 4
            hybrid_score += 2
        else:
            hybrid_score += 2
            llm_score += 1
    elif domain == "medium":
        rag_slm_score += 1
        hybrid_score += 1

    # Reasoning depth
    if reasoning in ["low", "simple"]:
        slm_score += 3
    elif reasoning == "medium":
        rag_slm_score += 2
        hybrid_score += 2
    else:
        llm_score += 4
        hybrid_score += 2

    # Output risk
    if risk in ["high", "very high"]:
        llm_score += 2
        hybrid_score += 3
    elif risk == "medium":
        hybrid_score += 2
        rag_slm_score += 1
    else:
        slm_score += 1

    scores = {
        "Small Language Model": slm_score,
        "Large Language Model": llm_score,
        "RAG + SLM": rag_slm_score,
        "Hybrid SLM + LLM": hybrid_score
    }

    best_strategy = max(scores, key=scores.get)

    strategy_details = {
        "Small Language Model": """
Recommended strategy:
Use a Small Language Model for this task.

Best fit when:
- The task is simple or repetitive.
- Cost control matters.
- Low latency matters.
- Offline or local use is needed.
- The output risk is low.
- The task does not require deep reasoning or broad synthesis.

Examples:
- Classification
- Simple summarization
- Drafting short templates
- Tagging research notes
- Basic extraction
- Simple chatbot responses
""",
        "Large Language Model": """
Recommended strategy:
Use a stronger Large Language Model.

Best fit when:
- The task needs complex reasoning.
- The output is high-stakes.
- The task needs deep synthesis.
- The user expects strong writing, analysis, or judgement.
- Accuracy and nuance matter more than cost.

Examples:
- Manuscript critique
- Grant strategy
- Complex literature synthesis
- High-value decision support
- Multi-step reasoning
""",
        "RAG + SLM": """
Recommended strategy:
Use RAG with a Small Language Model.

Best fit when:
- The task needs domain grounding.
- You have a local knowledge base.
- Privacy and cost matter.
- The model should answer from retrieved context.
- The task is not too complex.

Examples:
- Research note Q&A
- Postharvest terminology lookup
- Retrieval-based summaries
- Internal knowledge-base assistant
- Low-cost local ResearchLab assistant
""",
        "Hybrid SLM + LLM": """
Recommended strategy:
Use a hybrid SLM + LLM architecture.

Best fit when:
- Some tasks are simple and can be handled by an SLM.
- Some tasks require a stronger LLM.
- Cost must be controlled without sacrificing quality.
- Human review is needed for important outputs.
- You want an LLM fallback for difficult queries.

Suggested pattern:
- SLM for tagging, classification, extraction, draft summaries, and routing.
- RAG + SLM for grounded internal Q&A.
- LLM for final synthesis, complex reasoning, grant logic, and manuscript-level refinement.
"""
    }

    advice = f"""
# SLM Use-Case Fit Advice

## 1. Use Case

{use_case}

## 2. Task Type

{task_type}

---

# 3. Inputs Reviewed

Complexity level:
{complexity_level}

Privacy requirement:
{privacy_requirement}

Cost sensitivity:
{cost_sensitivity}

Latency requirement:
{latency_requirement}

Offline need:
{offline_need}

Hardware available:
{hardware_available}

Domain specificity:
{domain_specificity}

Reasoning depth:
{reasoning_depth}

Output risk:
{output_risk}

RAG available:
{rag_available}

---

# 4. Strategy Scores

| Strategy | Score |
|---|---:|
| Small Language Model | {slm_score} |
| Large Language Model | {llm_score} |
| RAG + SLM | {rag_slm_score} |
| Hybrid SLM + LLM | {hybrid_score} |

---

# 5. Recommended Strategy

{best_strategy}

{strategy_details[best_strategy]}

---

# 6. ResearchLab Guidance

For ResearchLab, SLMs are useful for:

1. Classifying research notes.
2. Extracting crop, method, context, and quality indicators.
3. Summarizing short retrieved chunks.
4. Running low-cost local experiments.
5. Acting as a first-pass assistant before Claude or another LLM reviews the output.

Do not use an SLM alone for:
- Final manuscript judgement.
- Complex grant strategy.
- High-stakes scientific interpretation.
- Unsupported recommendations to farmers or practitioners.

The strongest near-term architecture is:

SLM for low-cost local tasks
+
RAG for grounding
+
LLM fallback for complex synthesis
+
Human review for high-impact outputs
"""
    return advice.strip()


print("\nSLM Use-Case Fit Advisor")
print("Lesson 19: Small Language Models")
print("Type 'exit' anytime to stop.\n")

while True:
    use_case = input("Enter use case: ")

    if use_case.lower().strip() in ["exit", "quit", "stop"]:
        print("SLM use-case fit advisor ended.")
        break

    task_type = input("Task type, for example classification, summarization, RAG, chat, extraction: ")
    complexity_level = input("Complexity level, low / medium / high: ")
    privacy_requirement = input("Privacy requirement, low / medium / high / very high: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    latency_requirement = input("Latency requirement, low / medium / high / very high: ")
    offline_need = input("Offline need, yes / no / high: ")
    hardware_available = input("Hardware available, for example basic CPU laptop, strong GPU, cloud only: ")
    domain_specificity = input("Domain specificity, low / medium / high / very high: ")
    reasoning_depth = input("Reasoning depth needed, low / medium / high: ")
    output_risk = input("Output risk, low / medium / high / very high: ")
    rag_available = input("Is RAG available? yes / no / available: ")

    advice = generate_slm_fit_advice(
        use_case=use_case,
        task_type=task_type,
        complexity_level=complexity_level,
        privacy_requirement=privacy_requirement,
        cost_sensitivity=cost_sensitivity,
        latency_requirement=latency_requirement,
        offline_need=offline_need,
        hardware_available=hardware_available,
        domain_specificity=domain_specificity,
        reasoning_depth=reasoning_depth,
        output_risk=output_risk,
        rag_available=rag_available
    )

    print("\nGenerated SLM Use-Case Fit Advice:\n")
    print(advice)
    print("\n" + "=" * 100 + "\n")