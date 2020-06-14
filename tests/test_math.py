"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest


# --------------------------------------------------------------------------------
# A most basic test function
# --------------------------------------------------------------------------------

def test_one_plus_one():
  assert 1 + 1 == 2


# --------------------------------------------------------------------------------
# A test function to show assertion introspection
# --------------------------------------------------------------------------------

def test_one_plus_two():
  a = 1
  b = 2
  c = 3
  assert a + b == c


# --------------------------------------------------------------------------------
# A test function that verifies an exception
# --------------------------------------------------------------------------------

def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError) as e:
    num = 1 / 0
  
  assert 'division by zero' in str(e.value)


# --------------------------------------------------------------------------------
# A parametrized test function
# --------------------------------------------------------------------------------

products = [
  (2, 3, 6),            # postive integers
  (1, 99, 99),          # identity
  (0, 99, 0),           # zero
  (3, -4, -12),         # positive by negative
  (-5, -5, 25),         # negative by negative
  (2.5, 6.7, 16.75)     # floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
  assert a * b == product
