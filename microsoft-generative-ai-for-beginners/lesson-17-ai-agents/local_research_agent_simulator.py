# --------------------------------------------------
# Lesson 17 Build 1: Local Research Agent Simulator
# Microsoft Generative AI for Beginners adaptation
# Purpose:
# Simulate an AI agent with state, tools, tool selection,
# tool execution, state update, and final response.
# --------------------------------------------------


def generate_research_question(topic="", crop="", context=""):
    """
    Tool 1: Generate a research question, working title,
    and possible contribution.
    """

    if not topic:
        topic = "AI-enabled agricultural decision support"

    if "harvest maturity" in topic.lower() and "ai" not in topic.lower():
        topic = "AI-enabled harvest maturity assessment"

    if not crop:
        crop = "horticultural crops"

    if not context:
        context = "resource-constrained LMIC systems"

    return {
        "research_question": (
            f"How can {topic} improve postharvest decision-making "
            f"for {crop} in {context}?"
        ),
        "working_title": f"{topic} for {crop} in {context}",
        "possible_contribution": (
            "This study could clarify how AI tools can support better harvest timing, "
            "reduce postharvest losses, and improve value-chain decisions."
        )
    }


def normalize_search_terms(topic="", crop="", method="", context=""):
    """
    Normalize extracted arguments into searchable terms.
    This prevents strict search from failing when the extracted phrase
    is more elaborate than the stored record phrase.
    """

    query_terms = []

    if topic:
        topic_lower = topic.lower()

        if "harvest maturity" in topic_lower:
            query_terms.append("harvest maturity")
        elif "postharvest" in topic_lower:
            query_terms.append("postharvest")
        elif "ai adoption" in topic_lower:
            query_terms.append("ai adoption")
        else:
            query_terms.append(topic_lower)

    if crop:
        crop_lower = crop.lower()

        if "tomatoes" in crop_lower:
            query_terms.append("tomato")
        else:
            query_terms.append(crop_lower)

    if method:
        method_lower = method.lower()

        if "nir" in method_lower or "near-infrared" in method_lower:
            query_terms.append("near-infrared spectroscopy")
        else:
            query_terms.append(method_lower)

    if context:
        context_lower = context.lower()

        if "lmic" in context_lower:
            query_terms.append("lmic")
        elif "resource-constrained" in context_lower:
            query_terms.append("resource-constrained")
        elif "warm-chain" in context_lower:
            query_terms.append("warm-chain")
        else:
            query_terms.append(context_lower)

    return [term for term in query_terms if term]


def search_research_records(topic="", crop="", method="", context=""):
    """
    Tool 2: Search a small local research record list.
    This simulates a database or literature search tool.
    """

    records = [
        {
            "title": "AI for tomato harvest maturity detection",
            "topic": "harvest maturity",
            "crop": "tomato",
            "method": "computer vision",
            "context": "warm-chain horticultural systems",
            "finding": (
                "Computer vision can classify tomato maturity stages using colour "
                "and surface features."
            )
        },
        {
            "title": "NIR spectroscopy for avocado maturity",
            "topic": "internal quality",
            "crop": "avocado",
            "method": "near-infrared spectroscopy",
            "context": "non-destructive maturity testing",
            "finding": (
                "NIR can estimate dry matter and oil content as indicators "
                "of harvest maturity."
            )
        },
        {
            "title": "AI adoption barriers in LMIC agriculture",
            "topic": "AI adoption",
            "crop": "smallholder systems",
            "method": "literature review",
            "context": "LMIC agriculture",
            "finding": (
                "High cost, limited connectivity, weak extension support, "
                "and low technical capacity reduce AI adoption."
            )
        },
        {
            "title": "Smartphone AI tools for harvest timing",
            "topic": "decision support",
            "crop": "horticultural crops",
            "method": "mobile AI",
            "context": "resource-constrained farming systems",
            "finding": (
                "Smartphone-based AI tools can support harvest timing, grading, "
                "disease diagnosis, and market readiness."
            )
        }
    ]

    query_terms = normalize_search_terms(
        topic=topic,
        crop=crop,
        method=method,
        context=context
    )

    results = []

    for record in records:
        searchable_text = " ".join([
            record["title"],
            record["topic"],
            record["crop"],
            record["method"],
            record["context"],
            record["finding"]
        ]).lower()

        if not query_terms or all(term in searchable_text for term in query_terms):
            results.append(record)

    return {
        "query_terms_used": query_terms,
        "matches_found": len(results),
        "records": results
    }


