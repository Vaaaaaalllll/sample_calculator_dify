# WARNING: template code, may need edits
"""Command-line interface for the calculator application."""

import argparse
import sys
from typing import List, Optional

from calculator.calculator import Calculator


def parse_arguments(args: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command-line arguments.

    Args:
        args: List of arguments to parse (defaults to sys.argv)

    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(
        description="Simple Calculator - Perform basic arithmetic operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m calculator.cli --operation add --numbers 5 3
  python -m calculator.cli --operation divide --numbers 20 4
  python -m calculator.cli  # Interactive mode
        """,
    )

    parser.add_argument(
        "--operation",
        "-o",
        choices=["add", "subtract", "multiply", "divide", "power", "modulo"],
        help="Arithmetic operation to perform",
    )

    parser.add_argument(
        "--numbers",
        "-n",
        nargs="+",
        type=float,
        help="Numbers to operate on (space-separated)",
    )

    return parser.parse_args(args)


def interactive_mode():
    """Run calculator in interactive mode."""
    calc = Calculator()
    print("\n=== Simple Calculator - Interactive Mode ===")
    print("Available operations: add, subtract, multiply, divide, power, modulo")
    print("Type 'quit' or 'exit' to exit\n")

    while True:
        try:
            operation = input("Enter operation: ").strip().lower()

            if operation in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            if operation not in ["add", "subtract", "multiply", "divide", "power", "modulo"]:
                print(f"Error: Unknown operation '{operation}'")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = perform_operation(calc, operation, num1, num2)
            print(f"\nResult: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


def perform_operation(
    calc: Calculator, operation: str, num1: float, num2: float
) -> float:
    """Perform the specified operation.

    Args:
        calc: Calculator instance
        operation: Operation name
        num1: First operand
        num2: Second operand

    Returns:
        Result of the operation

    Raises:
        ValueError: If operation is invalid or calculation fails
    """
    operations = {
        "add": calc.add,
        "subtract": calc.subtract,
        "multiply": calc.multiply,
        "divide": calc.divide,
        "power": calc.power,
        "modulo": calc.modulo,
    }

    if operation not in operations:
        raise ValueError(f"Invalid operation: {operation}")

    return operations[operation](num1, num2)


def main():
    """Main entry point for the CLI."""
    args = parse_arguments()

    # If no arguments provided, run in interactive mode
    if args.operation is None or args.numbers is None:
        interactive_mode()
        return 0

    # Validate number of operands
    if len(args.numbers) != 2:
        print("Error: Exactly 2 numbers are required for the operation")
        return 1

    calc = Calculator()
    num1, num2 = args.numbers

    try:
        result = perform_operation(calc, args.operation, num1, num2)
        print(f"\nResult: {num1} {args.operation} {num2} = {result}")
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
