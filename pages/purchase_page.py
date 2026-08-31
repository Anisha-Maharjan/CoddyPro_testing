from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PurchasePage(BasePage):
    SUPPLIER_DROPDOWN = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/section[1]/div[2]/div[1]/div/button',
    )
    SUPPLIER_SEARCH_INPUT = (By.XPATH, '/html/body/div[2]/div[1]/div/input')

    PRODUCT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/section[2]/div[2]/button',
    )

    PRODUCT_SEARCH_INPUT = (By.XPATH, '//input[contains(@placeholder, "Search")]')
    PRODUCT_DONE_BUTTON = (By.XPATH, "//button[normalize-space()='Done']")

    SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/div/div/div[2]/button[2]',
    )

    CONFIRM_BUTTON = (By.XPATH, "//div[@role='alertdialog']//button[last()]")
    ADDED_MESSAGE = (
    By.XPATH,
    "//*[@id='root']/section/ol/li[contains(., 'Purchase') and contains(., 'Receipt') and contains(., 'Submitted!')]",
    )   

    @staticmethod
    def option_locator(text: str):
        return (
            By.XPATH,
            f"//*[self::button or @role='option'][contains(., '{text}')]",
        )

    def select_supplier(self, supplier_name: str):
        self.click(self.SUPPLIER_DROPDOWN)
        self.type_text(self.SUPPLIER_SEARCH_INPUT, supplier_name)
        self.click(self.option_locator(supplier_name))
        return self

    def add_product(self, product_name: str):
        self.click(self.PRODUCT_BUTTON)
        self.type_text(self.PRODUCT_SEARCH_INPUT, product_name)
        self.click(self.option_locator(product_name))
        self.click(self.PRODUCT_DONE_BUTTON)
        return self

    def save_and_confirm(self):
        self.click(self.SAVE_BUTTON)
        self.click(self.CONFIRM_BUTTON)
        return self

    def is_purchase_added(self, timeout: int = 10) -> bool:
        return self.is_visible(self.ADDED_MESSAGE, timeout=timeout)

    def create_purchase(self, supplier_name: str, product_name: str):
        self.select_supplier(supplier_name)
        self.add_product(product_name)
        self.save_and_confirm()
        return self
