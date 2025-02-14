# Python SQLite Agent Storage with Agno AI 🤖

![playground](./sqlite-agno-playground.gif)
![screenshot](./screenshot.png)

[![Agno](https://img.shields.io/badge/Agno-AI%20Agents-blue)](https://www.agno.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite)](https://www.sqlite.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.8-blue?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/Ollama-0.4.7-blue?logo=llama)](https://ollama.ai/)

This project demonstrates how to implement SQLite-based agent storage for persisting conversation history and session data using Agno AI. Based on the tutorial by [Jie Jenn](https://www.youtube.com/watch?v=-lEvd6JYafY).

## Features 🌟

- SQLite-based agent storage implementation
- Persistent conversation history
- Efficient session data management
- Workflow state persistence
- Real-time agent playground interface

## Prerequisites 📚

- Python 3.12 or higher
- Ollama installed and running
- Virtual environment (recommended)

## Installation 📦

1. Clone the repository:
```bash
git clone https://github.com/agno-ai/python-sqlite-agno-history-storage.git
cd python-sqlite-agno-history-storage
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration 🔧

1. Start the Ollama server:
```bash
ollama serve
```

2. The project uses SQLite for storage. The database will be automatically created at:
```
./storage/social_media_sessions.db
```

## Usage 🚀

1. Run the demo application:
```bash
python demo.py
```

2. Access the Agent Playground:
- Local URL: http://localhost:7777
- Playground URL: https://app.agno.com/playground?endpoint=localhost%3A7777

## Project Structure 📂

```
python-sqlite-agno-history-storage/
├── demo.py                 # Main demo application
├── load_storage.py         # SQLite storage configuration
├── requirements.txt        # Project dependencies
└── storage/               # SQLite database directory
    └── social_media_sessions.db
```

## How It Works 🔍

The project uses Agno's `SqliteAgentStorage` class to manage agent sessions and conversation history. Key components:

1. **Storage Configuration** (`load_storage.py`):
   - Configures SQLite storage for agent sessions
   - Defines table structure for storing conversation history
   - Manages session data persistence

2. **Demo Application** (`demo.py`):
   - Initializes the agent with SQLite storage
   - Sets up the playground interface
   - Handles real-time agent interactions

## Dependencies 📦

- `agno>=0.1.0`: Core Agno AI framework
- `sqlalchemy`: SQL toolkit and ORM
- `ollama`: LLM model management
- `fastapi`: Modern web framework
- `python-dotenv`: Environment variable management
- `uvicorn`: ASGI server implementation

## Credits 📚

- Tutorial by [Jie Jenn](https://www.youtube.com/watch?v=-lEvd6JYafY)
- [Agno AI](https://www.agno.com/) - AI Agent Framework

## License 📝

This project is licensed under the terms specified in the project's license file.

---
Built with [Agno](https://www.agno.com/) - The open-source platform for building, shipping, and monitoring agentic systems.
