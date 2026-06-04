# --------------------------------------------------
# Lesson 19 Build 3: Local SLM Task Router
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Route AI Lab tasks to SLM, RAG + SLM, LLM fallback,
# or human review based on complexity, risk, grounding need,
# privacy, and task type.
# --------------------------------------------------


def clean_words(text):
    punctuation = [".", ",", "?", "!", ":", ";", "(", ")", "[", "]", "{", "}"]

    for mark in punctuation:
        text = text.replace(mark, " ")

    return text.lower().split()


def detect_task_features(user_request):
    """
    Detect task features using simple keyword logic.
    This simulates the routing layer before connecting a real SLM or LLM.
    """

    text = user_request.lower()
    words = clean_words(user_request)

    features = {
        "task_type": "general",
        "needs_rag": False,
        "needs_llm": False,
        "needs_human_review": False,
        "risk_level": "low",
        "complexity": "low",
        "privacy_sensitive": False,
        "reason": []
    }

    # Simple SLM-suitable tasks
    if (
        "tag" in words
        or "classify" in words
        or "extract" in words
        or "label" in words
        or "summarize" in words
        or "summarise" in words
    ):
        features["task_type"] = "classification_extraction_summary"
        features["reason"].append("The request looks like tagging, classification, extraction, or summarization.")

    # RAG-suitable tasks
    if (
        "using my notes" in text
        or "knowledge base" in text
        or "retrieve" in words
        or "sources" in words
        or "evidence" in words
        or "grounded" in words
        or "literature" in words
    ):
        features["needs_rag"] = True
        features["task_type"] = "grounded_retrieval"
        features["complexity"] = "medium"
        features["reason"].append("The request needs evidence or retrieval from a knowledge base.")

    # LLM fallback tasks
    if (
        "critique" in words
        or "evaluate" in words
        or "strategy" in words
        or "grant" in words
        or "manuscript" in words
        or "reviewer" in words
        or "synthesize" in words
        or "synthesise" in words
        or "complex" in words
    ):
        features["needs_llm"] = True
        features["complexity"] = "high"
        features["risk_level"] = "medium"
        features["reason"].append("The request needs deeper reasoning, synthesis, critique, or strategic judgement.")

    # Human review tasks
    if (
        "advise farmers" in text
        or "harvest advice" in text
        or "recommend to farmers" in text
        or "medical" in words
        or "legal" in words
        or "financial" in words
        or "investment" in words
        or "live trading" in text
        or "submit" in words
        or "final decision" in text
    ):
        features["needs_human_review"] = True
        features["risk_level"] = "high"
        features["reason"].append("The request may affect real-world decisions and needs human review.")

    # Privacy-sensitive tasks
    if (
        "unpublished" in words
        or "confidential" in words
        or "private" in words
        or "collaborator" in words
        or "grant idea" in text
        or "proposal" in words
        or "student data" in text
    ):
        features["privacy_sensitive"] = True
        features["reason"].append("The request may involve private, unpublished, or sensitive information.")

    return features


def route_task(user_request):
    """
    Decide where the task should go.
    """

    features = detect_task_features(user_request)

    slm_score = 0
    rag_slm_score = 0
    llm_fallback_score = 0
    human_review_score = 0

    # Base routing logic
    if features["task_type"] == "classification_extraction_summary":
        slm_score += 4

    if features["needs_rag"]:
        rag_slm_score += 5
        slm_score += 1

    if features["needs_llm"]:
        llm_fallback_score += 5

    if features["needs_human_review"]:
        human_review_score += 6
        llm_fallback_score += 2

    if features["complexity"] == "low":
        slm_score += 3
    elif features["complexity"] == "medium":
        rag_slm_score += 2
        llm_fallback_score += 1
    else:
        llm_fallback_score += 3

    if features["risk_level"] == "low":
        slm_score += 2
    elif features["risk_level"] == "medium":
        llm_fallback_score += 2
        human_review_score += 1
    else:
        human_review_score += 4

    if features["privacy_sensitive"]:
        slm_score += 2
        rag_slm_score += 2
        human_review_score += 1

    scores = {
        "SLM": slm_score,
        "RAG + SLM": rag_slm_score,
        "LLM fallback": llm_fallback_score,
        "Human review": human_review_score
    }

    recommended_route = max(scores, key=scores.get)

    if human_review_score >= 6:
        recommended_route = "Human review"

    route_explanations = {
        "SLM": """
Recommended route:
Use a local Small Language Model.

Best for:
- Tagging
- Classification
- Short summaries
- Structured extraction
- Low-risk formatting
- Local private preprocessing

Example ResearchLab use:
Extract crop, method, context, maturity indicator, and value-chain condition from a literature note.
""",
        "RAG + SLM": """
Recommended route:
Use retrieval plus a Small Language Model.

Best for:
- Grounded answers from a local knowledge base
- Literature note Q&A
- Evidence-based short summaries
- Source-aware responses
- Private local research assistance

Example ResearchLab use:
Retrieve relevant postharvest notes, then ask the SLM to summarize only the retrieved context.
""",
        "LLM fallback": """
Recommended route:
Use a stronger Large Language Model.

Best for:
- Complex reasoning
- Manuscript critique
- Grant strategy
- Deep synthesis
- Multi-step interpretation
- High-quality academic writing support

Example ResearchLab use:
Ask Claude or another strong LLM to critique a manuscript section after RAG retrieves supporting context.
""",
        "Human review": """
Recommended route:
Human review required.

Best for:
- High-impact scientific interpretation
- Farmer-facing recommendations
- Manuscript submission decisions
- Grant submission decisions
- Financial, legal, health, or live trading decisions
- Any output that could cause real-world harm if wrong

Example ResearchLab use:
AI may draft or retrieve evidence, but a domain expert must validate before use.
"""
    }

    report = f"""
# Local SLM Task Routing Report

## User Request

{user_request}

---

# Detected Features

Task type:
{features["task_type"]}

Needs RAG:
{features["needs_rag"]}

Needs LLM:
{features["needs_llm"]}

Needs human review:
{features["needs_human_review"]}

Risk level:
{features["risk_level"]}

Complexity:
{features["complexity"]}

Privacy sensitive:
{features["privacy_sensitive"]}

Reasons:
{chr(10).join("- " + reason for reason in features["reason"]) if features["reason"] else "- No strong routing signals detected."}

---

# Routing Scores

| Route | Score |
|---|---:|
| SLM | {slm_score} |
| RAG + SLM | {rag_slm_score} |
| LLM fallback | {llm_fallback_score} |
| Human review | {human_review_score} |

---

# Recommended Route

{recommended_route}

{route_explanations[recommended_route]}

---

# ResearchLab Operating Rule

Use the cheapest safe model that can do the job well.

Suggested routing pattern:

1. SLM for low-risk classification, extraction, tagging, and short summaries.
2. RAG + SLM for grounded local knowledge-base questions.
3. LLM fallback for complex reasoning, synthesis, grant logic, and manuscript-level judgement.
4. Human review for high-impact, sensitive, external-facing, or decision-critical outputs.
"""
    return report.strip()


print("\nLocal SLM Task Router")
print("Lesson 19: Build 3")
print("Type 'exit' anytime to stop.\n")

while True:
    user_request = input("Enter task request: ")

    if user_request.lower().strip() in ["exit", "quit", "stop"]:
        print("Local SLM task router ended.")
        break

    routing_report = route_task(user_request)

    print("\nGenerated Task Routing Report:\n")
    print(routing_report)
    print("\n" + "=" * 100 + "\n")