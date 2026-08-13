import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# 1) Check if there's an upload-download page or different URL
urls_to_check = [
    "https://automationexercise.com/upload-download",
    "https://automationexercise.com/contact_us",
]
for url in urls_to_check:
    driver.get(url)
    time.sleep(2)
    print(f"=== {url} ===")
    print("Title:", driver.title)
    print("URL final:", driver.current_url)
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print("Buttons:", [b.text for b in buttons])
    all_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
    print("File inputs:", len(all_inputs))

# 2) Check Products page - category elements
driver.get("https://automationexercise.com/products")
time.sleep(2)
print("\n=== PRODUCTS CATEGORY SIDEBAR ===")
panels = driver.find_elements(By.XPATH, "//div[@id='accordian']//a")
for p in panels:
    print(f"  href={p.get_attribute('href')}, text='{p.text.strip()}', data-toggle={p.get_attribute('data-toggle')}")

# Check for any download-related links on the page
all_links = driver.find_elements(By.TAG_NAME, "a")
print("\n=== All Links with href containing 'download' ===")
for l in all_links:
    href = l.get_attribute("href") or ""
    if "download" in href.lower():
        print(f"  '{l.text}' -> {href}")

# 3) After signup - check what's on signup page
driver.get("https://automationexercise.com/signup")
time.sleep(2)
print("\n=== SIGNUP PAGE ===")
print("Title:", driver.title)
print("URL:", driver.current_url)
b_elements = driver.find_elements(By.TAG_NAME, "b")
for b in b_elements:
    print(f"  <b>: '{b.text}'")
h2_elements = driver.find_elements(By.TAG_NAME, "h2")
for h in h2_elements:
    print(f"  <h2>: '{h.text}'")

driver.quit()
