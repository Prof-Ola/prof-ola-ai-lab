# Lesson 18: Fine-Tuning Models

## Microsoft Course Concept

This lesson introduces fine-tuning for pre-trained language models.

Fine-tuning is different from prompt engineering and retrieval-augmented generation. Prompt engineering modifies the prompt input. RAG adds retrieved context to the prompt. Fine-tuning retrains the model itself using additional curated examples.

The lesson emphasizes that fine-tuning is an advanced technique. It should only be considered after testing alternatives such as prompt engineering and RAG, estimating cost, checking model tunability, preparing quality data, and confirming that the expected benefits outweigh the complexity.

## My Adaptation

I adapted the lesson into a Fine-Tuning Decision Advisor for my AI Lab.

The app helps decide whether a use case should use prompt engineering, RAG, function calling, agent workflows, fine-tuning, or a hybrid approach.

## Key Concepts Practised

- Fine-tuning decision-making
- Baseline comparison
- Prompt engineering vs RAG vs fine-tuning
- Training data readiness
- Evaluation readiness
- Cost-benefit reasoning
- ResearchLab model improvement strategy

## Build Completed

Fine-Tuning Decision Advisor.

## Main Lesson

Fine-tuning should not be the first solution. It should be used only when simpler approaches have been tested, enough high-quality examples are available, evaluation metrics are ready, and the expected benefit outweighs cost, complexity, and maintenance.
## Build 2: Fine-Tuning Dataset Readiness Checker

I built a fine-tuning dataset readiness checker.

The app evaluates whether a dataset is ready for fine-tuning based on example quantity, input-output quality, format consistency, domain relevance, duplicate checking, bias checking, sensitive data review, human review, validation data, evaluation data, baseline availability, expected behavior, deployment purpose, and cost estimation.

This supports Lesson 18 by emphasizing that fine-tuning requires curated, high-quality, reviewed data rather than random examples.

## Build 3: Fine-Tuning Example Formatter

I built a fine-tuning example formatter.

The app creates chat-style JSONL examples with system, user, and assistant messages. It can generate sample ResearchLab examples or allow one custom example to be created manually.

The app also validates the example structure before saving the output as JSONL and readable JSON.

This supports Lesson 18 by showing that fine-tuning requires structured, curated, reviewed examples rather than raw notes or unformatted text.

## Build 4: Fine-Tuning Evaluation Plan Generator

I built a fine-tuning evaluation plan generator.

The app creates CSV files for testing a base model, a prompt/RAG baseline, and a candidate fine-tuned model.

It generates:
- fine-tuning evaluation test cases
- evaluation scorecard
- deployment decision checklist
- evaluation summary

This supports Lesson 18 by ensuring that a fine-tuned model is only adopted if it clearly outperforms the baseline without reducing safety, groundedness, or reliability.

