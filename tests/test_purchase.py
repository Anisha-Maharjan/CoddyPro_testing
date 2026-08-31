from config import config


def test_add_purchase(logged_in_dashboard, navbar, purchase_page):
    navbar.go_to_purchase()

    purchase_page.create_purchase(
        supplier_name=config.EXISTING_SUPPLIER,
        product_name=config.EXISTING_ITEM,
    )

    assert purchase_page.is_purchase_added(), "Expected a 'Purchase added' confirmation message"
