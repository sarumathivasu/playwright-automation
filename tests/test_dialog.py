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
    