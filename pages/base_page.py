from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    # low level waits 
    def _wait(self, timeout: int = None) -> WebDriverWait:
        return self.wait if timeout is None else WebDriverWait(self.driver, timeout)

    def find_visible(self, locator, timeout: int = None):
        return self._wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator, timeout: int = None):
        return self._wait(timeout).until(EC.element_to_be_clickable(locator))

    # common actions 
    def open(self, url: str):
        self.driver.get(url)
        return self

    def click(self, locator, timeout: int = None):
        self.find_clickable(locator, timeout).click()
        return self

    def type_text(self, locator, text: str, timeout: int = None, clear_first: bool = True):
        field = self.find_visible(locator, timeout)
        if clear_first:
            field.clear()
        field.send_keys(text)
        return self

    def get_text(self, locator, timeout: int = None) -> str:
        return self.find_visible(locator, timeout).text

    def is_visible(self, locator, timeout: int = 5) -> bool:
        try:
            self._wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_text_present(self, locator, timeout: int = None) -> bool:
        try:
            self.find_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
