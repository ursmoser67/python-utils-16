# python-utils-16

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`python-utils-16` is a lightweight suite of high-performance Python utilities designed to streamline daily tasks like data transformation, file manipulation, and logging. It eliminates boilerplate code across modern workflows by providing clean, type-hinted helper functions optimized for Python 3.10+.

## Features

- **Safe File Operations:** Thread-safe JSON and YAML readers/writers equipped with automatic atomic backups.
- **Deep Dict Manipulation:** Utilities for safe nested key retrieval, recursive dictionary merging, and key sanitization.
- **Structured Logging:** Pre-configured JSON and colored console loggers with built-in contextual metadata tracking.
- **Resilience Decorators:** Robust function execution wrappers with configurable exponential backoff and retry logic.

## Installation

Install the package directly from PyPI using `pip`:

```bash
pip install python-utils-16
```

Or install from the source repository:

```bash
git clone https://github.com/Developer/python-utils-16.git
cd python-utils-16
pip install .
```

## Quick Start

```python
from python_utils_16 import DeepDict, retry, safe_load_json

# Safely load JSON with fallback defaults
config_data = safe_load_json("config.json", default={"database": {"port": 5432}})

# Query nested dictionaries without raising KeyError
config = DeepDict(config_data)
port = config.get_nested("database.port", default=5432)

# Automatically retry unreliable operations with exponential backoff
@retry(tries=3, delay=1.0, backoff=2.0)
def connect_to_service():
    print(f"Connecting to database on port {port}...")

connect_to_service()
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.