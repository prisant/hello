"""Tests for the greeter."""

import pytest

from hello.exceptions import InvalidNameError
from hello.models import Greeting
from hello.services import Greeter
from hello.utils import get_salutation


class TestUtils:
    def test_morning(self):
        assert get_salutation(8) == "Good morning"

    def test_afternoon(self):
        assert get_salutation(14) == "Good afternoon"

    def test_evening(self):
        assert get_salutation(20) == "Good evening"


class TestGreeting:
    def test_str(self):
        g = Greeting("Hello", "Alice")
        assert str(g) == "Hello, Alice!"


class TestGreeter:
    def test_greet_default(self, greeter: Greeter):
        result = greeter.greet()
        assert result.name == "World"

    def test_greet_override(self, greeter: Greeter):
        result = greeter.greet("Alice")
        assert result.name == "Alice"

    def test_greet_strips_whitespace(self, greeter: Greeter):
        result = greeter.greet("  Bob  ")
        assert result.name == "Bob"

    def test_greet_empty_raises(self, greeter: Greeter):
        with pytest.raises(InvalidNameError):
            greeter.greet("   ")
