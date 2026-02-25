"""Shared test fixtures."""

import pytest

from hello.config import Settings
from hello.services import Greeter


@pytest.fixture
def settings() -> Settings:
    """Return test settings."""
    return Settings(name="World")


@pytest.fixture
def greeter(settings: Settings) -> Greeter:
    """Return a fresh Greeter instance."""
    return Greeter(settings)
