# Lesson 11: Function Calling

## Microsoft Course Concept

This lesson introduces function calling. Function calling helps applications get more consistent structured outputs from language models and connect model outputs to external tools, APIs, databases, or application functions.

## My Adaptation

Because Azure OpenAI access may create paywall or setup friction, I first built a local function calling simulator.

The simulator demonstrates the same function-calling logic without requiring an external LLM API.

## Key Concepts Practised

- Function detection
- Argument extraction
- Structured function inputs
- Calling Python functions from user intent
- Tool-like application design
- Research workflow functions

## Build Completed

Local Function Calling Simulator.

## Main Lesson

Function calling allows an AI application to move from simply generating text to choosing a tool, passing structured arguments, running an action, and returning the result.

## Build 2: Function Calling JSON Router

I built a JSON-based function calling router that detects user intent, extracts arguments, calls the correct local Python function, and returns a structured JSON object.

This build improves the first simulator by making the function output machine-readable and easier to store, log, test, or pass into another application.

The JSON output includes timestamp, user message, function name, arguments, and function result.