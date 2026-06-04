# Lesson 21: Building With the Meta Family Models

## Microsoft Course Concept

This lesson introduces the Meta Llama family, focusing on Llama 3.1 and Llama 3.2.

Llama 3.1 supports advanced text-based generative AI workflows, including larger-context RAG, native function calling, multilingual tasks, and synthetic data generation.

Llama 3.2 extends the family into multimodal workflows, especially vision-based tasks using models such as Llama 3.2 11B Vision Instruct and Llama 3.2 90B Vision Instruct. Smaller Llama variants can also support edge or mobile-style low-latency workflows.

## My Adaptation

I adapted the lesson into a Meta Llama Model Selection Advisor for my AI Lab.

The app helps decide whether a task should use Llama 3.1 70B, Llama 3.1 405B, Llama 3.2 Vision, smaller edge-oriented Llama models, Claude/GPT fallback, or a hybrid Meta strategy.

## Key Concepts Practised

- Llama model selection
- RAG model planning
- Function calling model planning
- Vision model planning
- Synthetic data generation planning
- Edge/local deployment thinking
- Hybrid model routing
- ResearchLab task strategy

## Build Completed

Meta Llama Model Selection Advisor.

## Main Lesson

Llama 3.1 is useful for advanced text workflows such as RAG, function calling, multilingual tasks, and synthetic data generation. Llama 3.2 is useful when vision or multimodal understanding is required. Smaller Llama variants are better for lightweight local or edge tasks.

## Build 2: Llama Function Calling Planner

I built a Llama function calling planner.

The app recommends whether to use Llama 3.1 70B function calling, Llama 3.1 405B function calling, a hybrid Llama function-calling workflow, or Claude/GPT fallback.

It generates a function-calling architecture including tool schemas, call pattern, safety rules, and implementation steps.

This supports Lesson 21 by adapting Llama 3.1 native function calling into ResearchLab, Business Ops, and Trading Lab workflows.

## Build 3: Llama Vision Workflow Planner

I built a Llama vision workflow planner.

The app recommends whether a visual task should use Llama 3.2 11B Vision, Llama 3.2 90B Vision, Claude/GPT Vision fallback, human expert review, or a hybrid vision workflow.

It supports scientific figure interpretation, screenshot analysis, diagram review, postharvest crop image analysis, table and chart understanding, and visual evidence extraction.

This supports Lesson 21 by adapting Llama 3.2 Vision into ResearchLab visual workflows while keeping human expert review for high-risk scientific outputs.