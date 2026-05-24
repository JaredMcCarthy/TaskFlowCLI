# TaskFlowCLI

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A command-line task manager built in Python — simple, local, no dependencies.
Actively evolving toward v2.0 with JSON persistence, OOP architecture and a modular structure.

---

## Features

- **Add, edit, delete and list tasks** from the terminal
- **Mark tasks** as completed or pending
- **Filter by priority** — High or Low
- **Auto-generated unique ID** for every task
- **No external dependencies** — pure Python standard library

## Quick Start

```bash
git clone https://github.com/JaredMcCarthy/TaskFlowCLI.git
cd TaskFlowCLI
python main.py        # Windows
python3 main.py       # macOS / Linux
```

You can also just double-click `run.bat` on Windows or run `./run.sh` on macOS/Linux.

## What's coming in v2.0

- JSON file persistence (tasks saved between sessions)
- Full OOP rewrite with `Task` and `TaskManager` classes
- Robust error handling and input validation
- Clean modular structure across separate files/folders
- Unit tests and docstrings throughout

## License

This project is licensed under the MIT License.
