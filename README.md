# python-utils-16

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

python-utils-16 provides a set of practical utilities for common development tasks in Python. It focuses on reliable error handling, file operations, and configuration management without unnecessary dependencies.

## Features
- `@retry` decorator with exponential backoff for network and I/O operations
- `safe_write` function that creates timestamped backups before overwriting files
- Multi-format configuration loader supporting JSON, YAML, and environment variable overrides
- Utility functions for human-readable byte sizes and duration formatting

## Installation

```bash
pip install python-utils-16
```

To install the development version:

```bash
git clone https://github.com/Developer/python-utils-16.git
cd python-utils-16
pip install -e .
```

## Usage

```python
from python_utils_16 import retry, safe_write, load_config, format_size

@retry(max_attempts=3, backoff=2)
def fetch_data():
    # unreliable operation
    pass

safe_write("output.txt", "content here")
config = load_config("config.yaml")
print(format_size(1536000))
```

## License

MIT License