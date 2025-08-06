import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime


@pytest.fixture
def setup(browser):
    if browser=="edge":
        driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser--")
        return driver

    elif browser=="firefox":
        driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("Launching Firefox browser--")
        return driver
    else:
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching Chrome browser--")
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")



@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name']="nopCommercial"
    config._metadata['Module Name']="AccountRegistration"

def pytest_metadata(metadata):
    metadata.pop("Python version",None)
    metadata.pop("Plugins",None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\report.html\\" +datetime.now().strftime("%d-%m-%y %H-%M-%S")+".html"

