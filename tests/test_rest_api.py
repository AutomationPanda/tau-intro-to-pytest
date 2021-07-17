"""
This module contains basic REST API tests using requests.
Their purpose is to show how to use the pytest framework by example.


Chapter 9 - Feature Tests
-------------------------------
Related Important Links : 
1. Requests: HTTP for Humans : https://docs.python-requests.org/en/master/
2. DuckDuckGo API : https://duckduckgo.com/api
3. Tavern API Testing : https://tavern.readthedocs.io/en/latest/

There is a diference between testing "code" and testing "features".
Testing code directly is very important for several reasons unit tests or white box tests are typically small simple to write. Unit tests catch 
low level problmes at the source where they're easy to identify and fix and unit tests run very quickly meaning we can write several unit tests 
to maximize the coverage. 
However, pytest can also handle what we call feature tests or sometimes called Black Box Tests or integration tests or end-to-end tests or 
system tests or a whole bunch other similar names. Instead of making the direct calls to the prouct code they interact with a live instance of 
the product. For example, calling a rest api and loading a web page in a browser would both be example of feature tests.
Feature tests are important because they test the product in ways that would actually be used, for instance all the individual methods 
in the code may work as intended 

Chapter 10 - Extending PyTest with Plugins 
---------------------------------------------------
Related Important Links :
1. How to install and use plugins - https://docs.pytest.org/en/latest/how-to/plugins.html
2. Writing plugins - https://docs.pytest.org/en/latest/how-to/writing_plugins.html
3. pytest-bdd - https://github.com/pytest-dev/pytest-bdd
4. pytest-html - https://github.com/pytest-dev/pytest-html
5. pytest-cov’s documentation - https://pytest-cov.readthedocs.io/en/latest/index.html
6. Coverage.py - https://coverage.readthedocs.io/en/coverage-5.1/
7. xdist - https://docs.pytest.org/en/3.0.1/xdist.html
8. GUIDE TO PARALLEL TESTING - https://automationpanda.com/2018/01/21/to-infinity-and-beyond-a-guide-to-parallel-testing/

To run this file only : use command from directory - tau-intro-to-pytest : 
python -m pytest -m rest_api(marker_name)

Run the below Report Commands from the path : C:\Users\mayan\Documents\GitHub\tau-intro-to-pytest>
1. python -m pytest -m rest_api
2. python -m pytest --html=report.html - To generate the HTML report (HTML Plugin)
3. python -m pytest --cov=stuff (Coverage Plugin)
4. python -m pytest --cov=stuff --cov-report html - To generate the Coverage's HTML report (Coverage Plugin)
5. - To run the test in multiple parallel threads (xdist plugin)


"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import pytest
import requests


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():

  # Arrange
  url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

  # Act
  response = requests.get(url)
  body = response.json()

  # Assert
  assert response.status_code == 200
  assert 'Python' in body['AbstractText']
