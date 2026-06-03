# --------------------------------------------------
# Lesson 14 Build 1: AI App Lifecycle Planner
# Microsoft Generative AI for Beginners adaptation
# Purpose: Plan and manage the lifecycle of a generative AI application
# from ideation to building, evaluation, deployment, monitoring, and iteration.
# --------------------------------------------------


def diagnose_stage(current_stage):
    stage = current_stage.lower()

    if "idea" in stage or "explor" in stage or "prototype" in stage:
        return "Ideating / Exploring"

    if "build" in stage or "augment" in stage or "test" in stage or "rag" in stage:
        return "Building / Augmenting"

    if "deploy" in stage or "production" in stage or "monitor" in stage or "operational" in stage:
        return "Operationalizing"

    return "Unclear, treat as Ideating / Exploring until validated"


def generate_lifecycle_plan(
    app_name,
    app_purpose,
    target_users,
    current_stage,
    data_sources,
    ai_features,
    evaluation_metrics,
    risks,
    deployment_target,
    monitoring_needs
):
    lifecycle_stage = diagnose_stage(current_stage)

    plan = f"""
# Generative AI Application Lifecycle Plan

## 1. App Name

{app_name}

## 2. App Purpose

{app_purpose}

## 3. Target Users

{target_users}

## 4. Current Stage

User-described stage:
{current_stage}

Lifecycle diagnosis:
{lifecycle_stage}

## 5. Data Sources

{data_sources}

## 6. AI Features

{ai_features}

---

# A. Ideating / Exploring

Goal:
Confirm that the AI feature solves a real user or business problem before building too much.

Checklist:
- Define the problem clearly.
- Identify the primary user.
- Define the expected value.
- Confirm whether AI is actually needed.
- Test simple prompts manually.
- Compare possible models or tools.
- Identify required data sources.
- Define early success criteria.
- Identify risks before scaling.

Questions to answer:
- What user pain does this app solve?
- What task becomes easier, faster, safer, or better?
- What would make users trust this app?
- What could go wrong if the app gives a poor answer?

---

# B. Building / Augmenting

Goal:
Turn the idea into a working prototype and improve it with data, tools, RAG, function calling, evaluation, and guardrails.

Checklist:
- Build the first working prototype.
- Add structured prompts or system prompts.
- Add retrieval if external knowledge is needed.
- Add function calling if tool use is needed.
- Add error handling.
- Add UX messages for trust and transparency.
- Add security controls.
- Test with sample data.
- Evaluate outputs against expected results.
- Improve prompts, data structure, or workflow.

Current AI features to evaluate:
{ai_features}

---

# C. Operationalizing

Goal:
Prepare the app for real use with deployment, monitoring, cost control, safety, governance, and feedback.

Checklist:
- Define deployment environment.
- Add monitoring and logs.
- Track cost and usage.
- Track latency and response time.
- Add human review gates.
- Add feedback capture.
- Add security testing.
- Add version control.
- Document limitations.
- Define rollback plan.
- Decide who owns maintenance.

Deployment target:
{deployment_target}

---

# D. LLMOps Metrics

Track the following metrics:

## Quality
- Are responses useful?
- Are outputs relevant to the user task?
- Are formats consistent?
- Are answers complete enough?

Suggested metric:
{evaluation_metrics}

## Honesty / Groundedness
- Does the app avoid hallucinations?
- Does it stay within retrieved evidence?
- Does it admit when evidence is insufficient?

## Harm / Safety
- Does it avoid unsafe, biased, or inappropriate outputs?
- Does it resist prompt injection?
- Does it protect sensitive data?

## Cost
- What is the cost per request?
- How often is the API called?
- Can local models reduce cost?

## Latency
- How long does the app take to respond?
- Is the wait acceptable for users?
- Can caching or smaller models improve speed?

---

# E. Risk Register

Identified risks:
{risks}

Recommended controls:
- Add human review for high-impact outputs.
- Validate AI-generated claims.
- Keep API keys out of GitHub.
- Treat retrieved documents as untrusted data.
- Add prompt injection testing.
- Log failures and unusual behavior.
- Keep sensitive data out of prompts where possible.

---

# F. Monitoring Plan

Monitoring needs:
{monitoring_needs}

Suggested monitoring:
- Track number of requests.
- Track failed runs.
- Track user feedback.
- Track response time.
- Track API cost.
- Track hallucination or unsupported claim incidents.
- Track prompt injection attempts.
- Track low-confidence outputs.
- Review logs weekly during prototype testing.

---

# G. Feedback Loop

Suggested feedback questions:
1. Was the output useful?
2. Was the output accurate?
3. Was anything missing?
4. Did the response need human correction?
5. Should this output be trusted for real use?

Feedback categories:
- Useful
- Partly useful
- Not useful
- Incorrect
- Unsafe
- Needs more evidence
- Too long
- Too vague

---

# H. Versioning and Improvement Plan

Suggested version stages:

## Version 0.1
Basic prototype.

## Version 0.2
Add structured prompts and better error handling.

## Version 0.3
Add retrieval, CSV search, or document search.

## Version 0.4
Add UX messages, feedback, and human review warnings.

## Version 0.5
Add security tests and prompt injection resistance.

## Version 1.0
Ready for controlled users with monitoring and documented limitations.

---

# I. Immediate Next Actions

1. Confirm the app's current lifecycle stage.
2. Define three measurable evaluation metrics.
3. Add basic logging.
4. Add feedback capture.
5. Add prompt injection tests.
6. Add human review warnings.
7. Decide whether the app remains local, goes to AppSheet, or becomes a web app.
8. Document limitations in the README.
"""
    return plan.strip()


print("\nAI App Lifecycle Planner")
print("Lesson 14: Generative AI Application Lifecycle")
print("Type 'exit' anytime to stop.\n")

while True:
    app_name = input("Enter AI app name: ")

    if app_name.lower().strip() in ["exit", "quit", "stop"]:
        print("AI app lifecycle planner ended.")
        break

    app_purpose = input("What is the purpose of the app? ")
    target_users = input("Who are the target users? ")
    current_stage = input("What is the current stage, for example idea, prototype, testing, deployed? ")
    data_sources = input("What data sources does the app use? ")
    ai_features = input("What AI features does the app include? ")
    evaluation_metrics = input("What metrics should be used to evaluate success? ")
    risks = input("What risks or failure modes should be monitored? ")
    deployment_target = input("Where might the app be deployed or used? ")
    monitoring_needs = input("What needs to be monitored over time? ")

    plan = generate_lifecycle_plan(
        app_name=app_name,
        app_purpose=app_purpose,
        target_users=target_users,
        current_stage=current_stage,
        data_sources=data_sources,
        ai_features=ai_features,
        evaluation_metrics=evaluation_metrics,
        risks=risks,
        deployment_target=deployment_target,
        monitoring_needs=monitoring_needs
    )

    print("\nGenerated AI App Lifecycle Plan:\n")
    print(plan)
    print("\n" + "=" * 100 + "\n")