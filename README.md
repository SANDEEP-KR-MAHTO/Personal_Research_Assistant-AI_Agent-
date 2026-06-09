# Personal Research Assistant 🔍

A free AI agent that researches any topic for you — searches the web, synthesizes findings, and saves a Markdown report automatically.

Built with **LangGraph ReAct** + **Groq (free LLM)** + **DuckDuckGo Search**.

---

## How It Works

```
You ask a question
      ↓
[REASON] Plan what to search
      ↓
[ACT]    Search the web (DuckDuckGo)
      ↓
[OBSERVE] Read results → repeat 3-4 times
      ↓
[ACT]    Save report to reports/topic.md
      ↓
Final summary returned to you
```

---

## Project Structure

```
Simple_AI_Agent/
├── main.py          # Entry point — interactive loop
├── agent.py         # ReAct agent (LangGraph + Groq)
├── tools.py         # Tools: web_search, write_file, read_file, list_files
├── requirements.txt
├── .env.example
└── reports/         # Saved research reports (auto-created)
```

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/Simple_AI_Agent.git
cd Simple_AI_Agent
```

**2. Create a virtual environment**
```bash
python -m venv myenv
myenv\Scripts\activate      # Windows
# source myenv/bin/activate  # macOS/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Get a free Groq API key**
- Sign up at [console.groq.com](https://console.groq.com) (free, no credit card)
- Copy your API key

**5. Create a `.env` file**
```
GROQ_API_KEY=your_api_key_here
```

**6. Run**
```bash
python main.py
```

---

## Example

```
Research topic > Research the latest trends in AI agents in 2024

[Agent searches web 3-4 times, synthesizes findings]

✅ Report saved to reports/ai_agents_2024.md
```

---

## Free Stack

| Component  | Tool                                    |
|------------|-----------------------------------------|
| LLM        | Groq — `llama-4-scout` (free tier)      |
| Web Search | DuckDuckGo (no API key required)        |
| Agent Loop | LangGraph ReAct                         |
| Framework  | LangChain                               |

---

## Requirements

- Python 3.9+
- Free Groq API key
