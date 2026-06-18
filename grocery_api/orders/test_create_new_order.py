from playwright.sync_api import APIRequestContext
import json

import pytest 

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\data_global.json"

@pytest.mark.order(8)
def test_create_new_order(before_each_test: APIRequestContext):
   with open(filepath,"r") as file:
      data = json.load(file)
   payload = {
    "cartId": data["cart_id"],
    "customerName": "John Doe"
         }
   
   response = before_each_test.post(
      "/orders", 
      headers={
         "Authorization": f"Bearer {data['token']}",
         "Content-Type": "application/json"
      },
      data=payload
      )
   
   assert response.status == 201
   
   print(json.dumps(response.json(), indent=4))