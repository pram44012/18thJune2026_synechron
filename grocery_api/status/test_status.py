import json
from playwright.sync_api import APIRequestContext
import pytest

#filepath = "C:\\Playwright_python\\June2026_APITesting_Synechron\\data_global.json"
@pytest.mark.order(1)
def test_status(before_each_test: APIRequestContext):   
   response = before_each_test.get("/status", headers={"Content-Type":"application/json"}) 
   #get status code and print
   status_code=response.status
   print(f"status code ={status_code}")
   #Assert status code
   assert status_code==200
   #print json response
   print(response.json())
   #Assert json response status value as 'UP'
   assert response.json()["status"] == 'UP'
   print("---------------Response - headers------------------")
   print(response.headers)