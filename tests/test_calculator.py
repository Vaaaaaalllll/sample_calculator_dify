# WARNING: template code, may need edits
"""Unit tests for the Calculator class."""

import pytest
from calculator.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(10, 20) == 30

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(-10, 5) == -5

    def test_add_floats(self):
        """Test addition of floating-point numbers."""
        assert self.calc.add(2.5, 1.5) == 4.0
        assert self.calc.add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert self.calc.subtract(10, 4) == 6
        assert self.calc.subtract(20, 5) == 15

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(10, -5) == 15

    def test_subtract_floats(self):
        """Test subtraction of floating-point numbers."""
        assert self.calc.subtract(5.5, 2.5) == 3.0
        assert self.calc.subtract(0.3, 0.1) == pytest.approx(0.2)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert self.calc.multiply(6, 7) == 42
        assert self.calc.multiply(5, 5) == 25

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert self.calc.multiply(-5, 3) == -15
        assert self.calc.multiply(-4, -4) == 16

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 100) == 0

    def test_multiply_floats(self):
        """Test multiplication of floating-point numbers."""
        assert self.calc.multiply(2.5, 4) == 10.0
        assert self.calc.multiply(0.5, 0.5) == 0.25

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert self.calc.divide(20, 4) == 5.0
        assert self.calc.divide(15, 3) == 5.0

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert self.calc.divide(-20, 4) == -5.0
        assert self.calc.divide(-15, -3) == 5.0

    def test_divide_floats(self):
        """Test division of floating-point numbers."""
        assert self.calc.divide(10, 3) == pytest.approx(3.333333, rel=1e-5)
        assert self.calc.divide(7.5, 2.5) == 3.0

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

    def test_power_positive_numbers(self):
        """Test power operation with positive numbers."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(10, 0) == 1

    def test_power_negative_exponent(self):
        """Test power operation with negative exponent."""
        assert self.calc.power(2, -1) == 0.5
        assert self.calc.power(10, -2) == 0.01

    def test_power_fractional_exponent(self):
        """Test power operation with fractional exponent."""
        assert self.calc.power(4, 0.5) == 2.0
        assert self.calc.power(27, 1/3) == pytest.approx(3.0, rel=1e-5)

    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers."""
        assert self.calc.modulo(10, 3) == 1
        assert self.calc.modulo(17, 5) == 2
        assert self.calc.modulo(20, 4) == 0

    def test_modulo_negative_numbers(self):
        """Test modulo operation with negative numbers."""
        assert self.calc.modulo(-10, 3) == 2
        assert self.calc.modulo(10, -3) == -2

    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate modulo with zero divisor"):
            self.calc.modulo(10, 0)

    def test_last_result_tracking(self):
        """Test that last result is tracked correctly."""
        assert self.calc.get_last_result() is None

        self.calc.add(5, 3)
        assert self.calc.get_last_result() == 8

        self.calc.multiply(4, 5)
        assert self.calc.get_last_result() == 20

        self.calc.clear()
        assert self.calc.get_last_result() is None

    def test_chained_operations(self):
        """Test multiple operations in sequence."""
        result1 = self.calc.add(10, 5)
        assert result1 == 15

        result2 = self.calc.multiply(result1, 2)
        assert result2 == 30

        result3 = self.calc.divide(result2, 3)
        assert result3 == 10.0

        result4 = self.calc.subtract(result3, 5)
        assert result4 == 5.0

    def test_zero_operations(self):
        """Test operations with zero."""
        assert self.calc.add(0, 0) == 0
        assert self.calc.subtract(0, 0) == 0
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.power(0, 5) == 0

    def test_identity_operations(self):
        """Test identity operations."""
        assert self.calc.add(5, 0) == 5
        assert self.calc.subtract(5, 0) == 5
        assert self.calc.multiply(5, 1) == 5
        assert self.calc.divide(5, 1) == 5.0
        assert self.calc.power(5, 1) == 5


class TestCalculatorEdgeCases:
    """Test edge cases and boundary conditions."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        large_num = 10**100
        assert self.calc.add(large_num, large_num) == 2 * large_num
        assert self.calc.multiply(large_num, 2) == 2 * large_num

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        small_num = 10**-100
        result = self.calc.add(small_num, small_num)
        assert result == pytest.approx(2 * small_num, rel=1e-5)

    def test_mixed_int_float_operations(self):
        """Test operations with mixed int and float types."""
        assert self.calc.add(5, 2.5) == 7.5
        assert self.calc.multiply(3, 1.5) == 4.5
        assert self.calc.divide(10, 4) == 2.5

