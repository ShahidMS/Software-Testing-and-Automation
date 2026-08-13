# Software Testing and Automation (STA)

A collection of Selenium WebDriver automated tests for [Automation Exercise](https://automationexercise.com), a practice website for automation engineers.

## Project Structure

```
STA/
├── base_test.py             # Shared driver & wait utilities
├── config.py                # Test configuration constants
├── run_all_tests.py         # Test runner (runs all test modules)
├── test.py                  # Google page title test
├── contact.py               # Contact form submission test
├── download_file.py         # Product image loading test
├── email_registration.py    # Email format validation test
├── invalid_file.py          # Invalid file upload test
├── invalid_input.py         # Invalid login credentials test
├── product_filter.py        # Product search/filter test
├── registration.py          # New user signup test
├── shopping_cart.py         # Category browsing test
├── upload_file.py           # File upload via contact form test
├── investigate.py           # Page structure investigation script
├── investigate2.py          # Deeper page structure investigation
├── requirements.txt         # Python dependencies
└── README.md
```

## Prerequisites

- Python 3.8+
- Google Chrome browser

## Setup

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
python run_all_tests.py
```

This executes all test modules sequentially and prints pass/fail results.

## Tests Overview

| Test | Description |
|---|---|
| **Test (Google)** | Navigates to google.com and prints the page title |
| **Contact Form** | Fills and submits the contact form with a confirm dialog |
| **Download File** | Verifies a product image loads on the products page |
| **Email Registration Validation** | Tests browser-side email format validation |
| **Invalid File Upload** | Uploads an `.exe` file via the contact form |
| **Invalid Login** | Attempts login with wrong credentials and checks for error |
| **Product Filter** | Searches for a product by name and checks results |
| **Registration** | Creates a new user account (randomized email) |
| **Shopping Cart** | Browses a product category and verifies products display |
| **Upload File** | Uploads a `.txt` file via the contact form |

## Dependencies

- [Selenium](https://www.selenium.dev/) — Browser automation framework
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) — Automatic ChromeDriver management
