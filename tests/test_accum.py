"""
This module contains basic unit tests for the accum module.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# Imports - Chapter 5 - Testing Classes 
# --------------------------------------------------------------------------------

import pytest 
from stuff.accum import Accumulator


# --------------------------------------------------------------------------------
# Fixtures - Chpater 6 - Fixtures
# --------------------------------------------------------------------------------

@pytest.fixture   # this is a fixture 
# a fixture should always return a value. 
def accum():
  return Accumulator()


# --------------------------------------------------------------------------------
# Tests
# https://docs.pytest.org/en/stable/fixture.html
# https://realpython.com/introduction-to-python-generators/
# --------------------------------------------------------------------------------

@pytest.mark.accumulator
def test_accumulator_init(accum):
  assert accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum):
  accum.add()
  assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):
  accum.add(3)
  assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
  accum.add()
  accum.add()
  assert accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
  with pytest.raises(AttributeError, match=r"can't set attribute") as e:
    accum.count = 10


""" 

Chapter 7 - Commands and Configs 
--------------------------------------------

Related Links : 
PyTest Usage : https://docs.pytest.org/en/stable/usage.html
PyTest Configuration : https://docs.pytest.org/en/stable/customize.html
PyTest Configurations Options : https://docs.pytest.org/en/stable/reference.html#ini-options-ref

1. To run the pytest file - use command : python -m pytest <test_filename>
2. To get more details about the execution of test file - use command : python -m pytest "--verbose" or "-v"
3. To simply execute all the tests and keep the console clean - use command  : python -m pytest "--quiet" or "-q"
4. By default pytest run all the tests in a file. However, if you want to stop the test after one failure 
- use command  : python -m pytest "--exitfirst" or "-x" . As soon as the first failure happens pytest stops.
5. To stop running the tests after certain number of failures - use command  :
  python -m pytest --maxfail=<give the failure number of the scripts at which you want to stop>
6. Some times we needs to log the test result in a file : use command  : 
  python -m pytest --junit-xml report.xml <give any file name like report.xml)>


Chapter 8 - Filtering Tests 
----------------------------------

Related Important Links : 
1. pyTest - Usage : https://docs.pytest.org/en/stable/usage.html
2. PyTest - Configuration : https://docs.pytest.org/en/stable/customize.html
3. PyTest - Configurations Options : https://docs.pytest.org/en/stable/reference.html#ini-options-ref
4. PyTest - Working with custom markers - https://docs.pytest.org/en/stable/example/markers.html
5. PyTest - Marking test functions with attributes - https://docs.pytest.org/en/stable/mark.html
6. PyTest - testpaths - https://docs.pytest.org/en/stable/reference.html#confval-testpaths

To include only a single test file from the "tests" folder use command :
  python -m pytest tests/test_accum.py

Pytest can also run the individual test case functions - use command : 
  python -m pytest tests/test_accum.py::test_accumulator_add_one

Pytest can also run the individual test case functions containing a specific substring in it 
(we're using "one" substring and it will run the all test having "one" in it) - use command : 
  python -m pytest -k one

Pytest can also run the boolean logic with "and", "or" and "not" keywords in it 
(we're using "one" substring and it will run the all test having "one" in it) - use command : 
  python -m pytest -k "one and not accum"

PyTest provide "markers" to filter the tests :
  Any Test can have any number of markers. PyTest has few standard markers, but we can add our cutomer markers too. 
    @pytest.mark (it's a decorator) then add a suffix with the name of marker 
      example : @pytest.mark.math, @pytest.mark.xml 
        command : python -m pytest -m math or python -m pytest -m xml  

"""