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