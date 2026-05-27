from playwright .sync_api import Playwright,Page,expect


# https://practice.expandtesting.com/dynamic-table
# def test_dynamicpage(page:Page):
#     page.goto(" https://practice.expandtesting.com/dynamic-table")
#     b=page.locator("table.table-striped thead th").all_inner_texts()
#     for i in b:
#         print(i)
#     print(b)
#     print(len(b))
#     page.wait_for_timeout(5000)
#     # rows_all=b.locator('tr').all()
#     # for i in rows_all:
#     #     b.locator("th").nth(0) 
#     # print(rows_all)

def test_testdata(page:Page):
    page.goto(" https://practice.expandtesting.com/dynamic-table")
    data=page.locator("table.table-striped tbody tr")
    count_data=data.count()
    print(count_data)
    for i in range(count_data):
        # datas= data.nth(i).all_inner_texts() #allinner text o/p is ['System\t0.8 MB/s\t0%\t92.5 MB\t4.5 Mbps']
        datas = data.nth(i).inner_text()
        print(datas)
    # for i in data:
    #     print(i)
    #     print(len(i))
    # print(data)