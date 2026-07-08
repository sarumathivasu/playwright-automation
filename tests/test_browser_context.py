from playwright.sync_api import Playwright,expect

def test_browser(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page1=context.new_page()
    # page2=context.new_page()
    page1.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page1.locator("input[name='username']").fill("Admin")
    page1.locator("input[name='password']").fill("admin123")
    page1.on("popup",lambda popup:popup.wait_for_load_state())
    page2=page1.get_by_text("OrangeHRM, Inc").click()
    
    
    page1.wait_for_timeout(5000)
    allpopups=context.pages
    print(len(allpopups))
    for i in allpopups:
        print(i.url)
        titles=i.title()
        print(titles)
        expect(allpopups[0]).to_have_title("OrangeHRM")
        expect(allpopups[1]).to_have_title("OrangeHRM: All in One HR Software for Businesses | OrangeHRM")


# def test_browser_approac2(playwright:Playwright):
#     browser=playwright.chromium.launch(headless=False)
#     context=browser.new_context()
#     page1=context.new_page()
#     page1.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     with page1.expect_popup()as page2:
#         page1.get_by_text("OrangeHRM, Inc").click()
#         pages=page2.value
#     page1.wait_for_timeout(5000)
#     allpopups=context.pages
#     print(len(allpopups))


