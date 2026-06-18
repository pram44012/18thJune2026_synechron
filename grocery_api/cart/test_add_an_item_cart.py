import json

from playwright.async_api import APIRequestContext, Playwright
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\data_global.json"

@pytest.mark.order(5)
@pytest.mark.dependency(name="add_item", depends=["create_cart"], scope="session")
@pytest.mark.parametrize("pid",[1225,1709,1710,2177])

def test_add_an_item_cart(before_each_test: APIRequestContext, pid):
     
   # read base_uri fro json
     with open(filepath,"r") as file:
         data = json.load(file)
     payload ={
          "productId": pid,
          "quantity": 2
          
     }
     response = before_each_test.post(
         f"/carts/{data['cart_id']}/items", data=payload)
     assert response.status == 201
     response_json = response.json()
     print(json.dumps(response_json, indent=4))
     assert response_json['created'] == True
     data['item_id'] = response_json['itemId']
     with open(filepath, "w") as file:
         json.dump(data, file, indent=4)