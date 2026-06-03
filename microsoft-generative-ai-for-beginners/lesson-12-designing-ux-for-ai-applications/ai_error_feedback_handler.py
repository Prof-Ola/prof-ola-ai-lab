# --------------------------------------------------
# Lesson 12 Build 2: AI Error and Feedback Handler
# Microsoft Generative AI for Beginners adaptation
# Purpose: Generate clear, trustworthy, user-friendly AI app responses
# for errors, limitations, feedback, and human review.
# --------------------------------------------------


def get_error_response(error_type, app_name, user_task, missing_info="", suggested_action=""):
    """
    Return a user-friendly message based on the error or UX situation.
    """

    responses = {
        "unclear_input": f"""
I need a little more detail before I can help properly.

App: {app_name}
Task: {user_task}

What is unclear:
The request does not provide enough context for a reliable response.

Please clarify:
{missing_info if missing_info else "- the topic\n- the desired output\n- the target audience or context"}

Suggested next step:
{suggested_action if suggested_action else "Please restate your request with more specific details."}
""",

        "missing_data": f"""
I cannot complete this task because some required information is missing.

App: {app_name}
Task: {user_task}

Missing information:
{missing_info if missing_info else "Required data was not provided."}

Suggested next step:
{suggested_action if suggested_action else "Please provide the missing information and try again."}
""",

        "low_confidence": f"""
I can provide a draft response, but confidence is limited.

App: {app_name}
Task: {user_task}

Reason:
The available information may be incomplete, too broad, or not sufficiently verified.

Recommended action:
{suggested_action if suggested_action else "Please review the output carefully and verify important claims before using it."}
""",

        "out_of_scope": f"""
This request may be outside what {app_name} is designed to support.

Requested task:
{user_task}

This tool is intended to support its defined AI workflow, and this request may require another tool, expert, or verified source.

Suggested next step:
{suggested_action if suggested_action else "Please reframe the request within the app's purpose or use a more suitable tool."}
""",

        "evidence_limitation": f"""
The available evidence is not enough to make a strong claim.

App: {app_name}
Task: {user_task}

Evidence limitation:
{missing_info if missing_info else "The current records, notes, or sources do not provide enough support."}

Suggested next step:
{suggested_action if suggested_action else "Add more verified sources, documents, or records before drawing conclusions."}
""",

        "human_review_required": f"""
Human review is required before this output is used.

App: {app_name}
Task: {user_task}

Why review is needed:
This output may influence academic, institutional, financial, legal, research, student, or stakeholder decisions.

Suggested review:
{suggested_action if suggested_action else "Please check accuracy, context, tone, evidence, and appropriateness before sharing or submitting."}
""",

        "system_error": f"""
Something went wrong while processing the request.

App: {app_name}
Task: {user_task}

Possible reason:
There may be a system, API, file, data, or formatting issue.

Suggested next step:
{suggested_action if suggested_action else "Please try again. If the issue continues, check the input data, file paths, API keys, or system logs."}
""",

        "feedback_request": f"""
Was this response useful?

Please choose one:
1. Yes, this was useful.
2. Partly useful, but needs improvement.
3. No, this was not useful.

Optional:
What should be improved?
"""
    }

    return responses.get(error_type, responses["system_error"]).strip()


print("\nResearchLab AI Error and Feedback Handler")
print("Lesson 12: Build 2")
print("Type 'exit' anytime to stop.\n")

error_types = [
    "unclear_input",
    "missing_data",
    "low_confidence",
    "out_of_scope",
    "evidence_limitation",
    "human_review_required",
    "system_error",
    "feedback_request"
]

print("Available error/feedback types:")
for item in error_types:
    print(f"- {item}")

print()

while True:
    error_type = input("Enter error or feedback type: ")

    if error_type.lower().strip() in ["exit", "quit", "stop"]:
        print("Error and feedback handler ended.")
        break

    if error_type not in error_types:
        print("Unknown type. Please choose one from the list.\n")
        continue

    app_name = input("Enter app name: ")
    user_task = input("Enter user task: ")
    missing_info = input("Enter missing info, limitation, or reason: ")
    suggested_action = input("Enter suggested action: ")

    message = get_error_response(
        error_type=error_type,
        app_name=app_name,
        user_task=user_task,
        missing_info=missing_info,
        suggested_action=suggested_action
    )

    print("\nGenerated UX Message:\n")
    print(message)
    print("\n" + "=" * 100 + "\n")