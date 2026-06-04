from pathlib import Path
from datetime import datetime

ROOT = Path.cwd()


def backup_file(path: Path):
    if path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = path.with_name(f"{path.stem}_backup_{timestamp}{path.suffix}")
        backup_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Backed up {path.name} to {backup_path.name}")


def write_readme():
    readme_path = ROOT / "README.md"
    backup_file(readme_path)

    content = """# Prof Ola AI Lab

A practical AI learning and application portfolio built while working through the Microsoft Generative AI for Beginners course.

This repository adapts each lesson into real tools for three operating labs:

1. ResearchLab
2. Business Ops
3. Trading Lab

The goal is not just to complete lessons, but to build a reusable AI operating system for research, academic productivity, business workflows, and safe paper-trading experimentation.

---

## Core Philosophy

This project follows a build-first approach:

- Learn the concept.
- Build a local tool.
- Test it.
- Improve it.
- Commit it.
- Push it.
- Document the lesson.

The focus is practical mastery, not passive watching.

---

## AI Lab Tracks

### ResearchLab

ResearchLab focuses on academic and scientific workflows, especially:

- Postharvest technology
- Food security
- Horticultural crops
- AI-enabled harvest maturity assessment
- Literature review support
- RAG-based research assistance
- Grant and manuscript development
- Multi-agent research review

### Business Ops

Business Ops focuses on practical administrative and business workflows, including:

- Low-code planning
- Workflow automation
- Communication drafts
- Business process support
- Dashboard and tracker generation

### Trading Lab

Trading Lab focuses on safe, paper-trading-first AI concepts, including:

- Research and planning
- Risk-control thinking
- Monitoring concepts
- No live trading automation without strict safeguards
- No financial advice framing

---

## Completed Lessons and Builds

### Lesson 06: Text Generation

Built early text generation tools for research idea generation, research questions, titles, and practical applications.

Key concept:
Prompt engineering can turn a general LLM into a useful task assistant.

---

### Lesson 07: Chat Applications

Built menu-based and chat-style research assistants.

Key concept:
Chat applications require conversation flow, user intent handling, and structured responses.

---

### Lesson 08: Search Applications and Semantic Search

Built:

- Research Semantic Search App
- Research File Search App
- Research CSV RAG Answer Generator

Key concept:
Semantic search retrieves meaning, not just keywords. This became the foundation for later RAG systems.

---

### Lesson 09: Image Generation Applications

Built:

- Research Image Prompt Builder
- Prompt Saver App
- Thumbnail Prompt Specialist
- Scientific Figure Prompt Generator

Key concept:
Image generation requires structured prompt design, visual hierarchy, safety constraints, and audience-specific communication.

---

### Lesson 10: Low-Code AI Applications

Built paywall-safe alternatives inspired by Power Platform concepts, using Google Sheets and AppSheet-style workflows.

Key concept:
Low-code AI is about mapping data, users, actions, and workflows before building the app.

---

### Lesson 11: Function Calling

Built:

- Local Function Calling Simulator
- Claude-Assisted Function Calling Router

Key concept:
Function calling allows AI systems to choose structured tools instead of only generating text.

---

### Lesson 12: AI UX Design

Built UX message frameworks for AI transparency, feedback, human review, and trust.

Key concept:
A useful AI app must explain its limits, guide users, and create trust through clear UX.

---

### Lesson 13: Securing AI Applications

Built:

- AI Security Risk Assessment Generator
- Prompt Injection Test Harness
- AI App Security Checklist Scorer

Key concept:
AI apps require security testing, prompt-injection awareness, output validation, data protection, and human review.

---

### Lesson 14: Generative AI Application Lifecycle

Built:

- AI App Lifecycle Planner
- LLMOps Metrics Tracker Generator
- AI App Version Release Planner
- AI App Lifecycle Dashboard Data Generator

Key concept:
AI apps are never truly finished. They must be planned, measured, monitored, versioned, and improved.

---

### Lesson 15: RAG and Vector Databases

Built:

- Local RAG Knowledge Base Index Builder
- Local RAG Retriever
- Local RAG + Claude Grounded Answer Generator
- RAG Evaluation Logger

Key concept:
RAG connects an LLM to a knowledge base through chunking, embeddings, vector search, retrieval, grounded answer generation, and evaluation logging.

---

### Lesson 16: Open Models

Built:

- Open Model Selection Advisor
- Open Model Evaluation Matrix Generator
- Local Model Experiment Planner
- Open Model Deployment Strategy Planner

Key concept:
The best model is not always the biggest or most expensive. Model choice depends on task, quality, privacy, cost, latency, hardware, license, and deployment strategy.

---

### Lesson 17: AI Agents

Built:

- Local Research Agent Simulator
- Research Agent with Persistent State
- Multi-Agent Research Meeting Simulator
- Claude-Assisted Multi-Agent Research Meeting

Key concept:
An AI agent is not just a chatbot. It uses state, tools, memory, and role-specific reasoning to work toward a goal.

---

### Lesson 18: Fine-Tuning Models

Built:

- Fine-Tuning Decision Advisor
- Fine-Tuning Dataset Readiness Checker
- Fine-Tuning Example Formatter
- Fine-Tuning Evaluation Plan Generator

Key concept:
Fine-tuning should not be the first solution. It should only be considered after prompt engineering, RAG, function calling, or agents have been tested and the dataset is ready.

---

## Current AI Lab Architecture

```text
Prompt Engineering
↓
Chat Applications
↓
Semantic Search
↓
RAG
↓
Function Calling
↓
Agents
↓
Security
↓
Lifecycle Management
↓
Open Model Strategy
↓
Fine-Tuning Readiness