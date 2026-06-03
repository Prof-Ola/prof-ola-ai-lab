# --------------------------------------------------
# Lesson 16 Build 4: Open Model Deployment Strategy Planner
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Generate deployment strategies for open and proprietary models
# based on privacy, cost, hardware, latency, expected users,
# maintenance burden, and risk level.
# --------------------------------------------------


def generate_deployment_strategy(
    use_case,
    model_name,
    task_type,
    privacy_requirement,
    budget_sensitivity,
    hardware_available,
    expected_users,
    latency_need,
    maintenance_capacity,
    risk_level,
    preferred_deployment
):
    """
    Generate a practical deployment strategy for an AI model.
    """

    local_score = 0
    hosted_open_api_score = 0
    cloud_score = 0
    hybrid_score = 0
    proprietary_fallback_score = 0

    privacy = privacy_requirement.lower()
    budget = budget_sensitivity.lower()
    hardware = hardware_available.lower()
    latency = latency_need.lower()
    maintenance = maintenance_capacity.lower()
    risk = risk_level.lower()
    preferred = preferred_deployment.lower()

    # Privacy scoring
    if privacy in ["high", "very high"]:
        local_score += 4
        hybrid_score += 2
    elif privacy == "medium":
        hybrid_score += 2
        hosted_open_api_score += 1
    else:
        hosted_open_api_score += 2
        proprietary_fallback_score += 1

    # Budget scoring
    if budget in ["high", "very high"]:
        local_score += 2
        hosted_open_api_score += 2
        hybrid_score += 2
    elif budget == "medium":
        hosted_open_api_score += 2
        hybrid_score += 1
    else:
        proprietary_fallback_score += 2
        cloud_score += 1

    # Hardware scoring
    if "gpu" in hardware or "strong" in hardware:
        local_score += 3
        hybrid_score += 1
    elif "basic" in hardware or "cpu" in hardware or "laptop" in hardware:
        hosted_open_api_score += 3
        hybrid_score += 2
        proprietary_fallback_score += 1
    elif "cloud" in hardware:
        cloud_score += 3
        hosted_open_api_score += 1

    # Users
    try:
        user_count = int(expected_users)
    except ValueError:
        user_count = 1

    if user_count <= 2:
        local_score += 2
        hybrid_score += 1
    elif 3 <= user_count <= 20:
        hosted_open_api_score += 2
        cloud_score += 1
        hybrid_score += 2
    else:
        cloud_score += 3
        hosted_open_api_score += 2

    # Latency scoring
    if latency in ["high", "very high"]:
        local_score += 1
        hosted_open_api_score += 2
        cloud_score += 2
    elif latency == "medium":
        hosted_open_api_score += 1
        hybrid_score += 1

    # Maintenance scoring
    if maintenance in ["low", "very low"]:
        hosted_open_api_score += 3
        proprietary_fallback_score += 2
    elif maintenance == "medium":
        hybrid_score += 2
        hosted_open_api_score += 1
    else:
        local_score += 2
        cloud_score += 2

    # Risk scoring
    if risk in ["high", "very high"]:
        proprietary_fallback_score += 2
        hybrid_score += 3
        local_score += 1
    elif risk == "medium":
        hybrid_score += 2

    # Preference scoring
    if "local" in preferred:
        local_score += 3
    elif "api" in preferred:
        hosted_open_api_score += 3
    elif "cloud" in preferred:
        cloud_score += 3
    elif "hybrid" in preferred:
        hybrid_score += 3

    scores = {
        "Local laptop / workstation deployment": local_score,
        "Hosted open model API": hosted_open_api_score,
        "Cloud deployment": cloud_score,
        "Hybrid deployment": hybrid_score,
        "Proprietary API fallback": proprietary_fallback_score
    }

    best_strategy = max(scores, key=scores.get)

    strategy_details = {
        "Local laptop / workstation deployment": """
Recommended deployment:
Run the model locally using tools such as Ollama, LM Studio, or local Hugging Face inference.

Best when:
- Privacy is very important.
- Expected users are few.
- You want low recurring cost.
- You can accept slower speed on basic hardware.
- You are experimenting or working with sensitive research notes.

Controls needed:
- Keep local files organized.
- Track model version.
- Do not assume local models are automatically safe.
- Evaluate output quality before relying on results.
""",
        "Hosted open model API": """
Recommended deployment:
Use hosted open model APIs through services such as Hugging Face, Groq, Together AI, Fireworks, Replicate, OpenRouter, or Azure AI Foundry.

Best when:
- You want open model flexibility without managing hardware.
- You need better speed than your laptop can provide.
- Budget matters but full local deployment is inconvenient.
- You want to compare multiple open models quickly.

Controls needed:
- Review provider terms.
- Avoid sending sensitive data unless approved.
- Track cost and latency.
- Log model name and version where possible.
""",
        "Cloud deployment": """
Recommended deployment:
Deploy the model or app in a cloud environment.

Best when:
- Multiple users need access.
- You need scalability.
- You need stronger monitoring.
- You can manage infrastructure and security.
- You have a defined deployment budget.

Controls needed:
- Add access control.
- Add logging and monitoring.
- Secure secrets and API keys.
- Add usage limits.
- Create a rollback plan.
""",
        "Hybrid deployment": """
Recommended deployment:
Use a hybrid model stack.

Best when:
- Some tasks can be handled cheaply by open/local models.
- Critical tasks need stronger proprietary models.
- Privacy-sensitive preprocessing should happen locally.
- Final synthesis can use a stronger hosted model.
- You want cost control without sacrificing quality.

Suggested pattern:
- Local/open model for classification, tagging, extraction, first drafts, and simple summaries.
- Premium model for final reasoning, manuscript refinement, grant logic, and complex synthesis.
- RAG layer to ground outputs.
- Human review for high-impact outputs.
""",
        "Proprietary API fallback": """
Recommended deployment:
Use a strong proprietary API as the fallback or primary model for critical tasks.

Best when:
- Quality is more important than cost.
- You need strong reasoning and instruction following.
- Your local/open model outputs are not reliable enough.
- You need fast implementation.

Controls needed:
- Track API costs.
- Avoid unnecessary sensitive data sharing.
- Add human review.
- Keep local/open fallback where possible.
"""
    }

    plan = f"""
# Open Model Deployment Strategy Plan

## 1. Use Case

{use_case}

## 2. Model Name

{model_name}

## 3. Task Type

{task_type}

## 4. Deployment Constraints

Privacy requirement:
{privacy_requirement}

Budget sensitivity:
{budget_sensitivity}

Hardware available:
{hardware_available}

Expected users:
{expected_users}

Latency need:
{latency_need}

Maintenance capacity:
{maintenance_capacity}

Risk level:
{risk_level}

Preferred deployment:
{preferred_deployment}

---

# 5. Deployment Strategy Scores

| Deployment Strategy | Score |
|---|---:|
| Local laptop / workstation deployment | {local_score} |
| Hosted open model API | {hosted_open_api_score} |
| Cloud deployment | {cloud_score} |
| Hybrid deployment | {hybrid_score} |
| Proprietary API fallback | {proprietary_fallback_score} |

## 6. Recommended Deployment Strategy

{best_strategy}

{strategy_details[best_strategy]}

---

# 7. ResearchLab Recommendation

For ResearchLab, the most practical starting strategy is usually:

1. Use local models for private experimentation and low-risk tasks.
2. Use hosted open models for faster testing and model comparison.
3. Use Claude, GPT, or Gemini for high-value synthesis, grant logic, and manuscript-level refinement.
4. Keep RAG as the grounding layer.
5. Use evaluation logs before trusting a model in real workflows.

---

# 8. Deployment Readiness Checklist

Before deployment, confirm:

- Model license allows intended use.
- Data privacy risks are understood.
- API keys are stored safely.
- Outputs are evaluated with test prompts.
- Prompt injection tests are performed.
- Cost and latency are tracked.
- Human review is required for high-impact outputs.
- Rollback plan exists.
- App version is documented.
- Users are told the output is AI-generated.

---

# 9. Suggested Next Action

Run the same model through your Lesson 16 experiment plan and compare it against at least two alternatives before adopting it.

Do not choose a model because it is fashionable. Choose it because it survives your tests.
"""
    return plan.strip()


