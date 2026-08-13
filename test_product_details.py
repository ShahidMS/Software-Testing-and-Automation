import os
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = Path(__file__).resolve().parent
INDEX_URL = BASE_DIR.joinpath("index.html").as_uri()
TIMEOUT = 10
SHOT_DIR = BASE_DIR / "screenshots"


def screenshot(driver, label):
    SHOT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = SHOT_DIR / f"{label}_{stamp}.png"
    driver.save_screenshot(str(path))
    print(f"Screenshot saved: {path}")
    return path


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, TIMEOUT)

    try:
        driver.get(INDEX_URL)
        original_window = driver.current_window_handle

        detail_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".view-details"))
        )
        detail_btn.click()
        print("Clicked View Details")

        wait.until(lambda d: len(d.window_handles) == 2)
        driver.switch_to.window(
            [h for h in driver.window_handles if h != original_window][0]
        )
        print("Switched to new tab")

        wait.until(EC.visibility_of_element_located((By.ID, "spinner")))

        try:
            wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))
            print("Loading spinner disappeared")
        except Exception:
            screenshot(driver, "spinner_still_visible")
            raise

        try:
            wait.until(
                EC.visibility_of_element_located((By.ID, "product-details"))
            )
        except Exception:
            screenshot(driver, "details_not_visible")
            raise

        try:
            name = driver.find_element(By.ID, "product-name").text.strip()
            price = driver.find_element(By.ID, "product-price").text.strip()
            rating = driver.find_element(By.ID, "product-rating").text.strip()
        except Exception:
            screenshot(driver, "element_not_found")
            raise

        print(f"Product Name:   {name}")
        print(f"Product Price:  {price}")
        print(f"Product Rating: {rating}")

        assert name, "Product name is empty"
        assert price, "Product price is empty"
        assert rating, "Product rating is empty"

        driver.close()
        driver.switch_to.window(original_window)
        print("Closed new tab and returned to original window")
        assert driver.current_window_handle == original_window

        print("TEST PASSED")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
