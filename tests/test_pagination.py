from playwright.sync_api import Playwright, Page,expect

# def test_pagination(page:Page):
#     page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
#     # pagination=page.locator(".dt-paging-button:not(.first):not(.previous):not(.next):not(.last)")
#     pagination=page.locator('.dt-paging-button[aria-controls="example"]')
#     for i in range(pagination.count()):
#         print(pagination.nth(i).inner_text())
        
#     page.wait_for_timeout(3000)
#     # print(pagination.count())

def test_datafron_currentpage(page:Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    # pagination=page.locator(".dt-paging-button:not(.first):not(.previous):not(.next):not(.last)")
    headers=page.locator("#example thead th").all_inner_texts()
    # print(headers)
    pagination=page.locator("#example tbody tr")
    rows_count=pagination.count()
    for i in range(rows_count):
        row=pagination.nth(i)
        cells=row.locator("td")
        print("\nNewLine")
        for j in range(cells.count()):
            print(headers[j],":",cells.nth(j).inner_text())
