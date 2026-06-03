# --------------------------------------------------
# Lesson 16 Build 1: Open Model Selection Advisor
# Microsoft Generative AI for Beginners adaptation
# Purpose: Help choose between proprietary APIs, open model APIs,
# local open models, and hybrid model strategies.
# --------------------------------------------------


def generate_model_strategy(
    use_case,
    task_type,
    budget_sensitivity,
    privacy_requirement,
    quality_requirement,
    latency_requirement,
    local_deployment_need,
    fine_tuning_need,
    hardware_available,
    expected_users
):
    """
    Generate a practical model strategy based on project constraints.
    """

    score_open_local = 0
    score_open_api = 0
    score_proprietary = 0
    score_hybrid = 0

    # Budget
    if budget_sensitivity.lower() in ["high", "very high"]:
        score_open_local += 2
        score_open_api += 2
        score_hybrid += 1
    else:
        score_proprietary += 1

    # Privacy
    if privacy_requirement.lower() in ["high", "very high"]:
        score_open_local += 3
        score_hybrid += 1
    else:
        score_open_api += 1
        score_proprietary += 1

    # Quality
    if quality_requirement.lower() in ["high", "very high"]:
        score_proprietary += 3
        score_hybrid += 2
    else:
        score_open_api += 2
        score_open_local += 1

    # Latency
    if latency_requirement.lower() in ["high", "very high"]:
        score_open_local += 1
        score_open_api += 2
        score_hybrid += 1

    # Local deployment
    if local_deployment_need.lower() in ["yes", "y", "high"]:
        score_open_local += 4
        score_hybrid += 1

    # Fine-tuning
    if fine_tuning_need.lower() in ["yes", "y", "high"]:
        score_open_local += 2
        score_open_api += 2
        score_hybrid += 2

    # Hardware
    if "gpu" in hardware_available.lower() or "strong" in hardware_available.lower():
        score_open_local += 2
    elif "basic" in hardware_available.lower() or "cpu" in hardware_available.lower():
        score_open_api += 2
        score_proprietary += 1

    scores = {
        "Local open model": score_open_local,
        "Hosted open model API": score_open_api,
        "Proprietary model API": score_proprietary,
        "Hybrid strategy": score_hybrid
    }

    best_strategy = max(scores, key=scores.get)

    recommendations = {
        "Local open model": """
Recommended strategy:
Use a local open model through tools such as Ollama, LM Studio, or local Hugging Face inference.

Best fit when:
- Privacy is important.
- Budget must be controlled.
- You want offline or local experimentation.
- You are willing to accept lower quality than frontier proprietary models.
- You have enough hardware or can use smaller models.

Possible model families to test:
- Llama family
- Mistral family
- Mixtral family
- Phi family
- Qwen family
""",
        "Hosted open model API": """
Recommended strategy:
Use hosted open models through platforms such as Hugging Face, Groq, Together, Fireworks, Replicate, OpenRouter, or Azure AI Foundry.

Best fit when:
- You want lower cost than frontier proprietary models.
- You do not want to manage hardware.
- You want access to multiple open models.
- You want faster experimentation.

Possible model families to test:
- Llama
- Mistral / Mixtral
- Qwen
- DeepSeek
- Falcon
""",
        "Proprietary model API": """
Recommended strategy:
Use a strong proprietary model such as Claude, GPT, or Gemini for high-value tasks.

Best fit when:
- Quality and reliability matter more than cost.
- You need strong reasoning, writing, coding, or instruction following.
- You need stable performance for critical workflows.
- You are willing to pay per API usage.

Use this for:
- Manuscript drafting support
- Grant concept refinement
- Complex reasoning
- High-stakes summaries requiring careful human review
""",
        "Hybrid strategy": """
Recommended strategy:
Use a hybrid model stack.

Best fit when:
- Some tasks are simple and should be cheap.
- Some tasks are critical and need a stronger model.
- You want to reduce cost without sacrificing quality.
- You want local/private processing for sensitive data and premium models for advanced reasoning.

Suggested pattern:
- Local/open model for classification, tagging, summaries, and simple drafts.
- Proprietary model for final synthesis, complex reasoning, grant logic, and manuscript-level refinement.
"""
    }

    plan = f"""
# Open Model Selection Strategy

## 1. Use Case

{use_case}

## 2. Task Type

{task_type}

## 3. Project Constraints

Budget sensitivity:
{budget_sensitivity}

Privacy requirement:
{privacy_requirement}

Quality requirement:
{quality_requirement}

Latency requirement:
{latency_requirement}

Local deployment need:
{local_deployment_need}

Fine-tuning need:
{fine_tuning_need}

Hardware available:
{hardware_available}

Expected users:
{expected_users}

---

# 4. Strategy Scores

| Strategy | Score |
|---|---:|
| Local open model | {score_open_local} |
| Hosted open model API | {score_open_api} |
| Proprietary model API | {score_proprietary} |
| Hybrid strategy | {score_hybrid} |

## 5. Recommended Strategy

{best_strategy}

{recommendations[best_strategy]}

---

# 6. Practical Recommendation for AI Lab

For ResearchLab, Business Ops, and Trading Lab, the safest default is usually a hybrid strategy:

1. Use local or cheaper open models for low-risk, repetitive, or high-volume tasks.
2. Use premium proprietary models for high-value reasoning, final synthesis, or sensitive interpretation.
3. Never choose a model only by popularity.
4. Test models against your own tasks before trusting them.
5. Track cost, quality, groundedness, speed, and failure modes.

---

# 7. Model Evaluation Checklist

Before adopting a model, test:

- Does it answer your domain questions well?
- Does it hallucinate citations or facts?
- Does it follow formatting instructions?
- Does it handle long context?
- Does it support your language and tone needs?
- Is it affordable for your expected usage?
- Is it fast enough?
- Can it be deployed locally if privacy requires it?
- Does the license allow your intended use?
- Can you monitor and evaluate outputs?
"""
    return plan.strip()


print("\nOpen Model Selection Advisor")
print("Lesson 16: Open Source / Open Models")
print("Type 'exit' anytime to stop.\n")

while True:
    use_case = input("Enter use case: ")

    if use_case.lower().strip() in ["exit", "quit", "stop"]:
        print("Open model selection advisor ended.")
        break

    task_type = input("Enter task type, for example RAG, summarization, coding, classification, chat: ")
    budget_sensitivity = input("Budget sensitivity, low / medium / high / very high: ")
    privacy_requirement = input("Privacy requirement, low / medium / high / very high: ")
    quality_requirement = input("Quality requirement, low / medium / high / very high: ")
    latency_requirement = input("Latency requirement, low / medium / high / very high: ")
    local_deployment_need = input("Need local deployment? yes / no / high: ")
    fine_tuning_need = input("Need fine-tuning? yes / no / high: ")
    hardware_available = input("Hardware available, for example basic CPU laptop, strong GPU, cloud only: ")
    expected_users = input("Expected users: ")

    strategy = generate_model_strategy(
        use_case=use_case,
        task_type=task_type,
        budget_sensitivity=budget_sensitivity,
        privacy_requirement=privacy_requirement,
        quality_requirement=quality_requirement,
        latency_requirement=latency_requirement,
        local_deployment_need=local_deployment_need,
        fine_tuning_need=fine_tuning_need,
        hardware_available=hardware_available,
        expected_users=expected_users
    )

    print("\nGenerated Open Model Selection Strategy:\n")
    print(strategy)
    print("\n" + "=" * 100 + "\n")