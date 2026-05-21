# --------------------------------------------------
# Lesson 10 Build 4: AI Message Draft Generator
# Microsoft Generative AI for Beginners adaptation
# Purpose: Generate messages for low-code workflow automations
# such as AppSheet Automation, n8n, Power Automate, Zapier, or Make.
# --------------------------------------------------


def generate_workflow_messages(
    solution_name,
    message_type,
    recipient,
    record_name,
    status,
    deadline,
    next_action,
    tone,
    extra_context
):
    """
    Generate reusable message drafts for low-code workflow automations.
    """

    subject = f"{message_type}: {record_name}"

    short_message = f"""
Hello {recipient},

This is a quick update from {solution_name}.

Record: {record_name}
Current status: {status}
Deadline: {deadline}
Next action: {next_action}

Please review and take the required action.

Thank you.
""".strip()

    detailed_message = f"""
Dear {recipient},

This message is an automated update from {solution_name}.

The following record requires attention:

Record name:
{record_name}

Current status:
{status}

Deadline:
{deadline}

Required next action:
{next_action}

Additional context:
{extra_context}

Please review the record and complete the next action as soon as possible. If the task has already been completed, kindly update the system so that the record reflects the latest status.

Tone requested:
{tone}

Kind regards,
{solution_name} Automation
""".strip()

    whatsapp_message = f"""
Hello {recipient}, quick update from {solution_name}.

{record_name} is currently marked as: {status}.

Deadline: {deadline}
Next action: {next_action}

Please check and update when done.
""".strip()

    internal_log_summary = f"""
Automation message generated.

Solution: {solution_name}
Message type: {message_type}
Recipient: {recipient}
Record: {record_name}
Status: {status}
Deadline: {deadline}
Next action: {next_action}
Tone: {tone}
Context: {extra_context}
""".strip()

    ai_prompt = f"""
Write a {tone} {message_type} for {recipient}.

Context:
- Solution name: {solution_name}
- Record name: {record_name}
- Current status: {status}
- Deadline: {deadline}
- Next action required: {next_action}
- Additional context: {extra_context}

Requirements:
- Keep the message clear and professional.
- Do not invent facts.
- Mention the deadline and next action.
- Use a tone suitable for {recipient}.
- Keep it concise but complete.
""".strip()

    return {
        "subject": subject,
        "short_message": short_message,
        "detailed_message": detailed_message,
        "whatsapp_message": whatsapp_message,
        "internal_log_summary": internal_log_summary,
        "ai_prompt": ai_prompt
    }


print("\nAI Workflow Message Generator")
print("Lesson 10: Build 4")
print("Type 'exit' anytime to stop.\n")

while True:
    solution_name = input("Enter solution name: ")

    if solution_name.lower().strip() in ["exit", "quit", "stop"]:
        print("AI workflow message generator ended.")
        break

    message_type = input("Enter message type, for example deadline reminder, status update, weekly summary: ")
    recipient = input("Enter recipient or recipient group: ")
    record_name = input("Enter project, record, assignment, invoice, or task name: ")
    status = input("Enter current status: ")
    deadline = input("Enter deadline or relevant date: ")
    next_action = input("Enter next action required: ")
    tone = input("Enter tone, for example professional, warm, firm, concise: ")
    extra_context = input("Enter extra context: ")

    messages = generate_workflow_messages(
        solution_name=solution_name,
        message_type=message_type,
        recipient=recipient,
        record_name=record_name,
        status=status,
        deadline=deadline,
        next_action=next_action,
        tone=tone,
        extra_context=extra_context
    )

    print("\nGenerated Workflow Messages:\n")

    print("1. Email Subject:")
    print(messages["subject"])
    print("\n" + "-" * 80)

    print("2. Short Email Message:")
    print(messages["short_message"])
    print("\n" + "-" * 80)

    print("3. Detailed Email Message:")
    print(messages["detailed_message"])
    print("\n" + "-" * 80)

    print("4. WhatsApp-Style Message:")
    print(messages["whatsapp_message"])
    print("\n" + "-" * 80)

    print("5. Internal Log Summary:")
    print(messages["internal_log_summary"])
    print("\n" + "-" * 80)

    print("6. AI Prompt for Workflow Tool:")
    print(messages["ai_prompt"])

    print("\n" + "=" * 100 + "\n")