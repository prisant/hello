"""Entry point."""

import argparse

from hello import __version__
from hello.config import Settings
from hello.services import Greeter


def main(argv: list[str] | None = None) -> None:
    """Run the application."""
    parser = argparse.ArgumentParser(
        prog="hello",
        description="A tiny greeter app",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="",
        help="Name to greet (default: World, or GREET_NAME env var)",
    )

    parsed = parser.parse_args(argv)
    settings = Settings(name=parsed.name)
    greeter = Greeter(settings)
    greeting = greeter.greet()
    print(greeting)


if __name__ == "__main__":
    main()
