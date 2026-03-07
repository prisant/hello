# Development Guide

Quick reference for day-to-day development on this project.

## First-time setup

```bash
git clone https://github.com/prisant/hello.git
cd hello_project

python -m venv .venv
source .venv/bin/activate

make install          # editable install + dev deps + git hooks
```

## Daily workflow

```bash
# Run everything before committing
make all              # lint + typecheck + test

# Individual checks
make test             # pytest
make test-cov         # pytest with coverage report
make lint             # ruff check
make format           # ruff format
make typecheck        # mypy strict

# Fix lint issues automatically
ruff check --fix src/ tests/
ruff format src/ tests/

# Preview documentation
make docs             # serves at http://127.0.0.1:8000

# Clean build artifacts
make clean
```

## Git commit conventions

Commit messages use conventional prefixes. The changelog includes all
commits except those starting with `chore:` or `wip:`.

### Commit types

```bash
# New feature (appears in changelog)
git commit -am "feat: add batch processing mode"

# Bug fix (appears in changelog)
git commit -am "fix: handle empty input files gracefully"

# Documentation (appears in changelog)
git commit -am "docs: add API examples for batch mode"

# Test changes (appears in changelog)
git commit -am "test: add coverage for edge cases"

# Code restructuring (appears in changelog)
git commit -am "refactor: extract parser into separate module"

# Maintenance tasks (excluded from changelog)
git commit -am "chore: update dev dependencies"

# Work in progress (excluded from changelog)
git commit -am "wip: experimenting with async processing"
```

### Commit flags

```bash
# Stage and commit all tracked changes
git commit -am "feat: add new feature"

# Commit only staged changes
git add src/hello/services.py tests/test_greeter.py
git commit -m "fix: correct salutation logic"

# Amend the last commit (before pushing)
git commit --amend --no-edit        # keep same message
git commit --amend -m "new message" # change the message

# Skip the changelog hook for one commit
SKIP_CHANGELOG=1 git commit -am "chore: minor cleanup"
```

## Branching

```bash
# Create a feature branch
git checkout -b feature/my-change

# Switch back to main
git checkout main

# Merge a feature branch
git checkout main
git merge feature/my-change

# Delete a merged branch
git branch -d feature/my-change
```

## Releasing

```bash
# Bump version, commit, and tag in one step
make bump
# Prompts for the new version number, then:
#   - updates pyproject.toml
#   - updates src/hello/__init__.py
#   - commits the change
#   - creates an annotated git tag

# Push the release
git push && git push --tags
```

## Applying patches

When receiving a patch file:

```bash
# Move patch to project, apply, clean up, verify, commit, push
mv ~/Desktop/Downloads/my-feature.patch .
git apply my-feature.patch
rm my-feature.patch
ruff check --fix src/ tests/
ruff format src/ tests/
make all
git add -A
git commit -m "feat: description of change"
git push
```

Or as a one-liner:

```bash
mv ~/Desktop/Downloads/my-feature.patch . && git apply my-feature.patch && rm my-feature.patch && ruff check --fix src/ tests/ && ruff format src/ tests/ && make all && git add -A && git commit -m "feat: description of change" && git push
```

## Useful git commands

```bash
# View status and recent history
git status
git log --oneline -10
git log --oneline --decorate --graph

# See what changed
git diff                    # unstaged changes
git diff --cached           # staged changes
git diff HEAD~1             # changes since last commit

# Undo mistakes
git checkout -- file.py     # discard unstaged changes to a file
git reset HEAD file.py      # unstage a file
git reset --soft HEAD~1     # undo last commit, keep changes staged
git reset --hard HEAD~1     # undo last commit, discard changes (careful!)

# Stash work in progress
git stash                   # save uncommitted changes
git stash pop               # restore stashed changes

# Check remote state
git remote -v               # show remote URLs
git branch -a               # show all branches
git fetch                   # update remote tracking branches

# Tags
git tag                     # list tags
git tag -a v0.1.0 -m "msg" # create annotated tag
git push --tags             # push tags to remote
```

## Project structure

When adding new functionality, follow the existing module pattern:

| File | Purpose |
|------|---------|
| `config.py` | Settings from args or env vars |
| `models.py` | Greeting dataclass |
| `services.py` | Greeter business logic |
| `exceptions.py` | Custom error classes |
| `utils.py` | Time-of-day salutation helper |
| `main.py` | CLI entry point (keep thin, delegate to services) |

## Adding dependencies

```bash
# 1. Edit pyproject.toml
#    Runtime deps → [project.dependencies]
#    Dev-only deps → [project.optional-dependencies.dev]

# 2. Reinstall
pip install -e ".[dev]"
```
