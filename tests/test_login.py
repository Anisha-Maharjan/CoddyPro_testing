from config import config


def test_login_with_valid_credentials(login_page, dashboard_page):
    login_page.load()
    login_page.login(config.VALID_EMAIL, config.VALID_PASSWORD)

    assert dashboard_page.is_loaded(), "Dashboard heading did not appear after valid login"


def test_login_with_wrong_password(login_page):
    login_page.load()
    login_page.login(config.VALID_EMAIL, config.INVALID_PASSWORD)

    error_text = login_page.get_error_message(timeout=8)
    assert error_text, "Expected an error message to be shown for a wrong password"

    assert not login_page.is_dashboard_visible(timeout=2), (
        "Dashboard should NOT be reachable with a wrong password"
    )


def test_login_with_invalid_email(login_page):
    login_page.load()
    login_page.login("not_a_real_user@test.com", config.VALID_PASSWORD)

    error_text = login_page.get_error_message(timeout=8)
    assert error_text, "Expected an error message to be shown for an invalid email"

    assert not login_page.is_dashboard_visible(timeout=2), (
        "Dashboard should NOT be reachable with an unregistered email"
    )