# Projekt 2.0 — Übungsprojekt für Claude Code

Dies ist ein kleines Übungsprojekt, um den Umgang mit Claude Code zu lernen.

## Was ist das?
Eine simple Kommandozeilen-To-Do-Liste in Python (`app.py`). Aufgaben werden
in `todos.json` gespeichert.

## Befehle
- Aufgabe hinzufügen: `python3 app.py add "Text"`
- Aufgaben anzeigen: `python3 app.py list`
- Aufgabe erledigen: `python3 app.py done <nummer>`
- Aufgabe löschen: `python3 app.py remove <nummer>`
- Tests laufen lassen: `python3 -m pytest`

## Für Claude
- Halte Änderungen klein und fokussiert.
- Nach jeder Änderung an `app.py`: Tests laufen lassen.
- Style: einfache, gut lesbare Funktionen, keine externen Abhängigkeiten.
- Commits klein und gezielt (benannte Dateien), nie `git add -A`/`add .`.
- Eine Behauptung wie "funktioniert" zählt erst, wenn Tests es zeigen.
- Stolpersteine kurz in `LESSONS.md` festhalten, am selben Tag.
