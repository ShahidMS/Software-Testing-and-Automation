import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# 1) Download page
driver.get("https://automationexercise.com/upload-download")
time.sleep(3)
print("=== UPLOAD-DOWNLOAD PAGE ===")
print("Title:", driver.title)
buttons = driver.find_elements(By.TAG_NAME, "button")
print("Buttons:", [b.text for b in buttons])
links = driver.find_elements(By.TAG_NAME, "a")
print("Links (text):", [l.text for l in links])
all_ids = driver.find_elements(By.XPATH, "//*[@id]")
print("Elements with ID:", [(el.tag_name, el.get_attribute("id")) for el in all_ids])

# 2) Products page
driver.get("https://automationexercise.com/products")
time.sleep(3)
print("\n=== PRODUCTS PAGE ===")
print("Title:", driver.title)
selects = driver.find_elements(By.TAG_NAME, "select")
print("Select elements:", [s.get_attribute("id") or s.get_attribute("name") or "no-id" for s in selects])
all_ids = driver.find_elements(By.XPATH, "//*[@id]")
print("Elements with ID:", [(el.tag_name, el.get_attribute("id")) for el in all_ids if el.get_attribute("id")])
headers = driver.find_elements(By.XPATH, "//h2")
print("H2 headers:", [h.text for h in headers])

# 3) Login page (for registration)
driver.get("https://automationexercise.com/login")
time.sleep(3)
print("\n=== LOGIN PAGE ===")
print("Title:", driver.title)
inputs = driver.find_elements(By.TAG_NAME, "input")
print("Inputs:", [(i.get_attribute("name"), i.get_attribute("data-qa"), i.get_attribute("type"), i.get_attribute("placeholder")) for i in inputs])
buttons = driver.find_elements(By.TAG_NAME, "button")
print("Buttons:", [(b.text, b.get_attribute("data-qa")) for b in buttons])

# After signup flow (fill and submit)
driver.find_element(By.NAME, "name").send_keys("Test User")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("testuser999@example.com")
driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
time.sleep(3)
print("\n=== AFTER SIGNUP CLICK ===")
print("Current URL:", driver.current_url)
all_ids = driver.find_elements(By.XPATH, "//*[@id]")
print("Elements with ID:", [(el.tag_name, el.get_attribute("id")) for el in all_ids if el.get_attribute("id")])

driver.quit()
