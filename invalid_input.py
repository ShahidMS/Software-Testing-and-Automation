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
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys("wronguser@test.com")

        driver.find_element(By.NAME, "password").send_keys("wrongpassword")

        driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

        error = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")
            )
        )

        assert "incorrect" in error.text.lower()

        print("Invalid login test passed!")

        time.sleep(3)
