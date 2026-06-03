# --------------------------------------------------
# Lesson 12 Build 1: AI UX Message Framework Generator
# Microsoft Generative AI for Beginners adaptation
# Purpose: Generate UX messages for trustworthy, transparent,
# usable, and user-controlled AI applications.
# --------------------------------------------------


def generate_ux_framework(
    app_name,
    app_purpose,
    target_users,
    ai_tasks,
    user_control_options,
    human_review_needed,
    data_used,
    feedback_method
):
    """
    Generate UX messages for an AI application.
    """

    framework = f"""
# AI UX Message Framework

## 1. App Name

{app_name}

## 2. App Purpose

{app_purpose}

## 3. Target Users

{target_users}

## 4. Clear Capability Statement

This AI tool is designed to help with:

{ai_tasks}

It can support users by generating suggestions, summaries, structured outputs, or decision-support information based on the data provided.

## 5. Limitation Statement

This AI tool may make mistakes, misunderstand context, or produce incomplete outputs.

Users should not treat its output as final without review, especially where academic, financial, legal, health, student assessment, or institutional decisions are involved.

## 6. Human Review Notice

Human review is required for:

{human_review_needed}

The AI should assist decision-making, not replace responsible human judgement.

## 7. Data Use Notice

This tool may use the following user-provided data:

{data_used}

Users should avoid entering unnecessary sensitive or confidential information unless the system is approved for that use.

## 8. User Control Options

Users should be able to:

{user_control_options}

## 9. Feedback Prompt

After receiving an AI output, show users this feedback prompt:

"Was this response useful?"

Options:
- Yes, this was useful.
- Partly useful, but needs improvement.
- No, this was not useful.

Follow-up question:
"What should be improved?"

## 10. Friendly Error Message

If the AI cannot complete the task, show:

"Sorry, I could not complete that request properly. Please check whether the input is clear and complete. You can try again with more detail, or ask for a simpler output."

## 11. Out-of-Scope Message

If the user asks for something outside the app's purpose, show:

"This request may be outside what {app_name} is designed to support. I can help with {app_purpose}, but this request may require another tool, expert, or verified source."

## 12. Trust and Transparency Message

Show this near important AI outputs:

"AI-generated output. Please review before using. Important claims, references, data, or recommendations should be verified."

## 13. Pleasant Onboarding Message

Welcome to {app_name}.

This tool is here to support {target_users} by helping with {app_purpose}. Start by describing what you want to do, and the system will guide you step by step.

## 14. UX Design Checklist

Before deploying the app, check:

- Is the app easy to understand?
- Is the user told what the AI can and cannot do?
- Can users edit or reject AI outputs?
- Is there a feedback option?
- Are error messages clear and respectful?
- Is sensitive data protected?
- Is human review required for important outputs?
- Can the app be used with keyboard navigation?
- Are labels and instructions clear?
- Is the design accessible for users with different abilities?
"""
    return framework.strip()


print("\nAI UX Message Framework Generator")
print("Lesson 12: Designing UX for AI Applications")
print("Type 'exit' anytime to stop.\n")

while True:
    app_name = input("Enter AI app name: ")

    if app_name.lower().strip() in ["exit", "quit", "stop"]:
        print("UX framework generator ended.")
        break

    app_purpose = input("What is the purpose of the app? ")
    target_users = input("Who are the target users? ")
    ai_tasks = input("What AI tasks does the app perform? ")
    user_control_options = input("What control options should users have? ")
    human_review_needed = input("Where is human review needed? ")
    data_used = input("What user data or documents does the app use? ")
    feedback_method = input("How should users give feedback? ")

    framework = generate_ux_framework(
        app_name=app_name,
        app_purpose=app_purpose,
        target_users=target_users,
        ai_tasks=ai_tasks,
        user_control_options=user_control_options,
        human_review_needed=human_review_needed,
        data_used=data_used,
        feedback_method=feedback_method
    )

    print("\nGenerated AI UX Framework:\n")
    print(framework)
    print("\n" + "=" * 100 + "\n")