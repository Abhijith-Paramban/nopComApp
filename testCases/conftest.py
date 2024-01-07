from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester Name'] = 'Abhijith'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(config, metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




