import os

import pytest
import json
import selenium.webdriver


@pytest.fixture(scope="session")
def config():
    print(os.getcwd())
    with open("config.json") as config_file:
        config = json.load(config_file)

    assert config["browser"] in ["Chrome", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0
    return config


@pytest.fixture
def browser(config):
    # Initialize the ChromeDriver instance
    if config["browser"] == "Chrome":
        driver = selenium.webdriver.Chrome()
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        driver = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser {config["browser"]} is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    driver.implicitly_wait(config["implicit_wait"])

    # Return the webdriver instance for the set up
    yield driver

    # Quit the WebDriver instance for the cleanup
    driver.quit()
