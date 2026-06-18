import json
from playwright.sync_api import APIRequestContext,Playwright
import pytest

#filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\data_global.json"

parameters={
         #"category":"candy",
         #"results":2,
         #"available":"true"
      }
@pytest.mark.order(3)
def test_get_all_products_list(before_each_test: APIRequestContext):
  
   response = before_each_test.get(
      "/products",
      params=parameters
      
      )
   assert response.status == 200
   #print ( response.json())
   response_json = response.json()
   print( json.dumps(response_json, indent=4))