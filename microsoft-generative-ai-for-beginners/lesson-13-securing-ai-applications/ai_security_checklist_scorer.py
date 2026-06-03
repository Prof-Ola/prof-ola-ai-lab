# --------------------------------------------------
# Lesson 13 Build 3: AI App Security Checklist Scorer
# Microsoft Generative AI for Beginners adaptation
# Purpose: Score an AI app's security readiness before deployment.
# --------------------------------------------------


def get_score(prompt):
    """
    Ask for a score from 0 to 5 and validate input.
    """

    while True:
        try:
            score = int(input(prompt + " Score 0-5: "))

            if 0 <= score <= 5:
                return score

            print("Please enter a number from 0 to 5.")

        except ValueError:
            print("Invalid input. Please enter a whole number from 0 to 5.")


def interpret_score(total_score):
    """
    Interpret total security readiness score.
    Maximum score is 50.
    """

    if total_score >= 45:
        return "Ready for limited deployment with monitoring"
    elif total_score >= 35:
        return "Internal team testing ready"
    elif total_score >= 25:
        return "Controlled personal use only"
    else:
        return "Prototype only, not ready for users"


def generate_recommendations(scores):
    """
    Generate recommendations based on weak categories.
    """

    recommendations = []

    if scores["data_protection"] < 4:
        recommendations.append("Strengthen data protection. Avoid sensitive data, anonymize inputs, and add clear data-use notices.")

    if scores["prompt_injection_resistance"] < 4:
        recommendations.append("Improve prompt injection resistance. Treat user input and retrieved documents as untrusted data.")

    if scores["output_validation"] < 4:
        recommendations.append("Add output validation. Require verification for claims, citations, statistics, and recommendations.")

    if scores["api_key_management"] < 5:
        recommendations.append("Review API key management. Store secrets in .env, exclude .env from GitHub, and rotate exposed keys.")

    if scores["dependency_safety"] < 4:
        recommendations.append("Review dependency safety. Use trusted packages, update dependencies, and document model/package versions.")

    if scores["access_control"] < 4:
        recommendations.append("Add access controls. Separate admin, editor, and viewer roles where possible.")

    if scores["human_review"] < 4:
        recommendations.append("Add human review gates for academic, financial, legal, institutional, or high-impact outputs.")

    if scores["logging_monitoring"] < 3:
        recommendations.append("Add logging and monitoring for errors, suspicious prompts, failed runs, and user feedback.")

    if scores["rag_document_safety"] < 4:
        recommendations.append("Improve RAG/document safety. Do not allow retrieved documents to override system instructions.")

    if scores["error_handling"] < 4:
        recommendations.append("Improve error handling with clear, friendly, and safe failure messages.")

    if not recommendations:
        recommendations.append("Security posture looks strong for controlled use. Continue testing and monitoring before wider deployment.")

    return recommendations


def generate_security_score_report(app_name, app_purpose, scores):
    total_score = sum(scores.values())
    max_score = 50
    readiness = interpret_score(total_score)
    recommendations = generate_recommendations(scores)

    report = f"""
# AI App Security Checklist Score Report

## 1. App Name

{app_name}

## 2. App Purpose

{app_purpose}

## 3. Security Scores

| Category | Score / 5 |
|---|---:|
| Data protection | {scores["data_protection"]} |
| Prompt injection resistance | {scores["prompt_injection_resistance"]} |
| Output validation | {scores["output_validation"]} |
| API key management | {scores["api_key_management"]} |
| Dependency and supply chain safety | {scores["dependency_safety"]} |
| Access control | {scores["access_control"]} |
| Human review | {scores["human_review"]} |
| Logging and monitoring | {scores["logging_monitoring"]} |
| RAG and document safety | {scores["rag_document_safety"]} |
| Error handling | {scores["error_handling"]} |

## 4. Total Score

{total_score} / {max_score}

## 5. Readiness Level

{readiness}

## 6. Recommendations

"""

    for i, recommendation in enumerate(recommendations, start=1):
        report += f"{i}. {recommendation}\n"

    report += """
## 7. Deployment Guidance

- Prototype only: use for personal learning and testing.
- Controlled personal use: use only on non-sensitive data.
- Internal team testing: share with trusted collaborators only after access controls and review gates are added.
- Limited deployment: use with monitoring, logging, user guidance, and security review.

## 8. Final Warning

A working AI app is not automatically a safe AI app. Security, privacy, validation, and human oversight must be designed into the system before real users rely on it.
"""

    return report.strip()


print("\nAI App Security Checklist Scorer")
print("Lesson 13: Build 3")
print("Type 'exit' anytime to stop.\n")

while True:
    app_name = input("Enter AI app name: ")

    if app_name.lower().strip() in ["exit", "quit", "stop"]:
        print("Security checklist scorer ended.")
        break

    app_purpose = input("What is the purpose of the app? ")

    print("\nScore each category from 0 to 5.")
    print("0 = not addressed, 5 = strong control in place.\n")

    scores = {
        "data_protection": get_score("Data protection"),
        "prompt_injection_resistance": get_score("Prompt injection resistance"),
        "output_validation": get_score("Output validation"),
        "api_key_management": get_score("API key management"),
        "dependency_safety": get_score("Dependency and supply chain safety"),
        "access_control": get_score("Access control"),
        "human_review": get_score("Human review"),
        "logging_monitoring": get_score("Logging and monitoring"),
        "rag_document_safety": get_score("RAG and document safety"),
        "error_handling": get_score("Error handling")
    }

    report = generate_security_score_report(
        app_name=app_name,
        app_purpose=app_purpose,
        scores=scores
    )

    print("\nGenerated Security Score Report:\n")
    print(report)
    print("\n" + "=" * 100 + "\n")