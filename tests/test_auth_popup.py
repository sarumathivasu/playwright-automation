# from playwright.sync_api import Playwright,Page,expect

# def test_auth_approach1(page:Page):
#     page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#     expect(page.locator(".example h3")).to_contain_text("Basic Auth")



from playwright.sync_api import Playwright,expect

def test_auth_approach2(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(http_credentials={"username":"admin","password":"admin"})
    page1=context.new_page()
    page1.goto("https://the-internet.herokuapp.com/basic_auth")
    expect(page1.locator(".example h3")).to_contain_text("Basic Auth")
