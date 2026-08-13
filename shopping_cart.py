from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_test import driver_context, create_wait
from .config import BASE_URL


def run():
    with driver_context() as driver:
        driver.get(f"{BASE_URL}/category_products/1")

        wait = create_wait(driver)

        products = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "product-image-wrapper")
            )
        )

        assert len(products) > 0

        print(f"Shopping cart test passed! {len(products)} products found.")
