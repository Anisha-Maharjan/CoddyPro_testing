from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    DASHBOARD_LOADED_INDICATOR = (By.XPATH, "//*[contains(text(),'Amount Payable')]")
    CUSTOMERS_NAV = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/section[3]/a[3]/div[2]/p',
    )

    def is_loaded(self, timeout: int = 10) -> bool:
        return self.is_visible(self.DASHBOARD_LOADED_INDICATOR, timeout=timeout)

    def go_to_customers(self):
        self.click(self.CUSTOMERS_NAV)
        return self
