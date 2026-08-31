from config import config


def test_full_business_flow(
    logged_in_dashboard,
    navbar,
    customer_page,
    product_page,
    quotation_page,
    invoice_page,
    purchase_page,
):
    logged_in_dashboard.go_to_customers()
    data = config.NEW_CUSTOMER
    customer_page.add_customer(
        name=data["name"],
        vat=data["vat"],
        contact_name=data["contact_name"],
        phone=data["phone"],
        email=data["email"],
        customer_group=data["customer_group"],
    )
    assert customer_page.is_customer_added()

    navbar.go_to_products()
    product_page.add_product(config.NEW_PRODUCT_NAME)
    assert product_page.is_product_added()

    navbar.go_to_quotation()
    quotation_page.create_quotation(
        customer_name=config.EXISTING_CUSTOMER_FOR_DOCS,
        item_name=config.EXISTING_ITEM,
    )
    assert quotation_page.is_quotation_created()

    navbar.go_to_invoice()
    invoice_page.create_invoice(
        customer_name=config.EXISTING_CUSTOMER_FOR_DOCS,
        item_name=config.EXISTING_ITEM,
    )
    assert invoice_page.is_invoice_created()

    navbar.go_to_purchase()
    purchase_page.create_purchase(
        supplier_name=config.EXISTING_SUPPLIER,
        product_name=config.EXISTING_ITEM,
    )
    assert purchase_page.is_purchase_added()

    navbar.logout()