def draft_deadline_reminder(project="", deadline="", next_action=""):
    """
    Tool 3: Draft a deadline reminder.
    """

    if not project:
        project = "the project"

    if not deadline:
        deadline_phrase = "soon"
    elif deadline.lower() == "next week":
        deadline_phrase = "next week"
    else:
        deadline_phrase = f"on {deadline}"

    if not next_action:
        next_action = "review the project and update the status"

    return {
        "subject": f"Deadline Reminder: {project}",
        "message": (
            f"Hello, this is a reminder that '{project}' has an upcoming deadline "
            f"{deadline_phrase}. Next action required: {next_action}. "
            "Please review and update the project status."
        )
    }


def create_next_action_plan(goal=""):
    """
    Tool 4: Create a practical next-action plan.
    """

    if not goal:
        goal = "complete the research task"

    lower_goal = goal.lower()

    if "rag" in lower_goal:
        next_actions = [
            "Expand the knowledge base with more high-quality research notes and papers.",
            "Improve chunking strategy by testing different chunk sizes and overlaps.",
            "Evaluate retrieval quality using repeated test questions.",
            "Add stronger prompt-injection protection for retrieved context.",
            "Use the RAG evaluation logger to track groundedness, relevance, and limitation quality.",
            "Create a versioned release plan before using the app with other users."
        ]

    elif "manuscript" in lower_goal or "review" in lower_goal:
        next_actions = [
            "Clarify the manuscript objective and target journal.",
            "Refine the research question and review scope.",
            "Create a literature search strategy.",
            "Develop the manuscript structure.",
            "Identify gaps, conceptual framework, and contribution.",
            "Draft section by section with human review."
        ]

    else:
        next_actions = [
            "Clarify the exact objective.",
            "Identify the target users and expected output.",
            "Gather or retrieve supporting evidence.",
            "Draft a structured output.",
            "Review for accuracy, limitations, and next steps."
        ]

    return {
        "goal": goal,
        "next_actions": next_actions,
        "human_review_needed": (
            "Yes. Human review is needed before using outputs in manuscripts, "
            "grants, student assessment, institutional decisions, or public communication."
        )
    }


TOOLS = {
    "generate_research_question": generate_research_question,
    "search_research_records": search_research_records,
    "draft_deadline_reminder": draft_deadline_reminder,
    "create_next_action_plan": create_next_action_plan
}


def initialize_agent_state():
    """
    Create the starting state for the agent.
    State keeps track of past turns, current goal, selected tool,
    arguments, result, and next action.
    """

    return {
        "conversation_history": [],
        "current_goal": "",
        "selected_tool": "",
        "tool_arguments": {},
        "tool_result": {},
        "next_action": "",
        "status": "idle"
    }


def clean_words(text):
    """
    Convert text into simple word tokens for safer matching.
    This prevents matching 'search' inside 'researchlab'.
    """

    punctuation = [".", ",", "?", "!", ":", ";", "(", ")", "[", "]", "{", "}"]

    for mark in punctuation:
        text = text.replace(mark, " ")

    return text.lower().split()


def extract_arguments(user_message):
    """
    Extract simple arguments from the user message.
    In a real agent, an LLM would do this more intelligently.
    """

    text = user_message.lower()

    args = {
        "topic": "",
        "crop": "",
        "method": "",
        "context": "",
        "project": "",
        "deadline": "",
        "next_action": "",
        "goal": user_message
    }

    if "tomato" in text or "tomatoes" in text:
        args["crop"] = "tomato"

    if "avocado" in text:
        args["crop"] = "avocado"

    if "computer vision" in text:
        args["method"] = "computer vision"

    if "nir" in text or "near-infrared" in text or "near infrared" in text:
        args["method"] = "near-infrared spectroscopy"

    if "lmic" in text or "lmics" in text:
        args["context"] = "resource-constrained LMIC systems"

    if "resource-constrained" in text:
        args["context"] = "resource-constrained LMIC systems"

    if "warm-chain" in text or "warm chain" in text:
        args["context"] = "warm-chain horticultural systems"

    if "harvest maturity" in text:
        args["topic"] = "AI-enabled harvest maturity assessment"

    if "postharvest" in text:
        args["topic"] = "postharvest loss reduction"

    if "ai adoption" in text or "adoption barriers" in text:
        args["topic"] = "AI adoption"

    if "manuscript" in text:
        args["project"] = "manuscript project"

    if "review" in text:
        args["project"] = "literature review project"

    if "rag app" in text or "rag" in text:
        args["project"] = "ResearchLab RAG app"

    if "next week" in text:
        args["deadline"] = "next week"

    if "outline" in text:
        args["next_action"] = "complete the outline"

    return args


