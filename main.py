"""
Personal Research Assistant — Entry Point
Run: python main.py
"""

from agent import build_agent, run_research


BANNER = """
╔══════════════════════════════════════════════════════════╗
║          Personal Research Assistant  🔍                 ║
║  Powered by: Groq (free) + LangGraph ReAct + DuckDuckGo  ║
╚══════════════════════════════════════════════════════════╝

Commands:
  Type your research topic and press Enter
  Type 'quit' or 'exit' to stop

Example queries:
  • "Research the latest trends in AI agents in 2024"
  • "What are the best practices for Python async programming?"
  • "Summarize recent developments in quantum computing"
"""


def main():
    print(BANNER)

    try:
        agent = build_agent()
        print("✅ Agent ready! (Groq API connected)\n")
    except EnvironmentError as e:
        print(f"❌ Setup Error:\n{e}")
        return

    while True:
        try:
            query = input("Research topic > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye!")
            break

        if not query:
            continue

        if query.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break

        try:
            response = run_research(query, agent)
            print("\n" + "─" * 60)
            print(response)
            print("─" * 60 + "\n")
        except Exception as e:
            print(f"\n❌ Error during research: {e}\n")


if __name__ == "__main__":
    main()