print("\nOpen Model Deployment Strategy Planner")
print("Lesson 16: Build 4")
print("Type 'exit' anytime to stop.\n")

while True:
    use_case = input("Enter use case: ")

    if use_case.lower().strip() in ["exit", "quit", "stop"]:
        print("Open model deployment strategy planner ended.")
        break

    model_name = input("Enter model name: ")
    task_type = input("Enter task type, for example RAG, chat, summarization, coding: ")
    privacy_requirement = input("Privacy requirement, low / medium / high / very high: ")
    budget_sensitivity = input("Budget sensitivity, low / medium / high / very high: ")
    hardware_available = input("Hardware available, for example basic CPU laptop, strong GPU, cloud only: ")
    expected_users = input("Expected number of users, enter a number: ")
    latency_need = input("Latency need, low / medium / high / very high: ")
    maintenance_capacity = input("Maintenance capacity, low / medium / high: ")
    risk_level = input("Risk level, low / medium / high / very high: ")
    preferred_deployment = input("Preferred deployment, local / hosted API / cloud / hybrid / unsure: ")

    plan = generate_deployment_strategy(
        use_case=use_case,
        model_name=model_name,
        task_type=task_type,
        privacy_requirement=privacy_requirement,
        budget_sensitivity=budget_sensitivity,
        hardware_available=hardware_available,
        expected_users=expected_users,
        latency_need=latency_need,
        maintenance_capacity=maintenance_capacity,
        risk_level=risk_level,
        preferred_deployment=preferred_deployment
    )

    print("\nGenerated Open Model Deployment Strategy:\n")
    print(plan)
    print("\n" + "=" * 100 + "\n")