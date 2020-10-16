# PYTEST

## ABOUT PYTEST ##
- Pytest unit testing framework to provide us with 
  - a test runner, 
  - an assertion library and  
  - some basic reporting functionality
- Pytest is the TDD 'all in one' testing framework for Python
- Pytest can test any part of the stack including front-end components
- Pytest is powerful enough to test database and server components and functionality
- Pytest has a powerful yet simple fixture model that is unmatched in any other testing framework.
- Pytest's powerful fixture model allows grouping of fixtures
- Pytest has a hook function called pytest_generate_tests hook which is called when collecting a test function and one can use it to generate data
- By either using unittest.mock or using pytest-mock a thin wrapper that provides mock functionality for pytest
- Tests can be grouped with pytest by use of markers which are applied to various tests and one can run tests with the marker applied

## PYTEST VS TESTNG ##
https://knapsackpro.com/testing_frameworks/difference_between/pytest/vs/testng


## Running with pytest rules ##
- Any pytest file should start with test_ or end with _test
- pytest method names should start with test
- Any code should be wrapped in method only
- Method name should have sense
- -k stands for method names execution, -s logs in output  -v stands for more info metadata
- you can run specific file with py.test <filename>
- you can mark (tag) tests @pytest.mark.smoke and then run with -m
- you can skip tests with @pytest.mark.skip
- @pytest.mark.xfail
- fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixt
- fixture and make it available to all test cases (fixture name into parameters of method)
- @pytest.fixture(scope="class")
- the scope for which this fixture is shared, one of function, default, class, module, package, session
- @pytest.mark.usefixtures("setup")
- data driven and parameterization can be done with return statements in tuple format
- when you define fixture scope to class only, it will run once before class is initiated and at the end
- data driven tests using pytest and requests
  - @pytest.mark.parametrize("userid, expected_name", read_data_from_csv())
  

## Running all test from terminal ##
- py.test - this command will collect all tests as per above rules
- py.test -v (v stands for verbose with more information on test execution)
- py.test -s (for printing all console logs in the output)
- py.test -sv <filename>
- If two methods with same name in the test file, then pytest overrides the first method and only executes the second method
- Running selected test files using pytest
   - py.test test_demo2.py -sv
- Running selected test methods based on matching keywords
   - py.test -k CreditCard -sv (k is for matching regular expression)
- pytest --help
- py.test -k -> keyword
- py.test -v - > verbose
- py.test -m -> marker tests
- Pretty print command
  - pytest -sv test_post_headers_body_json_pprint.py::test_post_headers_body_json
  
  
## Report Generation ##
- Command to generate the HTML report [https://pypi.org/project/pytest-html/]
  - pip install pytest-html
  - pytest -sv --html report.html
  - pytest --html=report.html
  - py.test -sv test_demo1.py --html=report.html

- Pytest with allure report
  - pip install allure-pytest
  - py.test --alluredir=%allure_result_folder% ./tests
  - allure serve %allure_result_folder%



## Parallel Test Execution ##
- Using pytest plugin. pytest-xdist lets you scale up by increasing the test thread count and scale out by distributing test execution to remote machines
  - pip install pytest-xdist
  - py.test -m pytest -n 4

- To run tests in parallel, we recommend using Nose and MultiProcessing, which makes it very easy to run multiple Python tests simultaneously:
  - pip install nose==0.11
  - pip install multiprocessing
  - nosetests --processes=<number_of_processes>
