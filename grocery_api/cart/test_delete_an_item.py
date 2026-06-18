import json
from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\data_global.json"

@pytest.mark.order(6)
@pytest.mark.dependency(scope="session", depends=["add_item"])

def test_delete_an_item_from_cart(before_each_test: APIRequestContext):
    # read base_uri from json
    with open(filepath, "r") as file:
        data = json.load(file)
    
    # Delete the item from the cart
    response = before_each_test.delete(
        f"/carts/{data['cart_id']}/items/{data['item_id']}"
    )
    
    assert response.status == 204
    
    print(response)
    # Print the response JSON
    # response_json = response.json()
    # print(json.dumps(response_json, indent=4))