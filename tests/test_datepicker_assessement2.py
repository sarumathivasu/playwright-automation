from playwright.sync_api import Playwright,expect,Page

def test_railway(page:Page):
    page.goto("https://www.irctc.co.in/nget/train-search")
    alert=page.locator(".btn-primary").nth(1).click()
    from_date=page.locator("input[aria-label='Enter From station. Input is Mandatory.']").click()
    