def choose_tool(user_message):
    """
    Choose the best tool based on user intent.

    Important:
    - Planning intent is checked before search.
    - Word-level matching is used to avoid matching 'search' inside 'researchlab'.
    """

    text = user_message.lower()
    words = clean_words(user_message)

    # 1. Planning intent should come before search intent
    if (
        "plan" in words
        or "steps" in words
        or "next" in words
        or "improving" in words
        or "improve" in words
        or "roadmap" in words
    ):
        return "create_next_action_plan"

    # 2. Research question/title generation
    if (
        "research question" in text
        or "working title" in text
        or "generate a question" in text
        or "create a question" in text
        or "generate a research question" in text
    ):
        return "generate_research_question"

    # 3. Reminder/email/notification
    if (
        "reminder" in words
        or "deadline" in words
        or "email" in words
        or "notify" in words
        or "message" in words
    ):
        return "draft_deadline_reminder"

    # 4. Search intent using word-level matching
    if (
        "search" in words
        or "find" in words
        or "records" in words
        or "record" in words
        or "literature" in words
        or "studies" in words
        or "papers" in words
    ):
        return "search_research_records"

    return "create_next_action_plan"


def execute_selected_tool(tool_name, args):
    """
    Execute the selected tool safely using only allowed tools.
    """

    if tool_name not in TOOLS:
        return {
            "error": "No valid tool selected.",
            "available_tools": list(TOOLS.keys())
        }

    if tool_name == "generate_research_question":
        return TOOLS[tool_name](
            topic=args["topic"],
            crop=args["crop"],
            context=args["context"]
        )

    if tool_name == "search_research_records":
        return TOOLS[tool_name](
            topic=args["topic"],
            crop=args["crop"],
            method=args["method"],
            context=args["context"]
        )

    if tool_name == "draft_deadline_reminder":
        return TOOLS[tool_name](
            project=args["project"],
            deadline=args["deadline"],
            next_action=args["next_action"]
        )

    if tool_name == "create_next_action_plan":
        return TOOLS[tool_name](
            goal=args["goal"]
        )

    return {
        "error": "Tool execution failed unexpectedly."
    }


def agent_step(user_message, state):
    """
    Perform one agent step:
    1. Receive user goal
    2. Update state
    3. Extract arguments
    4. Choose tool
    5. Execute tool
    6. Store result
    7. Recommend next action
    """

    state["status"] = "thinking"
    state["current_goal"] = user_message

    state["conversation_history"].append({
        "role": "user",
        "content": user_message
    })

    args = extract_arguments(user_message)
    selected_tool = choose_tool(user_message)

    state["selected_tool"] = selected_tool
    state["tool_arguments"] = args
    state["status"] = "using_tool"

    tool_result = execute_selected_tool(selected_tool, args)

    state["tool_result"] = tool_result
    state["status"] = "completed"

    if selected_tool == "generate_research_question":
        state["next_action"] = (
            "Review the generated question and decide whether to refine the crop, "
            "context, method, or outcome."
        )

    elif selected_tool == "search_research_records":
        if tool_result.get("matches_found", 0) == 0:
            state["next_action"] = (
                "No matching records were found. Broaden the query, add more records, "
                "or search the full RAG knowledge base."
            )
        else:
            state["next_action"] = (
                "Review retrieved records and decide whether more evidence is needed."
            )

    elif selected_tool == "draft_deadline_reminder":
        state["next_action"] = "Review the reminder before sending."

    else:
        state["next_action"] = "Follow the next-action plan and update the task state."

    state["conversation_history"].append({
        "role": "agent",
        "tool_used": selected_tool,
        "result": tool_result
    })

    return state


def print_agent_response(state):
    """
    Display the agent state update in a readable way.
    """

    print("\nAgent State Update:\n")
    print(f"Status: {state['status']}")
    print(f"Current goal: {state['current_goal']}")
    print(f"Selected tool: {state['selected_tool']}")
    print(f"Next action: {state['next_action']}")

    print("\nTool Arguments:")
    shown_any_argument = False

    for key, value in state["tool_arguments"].items():
        if value:
            print(f"- {key}: {value}")
            shown_any_argument = True

    if not shown_any_argument:
        print("- No specific arguments extracted.")

    print("\nTool Result:")
    print(state["tool_result"])

    print("\nConversation turns stored:")
    print(len(state["conversation_history"]))


print("\nLocal Research Agent Simulator")
print("Lesson 17: AI Agents")
print("Type 'exit' anytime to stop.\n")

agent_state = initialize_agent_state()

while True:
    user_message = input("You: ")

    if user_message.lower().strip() in ["exit", "quit", "stop"]:
        print("Local research agent simulator ended.")
        break

    agent_state = agent_step(
        user_message=user_message,
        state=agent_state
    )

    print_agent_response(agent_state)
    print("\n" + "=" * 100 + "\n")