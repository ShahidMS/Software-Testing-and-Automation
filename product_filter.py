from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_test import driver_context, create_wait
from .config import BASE_URL


def run():
    with driver_context() as driver:
        driver.get(f"{BASE_URL}/products")

        wait = create_wait(driver)

        search_input = wait.until(
            EC.visibility_of_element_located((By.ID, "search_product"))
        )
        search_input.send_keys("Blue Top")

        driver.find_element(By.ID, "submit_search").click()

        products = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-image-wrapper"))
        )

        assert len(products) > 0, "No products found after search"

        print(f"Product filter test passed! {len(products)} products found.")
