"""Utility functions."""

from datetime import datetime


def get_salutation(hour: int | None = None) -> str:
    """Return a greeting based on time of day."""
    if hour is None:
        hour = datetime.now().hour

    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"
