import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

PAGE_URL = Path(__file__).resolve().parent.joinpath("index.html").as_uri()
TIMEOUT = 10
PRODUCT_NAME = "Wireless Mouse"
EXPECTED_STOCK = "In Stock"
NEW_PRICE = "29.99"


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, TIMEOUT)

    try:
        driver.get(PAGE_URL)
        wait.until(EC.visibility_of_element_located((By.ID, "search-input")))

        search_input = driver.find_element(By.ID, "search-input")
        search_input.send_keys(PRODUCT_NAME.lower())

        row = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//tbody/tr[.//td[contains(@class, 'product-name') and normalize-space()='{PRODUCT_NAME}']]")
            )
        )

        stock_text = row.find_element(By.CSS_SELECTOR, ".product-stock .badge").text.strip()
        assert stock_text.lower() == EXPECTED_STOCK.lower(), (
            f"Expected stock '{EXPECTED_STOCK}' but found '{stock_text}'"
        )
        print(f"Stock verified: {stock_text}")

        row.find_element(By.CSS_SELECTOR, ".btn-edit").click()

        wait.until(EC.visibility_of_element_located((By.ID, "modal-loader")))

        edit_form = wait.until(EC.visibility_of_element_located((By.ID, "edit-form")))
        print("Edit form fully loaded")

        price_input = driver.find_element(By.ID, "edit-price")
        price_input.clear()
        price_input.send_keys(NEW_PRICE)

        driver.find_element(By.ID, "save-btn").click()

        toast = wait.until(EC.visibility_of_element_located((By.ID, "toast")))
        message = driver.find_element(By.ID, "toast-message").text.strip()
        assert "updated successfully" in message.lower(), f"Unexpected toast: {message}"
        print(f"Success message verified: {message}")
        print("TEST PASSED: price updated to $29.99")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
