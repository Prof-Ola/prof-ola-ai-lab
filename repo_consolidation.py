from pathlib import Path
from datetime import datetime
import json

ROOT = Path.cwd()


def backup_file(path: Path):
    if path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = path.with_name(f"{path.stem}_backup_{timestamp}{path.suffix}")
        backup_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Backed up {path.name} to {backup_path.name}")


def write_lines(path: Path, lines):
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme():
    readme_path = ROOT / "README.md"
    backup_file(readme_path)

    lines = [
        "# Prof Ola AI Lab",
        "",
        "A practical AI learning and application portfolio built while working through the Microsoft Generative AI for Beginners course.",
        "",
        "This repository adapts the course into real tools for three operating labs:",
        "",
        "1. ResearchLab",
        "2. Business Ops",
        "3. Trading Lab",
        "",
        "The goal is not just to complete lessons, but to build a reusable AI operating system for research, academic productivity, business workflows, and safe paper-trading experimentation.",
        "",
        "## Core Philosophy",
        "",
        "- Learn the concept.",
        "- Build a local tool.",
        "- Test it.",
        "- Improve it.",
        "- Commit it.",
        "- Push it.",
        "- Document the lesson.",
        "",
        "## Completed Lessons and Builds",
        "",
        "| Lesson | Theme | Status |",
        "|---|---|---|",
        "| 06 | Text generation | Complete |",
        "| 07 | Chat applications | Complete |",
        "| 08 | Search applications and semantic search | Complete |",
        "| 09 | Image generation applications | Complete |",
        "| 10 | Low-code AI applications | Complete |",
        "| 11 | Function calling | Complete |",
        "| 12 | AI UX design | Complete |",
        "| 13 | Securing AI applications | Complete |",
        "| 14 | Generative AI application lifecycle | Complete |",
        "| 15 | RAG and vector databases | Complete |",
        "| 16 | Open models | Complete |",
        "| 17 | AI agents | Complete |",
        "| 18 | Fine-tuning models | Complete |",
        "",
        "## ResearchLab",
        "",
        "ResearchLab focuses on academic and scientific workflows, especially postharvest technology, food security, horticultural crops, AI-enabled harvest maturity assessment, literature review support, RAG-based research assistance, grant development, manuscript development, and multi-agent research review.",
        "",
        "## Business Ops",
        "",
        "Business Ops focuses on low-code planning, workflow automation, communication drafts, tracker generation, dashboard-ready outputs, and business process support.",
        "",
        "## Trading Lab",
        "",
        "Trading Lab focuses on safe, paper-trading-first AI concepts, risk-control thinking, monitoring concepts, and audit logging. It does not provide financial advice.",
        "",
        "## Current AI Lab Architecture",
        "",
        "Prompt engineering -> Chat applications -> Semantic search -> RAG -> Function calling -> Agents -> Security -> Lifecycle management -> Open model strategy -> Fine-tuning readiness",
        "",
        "## Important Safety Notes",
        "",
        "This repository may generate local logs, agent memory, RAG evaluation records, and multi-agent meeting records.",
        "",
        "These generated records may contain sensitive research ideas, unpublished manuscript concepts, collaborator details, grant strategy, or private notes.",
        "",
        "Runtime records should not be committed to GitHub.",
        "",
        "Recommended private folders include:",
        "",
        "- agent_state/",
        "- multi_agent_meeting_records/",
        "- claude_multi_agent_meeting_records/",
        "- rag_evaluation_logs/",
        "",
        "## Future Development Priorities",
        "",
        "### ResearchLab",
        "",
        "- Expand the RAG knowledge base.",
        "- Add metadata-rich retrieval.",
        "- Add source attribution.",
        "- Benchmark embedding models.",
        "- Improve evaluation logs.",
        "- Build a Streamlit interface.",
        "- Add safe persistent memory controls.",
        "",
        "### Business Ops",
        "",
        "- Convert trackers into Google Sheets or AppSheet workflows.",
        "- Build reusable templates for project management.",
        "- Add email and document drafting workflows.",
        "",
        "### Trading Lab",
        "",
        "- Keep everything paper-trading-first.",
        "- Add audit logs.",
        "- Add risk limits.",
        "- Add no-financial-advice safeguards.",
        "- Avoid live execution until governance, testing, and risk controls are mature.",
        "",
        "## Final Reflection",
        "",
        "This repository documents a practical journey from basic text generation to a structured AI application portfolio.",
        "",
        "It is not just a course folder. It is the foundation of a working AI Lab.",
    ]

    write_lines(readme_path, lines)
    print("Updated README.md")


