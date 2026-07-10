from playwright.sync_api import Playwright,expect

def test_traces(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    context.tracing.start(screenshots=True,snapshots=True)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_load_state("networkidle")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(6000)
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()