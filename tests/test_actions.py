from playwright.sync_api import Playwright,expect,Page
def test_actions(page:Page):
    page.goto("https://demo.guru99.com/test/drag_drop.html")
    source_001=page.locator("div#products li[data-id='1']")
    source_002=page.locator("div#products li[data-id='2']").nth(0)
    source_003=page.locator("div#products li[data-id='3']")
    source_004=page.locator("#fourth").nth(1)
    source_005=page.locator("div#products li[data-id='5']")
    source_006=page.locator("div#products li[data-id='6']")
    source_007=page.locator("div#products li[data-id='7']")
    source_008=page.locator("div#products li[data-id='8']")

    target1=page.locator("ol#bank")
    target2=page.locator("#amt7")
    target3=page.locator("ol#loan")
    target4=page.locator("#amt8")

    source_005.drag_to(target=target1)
    source_002.drag_to(target=target2)
    source_006.drag_to(target=target3)
    source_004.drag_to(target=target4)

    page.wait_for_timeout(4000)