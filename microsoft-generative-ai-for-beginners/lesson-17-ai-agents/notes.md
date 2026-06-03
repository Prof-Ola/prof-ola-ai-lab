# Lesson 17: AI Agents

## Microsoft Course Concept

This lesson introduces AI Agents.

AI Agents allow Large Language Models to perform tasks by giving them access to state and tools.

The lesson explains that:
- The LLM decides or reasons about what to do.
- State stores context, past actions, current progress, and results.
- Tools allow the agent to interact with databases, APIs, functions, external systems, or other agents.

The lesson also introduces agent frameworks such as LangChain Agents, AutoGen, TaskWeaver, and JARVIS.

## My Adaptation

I adapted the lesson into a Local Research Agent Simulator.

Instead of immediately using a complex framework, I built a simple local agent architecture that demonstrates the core agent loop:

User goal → state update → tool selection → tool execution → result storage → next action.

## Key Concepts Practised

- Agent state
- Tool selection
- Tool execution
- Conversation history
- State update
- Next-action planning
- Research workflow automation
- Safe local agent simulation

## Build Completed

Local Research Agent Simulator.

## Main Lesson

An AI agent is not just a chatbot. It is an LLM-based system that can maintain state, choose tools, execute actions, store results, and continue working toward a user goal.

## Build 2: Research Agent with Persistent State

I built a persistent research agent.

The app saves agent state into a JSON file, including conversation history, task memory, selected tools, tool results, and next actions.

This improves the first local agent simulator by allowing the agent to remember previous tasks across sessions.

This demonstrates one of the key parts of agent architecture: state management.

## Build 2: Research Agent with Persistent State

I built a persistent research agent.

The app saves agent state into a JSON file, including conversation history, task memory, selected tools, tool results, and next actions.

This improves the first local agent simulator by allowing the agent to remember previous tasks across sessions.

This demonstrates one of the key parts of agent architecture: state management.

## Build 4: Claude-Assisted Multi-Agent Research Meeting

I built a Claude-assisted multi-agent research meeting simulator.

The app uses Claude to simulate specialist agents:
- Research Director
- Postharvest Scientist
- AI Engineer
- Grant Strategist
- Ethics and Risk Reviewer

Each agent receives the same pitch and context, but responds from its assigned role. The app then uses Claude to synthesize all agent outputs into an integrated recommendation.

This improves the fixed-template multi-agent simulator by making the agent responses dynamic, context-aware, and closer to the AutoGen-style agent concept introduced in the lesson.
