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

        email = driver.find_element(By.XPATH, "//input[@data-qa='signup-email']")
        email.send_keys("invalid-email")

        driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

        time.sleep(2)

        validation = driver.execute_script(
            "return arguments[0].validationMessage;", email
        )

        print("Validation Message:", validation)

        assert validation != ""

        print("Email format validation test passed!")