def write_progress_map():
    progress_path = ROOT / "AI_LAB_PROGRESS_MAP.md"

    lines = [
        "# AI Lab Progress Map",
        "",
        "## Completed Course Adaptation",
        "",
        "| Lesson | Theme | Main Builds | Status |",
        "|---|---|---|---|",
        "| 06 | Text Generation | Research idea and question tools | Complete |",
        "| 07 | Chat Applications | Research chat assistant | Complete |",
        "| 08 | Search Applications | Semantic search and CSV RAG | Complete |",
        "| 09 | Image Generation | Research image prompt tools | Complete |",
        "| 10 | Low-Code AI | Google Sheets and AppSheet-style alternatives | Complete |",
        "| 11 | Function Calling | Local and Claude-assisted function routing | Complete |",
        "| 12 | AI UX | UX message and trust frameworks | Complete |",
        "| 13 | AI Security | Risk assessment, prompt injection, checklist scoring | Complete |",
        "| 14 | AI Lifecycle | Lifecycle planner, metrics, release planner, dashboard | Complete |",
        "| 15 | RAG and Vector Databases | Local RAG index, retriever, Claude answer generator, logger | Complete |",
        "| 16 | Open Models | Model selection, evaluation, experiment, deployment planning | Complete |",
        "| 17 | AI Agents | Local agent, persistent state, multi-agent meetings | Complete |",
        "| 18 | Fine-Tuning | Decision, readiness, formatting, evaluation planning | Complete |",
        "",
        "## ResearchLab Stack",
        "",
        "Research question generation -> Semantic search -> RAG retrieval -> Claude grounded answer generation -> Evaluation logging -> Agent planning -> Multi-agent review -> Lifecycle and security governance",
        "",
        "## Business Ops Stack",
        "",
        "Workflow idea -> Low-code table planning -> Tracker generation -> Automation prompt planning -> Communication drafting -> Dashboard-ready outputs",
        "",
        "## Trading Lab Stack",
        "",
        "Paper-trading concept -> Risk-control planning -> Monitoring logic -> Audit logging -> Human review -> No live execution without governance",
        "",
        "## Immediate Priorities",
        "",
        "1. Clean .gitignore.",
        "2. Stop committing private runtime records.",
        "3. Expand ResearchLab RAG knowledge base.",
        "4. Add source attribution to RAG answers.",
        "5. Benchmark embedding models.",
        "6. Create Streamlit prototype for ResearchLab.",
        "7. Build safe exportable portfolio summary.",
    ]

    write_lines(progress_path, lines)
    print("Created AI_LAB_PROGRESS_MAP.md")


def update_gitignore():
    gitignore_path = ROOT / ".gitignore"

    existing = ""
    if gitignore_path.exists():
        existing = gitignore_path.read_text(encoding="utf-8")

    additions = [
        "",
        "# Environment and secrets",
        ".env",
        ".env.*",
        "!.env.example",
        "",
        "# Python cache",
        "__pycache__/",
        "**/__pycache__/",
        "*.pyc",
        "",
        "# Virtual environments",
        ".venv/",
        "venv/",
        "env/",
        "",
        "# Private AI Lab runtime records",
        "microsoft-generative-ai-for-beginners/lesson-17-ai-agents/agent_state/",
        "microsoft-generative-ai-for-beginners/lesson-17-ai-agents/multi_agent_meeting_records/",
        "microsoft-generative-ai-for-beginners/lesson-17-ai-agents/claude_multi_agent_meeting_records/",
        "microsoft-generative-ai-for-beginners/lesson-15-rag-and-vector-databases/rag_evaluation_logs/",
        "",
        "# Local generated logs",
        "*.log",
    ]

    updated_lines = existing.splitlines()

    for line in additions:
        if line and line in updated_lines:
            continue
        updated_lines.append(line)

    write_lines(gitignore_path, updated_lines)
    print("Updated .gitignore")


def update_requirements():
    requirements_path = ROOT / "requirements.txt"

    existing_packages = set()
    if requirements_path.exists():
        existing_packages = {
            line.strip()
            for line in requirements_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        }

    required = {
        "anthropic",
        "python-dotenv",
        "sentence-transformers",
        "scikit-learn",
        "numpy",
        "pandas",
    }

    final_packages = sorted(existing_packages.union(required))
    write_lines(requirements_path, final_packages)
    print("Updated requirements.txt")


def create_safe_examples():
    examples_dir = ROOT / "safe_examples"
    examples_dir.mkdir(exist_ok=True)

    agent_example = {
        "agent_name": "ResearchLab Persistent Agent",
        "created_at": "YYYY-MM-DDTHH:MM:SS",
        "last_updated": "YYYY-MM-DDTHH:MM:SS",
        "conversation_history": [],
        "task_memory": [
            {
                "goal": "Example research planning task",
                "selected_tool": "create_next_action_plan",
                "tool_result": {
                    "next_actions": [
                        "Clarify objective",
                        "Gather evidence",
                        "Review output",
                    ]
                },
            }
        ],
        "status": "example",
    }

    meeting_example = {
        "timestamp": "YYYY-MM-DDTHH:MM:SS",
        "pitch": "Example AI app pitch",
        "context": "Example non-sensitive context",
        "agent_outputs": [],
        "integrated_recommendation": {
            "meeting_summary": "Example summary only."
        },
    }

    (examples_dir / "agent_state_example.json").write_text(
        json.dumps(agent_example, indent=2),
        encoding="utf-8",
    )

    (examples_dir / "multi_agent_meeting_example.json").write_text(
        json.dumps(meeting_example, indent=2),
        encoding="utf-8",
    )

    print("Created safe example JSON files")


def main():
    print("\nStarting AI Lab repo consolidation...\n")

    write_readme()
    write_progress_map()
    update_gitignore()
    update_requirements()
    create_safe_examples()

    print("\nConsolidation complete.")
    print("\nNext commands:")
    print("git status")
    print("git rm -r --cached microsoft-generative-ai-for-beginners/lesson-17-ai-agents/agent_state")
    print("git rm -r --cached microsoft-generative-ai-for-beginners/lesson-17-ai-agents/multi_agent_meeting_records")
    print("git rm -r --cached microsoft-generative-ai-for-beginners/lesson-17-ai-agents/claude_multi_agent_meeting_records")
    print("git add .")
    print('git commit -m "Consolidate AI Lab portfolio documentation and ignore private runtime records"')
    print("git push")


if __name__ == "__main__":
    main()