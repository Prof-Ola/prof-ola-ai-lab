# --------------------------------------------------
# Lesson 18 Build 1: Fine-Tuning Decision Advisor
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Help decide whether fine-tuning is justified, or whether
# prompt engineering, RAG, function calling, agents, or a hybrid
# approach should be tried first.
# --------------------------------------------------


def generate_fine_tuning_advice(
    use_case,
    current_problem,
    prompt_engineering_tried,
    rag_tried,
    function_calling_needed,
    agent_workflow_needed,
    data_available,
    data_quality,
    baseline_quality,
    cost_sensitivity,
    consistency_need,
    domain_behavior_need,
    evaluation_readiness,
    deployment_plan
):
    """
    Generate a fine-tuning decision recommendation.
    """

    fine_tuning_score = 0
    prompt_score = 0
    rag_score = 0
    function_calling_score = 0
    agent_score = 0
    hybrid_score = 0

    # Prompt engineering
    if prompt_engineering_tried.lower() in ["no", "n"]:
        prompt_score += 4
        hybrid_score += 1
    else:
        fine_tuning_score += 1

    # RAG
    if rag_tried.lower() in ["no", "n"]:
        if "knowledge" in current_problem.lower() or "citation" in current_problem.lower() or "evidence" in current_problem.lower():
            rag_score += 4
        else:
            rag_score += 2
    else:
        fine_tuning_score += 1

    # Function calling
    if function_calling_needed.lower() in ["yes", "y", "high"]:
        function_calling_score += 4
        hybrid_score += 2

    # Agents
    if agent_workflow_needed.lower() in ["yes", "y", "high"]:
        agent_score += 4
        hybrid_score += 2

    # Data availability
    if data_available.lower() in ["yes", "y", "high"]:
        fine_tuning_score += 3
    else:
        fine_tuning_score -= 4
        prompt_score += 2
        rag_score += 2

    # Data quality
    if data_quality.lower() in ["high", "very high"]:
        fine_tuning_score += 3
    elif data_quality.lower() == "medium":
        fine_tuning_score += 1
        hybrid_score += 1
    else:
        fine_tuning_score -= 3

    # Baseline quality
    if baseline_quality.lower() in ["poor", "weak", "low"]:
        fine_tuning_score += 2
    elif baseline_quality.lower() in ["good", "strong", "high"]:
        prompt_score += 2
        rag_score += 1
        fine_tuning_score -= 1

    # Cost
    if cost_sensitivity.lower() in ["high", "very high"]:
        fine_tuning_score -= 2
        prompt_score += 2
        rag_score += 2
    else:
        fine_tuning_score += 1

    # Consistency
    if consistency_need.lower() in ["high", "very high"]:
        fine_tuning_score += 3
        hybrid_score += 1

    # Domain behavior
    if domain_behavior_need.lower() in ["high", "very high"]:
        fine_tuning_score += 3
        hybrid_score += 1

    # Evaluation readiness
    if evaluation_readiness.lower() in ["yes", "y", "high"]:
        fine_tuning_score += 2
    else:
        fine_tuning_score -= 3

    # Deployment
    if deployment_plan.lower() in ["clear", "ready", "yes"]:
        fine_tuning_score += 1
    else:
        fine_tuning_score -= 1
        hybrid_score += 1

    scores = {
        "Prompt engineering first": prompt_score,
        "RAG first": rag_score,
        "Function calling first": function_calling_score,
        "Agent workflow first": agent_score,
        "Fine-tuning justified": fine_tuning_score,
        "Hybrid approach": hybrid_score
    }

    best_strategy = max(scores, key=scores.get)

    if fine_tuning_score >= 8 and fine_tuning_score >= max(prompt_score, rag_score, function_calling_score, agent_score):
        decision = "Fine-tuning may be justified, but only after confirming baseline results and evaluation criteria."
    elif best_strategy == "Fine-tuning justified":
        decision = "Fine-tuning is possible, but the case is not yet strong enough. Strengthen data and evaluation first."
    else:
        decision = f"Do not fine-tune yet. Use {best_strategy.lower()}."

    plan = f"""
# Fine-Tuning Decision Advice

## 1. Use Case

{use_case}

## 2. Current Problem

{current_problem}

---

# 3. Inputs Reviewed

Prompt engineering tried:
{prompt_engineering_tried}

RAG tried:
{rag_tried}

Function calling needed:
{function_calling_needed}

Agent workflow needed:
{agent_workflow_needed}

Data available:
{data_available}

Data quality:
{data_quality}

Baseline quality:
{baseline_quality}

Cost sensitivity:
{cost_sensitivity}

Need for consistent style or format:
{consistency_need}

Need for domain-specific behavior:
{domain_behavior_need}

Evaluation readiness:
{evaluation_readiness}

Deployment plan:
{deployment_plan}

---

# 4. Strategy Scores

| Strategy | Score |
|---|---:|
| Prompt engineering first | {prompt_score} |
| RAG first | {rag_score} |
| Function calling first | {function_calling_score} |
| Agent workflow first | {agent_score} |
| Fine-tuning justified | {fine_tuning_score} |
| Hybrid approach | {hybrid_score} |

---

# 5. Recommendation

{decision}

## Best current strategy

{best_strategy}

---

# 6. Practical Interpretation

Fine-tuning should not be the first move.

Use fine-tuning only when:
- Prompt engineering has been tested and is insufficient.
- RAG has been tested where external knowledge is needed.
- You have enough high-quality examples.
- You have a clear evaluation method.
- You know what behavior should change.
- The expected benefit outweighs cost, complexity, and maintenance.

Do not fine-tune just because the model is imperfect.
Many problems are better solved by better prompts, better retrieval, better data structure, function calling, or agent workflows.

---

# 7. Recommended Next Actions

1. Create a baseline using prompt engineering.
2. Create a RAG baseline if the problem requires factual grounding.
3. Define evaluation metrics.
4. Collect high-quality input-output examples.
5. Compare baseline vs improved approach.
6. Only consider fine-tuning if the baseline still fails in a repeated, measurable way.

---

# 8. ResearchLab Guidance

For ResearchLab, fine-tuning is not the immediate priority.

Current better priorities:
- Improve RAG metadata.
- Improve chunking strategy.
- Add source attribution.
- Benchmark embedding models.
- Strengthen evaluation logging.
- Build domain-specific prompt templates.
- Use agent workflows for planning and review.

Fine-tuning may become useful later for:
- Consistent academic formatting.
- Repeated domain-specific classification.
- Structured extraction from research notes.
- Specialist style adaptation after enough examples are collected.
"""
    return plan.strip()


