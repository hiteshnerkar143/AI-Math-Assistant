"""
Scientific Calculator Module

This module provides comprehensive mathematical operations including:
- Basic arithmetic operations
- Advanced mathematical functions
- Trigonometric functions
- Number theory operations
"""

import math
import re
import sympy as sp
from typing import Union, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Calculator:
    """
    A comprehensive scientific calculator with support for various mathematical operations.
    
    Attributes:
        last_result (float): The last calculated result
    """
    
    def __init__(self):
        """Initialize the calculator."""
        self.last_result = 0
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        result = a + b
        self.last_result = result
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Subtract b from a."""
        result = a - b
        self.last_result = result
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Multiply two numbers."""
        result = a * b
        self.last_result = result
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Divide a by b.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Error: Division by zero is not allowed")
        result = a / b
        self.last_result = result
        return result
    
    def modulus(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Calculate a modulo b."""
        if b == 0:
            raise ValueError("Error: Modulus by zero is not allowed")
        result = a % b
        self.last_result = result
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Calculate base raised to the power of exponent."""
        result = base ** exponent
        self.last_result = result
        return result
    
    def square_root(self, x: Union[int, float]) -> float:
        """
        Calculate square root of x.
        
        Raises:
            ValueError: If x is negative
        """
        if x < 0:
            raise ValueError("Error: Cannot calculate square root of a negative number")
        result = math.sqrt(x)
        self.last_result = result
        return result
    
    def cube_root(self, x: Union[int, float]) -> float:
        """Calculate cube root of x."""
        result = x ** (1/3) if x >= 0 else -((-x) ** (1/3))
        self.last_result = result
        return result
    
    def factorial(self, n: int) -> int:
        """
        Calculate factorial of n.
        
        Raises:
            ValueError: If n is negative or not an integer
        """
        if n < 0:
            raise ValueError("Error: Factorial of negative number is not defined")
        if not isinstance(n, int):
            raise ValueError("Error: Factorial only works with integers")
        result = math.factorial(n)
        self.last_result = result
        return result
    
    def percentage(self, part: Union[int, float], whole: Union[int, float]) -> float:
        """Calculate percentage of part relative to whole."""
        if whole == 0:
            raise ValueError("Error: Cannot calculate percentage with zero as whole")
        result = (part / whole) * 100
        self.last_result = result
        return result
    
    def logarithm(self, x: Union[int, float], base: int = 10) -> float:
        """
        Calculate logarithm of x with given base.
        
        Raises:
            ValueError: If x is non-positive or base is invalid
        """
        if x <= 0:
            raise ValueError("Error: Logarithm is only defined for positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Error: Logarithm base must be positive and not equal to 1")
        result = math.log(x, base)
        self.last_result = result
        return result
    
    def natural_log(self, x: Union[int, float]) -> float:
        """Calculate natural logarithm of x."""
        if x <= 0:
            raise ValueError("Error: Natural logarithm is only defined for positive numbers")
        result = math.log(x)
        self.last_result = result
        return result
    
    def lcm(self, a: int, b: int) -> int:
        """Calculate Least Common Multiple of a and b."""
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Error: LCM only works with integers")
        result = abs(a * b) // math.gcd(a, b) if a and b else 0
        self.last_result = result
        return result
    
    def gcd(self, a: int, b: int) -> int:
        """Calculate Greatest Common Divisor of a and b."""
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Error: GCD only works with integers")
        result = math.gcd(a, b)
        self.last_result = result
        return result
    
    def is_prime(self, n: int) -> bool:
        """Check if n is a prime number."""
        if not isinstance(n, int):
            raise ValueError("Error: Prime check only works with integers")
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_even(self, n: int) -> bool:
        """Check if n is even."""
        if not isinstance(n, int):
            raise ValueError("Error: Even/Odd check only works with integers")
        return n % 2 == 0
    
    def is_odd(self, n: int) -> bool:
        """Check if n is odd."""
        if not isinstance(n, int):
            raise ValueError("Error: Even/Odd check only works with integers")
        return n % 2 != 0
    
    def mean(self, numbers: list) -> float:
        """Calculate mean (average) of a list of numbers."""
        if not numbers:
            raise ValueError("Error: Cannot calculate mean of empty list")
        result = sum(numbers) / len(numbers)
        self.last_result = result
        return result
    
    def median(self, numbers: list) -> float:
        """Calculate median of a list of numbers."""
        if not numbers:
            raise ValueError("Error: Cannot calculate median of empty list")
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        if n % 2 == 1:
            result = sorted_numbers[n // 2]
        else:
            result = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
        self.last_result = result
        return result
    
    def mode(self, numbers: list) -> Union[int, float]:
        """Calculate mode (most frequent value) of a list of numbers."""
        if not numbers:
            raise ValueError("Error: Cannot calculate mode of empty list")
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        result = max(frequency, key=frequency.get)
        self.last_result = result
        return result
    
    def standard_deviation(self, numbers: list) -> float:
        """Calculate standard deviation of a list of numbers."""
        if not numbers:
            raise ValueError("Error: Cannot calculate standard deviation of empty list")
        mean_val = sum(numbers) / len(numbers)
        variance = sum((x - mean_val) ** 2 for x in numbers) / len(numbers)
        result = math.sqrt(variance)
        self.last_result = result
        return result
    
    def permutation(self, n: int, r: int) -> int:
        """
        Calculate permutation P(n, r).
        
        Raises:
            ValueError: If n or r are invalid
        """
        if not isinstance(n, int) or not isinstance(r, int):
            raise ValueError("Error: Permutation only works with integers")
        if n < 0 or r < 0 or r > n:
            raise ValueError("Error: Invalid arguments for permutation")
        result = math.factorial(n) // math.factorial(n - r)
        self.last_result = result
        return result
    
    def combination(self, n: int, r: int) -> int:
        """
        Calculate combination C(n, r).
        
        Raises:
            ValueError: If n or r are invalid
        """
        if not isinstance(n, int) or not isinstance(r, int):
            raise ValueError("Error: Combination only works with integers")
        if n < 0 or r < 0 or r > n:
            raise ValueError("Error: Invalid arguments for combination")
        result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        self.last_result = result
        return result
    
    def absolute_value(self, x: Union[int, float]) -> Union[int, float]:
        """Calculate absolute value of x."""
        result = abs(x)
        self.last_result = result
        return result
    
    def trigonometric(self, func: str, angle: float, in_degrees: bool = True) -> float:
        """
        Calculate trigonometric function.
        
        Args:
            func: 'sin', 'cos', or 'tan'
            angle: The angle value
            in_degrees: Whether angle is in degrees (True) or radians (False)
            
        Raises:
            ValueError: If function is not supported
        """
        if in_degrees:
            angle = math.radians(angle)
        
        if func.lower() == 'sin':
            result = math.sin(angle)
        elif func.lower() == 'cos':
            result = math.cos(angle)
        elif func.lower() == 'tan':
            result = math.tan(angle)
        else:
            raise ValueError(f"Error: Unsupported trigonometric function: {func}")
        
        self.last_result = result
        return result
    
    def evaluate_expression(self, expression: str) -> float:
        """
        Evaluate a mathematical expression safely using SymPy.
        
        Args:
            expression: The mathematical expression as a string
            
        Returns:
            The evaluated result
            
        Raises:
            ValueError: If expression is invalid
        """
        try:
            # Replace common notation with SymPy notation
            expression = expression.replace('^', '**')
            expression = expression.replace('sqrt', 'sp.sqrt')
            expression = expression.replace('sin', 'sp.sin')
            expression = expression.replace('cos', 'sp.cos')
            expression = expression.replace('tan', 'sp.tan')
            expression = expression.replace('log', 'sp.log')
            
            # Parse and evaluate using SymPy
            x = sp.Symbol('x')
            expr = sp.sympify(expression)
            result = float(expr)
            self.last_result = result
            return result
        except Exception as e:
            raise ValueError(f"Error: Invalid expression - {str(e)}")


# Singleton instance
_calculator = Calculator()


def get_calculator() -> Calculator:
    """Get the singleton calculator instance."""
    return _calculator
