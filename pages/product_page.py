from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_PRODUCT_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/div[1]/div[2]/button[3]',
    )

    NAME_FIELD = (
        By.XPATH,
        '//*[@id="product_item_name"]',
    )

    SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/main/form/div[4]/button[2]',
    )

    PRODUCT_CREATED_MESSAGE = (
        By.XPATH,
        "//*[contains(., 'Product created')]",
    )

    def _type_name_and_verify(self, name: str, retries: int = 2):
        last_seen_value = None
        for attempt in range(retries):
            field = self.find_clickable(self.NAME_FIELD)
            field.click()
            field.clear()
            field.send_keys(name)

            field = self.find_visible(self.NAME_FIELD)
            last_seen_value = field.get_attribute("value")
            if last_seen_value == name:
                return
        raise AssertionError(
            f"Product name field did not register the typed value after "
            f"{retries} attempt(s). Expected '{name}', field shows "
            f"'{last_seen_value}'."
        )

    def add_product(self, name: str):
        if not self.is_visible(self.NAME_FIELD, timeout=2):
            self.click(self.ADD_PRODUCT_BUTTON)
        self._type_name_and_verify(name)
        self.click(self.SAVE_BUTTON)
        return self

    def is_product_added(self, timeout: int = 10) -> bool:
        return self.is_visible(
            self.PRODUCT_CREATED_MESSAGE,
            timeout=timeout
        )