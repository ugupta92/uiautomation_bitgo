from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class TestSuite:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def validate_transaction_heading(self):
        url = "https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"
        expected_heading = "25 of 2875 Transactions"

        try:
            print(f"Visiting {url}")
            self.driver.get(url)
            time.sleep(10)
            heading_element = self.driver.find_element(By.CLASS_NAME, "font-h3")
            actual_heading = heading_element.text.strip()
            assert actual_heading == expected_heading, f"Heading mismatch"
        except Exception as e:
            print(f"Error: {e}")

    def print_hash_for_selected_transactions(self):
        try:
            transactions = self.driver.find_elements(By.CLASS_NAME, "transaction-box")
            print(f"Total transactions visible: {len(transactions)}")

            for transaction in transactions:
                input_items = transaction.find_elements(By.CLASS_NAME, "vin")
                output_items = transaction.find_elements(By.CLASS_NAME, "vout")

                if len(input_items) == 1 and len(output_items) == 2:
                    try:
                        hash_element = transaction.find_element(By.CSS_SELECTOR, "div.txn.font-p2 > a")
                        hash_value = hash_element.text.strip()
                        print(f"Hash Value is: {hash_value}")
                    except Exception as e:
                        print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    test = TestSuite()
    try:
        test.validate_transaction_heading()
        test.print_hash_for_selected_transactions()
    finally:
        test.close()
  
	
