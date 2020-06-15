"""
This module contains basic unit tests for the accum module.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
from stuff.accum import Accumulator


# --------------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------------

@pytest.fixture
def accum():
  return Accumulator()


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_accumulator_init(accum):
  assert accum.count == 0


def test_accumulator_add_one(accum):
  accum.add()
  assert accum.count == 1


def test_accumulator_add_three(accum):
  accum.add(3)
  assert accum.count == 3


def test_accumulator_add_twice(accum):
  accum.add()
  accum.add()
  assert accum.count == 2


def test_accumulator_cannot_set_count_directly(accum):
  with pytest.raises(AttributeError, match=r"can't set attribute") as e:
    accum.count = 10
