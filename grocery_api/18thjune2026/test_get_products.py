import json
from playwright.sync_api import APIRequestContext
import pytest

filepath = "C:\\Users\\pramudit.gaur\\Playwright_python\\June2026_APITesting_Synechron\\data_global.json"

@pytest.mark.order(2)
def test_get_products(before_each_test: APIRequestContext):
    """
    GET request to /products endpoint
    Uses base_url from data_global.json via conftest.py fixture
    """
    # Make GET request to /products endpoint
    response = before_each_test.get("/products")
    
    # Print response details for debugging
    print("\n--- Products Response ---")
    print(f"Status Code: {response.status}")
    response_json = response.json()
    print(f"Number of products: {len(response_json)}")
    
    # Assert status code is 200
    assert response.status == 200, f"Expected status 200, got {response.status}"
    
    # Verify response is a list
    assert isinstance(response_json, list), "Response should be a list of products"
    
    # Verify products have expected fields
    if len(response_json) > 0:
        first_product = response_json[0]
        assert "id" in first_product, "Product should contain 'id' field"
        assert "name" in first_product, "Product should contain 'name' field"
        print(f"\nSample Product: {json.dumps(first_product, indent=2)}")
    
    print("✓ Products endpoint test passed!")