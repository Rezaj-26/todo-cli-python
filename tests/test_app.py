import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import app


def setup_function():
    if app.TODO_FILE.exists():
        app.TODO_FILE.unlink()


def test_add_and_list(capsys):
    app.add("Milch kaufen")
    todos = app.load_todos()
    assert todos == [{"text": "Milch kaufen", "done": False}]


def test_done():
    app.add("Wäsche waschen")
    app.done(1)
    todos = app.load_todos()
    assert todos[0]["done"] is True


def test_remove():
    app.add("Zu löschen")
    app.remove(1)
    assert app.load_todos() == []


def test_edit():
    app.add("Alter Text")
    app.edit(1, "Neuer Text")
    todos = app.load_todos()
    assert todos[0]["text"] == "Neuer Text"


def test_done_invalid_index_does_not_crash(capsys):
    app.add("Einzige Aufgabe")
    app.done(99)
    todos = app.load_todos()
    assert todos[0]["done"] is False
    assert "Keine Aufgabe" in capsys.readouterr().out
