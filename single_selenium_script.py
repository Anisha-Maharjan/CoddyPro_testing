import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://demo.coddypro.com")

username_field = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)
password_field = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)
login_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/main/div[4]/section[2]/div/form/button')
    )
)

username_field.send_keys("testingforcoddy7@gmail.com")
password_field.send_keys("Testingcoddy@123")
login_button.click()

try:
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Dashboard')]")
        )
    )
    print("Login Successful!")
except:
    try:
        error_message = driver.find_element(
            By.CLASS_NAME, "error-message"
        ).text
        print(f"Login Failed: {error_message}")
    except:
        print("Login Failed")

customers_nav = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/section[3]/a[3]/div[2]/p'
        )
    )
)
customers_nav.click()

add_customer_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/div[1]/div[2]/button[2]'
        )
    )
)
add_customer_button.click()

customer_name_field = wait.until(
    EC.visibility_of_element_located((By.NAME, "customer_name"))
)
customer_vat_field = driver.find_element(By.NAME, "tax_id")
customer_contact_name = driver.find_element(By.NAME, "contact_name")
customer_phone_field = driver.find_element(By.NAME, "mobile_no")
customer_email_field = driver.find_element(By.ID, "email_id")
customer_address_field = driver.find_element(By.ID, "address_line1")
customer_company_number_field = driver.find_element(By.NAME, "company_phone")

customer_name_field.send_keys("Automation Test Customer")
customer_vat_field.send_keys("VAT123456")
customer_contact_name.send_keys("John Doe")
customer_phone_field.send_keys("9800000011")
customer_email_field.send_keys("autocustomer@test.com")
customer_address_field.send_keys("Kathmandu, Nepal")
customer_company_number_field.send_keys("9876543211")

customer_group_dropdown = wait.until(
    EC.visibility_of_element_located((By.ID, "customer_group"))
)
Select(customer_group_dropdown).select_by_index(1)

save_customer_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/div/header/button'
        )
    )
)
save_customer_button.click()

try:
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Automation Test Customer')]")
        )
    )
    print("Add Customer Successful!")
except:
    print("Add Customer Failed!")

products_nav = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/header/nav/a[4]/span[2]'
        )
    )
)
products_nav.click()

add_product_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/div[1]/div[2]/button[3]'
        )
    )
)
add_product_button.click()

product_name_field = wait.until(
    EC.visibility_of_element_located(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/form/div[3]/div/div[1]/div[2]/input'
        )
    )
)

product_name_field.send_keys("Automation Test Product")

save_product_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/form/div[4]/button[2]'
        )
    )
)
save_product_button.click()

try:
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Automation Test Product')]")
        )
    )
    print("Add Product Successful!")
except:
    print("Add Product Failed!")

quotation_nav = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/header/nav/a[2]/span[2]'
        )
    )
)
quotation_nav.click()

quotation_customer_dropdown = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/section[1]/div/div[1]/div[2]/div/button'
        )
    )
)
quotation_customer_dropdown.click()

quotation_customer_search = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//input[contains(@placeholder, "Search")]')
    )
)
quotation_customer_search.send_keys("MIS Global Pvt Ltd")

quotation_customer_option = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[self::button or @role='option'][contains(., 'MIS Global Pvt Ltd')]"
        )
    )
)
quotation_customer_option.click()

quotation_item_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/section[2]/div[3]/button'
        )
    )
)
quotation_item_button.click()

quotation_item_search = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//input[contains(@placeholder, "Search")]')
    )
)
quotation_item_search.send_keys("Laptop")

quotation_item_option = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[self::button or @role='option'][contains(., 'Laptop')]"
        )
    )
)
quotation_item_option.click()

quotation_item_done = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Done']")
    )
)
quotation_item_done.click()

save_quotation_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/aside/section/div[3]/div/div/button[3]'
        )
    )
)
save_quotation_button.click()

confirm_quotation_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="radix-:r1g:"]/div[2]/button[2]')
    )
)
confirm_quotation_button.click()
time.sleep(2)

try:
    wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(),'Quotation') and contains(text(),'created')]"
            )
        )
    )
    print("Create Quotation Successful!")
except:
    print("Create Quotation Failed!")

invoice_nav = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/header/nav/a[1]/span[2]'
        )
    )
)
invoice_nav.click()


invoice_customer_dropdown = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/section[1]/div/div[1]/div[2]/div/button'
        )
    )
)
invoice_customer_dropdown.click()

invoice_customer_search = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[2]/div[1]/div/input')
    )
)
invoice_customer_search.send_keys("MIS Global Pvt Ltd")

invoice_customer_option = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[self::button or @role='option'][contains(., 'MIS Global Pvt Ltd')]"
        )
    )
)
invoice_customer_option.click()

invoice_item_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/section[2]/div[3]/button'
        )
    )
)
invoice_item_button.click()

invoice_item_search = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="radix-:r29:"]/div[2]/div[1]/input')
    )
)
invoice_item_search.send_keys("Laptop")

invoice_item_option = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[self::button or @role='option'][contains(., 'Laptop')]"
        )
    )
)
invoice_item_option.click()

invoice_item_done = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@id=\"radix-:r29:\"]/div[2]/div[3]/button")
    )
)
invoice_item_done.click()

save_invoice_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/aside/section/div[3]/div/div/button[3]'
        )
    )
)
save_invoice_button.click()

confirm_invoice_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="radix-:r2d:"]/div[2]/button[2]')
    )
)
confirm_invoice_button.click()
time.sleep(2)

try:
    wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(),'Invoice') and contains(text(),'created')]"
            )
        )
    )
    print("Create Invoice Successful!")
except:
    print("Create Invoice Failed!")

purchase_nav = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[1]/div[3]/header/nav/a[5]/span[2]')
    )
)
purchase_nav.click()

purchase_supplier_dropdown = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/section[1]/div[2]/div[1]/div/button'
        )
    )
)
purchase_supplier_dropdown.click()

purchase_supplier_search = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[2]/div[1]/div/input')
    )
)
purchase_supplier_search.send_keys("Bhairahawa Suppliers")

purchase_supplier_option = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[self::button or @role='option'][contains(., 'Bhairahawa Suppliers')]"
        )
    )
)
purchase_supplier_option.click()

purchase_product_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/section[2]/div[2]/button'
        )
    )
)
purchase_product_button.click()

purchase_product_search = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="radix-:r3b:"]/div[2]/div[1]/input')
    )
)
purchase_product_search.send_keys("Laptop")

purchase_product_option = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//*[self::button or @role='option'][contains(., 'Laptop')]"
        )
    )
)
purchase_product_option.click()

purchase_product_done = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@id=\"radix-:r3b:\"]/div[2]/div[3]/button")
    )
)
purchase_product_done.click()

save_purchase_button = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[3]/div/main/div/div/div/div[2]/button[2]'
        )
    )
)
save_purchase_button.click()

confirm_purchase_button = driver.find_element(By.XPATH, "//*[@id=\"radix-:r37:\"]/div[2]/button[2]")
confirm_purchase_button.click()
time.sleep(2)

try:
    purchase_added = driver.find_element(By.XPATH, "//*[contains(text(),'Purchase') and contains(text(),'added')]")
    print("Add Purchase Successful!")
except:
    print("Add Purchase Failed!")

logout_element = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="root"]/div[1]/div[2]/aside/div/div[4]/button'
        )
    )
)
logout_element.click()

logout_element = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="radix-:rc:"]/div[2]/button[2]'
        )
    )
)
logout_element.click()

driver.quit()