# --------------------------------------------------
# Lesson 10 Build 3: AppSheet Automation Prompt Generator
# Microsoft Generative AI for Beginners adaptation
# Purpose: Generate low-code automation prompts for AppSheet, n8n,
# Power Automate, and AI-assisted workflow messages.
# --------------------------------------------------


def build_automation_blueprint(
    solution_name,
    trigger_event,
    data_source,
    condition,
    action,
    recipients,
    message_purpose,
    ai_assistance,
    success_outcome
):
    blueprint = f"""
# Low-Code Automation Blueprint

## 1. Solution Name

{solution_name}

## 2. Automation Trigger

The automation should start when:

{trigger_event}

## 3. Data Source

The automation should use data from:

{data_source}

## 4. Condition or Rule

The automation should only run when:

{condition}

## 5. Main Action

The automation should perform this action:

{action}

## 6. Recipients or Users Affected

The automation should notify or update:

{recipients}

## 7. Message Purpose

The message or output should:

{message_purpose}

## 8. AI Assistance Needed

AI should help with:

{ai_assistance}

## 9. AppSheet Automation Prompt

Use this prompt in AppSheet Automation or as your design instruction:

"Create an automation for {solution_name}. The automation should trigger when {trigger_event}. It should use data from {data_source}. It should only run when {condition}. The automation should {action}. It should notify or update {recipients}. The message should {message_purpose}. If AI support is available, use it to {ai_assistance}. Add logging so each automation run is recorded."

## 10. n8n Workflow Prompt

Use this prompt in n8n or an AI workflow builder:

"Build an n8n workflow for {solution_name}. Trigger the workflow when {trigger_event}. Read data from {data_source}. Check this condition: {condition}. If the condition is true, perform this action: {action}. Send the result to {recipients}. Use AI to {ai_assistance}. Store a log of the workflow execution, including timestamp, record ID, status, and any error message."

## 11. Power Automate Equivalent Prompt

Use this prompt in Power Automate Copilot if access is available:

"Create a Power Automate flow for {solution_name}. The flow should trigger when {trigger_event}. It should connect to {data_source}, check whether {condition}, then {action}. It should notify {recipients}. Use AI Builder or Create Text with GPT to {ai_assistance}. Add error handling and log each run."

## 12. AI Text Generation Prompt

Use this prompt inside Claude, Gemini, ChatGPT, AI Builder, or another text-generation model:

"Write a clear, professional message for {recipients}. The purpose of the message is to {message_purpose}. Use the following context from {solution_name}: trigger event = {trigger_event}; condition = {condition}; action required = {action}. Keep the tone professional, concise, and action-oriented. Do not invent facts. If information is missing, state what needs to be confirmed."

## 13. Success Outcome

The automation is successful if:

{success_outcome}

## 14. Testing Checklist

Before using this automation with real users, test the following:

- Does the trigger run at the right time?
- Does the condition filter records correctly?
- Does the automation send messages to the correct recipients?
- Is the message accurate and professional?
- Are failed runs logged?
- Is there a human review step where needed?
- Is sensitive information protected?
- Are duplicate notifications avoided?

## 15. Risks and Controls

Potential risks:
- Incorrect trigger settings
- Duplicate notifications
- Missing or wrong recipient email
- AI-generated message containing incorrect details
- Poor data quality
- Automation running too often
- Sensitive information being exposed

Controls:
- Use required fields in the data source
- Validate email fields
- Add a test mode before live deployment
- Keep human review for sensitive messages
- Log every automation run
- Add clear failure notifications
- Limit automation frequency where appropriate
"""
    return blueprint.strip()


print("\nAppSheet Automation Prompt Generator")
print("Lesson 10: Build 3")
print("Type 'exit' anytime to stop.\n")

while True:
    solution_name = input("Enter solution name: ")

    if solution_name.lower().strip() in ["exit", "quit", "stop"]:
        print("Automation prompt generator ended.")
        break

    trigger_event = input("What should trigger the automation? ")
    data_source = input("What data source should it use? ")
    condition = input("What condition must be true? ")
    action = input("What action should the automation perform? ")
    recipients = input("Who should receive the update or be affected? ")
    message_purpose = input("What should the message or output achieve? ")
    ai_assistance = input("What should AI help generate, classify, extract, or summarize? ")
    success_outcome = input("What outcome would show this automation is successful? ")

    blueprint = build_automation_blueprint(
        solution_name=solution_name,
        trigger_event=trigger_event,
        data_source=data_source,
        condition=condition,
        action=action,
        recipients=recipients,
        message_purpose=message_purpose,
        ai_assistance=ai_assistance,
        success_outcome=success_outcome
    )

    print("\nGenerated Low-Code Automation Blueprint:\n")
    print(blueprint)
    print("\n" + "=" * 100 + "\n")