"""Application configuration."""

from dataclasses import dataclass
import os


@dataclass
class Settings:
    name: str = ""

    def __post_init__(self) -> None:
        if not self.name:
            self.name = os.getenv("GREET_NAME", "World")
