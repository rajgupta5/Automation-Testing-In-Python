import pytest

dewey_host = None
linda_host = None
facsimile_host = None

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev"
    )

@pytest.fixture(scope='class')
def setUp(request):

    global dewey_host
    global linda_host

    env = request.config.getoption("env")

    if env == 'dev':
        dewey_host = "http://dewey.dev.aws.hotwire.com"
        linda_host = "http://dev.rtpclinda.aws.hotwire.com"

    request.cls.dewey_host = dewey_host
    request.cls.linda_host = linda_host
