# --------------------------------------------------
# Lesson 20 Build 2: Mistral RAG Pattern Planner
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Generate a RAG architecture plan using Mistral models
# for ResearchLab, Business Ops, or other AI Lab workflows.
# --------------------------------------------------


def generate_mistral_rag_plan(
    project_name,
    use_case,
    document_type,
    knowledge_domain,
    expected_questions,
    context_window_need,
    multilingual_need,
    function_calling_need,
    cost_sensitivity,
    latency_sensitivity,
    privacy_requirement,
    vector_store_preference,
    deployment_preference,
    evaluation_readiness
):
    """
    Generate a Mistral RAG pattern plan.
    """

    mistral_large_score = 0
    mistral_small_score = 0
    mistral_nemo_score = 0
    hybrid_score = 0

    context_need = context_window_need.lower().strip()
    multilingual = multilingual_need.lower().strip()
    function_calling = function_calling_need.lower().strip()
    cost = cost_sensitivity.lower().strip()
    latency = latency_sensitivity.lower().strip()
    privacy = privacy_requirement.lower().strip()
    vector_store = vector_store_preference.lower().strip()
    deployment = deployment_preference.lower().strip()
    evaluation = evaluation_readiness.lower().strip()

    # Context window and RAG complexity
    if context_need in ["high", "very high", "large"]:
        mistral_large_score += 5
        hybrid_score += 2
    elif context_need == "medium":
        mistral_large_score += 3
        mistral_nemo_score += 2
        hybrid_score += 2
    else:
        mistral_small_score += 2
        mistral_nemo_score += 2

    # Multilingual
    if multilingual in ["yes", "y", "high"]:
        mistral_large_score += 3
        mistral_nemo_score += 3
        hybrid_score += 1

    # Function calling
    if function_calling in ["yes", "y", "high"]:
        mistral_large_score += 3
        mistral_nemo_score += 4
        hybrid_score += 2

    # Cost
    if cost in ["high", "very high"]:
        mistral_small_score += 4
        mistral_nemo_score += 3
        hybrid_score += 2
    elif cost == "medium":
        mistral_nemo_score += 2
        mistral_small_score += 1
    else:
        mistral_large_score += 2

    # Latency
    if latency in ["high", "very high"]:
        mistral_small_score += 3
        mistral_nemo_score += 2
    elif latency == "medium":
        mistral_nemo_score += 2
        hybrid_score += 1

    # Privacy
    if privacy in ["high", "very high"]:
        mistral_nemo_score += 3
        mistral_small_score += 2
        hybrid_score += 2
    elif privacy == "medium":
        hybrid_score += 1

    # Vector store preference
    if "faiss" in vector_store or "local" in vector_store:
        mistral_nemo_score += 2
        mistral_small_score += 1
    elif "cloud" in vector_store or "azure" in vector_store:
        mistral_large_score += 2
        hybrid_score += 1

    # Deployment
    if "local" in deployment:
        mistral_nemo_score += 3
        mistral_small_score += 2
    elif "github" in deployment:
        mistral_large_score += 1
        mistral_small_score += 1
        mistral_nemo_score += 1
    elif "azure" in deployment or "cloud" in deployment:
        mistral_large_score += 3
        hybrid_score += 2
    elif "hybrid" in deployment:
        hybrid_score += 4

    # Evaluation readiness
    if evaluation in ["yes", "ready", "high"]:
        mistral_large_score += 1
        mistral_nemo_score += 1
        hybrid_score += 1
    else:
        hybrid_score += 1

    scores = {
        "Mistral Large RAG": mistral_large_score,
        "Mistral Small RAG": mistral_small_score,
        "Mistral NeMo RAG": mistral_nemo_score,
        "Hybrid Mistral RAG": hybrid_score
    }

    recommended_strategy = max(scores, key=scores.get)

    strategy_explanations = {
        "Mistral Large RAG": """
Recommended strategy:
Use Mistral Large for the answer generation layer.

Best when:
- The RAG system needs a larger context window.
- Retrieved chunks may be long or complex.
- Multilingual queries are expected.
- Function calling may be added.
- Stronger reasoning is needed.

Use this for:
Advanced ResearchLab literature synthesis, multilingual academic Q&A, and complex grounded answers.
""",
        "Mistral Small RAG": """
Recommended strategy:
Use Mistral Small for lightweight RAG.

Best when:
- Cost and latency matter.
- Questions are short and repetitive.
- Retrieved context is small.
- Output risk is low.

Use this for:
Short summaries, quick internal Q&A, and lightweight Business Ops knowledge retrieval.
""",
        "Mistral NeMo RAG": """
Recommended strategy:
Use Mistral NeMo for open-model RAG experimentation.

Best when:
- Open licensing matters.
- Local or hybrid deployment is preferred.
- Function calling may be tested.
- Future fine-tuning is possible.
- Flexibility matters.

Use this for:
ResearchLab open-model experiments, local RAG prototypes, and function-calling RAG workflows.
""",
        "Hybrid Mistral RAG": """
Recommended strategy:
Use a hybrid Mistral RAG workflow.

Best when:
- Some tasks are lightweight and some are complex.
- Cost control matters but quality cannot be sacrificed.
- Local/private retrieval is needed.
- Stronger model fallback is needed for final synthesis.

Suggested pattern:
Mistral Small or NeMo for initial retrieval summaries.
Mistral Large for complex grounded answer generation.
Claude/GPT fallback for final manuscript or grant-level judgement.
"""
    }

    plan = f"""
# Mistral RAG Pattern Plan

## 1. Project Name

{project_name}

## 2. Use Case

{use_case}

## 3. Document Type

{document_type}

## 4. Knowledge Domain

{knowledge_domain}

## 5. Expected Questions

{expected_questions}

---

# 6. RAG Design Inputs

Context window need:
{context_window_need}

Multilingual need:
{multilingual_need}

Function calling need:
{function_calling_need}

Cost sensitivity:
{cost_sensitivity}

Latency sensitivity:
{latency_sensitivity}

Privacy requirement:
{privacy_requirement}

Vector store preference:
{vector_store_preference}

Deployment preference:
{deployment_preference}

Evaluation readiness:
{evaluation_readiness}

---

# 7. Strategy Scores

| Strategy | Score |
|---|---:|
| Mistral Large RAG | {mistral_large_score} |
| Mistral Small RAG | {mistral_small_score} |
| Mistral NeMo RAG | {mistral_nemo_score} |
| Hybrid Mistral RAG | {hybrid_score} |

---

# 8. Recommended Strategy

{recommended_strategy}

{strategy_explanations[recommended_strategy]}

---

# 9. Suggested RAG Architecture

## Data layer

- Store documents as clean text or structured notes.
- Preserve metadata such as crop, method, region, storage condition, maturity indicator, source, and year.
- Separate public sources from private or unpublished notes.

## Chunking layer

Recommended starting point:
- Chunk size: 500 to 1,000 words for research notes.
- Overlap: 50 to 150 words.
- Keep headings and source metadata attached to each chunk.

## Embedding layer

Options:
- Cohere multilingual embeddings for multilingual RAG experiments.
- BGE or E5 embeddings for local open-source retrieval.
- Domain testing required before final selection.

## Vector store layer

Options:
- FAISS for local prototypes.
- Chroma for local developer-friendly workflows.
- Azure AI Search for production cloud workflows.
- Other vector stores if scaling later.

## Retrieval layer

Recommended:
- Top-k: 3 to 5 chunks.
- Add metadata filters for crop, method, context, and region.
- Log retrieved chunks and similarity scores.

## Generation layer

Recommended:
- Use the selected Mistral model only with retrieved context.
- Instruct the model not to invent citations or facts.
- Require limitation statements when evidence is weak.

## Evaluation layer

Track:
- Retrieval relevance.
- Groundedness.
- Answer accuracy.
- Citation/source traceability.
- Latency.
- Cost.
- User feedback.
- Safety failures.

---

# 10. ResearchLab Safety Rules

1. Do not allow the model to invent citations.
2. Always show or store retrieved source chunks.
3. Require human review for manuscript, grant, and farmer-facing outputs.
4. Add prompt injection tests before connecting external tools.
5. Keep private research notes out of public repositories.
6. Use evaluation logs before expanding to other users.

---

# 11. Next Actions

1. Define the first 20 evaluation questions.
2. Add metadata to the ResearchLab knowledge base.
3. Test FAISS or Chroma with the current notes.
4. Compare Mistral Large, NeMo, and current Claude RAG outputs.
5. Record groundedness, latency, and cost.
6. Decide whether Mistral should replace, complement, or sit behind Claude as a lower-cost option.
"""
    return plan.strip()


