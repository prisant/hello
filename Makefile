.PHONY: install install-hooks test test-cov lint format typecheck pylint changelog docs docs-build bump clean all

install:
	pip install -e ".[dev]"
	$(MAKE) install-hooks

install-hooks:
	git config core.hooksPath scripts/hooks
	@echo "Git hooks installed (using scripts/hooks/)"

test:
	pytest

test-cov:
	pytest --cov=hello --cov-report=term-missing

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/

typecheck:
	mypy src/

pylint:
	pylint src/

changelog:
	./scripts/generate_changelog.sh

docs:
	mkdocs serve

docs-build:
	mkdocs build

bump:
	@read -p "New version: " v; \
	sed -i "s/^version = .*/version = \"$$v\"/" pyproject.toml; \
	sed -i "s/^__version__ = .*/__version__ = \"$$v\"/" src/hello/__init__.py; \
	SKIP_CHANGELOG=1 git add -A && git commit -m "chore: bump to v$$v" && git tag -a "v$$v" -m "v$$v"; \
	echo "Bumped to v$$v — run 'git push && git push --tags' to publish"

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov/ site/
	find . -type d -name __pycache__ -exec rm -rf {} +

all: lint typecheck pylint test
