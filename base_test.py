import os
from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from .config import TIMEOUT, DOWNLOAD_DIR


def create_driver():
    download_path = os.path.abspath(DOWNLOAD_DIR)
    os.makedirs(download_path, exist_ok=True)

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def create_wait(driver, timeout=TIMEOUT):
    return WebDriverWait(driver, timeout)


@contextmanager
def driver_context():
    driver = create_driver()
    try:
        yield driver
    finally:
        driver.quit()
