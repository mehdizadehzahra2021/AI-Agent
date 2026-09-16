# AI Tool-Using Agent

A local AI Agent built with Python, Ollama, and Qwen3, designed to understand user requests, select appropriate tools, execute them, and generate a final response based on the tool results.

This project is being developed hands-on as a foundation for building practical AI Agents and business automation systems.

## 🚀 Current Capabilities

- Local LLM inference with Ollama
- Qwen3 model integration
- LLM-powered Tool / Function Calling
- Current time tool
- Calculator tool
- Web search using Tavily
- Tool execution and result handling
- Conversational message history
- Git and GitHub version control

## 🧠 How It Works

The Agent follows a simple tool-using workflow:

User Request
     ↓
   Qwen3
     ↓
Decide whether a tool is needed
     ↓
  Select Tool
     ↓
Python executes the tool
     ↓
  Tool Result
     ↓
   Qwen3
     ↓
 Final Answer

The important concept is that the LLM does not directly execute Python functions. It decides which tool should be used and what arguments should be passed, while Python performs the actual execution.

## 🛠️ Available Tools

### ⏰ Time Tool

Returns the current local time when the user asks for the current time.

### 🧮 Calculator

Performs calculations using a Python function selected through tool calling.

### 🌐 Web Search

Uses Tavily to search the web when the Agent needs external information.

Search results are processed and passed back to the LLM so it can generate a final response.

## 💻 Tech Stack

- Python
- Ollama
- Qwen3
- Tavily
- Git
- GitHub

## 📁 Project Structure

AI Agent/
│
├── main.py
├── README.md
├── .gitignore
├── .env
└── .venv/

Sensitive configuration such as API keys is stored in .env and excluded from version control.

## 📌 Project Development

The project is being developed incrementally, with Git checkpoints documenting the evolution of the Agent.

Current development milestones include:

- Initial local LLM integration
- Tool calling implementation
- Multiple tool integration
- Web search integration
- Tool result processing
- Git/GitHub version control

## 🔭 Future Development

Planned improvements include:

- More robust tool execution architecture
- Memory and conversation state
- RAG and document processing
- File-based tools
- Business-oriented automation tools
- Workflow automation
- Improved reliability and error handling
- More production-ready Agent architecture

## 🎯 Project Goal

The long-term goal is to evolve this project from a basic local AI Agent into a practical AI automation system capable of using tools, processing information, and performing real-world business tasks.

The project also serves as a hands-on portfolio demonstrating practical experience with LLMs, AI Agents, tool calling, Python, and automation workflows
