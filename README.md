# WARNING: template code, may need edits
# Sample Calculator - Dify

A simple, well-structured Python calculator application with support for basic arithmetic operations.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Modular architecture for easy extension
- Comprehensive test coverage
- Command-line interface
- Error handling for edge cases (division by zero, invalid inputs)

## Project Structure

```
sample_calculator_dify/
├── src/
│   └── calculator/
│       ├── __init__.py
│       ├── calculator.py       # Core calculator logic
│       └── cli.py             # Command-line interface
├── tests/
│   ├── __init__.py
│   └── test_calculator.py     # Unit tests
├── docs/
│   └── usage.md              # Detailed usage guide
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── setup.py
└── README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sample_calculator_dify.git
cd sample_calculator_dify
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install the package:
```bash
pip install -e .
```

4. For development (includes testing tools):
```bash
pip install -e ".[dev]"
```

## Usage

### As a Command-Line Tool

```bash
# Interactive mode
python -m calculator.cli

# Direct calculation
python -m calculator.cli --operation add --numbers 5 3
python -m calculator.cli --operation subtract --numbers 10 4
python -m calculator.cli --operation multiply --numbers 6 7
python -m calculator.cli --operation divide --numbers 20 4
```

### As a Python Module

```python
from calculator.calculator import Calculator

calc = Calculator()

result = calc.add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

result = calc.divide(10, 2)
print(f"10 / 2 = {result}")  # Output: 10 / 2 = 5.0
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=calculator --cov-report=html

# Run specific test file
pytest tests/test_calculator.py
```

## Development

### Adding New Operations

1. Add the method to `src/calculator/calculator.py`
2. Add corresponding tests to `tests/test_calculator.py`
3. Update the CLI in `src/calculator/cli.py` if needed

### Code Style

This project follows PEP 8 guidelines. Format your code before committing:

```bash
black src/ tests/
flake8 src/ tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Author

Your Name

## Changelog

### v1.0.0 (2024)
- Initial release
- Basic arithmetic operations
- CLI interface
- Comprehensive test suite
