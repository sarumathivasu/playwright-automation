from playwright.sync_api import Playwright, Page, expect


# 1. Count total number of rows in table
def test_total_rows(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator('table[name="BookTable"] tbody tr:has(td)')

    row_count = rows.count()

    print("Total Rows:", row_count)


# 2. Count total number of headers
def test_total_headers(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    headers = page.locator('table[name="BookTable"] tbody th')

    header_count = headers.count()

    print("Total Headers:", header_count)

    for i in range(header_count):

        print(headers.nth(i).inner_text())


# 3. Read all data from row 2
def test_second_row_data(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    second_row = page.locator(
        'table[name="BookTable"] tbody tr:has(td)'
    ).nth(1)

    datas = second_row.locator("td").all_inner_texts()

    print(datas)


# 4. Read all data excluding header
def test_all_data_excluding_header(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator('table[name="BookTable"] tbody tr:has(td)')

    row_count = rows.count()

    for i in range(row_count):

        row = rows.nth(i)

        print(row.inner_text())


# 5. Print books whose author is Mukesh
def test_author_mukesh(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator('table[name="BookTable"] tbody tr:has(td)')

    row_count = rows.count()

    for i in range(row_count):

        row = rows.nth(i)

        author = row.locator("td").nth(1).inner_text()

        if author == "Mukesh":

            print(row.inner_text())


# 6. Calculate total price
def test_total_price(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    rows = page.locator('table[name="BookTable"] tbody tr:has(td)')

    row_count = rows.count()

    total_price = 0

    for i in range(row_count):

        row = rows.nth(i)

        price = row.locator("td").nth(3).inner_text()

        total_price += int(price)

    print("Total Price:", total_price)