.PHONY: install install-hooks test lint format typecheck changelog clean all

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

changelog:
	./scripts/generate_changelog.sh

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +

all: lint typecheck test
