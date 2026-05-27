from playwright.sync_api import Playwright, Page, expect


# 1. Count total number of rows in table
def test_total_rows(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # locate all rows excluding header
    total_rows = page.locator('table[name="BookTable"] tbody tr:has(td)')

    # count rows
    row_count = total_rows.count()

    print("Total number of rows:", row_count)

    # print rows one by one
    for i in range(row_count):

        print(total_rows.nth(i).inner_text())



# 2. Count total number of headers
def test_total_headers(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # locate all headers
    headers = page.locator('table[name="BookTable"] tbody th')

    # count headers
    header_count = headers.count()

    print("Total headers:", header_count)

    # print all headers
    for i in range(header_count):

        print(headers.nth(i).inner_text())



# 3. Read all data from second row
def test_second_row(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # locate second row
    second_row = page.locator(
        'table[name="BookTable"] tbody tr:has(td)'
    ).nth(1)

    # get all td values from second row
    second_row_data = second_row.locator("td").all_inner_texts()

    print("Second row data:")

    for i in second_row_data:

        print(i)



# 4. Read all data excluding header
def test_all_data(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # locate all rows excluding header
    total_no = page.locator('table[name="BookTable"] tbody tr:has(td)')

    # count rows
    countss = total_no.count()

    print("Total rows:", countss)

    # print row by row
    for i in range(countss):

        print(total_no.nth(i).inner_text())

    # store all rows in list
    a = total_no.all_inner_texts()

    print("All rows list:")

    for i in a:

        print(i)

    counts = len(a)

    print("Length of list:", counts)

    expect(total_no).to_have_count(counts)



# 5. Print books whose author is Mukesh
def test_author(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # locate all rows excluding header
    locator_find = page.locator(
        'table[name="BookTable"] tbody tr:has(td)'
    )

    # count rows
    row_count = locator_find.count()

    print("Total rows:", row_count)

    # loop all rows
    for i in range(row_count):

        # get single row
        single_row_at_a_time = locator_find.nth(i)

        # get author column
        author = single_row_at_a_time.locator("td").nth(1).inner_text()

        print("Author name:", author)

        # check author
        if author == "Mukesh":

            print("Matched Row:")

            print(single_row_at_a_time.inner_text())



# 6. Calculate total price
def test_totalprice(page: Page):

    page.goto("https://testautomationpractice.blogspot.com/")

    # locate all rows excluding header
    locator_find = page.locator(
        'table[name="BookTable"] tbody tr:has(td)'
    )

    # count rows
    row_count = locator_find.count()

    print("Total rows:", row_count)

    total_price = 0

    # loop all rows
    for i in range(row_count):

        # get single row
        single_row_at_a_time = locator_find.nth(i)

        # get price column
        price = single_row_at_a_time.locator("td").nth(3).inner_text()

        print("Current Price:", price)

        # add prices
        total_price += int(price)

        print("Running Total:", total_price)

    print("Final Total Price:", total_price)