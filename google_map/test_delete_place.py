import json
from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\googledata.json"

@pytest.mark.order(4)
@pytest.mark.dependency(name="delete_place", depends=["update_place"], scope="session")
def test_delete_place(before_each_test: APIRequestContext):
    # Load config
    with open(filepath, "r") as f:
        cfg = json.load(f)

    assert "place_id" in cfg, "place_id must be stored in googledata.json by add_place"
    place_id = cfg["place_id"]

    delete_payload = {"place_id": place_id}
    delete_resp = before_each_test.delete(
        "/maps/api/place/delete/json",
        params={"key": cfg["key"]},
        headers={"Content-Type": "application/json"},
        data=json.dumps(delete_payload)
    )

    assert delete_resp.status == 200
    delete_json = delete_resp.json()
    assert delete_json.get("status") == "OK", f"Expected OK status, got {delete_json}"

    get_resp = before_each_test.get(
        "/maps/api/place/get/json",
        params={"key": cfg["key"], "place_id": place_id}
    )
    assert get_resp.status in (400, 404)