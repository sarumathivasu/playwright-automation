from playwright.sync_api import sync_playwright, Page, expect


def test_bootstrapdropdown(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login to OrangeHRM application

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    page.get_by_role("button", name=" Login ").click()

    # Navigate to PIM module

    page.get_by_text('PIM').click()

    # Locate all bootstrap dropdowns

    dropdown = page.locator(".oxd-select-text")

    page.wait_for_timeout(5000)

    # Click the first dropdown

    dropdown.nth(0).click()

    # Capture all dropdown option texts

    options = page.locator(".oxd-select-option")

    values = [i.strip() for i in options.all_text_contents()]

    print(values)

    # Select the 5th option from dropdown

    options.nth(4).click()

    page.wait_for_timeout(5000)