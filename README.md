# python-utils-16

A collection of lightweight, high-performance utility functions designed to streamline repetitive Python development tasks. This library focuses on simplifying common operations in file handling, data formatting, and process synchronization.

## Features

*   **Robust File Operations**: Simplified wrappers for recursive directory traversal and atomic file writes.
*   **Time-Series Helpers**: Built-in decorators for benchmarking function execution and caching recurring calculations.
*   **String Manipulation**: Advanced slugify and sanitization utilities for cleaning user-provided inputs.
*   **Concurrency Support**: Thread-safe logging and queue management tools to improve multi-threaded application reliability.

## Installation

Install the package via pip:

```bash
pip install python-utils-16
```

If you are working in a development environment, you can install the dependencies directly:

```bash
pip install -r requirements.txt
```

## Basic Usage

Import the required utilities directly from the package to enhance your workflow:

```python
from pyutils16.files import safe_write
from pyutils16.decorators import time_execution

@time_execution
def process_data(data):
    # Process your data here
    safe_write("output.txt", str(data))

process_data({"key": "value"})
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.