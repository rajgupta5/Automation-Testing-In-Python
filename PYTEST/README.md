# PYTEST

## PYTEST VS TESTNG ##
https://knapsackpro.com/testing_frameworks/difference_between/pytest/vs/testng

## Parallel Test Execution with Pytest ##
- Using pytest plugin. pytest-xdist lets you scale up by increasing the test thread count and scale out by distributing test execution to remote machines
  - $ pipenv run python -m pytest -n 4

- To run tests in parallel, we recommend using Nose and MultiProcessing, which makes it very easy to run multiple Python tests simultaneously:
  - pip install nose==0.11
  - pip install multiprocessing
  - nosetests --processes=<number_of_processes>
