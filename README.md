# Automation-Testing-In-Python

## REST API TESTING ## 
- Requests
- Pytest
- tavern

## UI TESTING ##
- selenium

## PERFORMANCE TESTING ##
- locust

## BDD TESTING ##
- behave
- allure-behave

## OTHER PYTHON PACKAGES ##
- pdb (For debugging and breakpoints)
- PyMySQL (For MYSQL)
- setuptools (For packaging)
- logging (For logs)

## VIRTUAL ENVIRONMENT ##
- virtualenv
- conda
- https://towardsdatascience.com/micropipenv-best-practices-for-installing-python-dependencies-72203925eb0d

## SDET PYTHON ##
- https://docs.google.com/document/d/1uIaG2wAupgPkpOtBpOsRK5T-NZvOEzhIIUg82hdjwvg/edit#

## Parallel Test Execution with Pytest ##
- Using pytest plugin. pytest-xdist lets you scale up by increasing the test thread count and scale out by distributing test execution to remote machines
  - $ pipenv run python -m pytest -n 4

- To run tests in parallel, we recommend using Nose and MultiProcessing, which makes it very easy to run multiple Python tests simultaneously:
  - pip install nose==0.11
  - pip install multiprocessing
  - nosetests --processes=<number_of_processes>

## Python BDD Frameworks ##
- https://blog.testproject.io/2019/05/16/python-testing-framework-pros-cons/


## PYTEST VS TESTNG ##
https://knapsackpro.com/testing_frameworks/difference_between/pytest/vs/testng

## TOP 5 PYTHON FRAMEWORKS ##
https://www.lambdatest.com/blog/top-5-python-frameworks-for-test-automation-in-2019/

1. ROBOT
2. PYTEST
3. UNITTEST OR PYUNIT
4. BEHAVE
5. LETTUCE
