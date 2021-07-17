"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest


# --------------------------------------------------------------------------------
# A most basic test function - Chapter 1 - The First Test Case
# --------------------------------------------------------------------------------

@pytest.mark.math
def test_one_plus_one():
  assert 1 + 1 == 2


# --------------------------------------------------------------------------------
# A test function to show assertion introspection - Chapter 2 -  Failing Test Case
# --------------------------------------------------------------------------------

@pytest.mark.math
def test_one_plus_two():
  a = 1
  b = 2
  c = 3
  assert a + b == c


# --------------------------------------------------------------------------------
# A test function that verifies an exception - Chapter 3 - A Test Case with an Exception
# --------------------------------------------------------------------------------

@pytest.mark.math
def test_divide_by_zero():
  # In Python, "with" is a special statement for automatically handling extra "enter" and "exit" logic for a caller.
  # It's most commonly used for File Input and Output. The "enter" logic opens the file body reads or writes 
  # and the "exit" logic closes the file. For "pytest.raises" the "enter" logic makes the code to catch any exceptions 
  # and "exit" logic asserts if the desired exception type was actually raised.
  with pytest.raises(ZeroDivisionError) as e:
    num = 1 / 0
  
  assert 'division by zero' in str(e.value)


# --------------------------------------------------------------------------------
# A parametrized test function - Chapter 4 - Parameterized Test Case 
# DRY Principle :- Don't Repeat Yourself! 
# https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
# --------------------------------------------------------------------------------

products = [            # Below comments are the Multiplication Test Ideas
  (2, 3, 6),            # postive integers
  (1, 99, 99),          # identity
  (0, 99, 0),           # zero
  (3, -4, -12),         # positive by negative
  (-5, -5, 25),         # negative by negative
  (2.5, 6.7, 16.75)     # floats
]


@pytest.mark.math
# https://docs.pytest.org/en/6.2.x/parametrize.html
# @pytest.mark.parametrize - is a decorator for the - test_multiplication() function.
# In Python, a decorator is a special function that wraps around another functon.
# We need to pass 2 functions into the decorator - the first argument is string containing the comma seperated list of variable names. 
# These parameters must match the parameter (here in this exmaple - a, b, product) names for the Test Case function.

# Pytest Parameters make it easy to do the data driven testing in which the same Test cases cranck through multiple inputs. This Test case 
# is just a basic example that what you can do with paramaters. We can use any python object for parameter values not just integers. 
# Since parameters are passed into the test cases as a list, we could also store the data into the external files like csv's or excel 
# spreadhsheets and read them when the test runs. 
@pytest.mark.parametrize('a, b, product', products)
# Inner function - is the Test Case. 
def test_multiplication(a, b, product):
  assert a * b == product