from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InvoicePage(BasePage):
    CUSTOMER_DROPDOWN = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/main/section[1]/div/div[1]/div[2]/div/button',
    )
    CUSTOMER_SEARCH_INPUT = (By.XPATH, '/html/body/div[2]/div[1]/div/input')

    ITEM_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/main/section[2]/div[3]/button',
    )

    ITEM_SEARCH_INPUT = (By.XPATH, '//input[contains(@placeholder, "Search")]')
    ITEM_DONE_BUTTON = (By.XPATH, "//button[normalize-space()='Done']")

    TAX_DEFAULT_UNSELECT = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/section/div[2]/div[2]/div[2]/label[1]/span/span[2]',
    )
    TAX_REQUIRED_SELECT = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/section/div[2]/div[2]/div[2]/label[3]/span/span[2]',
    )

    SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/main/div/aside/section/div[3]/div/div/button[3]',
    )
    CONFIRM_BUTTON = (By.XPATH, "//div[@role='alertdialog']//button[last()]")
    CREATED_MESSAGE = (
        By.XPATH,
        "//*[@id='root']/section/ol/li[contains(., 'Invoice issued successfully')]",
    )

    @staticmethod
    def option_locator(text: str):
        return (
            By.XPATH,
            f"//*[self::button or @role='option'][contains(., '{text}')]",
        )

    def select_customer(self, customer_name: str):
        self.click(self.CUSTOMER_DROPDOWN)
        self.type_text(self.CUSTOMER_SEARCH_INPUT, customer_name)
        self.click(self.option_locator(customer_name))
        return self

    def add_item(self, item_name: str):
        self.click(self.ITEM_BUTTON)
        self.type_text(self.ITEM_SEARCH_INPUT, item_name)
        self.click(self.option_locator(item_name))
        self.click(self.ITEM_DONE_BUTTON)
        return self

    def adjust_tax_selection(self):
        self.click(self.TAX_DEFAULT_UNSELECT)
        self.click(self.TAX_REQUIRED_SELECT)
        return self

    def save_and_confirm(self):
        self.click(self.SAVE_BUTTON)
        self.click(self.CONFIRM_BUTTON)
        return self

    def is_invoice_created(self, timeout: int = 10) -> bool:
        return self.is_visible(self.CREATED_MESSAGE, timeout=timeout)

    def create_invoice(self, customer_name: str, item_name: str):
        self.select_customer(customer_name)
        self.add_item(item_name)
        self.adjust_tax_selection()
        self.save_and_confirm()
        return self