print("\nMistral RAG Pattern Planner")
print("Lesson 20: Build 2")
print("Type 'exit' anytime to stop.\n")

while True:
    project_name = input("Enter project name: ")

    if project_name.lower().strip() in ["exit", "quit", "stop"]:
        print("Mistral RAG pattern planner ended.")
        break

    use_case = input("Enter use case: ")
    document_type = input("Document type, for example research notes, PDFs, transcripts, reports: ")
    knowledge_domain = input("Knowledge domain: ")
    expected_questions = input("Expected question types: ")
    context_window_need = input("Context window need, low / medium / high / very high: ")
    multilingual_need = input("Multilingual need, yes / no / high: ")
    function_calling_need = input("Function calling need, yes / no / high: ")
    cost_sensitivity = input("Cost sensitivity, low / medium / high / very high: ")
    latency_sensitivity = input("Latency sensitivity, low / medium / high / very high: ")
    privacy_requirement = input("Privacy requirement, low / medium / high / very high: ")
    vector_store_preference = input("Vector store preference, FAISS / Chroma / Azure AI Search / local / unsure: ")
    deployment_preference = input("Deployment preference, local / GitHub Models / Azure / cloud / hybrid / unsure: ")
    evaluation_readiness = input("Evaluation readiness, yes / no / partial / high: ")

    plan = generate_mistral_rag_plan(
        project_name=project_name,
        use_case=use_case,
        document_type=document_type,
        knowledge_domain=knowledge_domain,
        expected_questions=expected_questions,
        context_window_need=context_window_need,
        multilingual_need=multilingual_need,
        function_calling_need=function_calling_need,
        cost_sensitivity=cost_sensitivity,
        latency_sensitivity=latency_sensitivity,
        privacy_requirement=privacy_requirement,
        vector_store_preference=vector_store_preference,
        deployment_preference=deployment_preference,
        evaluation_readiness=evaluation_readiness
    )

    print("\nGenerated Mistral RAG Pattern Plan:\n")
    print(plan)
    print("\n" + "=" * 100 + "\n")