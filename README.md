# python-utils-16

A collection of lightweight, high-performance Python utilities designed to streamline common development tasks. This library simplifies boilerplate-heavy operations like file I/O management, data transformation, and environment configuration.

## Features

*   **FileStream API**: An intuitive context-manager interface for handling multi-format file reading and writing with built-in error serialization.
*   **Dict-Mapper**: High-speed schema-based data transformation tool for normalizing deeply nested JSON structures into flat dictionaries.
*   **Task-Scheduler**: A decorator-based utility for wrapping long-running functions with automatic retry logic and exponential backoff.
*   **Env-Vault**: A secure, type-safe loader for environment variables that prevents runtime failures through strict schema validation.

## Installation

Install the library directly from PyPI:

```bash
pip install python-utils-16
```

If you prefer to install from source:

```bash
git clone https://github.com/Developer/python-utils-16.git
cd python-utils-16
pip install -e .
```

## Usage

Here is a quick example of using the `Dict-Mapper` to sanitize incoming data:

```python
from utils16 import DictMapper

schema = {"user_id": "id", "full_name": "name"}
data = {"id": 101, "name": "Alice Doe", "ignored_field": "hidden"}

mapper = DictMapper(schema)
clean_data = mapper.transform(data)

print(clean_data)
# Output: {'user_id': 101, 'full_name': 'Alice Doe'}
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.