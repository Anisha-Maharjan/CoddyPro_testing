from config import config


def test_add_customer(logged_in_dashboard, customer_page):
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

    assert customer_page.is_customer_added(), "Customer was not added"


def test_add_customer_with_invalid_email(logged_in_dashboard, customer_page):
    logged_in_dashboard.go_to_customers()

    data = config.NEW_CUSTOMER
    customer_page.add_customer(
        name=data["name"],
        vat=data["vat"],
        contact_name=data["contact_name"],
        phone=data["phone"],
        email=config.INVALID_CUSTOMER_EMAIL,
        customer_group=data["customer_group"],
    )

    assert not customer_page.is_customer_added(timeout=5), (
        "Customer should NOT be created when the email address is invalid"
    )

    validation_message = customer_page.get_email_validation_message()
    assert validation_message, (
        "Expected the browser's native email validation to flag "
        f"'{config.INVALID_CUSTOMER_EMAIL}' as invalid (got no "
        "validationMessage - if this app uses custom validation instead "
        "of the native constraint API, this assertion may need to be "
        "replaced with a check for that custom error element instead)"
    )