print("\nFine-Tuning Decision Advisor")
print("Lesson 18: Fine-Tuning Models")
print("Type 'exit' anytime to stop.\n")

while True:
    use_case = input("Enter use case: ")

    if use_case.lower().strip() in ["exit", "quit", "stop"]:
        print("Fine-tuning decision advisor ended.")
        break

    current_problem = input("What problem are you trying to fix? ")
    prompt_engineering_tried = input("Have you tried prompt engineering? yes / no: ")
    rag_tried = input("Have you tried RAG if external knowledge is needed? yes / no: ")
    function_calling_needed = input("Does the task need structured tool use or function calling? yes / no / high: ")
    agent_workflow_needed = input("Does the task need multi-step agent workflow? yes / no / high: ")
    data_available = input("Do you have enough training examples? yes / no / high: ")
    data_quality = input("Training data quality, low / medium / high / very high: ")
    baseline_quality = input("Current baseline quality, poor / weak / medium / good / strong: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    consistency_need = input("Need for consistent style or format, low / medium / high / very high: ")
    domain_behavior_need = input("Need for domain-specific behavior, low / medium / high / very high: ")
    evaluation_readiness = input("Are evaluation metrics ready? yes / no / high: ")
    deployment_plan = input("Deployment plan status, unclear / partial / clear / ready / yes: ")

    advice = generate_fine_tuning_advice(
        use_case=use_case,
        current_problem=current_problem,
        prompt_engineering_tried=prompt_engineering_tried,
        rag_tried=rag_tried,
        function_calling_needed=function_calling_needed,
        agent_workflow_needed=agent_workflow_needed,
        data_available=data_available,
        data_quality=data_quality,
        baseline_quality=baseline_quality,
        cost_sensitivity=cost_sensitivity,
        consistency_need=consistency_need,
        domain_behavior_need=domain_behavior_need,
        evaluation_readiness=evaluation_readiness,
        deployment_plan=deployment_plan
    )

    print("\nGenerated Fine-Tuning Decision Advice:\n")
    print(advice)
    print("\n" + "=" * 100 + "\n")