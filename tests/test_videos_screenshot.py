from playwright.sync_api import Playwright,expect,Page
import time
import datetime
import pytest

def test_video(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(record_video_dir="videos/" , record_video_size={"width":1024,"height":768})
    page=context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(6000)

def test_screenshot(page:Page):
    page.goto("https://orangehrm.com/")
    current_timestamp=str(int(time.time()))
    page.screenshot(path=f"screenshots/001_{current_timestamp}.png",full_page=True)

    