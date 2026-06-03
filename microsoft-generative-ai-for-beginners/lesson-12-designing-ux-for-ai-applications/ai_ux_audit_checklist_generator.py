# --------------------------------------------------
# Lesson 12 Build 3: AI UX Audit Checklist Generator
# Microsoft Generative AI for Beginners adaptation
# Purpose: Audit AI apps for usability, trust, transparency,
# accessibility, control, feedback, and responsible UX.
# --------------------------------------------------


def generate_ux_audit(
    app_name,
    app_purpose,
    target_users,
    main_ai_outputs,
    data_used,
    high_risk_areas,
    current_feedback_method,
    current_error_handling
):
    audit = f"""
# AI UX Audit Checklist

## 1. App Name

{app_name}

## 2. App Purpose

{app_purpose}

## 3. Target Users

{target_users}

## 4. Main AI Outputs

{main_ai_outputs}

## 5. Data Used by the App

{data_used}

## 6. High-Risk Areas

{high_risk_areas}

---

# A. Usefulness

Check whether the app clearly helps users complete a real task.

Questions:
- Does the app solve a specific user problem?
- Are the outputs actionable?
- Does the app reduce time, confusion, or effort?
- Is the app focused, or is it trying to do too many things?

Recommended improvement:
Make the primary user task clear on the first screen or first message.

---

# B. Reliability

Check whether the app performs consistently and handles mistakes well.

Questions:
- Does the app produce consistent output formats?
- Does it validate required inputs?
- Does it handle missing data?
- Does it show a clear error message when something fails?
- Does it avoid pretending to know when evidence is limited?

Current error handling:
{current_error_handling}

Recommended improvement:
Add structured error messages for missing data, low confidence, out-of-scope requests, and evidence limitations.

---

# C. Accessibility

Check whether different users can access and use the app.

Questions:
- Can the app be used with keyboard navigation?
- Are instructions clear and simple?
- Is the language understandable to non-technical users?
- Are outputs readable and not overloaded?
- If visual outputs are used, is there alternative text or explanation?

Recommended improvement:
Use plain language, clear headings, short paragraphs, and accessible colour contrast in any interface.

---

# D. Pleasantness

Check whether the app feels respectful, clear, and easy to use.

Questions:
- Does the app greet users clearly?
- Does it guide users step by step?
- Are error messages friendly rather than blaming the user?
- Does the app avoid overwhelming users with long unstructured outputs?

Recommended improvement:
Use warm onboarding, concise instructions, and optional deeper details instead of dumping everything at once.

---

# E. Trust and Transparency

Check whether users understand that AI is involved and what its limits are.

Questions:
- Does the app clearly say when output is AI-generated?
- Does it explain what the AI can and cannot do?
- Does it warn users to verify important claims?
- Does it avoid fake citations, fake certainty, or overclaiming?

Recommended improvement:
Add a visible notice: "AI-generated output. Please review and verify important claims before use."

---

# F. User Control

Check whether users remain in control of the AI process.

Questions:
- Can users edit the input?
- Can users reject or revise the output?
- Can users choose whether data is saved?
- Can users ask for shorter, longer, simpler, or more technical versions?

Recommended improvement:
Add options such as revise, regenerate, shorten, expand, simplify, and discard.

---

# G. Human Review

Check whether human review is required where needed.

High-risk areas:
{high_risk_areas}

Questions:
- Is human review required before academic, financial, legal, health, student, or institutional decisions?
- Does the app flag outputs that should not be used directly?
- Are users warned not to submit AI outputs without review?

Recommended improvement:
Add human review notices for high-risk outputs.

---

# H. Feedback Loop

Current feedback method:
{current_feedback_method}

Questions:
- Can users rate the response?
- Can users explain what was wrong or missing?
- Is feedback stored or reviewed?
- Is there a way to improve the app based on feedback?

Recommended improvement:
Add a simple feedback option: useful, partly useful, not useful, plus a short comment field.

---

# I. Data Privacy and Security

Check whether user data is handled responsibly.

Questions:
- What data does the app collect?
- Is sensitive information necessary?
- Are users warned before entering confidential data?
- Are API keys excluded from public repositories?
- Are files, logs, and outputs stored safely?

Recommended improvement:
Add a data notice and avoid collecting unnecessary sensitive data.

---

# J. Overall UX Readiness Score

Score each category from 1 to 5:

- Usefulness:
- Reliability:
- Accessibility:
- Pleasantness:
- Trust and transparency:
- User control:
- Human review:
- Feedback:
- Privacy and security:

Interpretation:
- 40 to 45: Strong UX readiness
- 30 to 39: Good but needs refinement
- 20 to 29: Prototype stage
- Below 20: Not ready for users

---

# Final Recommendation

Before making {app_name} user-facing, improve the following:

1. Add clear AI-generated output notices.
2. Add human review warnings for high-risk outputs.
3. Add user feedback capture.
4. Add friendly error messages.
5. Add user control options for revision, regeneration, and rejection.
"""
    return audit.strip()


print("\nAI UX Audit Checklist Generator")
print("Lesson 12: Build 3")
print("Type 'exit' anytime to stop.\n")

while True:
    app_name = input("Enter app name: ")

    if app_name.lower().strip() in ["exit", "quit", "stop"]:
        print("UX audit checklist generator ended.")
        break

    app_purpose = input("What is the purpose of the app? ")
    target_users = input("Who are the target users? ")
    main_ai_outputs = input("What are the main AI outputs? ")
    data_used = input("What data does the app use? ")
    high_risk_areas = input("What are the high-risk areas? ")
    current_feedback_method = input("What feedback method currently exists? ")
    current_error_handling = input("How does the app currently handle errors? ")

    audit = generate_ux_audit(
        app_name=app_name,
        app_purpose=app_purpose,
        target_users=target_users,
        main_ai_outputs=main_ai_outputs,
        data_used=data_used,
        high_risk_areas=high_risk_areas,
        current_feedback_method=current_feedback_method,
        current_error_handling=current_error_handling
    )

    print("\nGenerated AI UX Audit Checklist:\n")
    print(audit)
    print("\n" + "=" * 100 + "\n")