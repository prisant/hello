"""Business logic."""

from hello.config import Settings
from hello.exceptions import InvalidNameError
from hello.models import Greeting
from hello.utils import get_salutation


class Greeter:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def greet(self, name: str | None = None) -> Greeting:
        """Build a greeting for the given name (or the configured default)."""
        name = name or self.settings.name

        if not name.strip():
            raise InvalidNameError("Name cannot be empty")

        return Greeting(
            salutation=get_salutation(),
            name=name.strip(),
        )
