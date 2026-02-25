# WARNING: template code, may need edits
"""Core calculator module with basic arithmetic operations."""

from typing import Union


class Calculator:
    """A simple calculator class supporting basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator."""
        self.last_result = None

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Examples:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8
            >>> calc.add(2.5, 1.5)
            4.0
        """
        result = a + b
        self.last_result = result
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract second number from first.

        Args:
            a: Number to subtract from
            b: Number to subtract

        Returns:
            Difference of a and b

        Examples:
            >>> calc = Calculator()
            >>> calc.subtract(10, 4)
            6
            >>> calc.subtract(5.5, 2.5)
            3.0
        """
        result = a - b
        self.last_result = result
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Examples:
            >>> calc = Calculator()
            >>> calc.multiply(6, 7)
            42
            >>> calc.multiply(2.5, 4)
            10.0
        """
        result = a * b
        self.last_result = result
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide first number by second.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            ValueError: If b is zero

        Examples:
            >>> calc = Calculator()
            >>> calc.divide(20, 4)
            5.0
            >>> calc.divide(10, 3)
            3.3333333333333335
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.last_result = result
        return result

    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent.

        Args:
            base: Base number
            exponent: Power to raise to

        Returns:
            Base raised to exponent

        Examples:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8
            >>> calc.power(5, 2)
            25
        """
        result = base ** exponent
        self.last_result = result
        return result

    def modulo(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Calculate remainder of division.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            Remainder of a divided by b

        Raises:
            ValueError: If b is zero

        Examples:
            >>> calc = Calculator()
            >>> calc.modulo(10, 3)
            1
            >>> calc.modulo(17, 5)
            2
        """
        if b == 0:
            raise ValueError("Cannot calculate modulo with zero divisor")
        result = a % b
        self.last_result = result
        return result

    def get_last_result(self) -> Union[int, float, None]:
        """Get the result of the last operation.

        Returns:
            Last calculated result or None if no operations performed
        """
        return self.last_result

    def clear(self) -> None:
        """Clear the last result."""
        self.last_result = None
