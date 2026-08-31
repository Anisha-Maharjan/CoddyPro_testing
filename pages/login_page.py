from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://demo.coddypro.com"

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/main/div[4]/section[2]/div/form/button')
    DASHBOARD_LOADED_INDICATOR = (By.XPATH, "//*[contains(text(),'Amount Payable')]")
    ERROR_MESSAGE = (
        By.XPATH,
        "//section/ol/li[contains(., 'Login failed') and contains(., 'Invalid login credentials')]",
    )
    ERROR_MESSAGE_FALLBACK = (
        By.XPATH,
        "//*[self::div or self::p or self::span][contains(text(), 'Login failed') or contains(text(), 'Invalid login credentials')]",
    )

    def load(self):
        self.open(self.URL)
        self.find_visible(self.USERNAME_FIELD)
        return self

    def login(self, email: str, password: str):
        self.type_text(self.USERNAME_FIELD, email)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def is_dashboard_visible(self, timeout: int = 10) -> bool:
        return self.is_visible(self.DASHBOARD_LOADED_INDICATOR, timeout=timeout)

    def get_error_message(self, timeout: int = 5) -> str:
        if self.is_visible(self.ERROR_MESSAGE, timeout=timeout):
            return self.get_text(self.ERROR_MESSAGE)
        if self.is_visible(self.ERROR_MESSAGE_FALLBACK, timeout=2):
            return self.get_text(self.ERROR_MESSAGE_FALLBACK)
        return None