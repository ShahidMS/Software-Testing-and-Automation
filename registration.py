import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_test import driver_context, create_wait
from .config import BASE_URL


def run():
    with driver_context() as driver:
        driver.get(f"{BASE_URL}/login")

        wait = create_wait(driver)

        wait.until(
            EC.visibility_of_element_located((By.NAME, "name"))
        ).send_keys("John Doe")

        email = f"john{random.randint(10000, 99999)}@example.com"
        driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)

        driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

        heading = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//b[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'enter account information')]")
            )
        )

        assert "enter account information" in heading.text.lower()

        print("Registration page opened successfully!")

        time.sleep(3)
