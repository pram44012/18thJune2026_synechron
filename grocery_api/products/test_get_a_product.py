import json
from playwright.sync_api import APIRequestContext
import pytest

#filepath = "C:\\Playwright_python\\June2026_APITesting_Synechron\\data_global.json"
@pytest.mark.order(2)
def test_get_a_product_details(before_each_test: APIRequestContext):
   
   response  =before_each_test.get("/products/5774")
   assert response.status == 200
   response_json =response.json()
   print(json.dumps(response_json,indent = 4))