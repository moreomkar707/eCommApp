import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager




@pytest.fixture()
def setup(browser):

    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# def pytest_configure(config):
#     config._matadata['Project Name'] = 'eComm'
#     config._matadata['Module Name'] = 'Customer'
#     config._matadata['Tester'] = 'QA Omkar More'


# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config.metadata["Project Name"] = "nop Commerce"
#     config.metadata["Module Name"] = "Customers"
#     config.metadata["Tester"] = "QA omkar"
#
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)