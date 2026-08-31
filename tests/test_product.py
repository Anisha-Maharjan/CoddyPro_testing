from config import config


def test_add_product(logged_in_dashboard, navbar, product_page):
    navbar.go_to_products()

    product_page.add_product(config.NEW_PRODUCT_NAME)

    assert product_page.is_product_added(), "Product was not created"
