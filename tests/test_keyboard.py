from playwright.sync_api import Playwright,Page,expect

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    name=page.get_by_placeholder("Enter Name")
    name.focus()
    page.keyboard.insert_text("sarumathi")
    email=page.keyboard.press("Tab")
    page.keyboard.insert_text("saru@yopmail.com")
    page.keyboard.press("Tab")
    page.keyboard.insert_text("9445116422")
    page.keyboard.press("Tab")
    page.keyboard.insert_text("256,middle street thiruvannamalai")
    page.wait_for_timeout(5000)




