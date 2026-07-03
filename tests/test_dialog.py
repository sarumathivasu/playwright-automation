from playwright.sync_api import Playwright,Page,expect

"""
first need to call an event that is 
page.on(parameter)
first parameter is "dialog"(keyword)  and then second parameter is what should we have to do with that dialog box
dialog.accept()  

registering an event - approach 1 

to skip the test case then we can give @pytest.mark.skip

lambda parameters : expression

"""


def test_approach_001(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("dialog",lambda dialog:dialog.accept())
    page.wait_for_timeout(2000)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)

def test_approach_confirm(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("dialog",lambda dialog:dialog.dismiss())
    page.wait_for_timeout(1000)
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)

def test_approach_prompt(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("dialog",lambda dialog:dialog.accept("sarumathiv"))
    page.locator("#promptBtn").click()
    page.wait_for_timeout(500)


#new page.

def test_newpage_approach1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    with page.expect_popup() as popup:
        page.get_by_text("New Tab").click()
        new_page=popup.value
        page.wait_for_timeout(5000)
        expect(new_page).to_have_url("https://www.pavantestingtools.com/")
        expect(new_page).to_have_title("SDET-QA Blog")

# Popup window

def test_newpage_approach2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    context=page.context
    with context.expect_page() as popup:
        page.get_by_text("Popup Windows").click()
        new_page=popup.value
        page.wait_for_timeout(5000)
        print(new_page.url)
        # expect(new_page).to_have_url("https://www.selenium.dev/")
        # expect(new_page).to_have_title("SDET-QA Blog")
    
    