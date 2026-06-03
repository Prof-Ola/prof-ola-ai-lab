# --------------------------------------------------
# Lesson 14 Build 3: AI App Version Release Planner
# Microsoft Generative AI for Beginners adaptation
# Purpose: Plan AI app releases, readiness, risks, rollback,
# version changes, and lifecycle improvement steps.
# --------------------------------------------------


def generate_release_plan(
    app_name,
    current_version,
    next_version,
    release_goal,
    features_added,
    bugs_fixed,
    metrics_improved,
    risks_reduced,
    known_limitations,
    testing_completed,
    deployment_target,
    rollback_plan,
    release_owner
):
    plan = f"""
# AI App Version Release Plan

## 1. App Name

{app_name}

## 2. Current Version

{current_version}

## 3. Next Version

{next_version}

## 4. Release Goal

{release_goal}

---

# A. Features Added

{features_added}

Checklist:
- Are the new features clearly documented?
- Are users told what changed?
- Are new features tested with realistic prompts?
- Are new features aligned with the app's purpose?

---

# B. Bugs Fixed

{bugs_fixed}

Checklist:
- Were the bugs reproduced before fixing?
- Were the fixes tested?
- Did the fixes introduce any new issues?
- Were edge cases tested?

---

# C. Metrics Improved

{metrics_improved}

Suggested LLMOps metrics to review:
- Response quality
- Groundedness
- Safety
- Format consistency
- Latency
- Cost per request
- User usefulness rating
- Error rate
- Failed run frequency

---

# D. Risks Reduced

{risks_reduced}

Risk reduction checklist:
- Prompt injection resistance improved?
- Output validation improved?
- Human review warnings added?
- API key handling checked?
- Sensitive data handling improved?
- Error messages improved?
- RAG/document safety improved?
- Overreliance warnings added?

---

# E. Known Limitations

{known_limitations}

Release note:
These limitations should be documented clearly before the version is shared with any user.

---

# F. Testing Completed

{testing_completed}

Minimum test checklist:
- Normal user request test
- Empty input test
- Malformed input test
- Out-of-scope request test
- Prompt injection test
- Fake citation request test
- Low-evidence test
- System error handling test
- Human review warning test
- Output format consistency test

---

# G. Deployment Target

{deployment_target}

Deployment readiness:
- Local prototype: acceptable for learning and controlled personal use.
- Internal testing: requires access control, notes, and feedback collection.
- Controlled users: requires monitoring, security review, and rollback plan.
- Public deployment: requires stronger security, governance, privacy, and legal review.

---

# H. Rollback Plan

{rollback_plan}

Rollback checklist:
- Can the previous version still be used?
- Is the previous code available in GitHub?
- Are generated files or outputs backed up?
- Can API/model changes be reversed?
- Are users informed if the release is withdrawn?

---

# I. Release Owner

{release_owner}

Responsibilities:
- Approve the release.
- Confirm tests were completed.
- Review known limitations.
- Monitor early use.
- Decide whether to continue, revise, or roll back.

---

# J. Release Decision

Choose one:

[ ] Release approved
[ ] Release approved for personal testing only
[ ] Release approved for internal testing only
[ ] Release delayed pending fixes
[ ] Release rejected

Reason:
Write the reason for the release decision here.

---

# K. Recommended Next Version

After {next_version}, consider:

## Next improvement options
1. Add better logging.
2. Add feedback capture.
3. Add stronger security tests.
4. Add UX improvements.
5. Add evaluation test cases.
6. Add versioned prompts.
7. Add deployment documentation.
8. Add cost and latency tracking.

## Suggested version path
- {next_version}: Current planned release.
- v0.4: UX/security hardening.
- v0.5: Metrics and monitoring.
- v1.0: Controlled user release.
"""
    return plan.strip()


print("\nAI App Version Release Planner")
print("Lesson 14: Build 3")
print("Type 'exit' anytime to stop.\n")

while True:
    app_name = input("Enter AI app name: ")

    if app_name.lower().strip() in ["exit", "quit", "stop"]:
        print("AI app release planner ended.")
        break

    current_version = input("Enter current version, for example v0.1: ")
    next_version = input("Enter next version, for example v0.2: ")
    release_goal = input("What is the goal of this release? ")
    features_added = input("What features were added? ")
    bugs_fixed = input("What bugs were fixed? ")
    metrics_improved = input("What metrics improved or should improve? ")
    risks_reduced = input("What risks were reduced? ")
    known_limitations = input("What known limitations remain? ")
    testing_completed = input("What testing has been completed? ")
    deployment_target = input("Where will this version be used or deployed? ")
    rollback_plan = input("What is the rollback plan? ")
    release_owner = input("Who owns or approves this release? ")

    plan = generate_release_plan(
        app_name=app_name,
        current_version=current_version,
        next_version=next_version,
        release_goal=release_goal,
        features_added=features_added,
        bugs_fixed=bugs_fixed,
        metrics_improved=metrics_improved,
        risks_reduced=risks_reduced,
        known_limitations=known_limitations,
        testing_completed=testing_completed,
        deployment_target=deployment_target,
        rollback_plan=rollback_plan,
        release_owner=release_owner
    )

    print("\nGenerated AI App Version Release Plan:\n")
    print(plan)
    print("\n" + "=" * 100 + "\n")