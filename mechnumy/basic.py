"""

This module provides fundamental mathematical operations and utilities
that serve as building blocks for more advanced numerical methods.

Key Features:
- Common mathematical functions (e.g., addition, subtraction, etc.).
- Helper utilities for array manipulations and scalar operations.
- Input validation and general-purpose numerical tools.

Example:
    from mechnumy.basic import add
    result = add(2, 3)
"""


def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def square(number, power):
    return number ** power