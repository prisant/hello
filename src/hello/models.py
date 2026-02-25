"""Data models."""

from dataclasses import dataclass


@dataclass
class Greeting:
    salutation: str
    name: str

    def __str__(self) -> str:
        return f"{self.salutation}, {self.name}!"
