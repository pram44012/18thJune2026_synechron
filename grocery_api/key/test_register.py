import json
import random
from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\data_global.json"

@pytest.mark.order(7)
def test_create_new_account(before_each_test: APIRequestContext):
    # read base_uri from json
    with open(filepath, "r") as file:
        data = json.load(file)
    payload ={
   "clientName": "srinivasnarayan",
   "clientEmail": f"valentin{random.randint(1000, 9999)}@example{random.randint(1, 100)}.com"
    }
    response = before_each_test.post(
        "/api-clients", data=payload)
    response_json = response.json()
    assert response.status == 201
    print(json.dumps(response_json, indent=4))
    data["token"] = response_json["accessToken"]
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)