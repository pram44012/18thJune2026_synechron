import json
from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\googledata.json"

@pytest.mark.order(3)
@pytest.mark.dependency(name="update_place", depends=["get_place"], scope="session")
def test_update_place(before_each_test: APIRequestContext):
    # Load config
    with open(filepath, "r") as f:
        cfg = json.load(f)

    assert "place_id" in cfg, "place_id must be stored in googledata.json by add_place"
    place_id = cfg["place_id"]

    new_address = "Jalahalli,East"
    update_payload = {
        "place_id": place_id,
        "address": new_address,
        "key": cfg["key"]
    }

    update_resp = before_each_test.put(
        "/maps/api/place/update/json",
        params={"key": cfg["key"]},
        headers={"Content-Type": "application/json"},
        data=json.dumps(update_payload)
    )

    assert update_resp.status == 200
    update_json = update_resp.json()
    assert update_json.get("msg") is not None or update_json.get("status") == "OK"

    get_resp = before_each_test.get(
        "/maps/api/place/get/json",
        params={"key": cfg["key"], "place_id": place_id}
    )
    assert get_resp.status == 200
    get_json = get_resp.json()
    assert get_json.get("address") == new_address, f"Expected updated address {new_address}, got {get_json.get('address')}"