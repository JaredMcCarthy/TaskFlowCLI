# TaskFlowCLI

## About
TaskFlowCLI is a Python project that runs directly from your PC terminal.

- It allows you to **manage basic tasks**: add, list, mark as completed or pending.  
- All data is stored **locally** (currently in memory), keeping it **lightweight and easy to use**.  
- The idea of the project is to evolve into a **command-line assistant** that can automate actions, open apps, or launch websites directly from the terminal.

## Current Features
- Add, edit, delete, and list tasks.  
- Mark tasks as **completed** or **pending**.  
- Filter tasks by **priority** (High / Low).  
- Automatic unique ID for each task. 

## Future Plans
- Automate small tasks (like opening programs or websites).  
- Add note support.  
- Explore AI or database integrations.

## How to Run
### Windows
1. Open your PC terminal.  
2. Run the `run.bat` file by double-clicking it or from the terminal: 
3. ```bash run.bat ```
### macOS / Linux
1. Open your terminal.
2. Run the run.sh file with execution permissions:
3. ```chmod +x run.sh```
4. ```./run.s```

- You can also run it directly from Python:
```
python main.py   # Windows
python3 main.py  # macOS / Linux
```
## Quick Start
```bash
git clone https://github.com/JaredMcCarthy/TaskFlowCLI.git
cd TaskFlowCLI
#then use run.bat or run.sh depending on your operating system
```

## Contributing
Contributions are welcome!
- Fork the repository
- Create a new branch
- Commit your changes
- Open a pull request

Please keep the code simple and readable and thank you for contribute.

## License
This project is licensed under the MIT License.
