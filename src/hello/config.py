"""Application configuration."""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    name: str = ""

    def __post_init__(self) -> None:
        if not self.name:
            self.name = os.getenv("GREET_NAME", "World")
