# --------------------------------------------------
# Lesson 10 Build 1: AppSheet Solution Blueprint Builder
# Microsoft Generative AI for Beginners adaptation
# Paywall-safe low-code route using Google Sheets + AppSheet
# --------------------------------------------------


def build_appsheet_blueprint(
    solution_name,
    problem,
    users,
    data_to_track,
    user_actions,
    automation_needs,
    ai_needs,
    success_outcomes
):
    blueprint = f"""
# AppSheet Low-Code AI Solution Blueprint

## 1. Solution Name

{solution_name}

## 2. Problem to Solve

{problem}

## 3. Primary Users

{users}

## 4. Recommended Low-Code Stack

### Google Sheets
Use Google Sheets as the first database layer. Each sheet tab should represent a major data table.

### Google AppSheet
Use AppSheet to generate the app interface from the Google Sheets data structure.

### AppSheet Automation or n8n
Use AppSheet Automation or n8n to trigger reminders, email updates, approval flows, and recurring summaries.

### AI Helper
Use Claude, Gemini, ChatGPT, or a local Python helper to generate summaries, classify records, draft emails, and suggest next actions.

## 5. Data to Track

{data_to_track}

## 6. Suggested Google Sheets Tables

Create these sheet tabs:

### MainRecords
Suggested columns:
- RecordID
- Title
- Category
- Owner
- Status
- Priority
- DueDate
- NextAction
- Notes
- CreatedDate
- LastUpdated

### People
Suggested columns:
- PersonID
- FullName
- Role
- Email
- Phone
- Organization

### ActivityLog
Suggested columns:
- LogID
- RecordID
- ActionDate
- ActionType
- Comment
- UpdatedBy

### Documents
Suggested columns:
- DocumentID
- RecordID
- DocumentName
- DocumentType
- Link
- UploadDate

## 7. User Actions Required

The app should allow users to:

{user_actions}

## 8. AppSheet App Prompt

Use this prompt in AppSheet or as your design instruction:

"Build an AppSheet app called {solution_name}. The app should help {users} solve this problem: {problem}. The app should track: {data_to_track}. Users should be able to: {user_actions}. Create views for active records, overdue records, completed records, people, activity logs, and documents. Include forms for adding and updating records."

## 9. Automation Prompt

Use this prompt for AppSheet Automation or n8n:

"Create an automation for {solution_name}. The automation should: {automation_needs}. It should trigger when a record is created, updated, approaching a deadline, or marked as completed. It should send email notifications to relevant users and log the action in the ActivityLog table."

## 10. AI Use Case

AI need:
{ai_needs}

Suggested AI features:
- Generate short summaries of records.
- Suggest next actions based on status and deadline.
- Draft reminder emails.
- Classify records by category or urgency.
- Generate weekly progress summaries.
- Identify records at risk of delay.

## 11. Success Outcomes

The solution should be considered successful if it achieves:

{success_outcomes}

## 12. Risks and Controls

Potential risks:
- Poor data entry
- Missing deadlines
- Users ignoring notifications
- AI-generated summaries being inaccurate
- Sensitive information being exposed
- Workflow failures

Controls:
- Use required fields in Google Sheets/AppSheet.
- Use dropdowns for Status, Priority, and Category.
- Add email validation.
- Keep human review for AI-generated text.
- Avoid storing confidential API keys in public files.
- Review automation logs weekly.
"""
    return blueprint.strip()


print("\nAppSheet Solution Blueprint Builder")
print("Lesson 10: Low-Code AI Applications")
print("Type 'exit' anytime to stop.\n")

while True:
    solution_name = input("Enter solution name: ")

    if solution_name.lower().strip() in ["exit", "quit", "stop"]:
        print("Blueprint builder ended.")
        break

    problem = input("Describe the problem this solution should solve: ")
    users = input("Who will use this solution? ")
    data_to_track = input("What data should the solution track? ")
    user_actions = input("What actions should users perform in the app? ")
    automation_needs = input("What automation is needed? ")
    ai_needs = input("What AI capability is needed? ")
    success_outcomes = input("What outcomes would show success? ")

    blueprint = build_appsheet_blueprint(
        solution_name=solution_name,
        problem=problem,
        users=users,
        data_to_track=data_to_track,
        user_actions=user_actions,
        automation_needs=automation_needs,
        ai_needs=ai_needs,
        success_outcomes=success_outcomes
    )

    print("\nGenerated AppSheet Low-Code AI Blueprint:\n")
    print(blueprint)
    print("\n" + "=" * 100 + "\n")