# Lesson 19: Small Language Models

## Microsoft Course Concept

This lesson introduces Small Language Models, also called SLMs.

SLMs are smaller and less compute-intensive than large language models. They can still perform useful natural language tasks such as text generation, text completion, translation, and summarization, but usually with some trade-offs in reasoning depth, broad knowledge, or performance.

The lesson uses Microsoft Phi-3 and Phi-3.5 as examples of SLMs, covering text, vision, and mixture-of-experts scenarios. It also introduces ways to run or access these models through platforms such as GitHub Models, Azure AI Studio, Hugging Face, Ollama, NVIDIA NIM, and ONNX Runtime.

## My Adaptation

I adapted the lesson into an SLM Use-Case Fit Advisor for my AI Lab.

The app helps decide whether a task should use a Small Language Model, Large Language Model, RAG + SLM, or a hybrid SLM + LLM strategy.

## Key Concepts Practised

- SLM vs LLM decision-making
- Cost and latency tradeoffs
- Local and offline deployment thinking
- RAG + SLM architecture
- Hybrid SLM + LLM design
- ResearchLab task routing
- Safe use of smaller models

## Build Completed

SLM Use-Case Fit Advisor.

## Main Lesson

Small Language Models are useful when tasks are simple, repetitive, local, private, low-cost, or latency-sensitive. They should not replace stronger LLMs for complex reasoning, high-stakes synthesis, or final academic judgement.

## Build 2: Phi Model Deployment Planner

I built a Phi model deployment planner.

The app recommends a Phi-3 or Phi-3.5 model option and deployment route based on task type, modality, complexity, hardware, privacy, cost, latency, offline needs, multilingual needs, vision needs, scale, and preferred platform.

It supports options such as Phi-3 mini, Phi-3.5 mini, Phi Vision, Phi MoE, Ollama, ONNX Runtime, Hugging Face, GitHub Models, Azure AI Studio, and NVIDIA NIM.

This supports Lesson 19 by helping decide how small language models can be deployed practically for ResearchLab, Business Ops, and local AI workflows.

## Build 3: Local SLM Task Router

I built a local SLM task router.

The app classifies user requests and routes them to one of four pathways:
- SLM
- RAG + SLM
- LLM fallback
- Human review

The routing decision is based on task type, complexity, grounding need, risk level, privacy sensitivity, and whether the request requires deeper reasoning.

This supports Lesson 19 by showing how small language models can be used as efficient local task handlers while stronger models and human review remain available for complex or high-risk tasks.

## Build 4: SLM Evaluation Matrix Generator

I built an SLM evaluation matrix generator.

The app creates CSV templates for comparing small language models such as Phi-3 mini, Phi-3.5 mini, Mistral, Qwen, Gemma, and Llama-style models across ResearchLab, Business Ops, and Trading Lab tasks.

It generates:
- SLM evaluation matrix
- SLM evaluation scorecard
- SLM model comparison summary
- SLM deployment decision matrix
- SLM evaluation summary

This supports Lesson 19 by ensuring that small language models are evaluated against real workflow tasks before being trusted or deployed.