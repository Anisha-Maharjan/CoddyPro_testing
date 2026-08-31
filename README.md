CoddyPro Selenium POM Framework

Page Object Model test suite for the CoddyPro demo app, using Selenium + pytest.

Test Summary

10 tests across 6 modules, all passing.

Module	  | Tests | What's covered
Login	  |  3	  | Valid login; wrong password (rejected + error shown); invalid/unregistered email (rejected + error shown)
Customer  |	 2	  | Add a new customer (valid data); add customer with an invalid email (rejected, no customer created)
Product	  |  1	  | Add a new product
Quotation |	 1	  | Create a quotation for an existing customer + item
Invoice	  |  1	  | Create an invoice for an existing customer + item
Purchase  |  1	  | Record a purchase from an existing supplier + item
Full flow |  1	  | End-to-end smoke test: login -> customer -> product -> quotation -> invoice -> purchase -> logout, all in one session

How it works: each test drives the real app through Selenium (Chrome), using Page Object classes in pages/ that isolate every locator and on-page action from the test logic itself. Tests assert against the app's own confirmation toasts (e.g. "Customer created", "Invoice issued successfully") rather than assuming success, so a test only passes if the app actually did the thing.

Result: every test currently passes against the live demo app.

Structure
coddypro_pom/
├── pages/
│   ├── base_page.py       # shared wait/action helpers, every page inherits this
│   ├── login_page.py
│   ├── dashboard_page.py  # holds the dashboard-only "Customers" nav link
│   ├── navbar.py          # shared header nav (Products/Quotation/Invoice/Purchase/logout)
│   ├── customer_page.py
│   ├── product_page.py
│   ├── quotation_page.py
│   ├── invoice_page.py
│   └── purchase_page.py
├── tests/
│   ├── conftest.py        # driver + page-object fixtures, auto-captures a
│   │                       # screenshot + page source on any failure
│   ├── test_login.py       # valid login + 2 negative assertions
│   ├── test_customer.py    # add customer (valid) + add customer (invalid email)
│   ├── test_product.py
│   ├── test_quotation.py
│   ├── test_invoice.py
│   ├── test_purchase.py
│   └── test_e2e_flow.py   # single-session smoke test of the whole journey
├── config/
│   └── config.py          # URL + test data, nothing hardcoded in tests
├── pytest.ini
└── requirements.txt
Setup
bash
pip install -r requirements.txt

Requires chromedriver matching your installed Chrome version to be on PATH.

Running
bash
pytest                          # run everything
pytest tests/test_login.py      # just login
pytest -k "not e2e_flow"        # skip the long combined smoke test

On any failure, a screenshot and full page source are saved to failure_artifacts/ (named after the failing test) so you can see exactly what the browser saw at the moment it failed.