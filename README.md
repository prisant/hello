# hello

A tiny greeter app demonstrating a multifile Python project structure.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

```bash
# Uses default name "World"
hello

# Pass a name as argument
hello Alice

# Or set via environment variable
GREET_NAME="Bob" hello
```

## Development

```bash
# Run tests
pytest

# Run tests with coverage
make test-cov

# Lint, type check, and test in one shot
make all

# Regenerate changelog manually
make changelog
```

## Changelog

`CHANGELOG.md` is auto-generated from git history via a `post-commit` hook.

The hook runs `scripts/generate_changelog.sh` after every commit, grouping
entries by tag. To create a release:

```bash
git tag -a v0.1.0 -m "First release"
git commit --allow-empty -m "chore: trigger changelog for v0.1.0"
```

Commit messages starting with `chore:` or `wip:` are excluded from the changelog.

## Project Structure

```
hello_project/
├── LICENSE                # MIT license
├── README.md
├── CHANGELOG.md           # Auto-generated from git history
├── .gitignore
├── Makefile
├── pyproject.toml         # Project config, metadata, dependencies
├── scripts/
│   └── generate_changelog.sh
├── src/
│   └── hello/
│       ├── __init__.py    # Package init, version
│       ├── main.py        # Entry point (CLI args → Settings → Greeter)
│       ├── config.py      # Settings from args or env vars
│       ├── models.py      # Greeting dataclass
│       ├── services.py    # Greeter business logic
│       ├── exceptions.py  # Custom errors
│       └── utils.py       # Time-of-day salutation helper
└── tests/
    ├── conftest.py        # Shared pytest fixtures
    └── test_greeter.py    # Tests for all modules
```

## License

[MIT](LICENSE)
