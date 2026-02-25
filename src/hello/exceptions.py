"""Custom exceptions."""


class HelloError(Exception):
    """Base exception."""


class InvalidNameError(HelloError):
    """Raised when the name is invalid."""
