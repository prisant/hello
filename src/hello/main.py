"""Entry point."""

import sys

from hello.config import Settings
from hello.services import Greeter


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    settings = Settings(name=name)
    greeter = Greeter(settings)
    greeting = greeter.greet()
    print(greeting)


if __name__ == "__main__":
    main()
