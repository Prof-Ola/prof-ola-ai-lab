# Lesson 16: Open Source / Open Models

## Microsoft Course Concept

This lesson introduces open models and explains that many models called open source may be better described as open models because not all training datasets, weights, evaluation code, fine-tuning code, and training metrics are always fully public.

The lesson covers benefits of open models such as customization, cost, and flexibility. It also introduces examples such as Llama, Mistral, Falcon, and model discovery through Hugging Face and Azure AI Foundry.

## My Adaptation

I adapted the lesson into an Open Model Selection Advisor for my AI Lab.

The app helps decide whether a project should use a local open model, hosted open model API, proprietary model API, or hybrid model strategy.

## Key Concepts Practised

- Open model selection
- Cost-quality tradeoff
- Privacy-aware model choice
- Local vs hosted model strategy
- Hybrid model architecture
- Model evaluation checklist
- ResearchLab model planning

## Build Completed

Open Model Selection Advisor.

## Main Lesson

The best model is not always the biggest, newest, or most expensive model. The right model depends on the task, privacy requirements, quality needs, cost constraints, latency, hardware, and deployment strategy.

## Build 2: Open Model Evaluation Matrix Generator

I built an open model evaluation matrix generator.

The app creates a CSV template for comparing proprietary and open models across cost, quality, privacy, latency, local deployability, fine-tuning potential, licensing, and fit for ResearchLab, Business Ops, and Trading Lab.

This supports Lesson 16 by turning model selection into a structured evaluation process rather than choosing models based on hype or popularity.