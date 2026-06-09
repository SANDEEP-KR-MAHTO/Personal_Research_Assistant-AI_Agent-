"""
Personal Research Assistant — ReAct Agent
Built with LangGraph + Groq (free tier)

ReAct loop: Reason → Act (tool call) → Observe (result) → Reason → ...
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

from tools import TOOLS

load_dotenv()

SYSTEM_PROMPT = """You are a thorough Personal Research Assistant. Your job is to help users
research any topic by searching the web, gathering information from multiple angles, and
producing a well-structured written report.

Follow this workflow for every research request:
1. PLAN — Break the topic into 2-4 focused sub-questions.
2. SEARCH — Run a web_search for each sub-question. Use specific, targeted queries.
3. SYNTHESIZE — Combine findings into coherent sections with key insights.
4. SAVE — Write a well-formatted Markdown report using write_file.
5. CONFIRM — Tell the user where the report was saved and give a brief summary.

Report format (Markdown):
  # [Topic]
  **Date:** YYYY-MM-DD
  ## Overview
  ## Key Findings
  ## [Section per sub-topic]
  ## Sources & References
  ## Summary

Guidelines:
- Always search before answering — do not rely on training knowledge alone.
- Run at least 3 different searches to get a well-rounded view.
- Be factual and cite what you found in each search.
- Save every research output to a file automatically.
"""


def build_agent(model: str = "meta-llama/llama-4-scout-17b-16e-instruct"):
    """Create and return the ReAct agent."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY not set.\n"
            "1. Sign up free at https://console.groq.com\n"
            "2. Copy your API key\n"
            "3. Create a .env file with: GROQ_API_KEY=your_key_here"
        )

    llm = ChatGroq(
        model=model,
        temperature=0,
        api_key=api_key,
    )

    agent = create_react_agent(
        model=llm,
        tools=TOOLS,
        prompt=SYSTEM_PROMPT,
    )
    return agent


def run_research(query: str, agent=None) -> str:
    """Run the agent on a research query and return the final response."""
    if agent is None:
        agent = build_agent()

    print(f"\n{'='*60}")
    print(f" Research Query: {query}")
    print(f"{'='*60}\n")

    result = agent.invoke({"messages": [HumanMessage(content=query)]})
    final_message = result["messages"][-1].content
    return final_message
