import json
import sys
from pathlib import Path

TODO_FILE = Path(__file__).parent / "todos.json"


def load_todos():
    if not TODO_FILE.exists():
        return []
    return json.loads(TODO_FILE.read_text())


def save_todos(todos):
    TODO_FILE.write_text(json.dumps(todos, indent=2, ensure_ascii=False))


def add(text):
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print(f"Hinzugefügt: {text}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("Keine Aufgaben.")
        return
    for i, todo in enumerate(todos, start=1):
        mark = "x" if todo["done"] else " "
        print(f"[{mark}] {i}. {todo['text']}")


def check_index(todos, index):
    if index < 1 or index > len(todos):
        print(f"Keine Aufgabe mit Nummer {index}. Es gibt {len(todos)} Aufgabe(n).")
        return False
    return True


def done(index):
    todos = load_todos()
    if not check_index(todos, index):
        return
    todos[index - 1]["done"] = True
    save_todos(todos)
    print(f"Erledigt: {todos[index - 1]['text']}")


def edit(index, new_text):
    todos = load_todos()
    if not check_index(todos, index):
        return
    old_text = todos[index - 1]["text"]
    todos[index - 1]["text"] = new_text
    save_todos(todos)
    print(f"Geändert: '{old_text}' -> '{new_text}'")


def remove(index):
    todos = load_todos()
    if not check_index(todos, index):
        return
    removed = todos.pop(index - 1)
    save_todos(todos)
    print(f"Entfernt: {removed['text']}")


def main():
    if len(sys.argv) < 2:
        print("Nutzung: app.py [add|list|done|remove] ...")
        return

    command = sys.argv[1]
    if command == "add":
        add(" ".join(sys.argv[2:]))
    elif command == "list":
        list_todos()
    elif command == "done":
        done(int(sys.argv[2]))
    elif command == "edit":
        edit(int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif command == "remove":
        remove(int(sys.argv[2]))
    else:
        print(f"Unbekannter Befehl: {command}")


if __name__ == "__main__":
    main()
