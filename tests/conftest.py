import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    # init browser
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  # implicitly wait
    driver.maximize_window()

    yield driver

    # quite driver after test
    driver.quit()