# hello

A tiny greeter app demonstrating a multifile Python project structure.

## Overview

`hello` is a minimal but complete Python project that generates time-aware
greetings. It serves as a reference template showing how to organize a
multifile Python package with proper configuration, testing, documentation,
and version control.

## Features

- **Time-aware greetings** — automatically says "Good morning", "Good afternoon",
  or "Good evening" based on the current hour
- **Flexible input** — accepts a name via CLI argument, environment variable,
  or programmatic API
- **Clean architecture** — separated into config, models, services, and utilities
- **Fully tested** — pytest suite with shared fixtures
- **Auto-generated changelog** — git post-commit hook maintains CHANGELOG.md

## Quick start

```bash
pip install -e "."
hello Alice
```

Output:

```
Good morning, Alice!
```

See [Getting Started](getting-started.md) for full setup instructions.

## Project layout

```
hello_project/
├── pyproject.toml         # Project config, metadata, dependencies
├── mkdocs.yml             # Documentation config
├── src/
│   └── hello/
│       ├── __init__.py    # Package version
│       ├── main.py        # CLI entry point
│       ├── config.py      # Settings from args / env vars
│       ├── models.py      # Greeting dataclass
│       ├── services.py    # Greeter business logic
│       ├── exceptions.py  # Custom errors
│       └── utils.py       # Time-of-day helper
└── tests/
    ├── conftest.py        # Shared fixtures
    └── test_greeter.py    # Test suite
```
