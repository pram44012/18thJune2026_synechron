import json
from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\googledata.json"

@pytest.mark.order(1)
@pytest.mark.dependency(name="add_place", scope="session")
def test_add_place(before_each_test: APIRequestContext):
    # Load config
    with open(filepath, "r") as f:
        cfg = json.load(f)

    payload = {
      "location": {"lat": -38.383494, "lng": 33.427362},
      "accuracy": 50,
      "name": "BajajFinSer",
      "phone_number": "(+91) 983 893 3937",
      "address": "Bagalur,Yelahanka",
      "types": ["shoe park", "shop"],
      "website": "http://google.com",
      "language": cfg.get("language", "Eng-IN")
    }

    # Use explicit full URL to ensure correct host is used
    url = f"{cfg['base_url']}/maps/api/place/add/json"
    response = before_each_test.post(
        url,
        params={"key": cfg["key"]},
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    assert response.status == 200
    resp_json = response.json()
    print(json.dumps(resp_json, indent=4))
    assert resp_json.get("status") == "OK", "Expected status OK"
    assert "place_id" in resp_json, "Add place response must contain place_id"

    cfg["place_id"] = resp_json["place_id"]
    with open(filepath, "w") as f:
        json.dump(cfg, f, indent=2)