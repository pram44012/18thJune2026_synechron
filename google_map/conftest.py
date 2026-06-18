import json
from playwright.sync_api import Playwright
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\googledata.json"

@pytest.fixture(scope="function")
def before_each_test(playwright: Playwright):
    # Load the global data from the JSON file
    with open(filepath, "r") as file:
        data = json.load(file)
    request = playwright.request.new_context(base_url=data["base_url"])
    yield request
    request.dispose()