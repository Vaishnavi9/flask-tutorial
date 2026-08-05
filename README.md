# Flask Tutorial

Minimal Flask hello-world app for learning.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## Project structure

```text
flask-tutorial/
├── README.md
├── pyproject.toml
├── .gitignore
├── .python-version
└── src/
    └── flask_tutorial/
        ├── __init__.py              # package entry (main, my_app)
        └── flask_tutorial.py        # Flask app + routes
```

## Setup

```bash
cd /Users/vaishnavidhanwade/Projects/flask-tutorial
uv sync
```

This creates `.venv` and installs Flask.

## Run the server

Any of these work:

```bash
# recommended (Flask CLI)
uv run flask --app flask_tutorial.flask_tutorial:my_app run --debug

# via project script
uv run flask-tutorial

# as a module
uv run python -m flask_tutorial.flask_tutorial
```

Then open: http://127.0.0.1:5000/

You should see: `Hello World!`

Stop the server with `Ctrl+C`.

### Custom host / port

```bash
uv run flask --app flask_tutorial.flask_tutorial:my_app run --debug --host 127.0.0.1 --port 5000
```

## Quick test

```bash
curl http://127.0.0.1:5000/
```

## Git

This project is already a git repo on branch `main`.

Useful commands:

```bash
git status
git add .
git commit -m "Your message"
git log --oneline
```

To push to GitHub (after creating a remote repo):

```bash
gh repo create flask-tutorial --private --source=. --remote=origin --push
# or
git remote add origin <your-repo-url>
git push -u origin main
```

## Notes

- Debug mode auto-reloads when you edit code.
- Do not use the development server in production.
