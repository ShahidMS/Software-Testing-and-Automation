from selenium.webdriver.common.by import By

from .base_test import driver_context
from .config import BASE_URL


def run():
    with driver_context() as driver:
        driver.get(f"{BASE_URL}/products")

        product_img = driver.find_element(
            By.XPATH, "(//div[@class='product-image-wrapper']//img)[1]"
        )
        src = product_img.get_attribute("src")

        assert src and src.startswith("http"), f"Product image src missing or invalid: {src}"

        print(f"Product image loaded successfully: {src}")
