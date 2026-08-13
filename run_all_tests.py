import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from STA import test
from STA import contact
from STA import download_file
from STA import email_registration
from STA import invalid_file
from STA import invalid_input
from STA import product_filter
from STA import registration
from STA import shopping_cart
from STA import upload_file


def main():
    tests = [
        ("Test (Google)", test),
        ("Contact Form", contact),
        ("Download File", download_file),
        ("Email Registration Validation", email_registration),
        ("Invalid File Upload", invalid_file),
        ("Invalid Login", invalid_input),
        ("Product Filter", product_filter),
        ("Registration", registration),
        ("Shopping Cart", shopping_cart),
        ("Upload File", upload_file),
    ]

    passed = 0
    failed = 0

    for name, module in tests:
        print(f"\n{'='*60}")
        print(f"Running: {name}")
        print(f"{'='*60}")
        try:
            module.run()
            print(f"  PASSED: {name}")
            passed += 1
        except Exception as e:
            print(f"  FAILED: {name} — {e}")
            failed += 1

    print(f"\n{'='*60}")
    print(f"RESULTS: {passed} passed, {failed} failed, {len(tests)} total")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
