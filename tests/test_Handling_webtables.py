from playwright.sync_api import Playwright,Page,expect

def test_static_webtables(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # a=page.locator('[name="BookTable"]')
    # expect(a).to_be_visible()
    # page.wait_for_timeout(3000)

    # b=page.locator('table[name="BookTable"] tbody tr')
    # c=[i.strip() for i in b.all_text_contents()]
    # # print(len(c))
    # d=len(c)
    # print(d)

    # expect(b).to_have_count(d)

    # column=page.locator('table[name="BookTable"] tbody th')
    # col=column.all_text_contents()
    # print(col)
    # print(len(col))
    # page.wait_for_timeout(3000)

    # datas=page.locator('table[name="BookTable"] tbody tr').all()
    # data=datas.all_text_contents()
    # page.wait_for_timeout(5000)
    # print(len(data))
    # print(data)
    # # page.wait_for_timeout(3000)
