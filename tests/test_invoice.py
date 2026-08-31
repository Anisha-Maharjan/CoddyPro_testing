from config import config


def test_create_invoice(logged_in_dashboard, navbar, invoice_page):
    navbar.go_to_invoice()

    invoice_page.create_invoice(
        customer_name=config.EXISTING_CUSTOMER_FOR_DOCS,
        item_name=config.EXISTING_ITEM,
    )

    assert invoice_page.is_invoice_created(), "Expected an 'Invoice created' confirmation message"
