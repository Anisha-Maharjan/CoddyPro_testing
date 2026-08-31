from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NavBar(BasePage):

    INVOICE_NAV = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/header/nav/a[1]/span[2]')
    QUOTATION_NAV = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/header/nav/a[2]/span[2]')
    PRODUCTS_NAV = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/header/nav/a[4]/span[2]')
    PURCHASE_NAV = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/header/nav/a[5]/span[2]')

    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/aside/div/div[4]/button')
    LOGOUT_CONFIRM_BUTTON = (By.XPATH, '//*[@id="radix-:rc:"]/div[2]/button[2]')

    def go_to_invoice(self):
        self.click(self.INVOICE_NAV)
        return self

    def go_to_quotation(self):
        self.click(self.QUOTATION_NAV)
        return self

    def go_to_products(self):
        self.click(self.PRODUCTS_NAV)
        return self

    def go_to_purchase(self):
        self.click(self.PURCHASE_NAV)
        return self

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
        self.click(self.LOGOUT_CONFIRM_BUTTON)
        return self
