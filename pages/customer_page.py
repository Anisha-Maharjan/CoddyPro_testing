from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class CustomerPage(BasePage):
    ADD_CUSTOMER_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/div[1]/div[2]/button[2]',
    )

    NAME_FIELD = (By.NAME, "customer_name")
    VAT_FIELD = (By.NAME, "tax_id")
    CONTACT_NAME_FIELD = (By.NAME, "contact_name")
    PHONE_FIELD = (By.NAME, "mobile_no")
    EMAIL_FIELD = (By.XPATH, "//*[@id='customer-form']/div/section[2]/div[2]/div/div[2]/input")
    CUSTOMER_GROUP_DROPDOWN = (By.ID, "customer_group")

    SAVE_BUTTON = (
        By.XPATH,
        '//*[@id="root"]/div[1]/div[3]/div/main/div/div/header/button',
    )
    
    CREATED_MESSAGE = (
        By.XPATH,
        "//*[@id='root']/section/ol/li[contains(., 'Customer') and contains(., 'created')]",
    )

    def open_add_customer_form(self):
        self.click(self.ADD_CUSTOMER_BUTTON)
        self.find_visible(self.NAME_FIELD)
        return self

    def select_customer_group(self, group_name: str = None):
        dropdown_element = self.find_visible(self.CUSTOMER_GROUP_DROPDOWN)
        select = Select(dropdown_element)
        if group_name:
            select.select_by_visible_text(group_name)
        else:
            select.select_by_index(1)
        return self

    def fill_customer_form(
        self,
        name: str,
        vat: str,
        contact_name: str,
        phone: str,
        email: str,
        customer_group: str = None,
    ):
        self.type_text(self.NAME_FIELD, name)
        self.type_text(self.VAT_FIELD, vat)
        self.type_text(self.CONTACT_NAME_FIELD, contact_name)
        self.type_text(self.PHONE_FIELD, phone)
        self.type_text(self.EMAIL_FIELD, email)
        self.select_customer_group(customer_group)
        return self

    def save(self):
        self.click(self.SAVE_BUTTON)
        return self

    def is_customer_added(self, timeout: int = 10) -> bool:
        return self.is_visible(self.CREATED_MESSAGE, timeout=timeout)

    def get_email_validation_message(self) -> str:
        field = self.find_visible(self.EMAIL_FIELD)
        return field.get_attribute("validationMessage") or ""

    def add_customer(
        self,
        name: str,
        vat: str,
        contact_name: str,
        phone: str,
        email: str,
        customer_group: str = None,
    ):
        self.open_add_customer_form()
        self.fill_customer_form(
            name, vat, contact_name, phone, email, customer_group
        )
        self.save()
        return self