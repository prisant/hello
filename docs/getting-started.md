# Getting Started

## Prerequisites

- Python 3.10 or later
- pip
- git (for changelog automation)

## Installation

Clone the repository and install in a virtual environment:

```bash
git clone https://github.com/yourname/hello.git
cd hello_project

python -m venv .venv
source .venv/bin/activate    # Linux / macOS
# .venv\Scripts\activate     # Windows

make install
```

`make install` does two things: installs the package with dev dependencies
(`pip install -e ".[dev]"`) and configures the git changelog hook.

## Usage

### Command line

After installation, the `hello` command is available:

```bash
# Default — greets "World"
hello

# Pass a name as an argument
hello Alice

# Set via environment variable
GREET_NAME="Bob" hello
```

### As a library

You can also use `hello` programmatically:

```python
from hello.config import Settings
from hello.services import Greeter

settings = Settings(name="Alice")
greeter = Greeter(settings)
greeting = greeter.greet()

print(greeting)          # Good afternoon, Alice!
print(greeting.name)     # Alice
print(greeting.salutation)  # Good afternoon
```

### Override the name at call time

```python
greeter = Greeter(Settings(name="Default"))
greeting = greeter.greet("Override")
print(greeting)  # Good evening, Override!
```

## Running without installing

If you just want to try it without a full install:

```bash
PYTHONPATH=src python -m hello.main Alice
```

## Running tests

```bash
# Basic test run
pytest

# With coverage report
make test-cov

# Lint, type check, and test in one shot
make all
```

## Changelog automation

Every `git commit` automatically regenerates `CHANGELOG.md` from your commit
history. The hook groups entries by tag.

To create a release:

```bash
git tag -a v0.1.0 -m "First release"
git commit --allow-empty -m "chore: trigger changelog for v0.1.0"
```

Commits prefixed with `chore:` or `wip:` are excluded from the changelog.

To skip the hook for a single commit:

```bash
SKIP_CHANGELOG=1 git commit -m "quick fix"
```
