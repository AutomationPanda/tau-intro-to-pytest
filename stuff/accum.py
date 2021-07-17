"""
This module contains a basic accumulator class.
Its purpose is to show how to use the pytest framework for testing classes.
"""


# --------------------------------------------------------------------------------
# Class: Accumulator

# Let's write some Unit Tests for a new Class. Unit Tests are small tests that directly cover functions 
# and class methods, more genreally they cover units of work. 
# https://docs.python.org/3/tutorial/classes.html
# 
# To write unit tests, we first need to create a new python package and module. We created this directory 
# named "stuff". Inside this directory, we created a file name "__init__.py". In python any directory/folder 
# having the "__init__.py" file is treated as a package and anymodules inside that package may be imported 
# by the other modules.
# To our surprise, we don't have any "__init__.py" file in the "tests" directory, because python doesn't 
# require the 'tests' files to be a package. Infact, making the tests file a package may have the unintended
# consequences.  
# --------------------------------------------------------------------------------

class Accumulator:

  def __init__(self):
    self._count = 0     # _count : is a private variable.

  @property             # @property is a decorator.
  # In Python, properties control how caller can get and set values. With this property, a caller can get the
  # count value, but can't set the value directly with an assignment statement. 
  def count(self):
    return self._count
  
  def add(self, more=1):
    self._count += more
