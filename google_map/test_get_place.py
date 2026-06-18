import json
from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\googledata.json"

@pytest.mark.order(2)
@pytest.mark.dependency(name="get_place", depends=["add_place"], scope="session")
def test_get_place(before_each_test: APIRequestContext):
    # Load config
    with open(filepath, "r") as f:
        cfg = json.load(f)

    assert "place_id" in cfg, "place_id must be stored in googledata.json by add_place"
    place_id = cfg["place_id"]

    get_resp = before_each_test.get(
        "/maps/api/place/get/json",
        params={"key": cfg["key"], "place_id": place_id}
    )
    assert get_resp.status == 200
    get_json = get_resp.json()
    print(json.dumps(get_json, indent=4))
    assert get_json.get("address") == "Bagalur,Yelahanka"