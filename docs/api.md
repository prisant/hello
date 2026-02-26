# API Reference

## hello.config

### `Settings`

```python
@dataclass
class Settings:
    name: str = ""
```

Application configuration. Reads the greeting name from:

1. The `name` parameter passed directly
2. The `GREET_NAME` environment variable
3. Falls back to `"World"`

**Example:**

```python
from hello.config import Settings

# Explicit name
s = Settings(name="Alice")

# From environment (GREET_NAME=Bob)
s = Settings()
print(s.name)  # "Bob"

# Default fallback
s = Settings()
print(s.name)  # "World"
```

---

## hello.models

### `Greeting`

```python
@dataclass
class Greeting:
    salutation: str
    name: str
```

Holds a greeting's components. The string representation combines them:

```python
from hello.models import Greeting

g = Greeting(salutation="Good morning", name="Alice")
print(g)           # "Good morning, Alice!"
print(g.salutation) # "Good morning"
print(g.name)       # "Alice"
```

---

## hello.services

### `Greeter`

```python
class Greeter:
    def __init__(self, settings: Settings) -> None
    def greet(self, name: str | None = None) -> Greeting
```

Builds time-aware greetings.

**`__init__(settings)`** — Takes a `Settings` instance for default configuration.

**`greet(name=None)`** — Returns a `Greeting`. Uses the provided `name`, or
falls back to `settings.name`. Strips whitespace from the name.

**Raises:** `InvalidNameError` if the name is empty or whitespace-only.

**Example:**

```python
from hello.config import Settings
from hello.services import Greeter

greeter = Greeter(Settings(name="World"))
greeter.greet()          # Greeting(salutation="Good evening", name="World")
greeter.greet("Alice")   # Greeting(salutation="Good evening", name="Alice")
greeter.greet("   ")     # raises InvalidNameError
```

---

## hello.utils

### `get_salutation(hour=None)`

```python
def get_salutation(hour: int | None = None) -> str
```

Returns a greeting based on time of day:

| Hour range | Return value         |
|------------|----------------------|
| 0–11       | `"Good morning"`     |
| 12–16      | `"Good afternoon"`   |
| 17–23      | `"Good evening"`     |

If `hour` is `None`, uses the current system time.

**Example:**

```python
from hello.utils import get_salutation

get_salutation(8)    # "Good morning"
get_salutation(14)   # "Good afternoon"
get_salutation(20)   # "Good evening"
get_salutation()     # depends on current time
```

---

## hello.exceptions

### `HelloError`

Base exception for all application errors.

### `InvalidNameError`

Raised when a name is empty or contains only whitespace.
Inherits from `HelloError`.

```python
from hello.exceptions import InvalidNameError, HelloError

try:
    greeter.greet("   ")
except InvalidNameError as e:
    print(e)  # "Name cannot be empty"
except HelloError:
    print("Some other application error")
```
