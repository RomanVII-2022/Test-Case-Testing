from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup():
    driver=webdriver.Chrome(service=Service("C:\\Program Files (x86)\\chromedriver.exe"))
    return driver


###### Pytest HTML Report ######
def pytest_configure(config):
    config._metadata['Project Name'] = 'E-commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'User'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
