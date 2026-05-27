from playwright .sync_api import Playwright,Page,expect

# Dynamic Table Practice
# URL:
# https://practice.expandtesting.com/dynamic-table

# https://practice.expandtesting.com/dynamic-table
def test_dynamic_table(page:Page):
    # Open the webpage
    page.goto("https://practice.expandtesting.com/dynamic-table")
        # ==========================================
    # TASK 1 : GET ALL HEADER VALUES
    # ==========================================

    # Locate all table headers
    locator_header=page.locator("table.table-striped thead th")

     # Get all header texts as list
    get_header=locator_header.all_inner_texts()

    # Print headers
    print(get_header)

    # Count total headers
    count_header_rows=locator_header.count()
    print("header counter is:", count_header_rows)

    # ==========================================
    # TASK 2 : FIND CPU COLUMN INDEX
    # ==========================================

    # Find index position of CPU header

    cpu_index=get_header.index("CPU")
    print("cpu index is:",cpu_index)

    # ==========================================
    # TASK 3 : GET ALL TABLE ROWS
    # ==========================================

    # Locate all body rows

    locator_get_all_rows=page.locator("table.table-striped tbody tr")

    # we get all the rows
    # get_all_rows=locator_get_all_rows.all_inner_texts()
    # print(get_all_rows)

    # Count total rows
    count_all_rows=locator_get_all_rows.count()
    print("all rows count", count_all_rows)

    # Empty variable to store chrome cpu value

    chrome_cpu =""

    # ==========================================
    # TASK 4 : LOOP THROUGH EACH ROW
    # ==========================================

    for i in range(count_all_rows):

            # Get one row at a time

        line_by_line=locator_get_all_rows.nth(i)

            # Get complete row text

        all_line=line_by_line.inner_text()

        # print("current line")
        # print("get value", all_line)
        

    # ==========================================
    # TASK 5 : FIND CHROME ROW
    # ==========================================

        if "Chrome" in all_line:

            # Get CPU value from Chrome row
            # cpu_index used because CPU column changes dynamically

            chrome_cpu=line_by_line.locator("td").nth(cpu_index).inner_text()
            print("Chrome CPU value:",chrome_cpu)
            page.wait_for_timeout(5000)

    # ==========================================
    # TASK 6 : GET YELLOW TEXT VALUE
    # ==========================================

            # Yellow label shown above table

            a=page.locator("#chrome-cpu")
            b=a.all_inner_texts()
            print("yellow_text",b)

    # ==========================================
    # TASK 7 : ASSERTION
    # ==========================================

            # Verify yellow text contains %

            # b= expect(page.locator("#chrome-cpu")).to_contain_text(["%"])
            expect(a).to_contain_text("%")










