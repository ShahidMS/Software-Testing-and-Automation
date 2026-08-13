from .base_test import driver_context


def run():
    with driver_context() as driver:
        driver.get("https://www.google.com")
        print(driver.title)
