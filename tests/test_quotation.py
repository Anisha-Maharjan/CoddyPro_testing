from config import config


def test_create_quotation(logged_in_dashboard, navbar, quotation_page):
    navbar.go_to_quotation()

    quotation_page.create_quotation(
        customer_name=config.EXISTING_CUSTOMER_FOR_DOCS,
        item_name=config.EXISTING_ITEM,
    )

    assert quotation_page.is_quotation_created(), "Expected a 'Quotation created' confirmation message"
