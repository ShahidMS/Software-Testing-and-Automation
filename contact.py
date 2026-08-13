from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_test import driver_context, create_wait
from .config import BASE_URL


def run():
    with driver_context() as driver:
        driver.get(f"{BASE_URL}/contact_us")

        wait = create_wait(driver)

        wait.until(
            EC.visibility_of_element_located((By.NAME, "name"))
        ).send_keys("John Doe")

        driver.find_element(By.NAME, "email").send_keys("john@example.com")
        driver.find_element(By.NAME, "subject").send_keys("Testing Contact Form")
        driver.find_element(By.ID, "message").send_keys("This is a Selenium test.")

        driver.find_element(By.NAME, "submit").click()

        wait.until(EC.alert_is_present())
        driver.switch_to.alert.accept()

        print("Contact form submitted successfully!")
