"""
Tools for the Personal Research Assistant:
  - web_search    : DuckDuckGo search (free, no API key)
  - read_file     : Read content from a local file
  - write_file    : Write / append content to a local file
  - list_files    : List files in the reports directory
"""

import os
from datetime import datetime
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

REPORTS_DIR = "reports"


def _ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)


# ── Web Search ──────────────────────────────────────────────────────────────

_ddg = DuckDuckGoSearchRun()

@tool
def web_search(query: str) -> str:
    """Search the web for up-to-date information on any topic.
    Use this when you need current facts, news, or information not in your training data.
    Input should be a clear search query string.
    """
    try:
        result = _ddg.run(query)
        return result if result else "No results found for this query."
    except Exception as e:
        return f"Search failed: {e}. Try rephrasing the query."


# ── File Operations ──────────────────────────────────────────────────────────

@tool
def write_file(filename_and_content: str) -> str:
    """Save research findings to a file in the reports/ directory.
    Input format: 'filename.md|||content to write'
    Use '|||' as the separator between filename and content.
    The filename should be descriptive, e.g. 'ai_trends_2024.md'.
    """
    _ensure_reports_dir()
    if "|||" not in filename_and_content:
        return "Error: Input must be in format 'filename|||content'."

    filename, content = filename_and_content.split("|||", 1)
    filename = filename.strip()

    if not filename:
        filename = f"research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    filepath = os.path.join(REPORTS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())

    return f"Report saved to '{filepath}' ({len(content)} characters)."


@tool
def read_file(filename: str) -> str:
    """Read the content of a previously saved research file from the reports/ directory.
    Input: just the filename, e.g. 'ai_trends_2024.md'.
    """
    _ensure_reports_dir()
    filepath = os.path.join(REPORTS_DIR, filename.strip())
    if not os.path.exists(filepath):
        return f"File '{filename}' not found in reports/. Use list_files to see available files."
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return content if content else "(empty file)"


@tool
def list_files(dummy: str = "") -> str:
    """List all saved research reports in the reports/ directory.
    No input required — pass an empty string or any value.
    """
    _ensure_reports_dir()
    files = os.listdir(REPORTS_DIR)
    if not files:
        return "No reports saved yet."
    return "Saved reports:\n" + "\n".join(f"  - {f}" for f in sorted(files))


# ── Exported tool list ────────────────────────────────────────────────────────

TOOLS = [web_search, write_file, read_file, list_files]
