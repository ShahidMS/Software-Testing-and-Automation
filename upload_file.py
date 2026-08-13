import os
import time
import tempfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_test import driver_context, create_wait
from .config import BASE_URL, UPLOAD_FILE_CONTENT


def run():
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as f:
        f.write(UPLOAD_FILE_CONTENT)
        upload_path = f.name

    try:
        with driver_context() as driver:
            driver.get(f"{BASE_URL}/contact_us")

            wait = create_wait(driver)

            wait.until(
                EC.visibility_of_element_located((By.NAME, "name"))
            ).send_keys("John Doe")

            driver.find_element(By.NAME, "email").send_keys("john@example.com")
            driver.find_element(By.NAME, "subject").send_keys("File Upload Test")
            driver.find_element(By.ID, "message").send_keys("Testing file upload using Selenium.")

            driver.find_element(By.NAME, "upload_file").send_keys(upload_path)

            driver.find_element(By.NAME, "submit").click()

            wait.until(EC.alert_is_present())
            driver.switch_to.alert.accept()

            print("Valid file uploaded successfully!")
    finally:
        if os.path.exists(upload_path):
            os.unlink(upload_path)
