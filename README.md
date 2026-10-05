# To-Do CLI (Python)

A small command-line to-do list written in Python. Tasks are stored in a JSON file. The program uses only the Python standard library; the messages are in German.

## Usage

```bash
python3 app.py add "Buy milk"      # add a task
python3 app.py list                # show all tasks
python3 app.py done 1              # mark task 1 as done
python3 app.py edit 1 "Buy bread"  # change the text of task 1
python3 app.py remove 1            # delete task 1
```

## Tests

The project has automated tests written with pytest. They cover adding, listing, completing, editing and removing tasks, and they check that an invalid task number does not crash the program.

```bash
python3 -m pytest
```

## How it was built

This is a practice project for working with Claude Code, an AI coding agent. The working rules are written down in `CLAUDE.md`: keep changes small, run the tests after every change, and only call something "working" once the tests show it.

## Author

Reza Jafari
