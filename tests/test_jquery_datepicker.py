from playwright.sync_api import Playwright , Page,expect

def test_jquery_datepicker_approach_1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    date_picker_001=page.locator(".hasDatepicker").nth(0)
    date_picker_001.scroll_into_view_if_needed()
    date_picker_001.click()
    date_picker_001.fill("06/25/2026")
    page.wait_for_timeout(3000)


def test_jquery_datepicker_approach_002(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    date_picker_01=page.locator(".hasDatepicker").nth(0)
    date_picker_01.scroll_into_view_if_needed()
    date_picker_01.click()

    is_future=False
    year="2025"
    month="October"
    date="26"

    select_option(page,year,month,date,is_future)
    print(date_picker_01.input_value())
    page.wait_for_timeout(3000)

def select_option(page, target_year,target_month,target_date,is_future):
    while True:
        current_month=page.locator(".ui-datepicker-month").text_content()
        current_year=page.locator(".ui-datepicker-year").text_content()
        if current_month==target_month and current_year==target_year:
            break
        if is_future==True:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    all_dates=page.locator(".ui-datepicker-calendar td").all()
    print(all_dates)
    for i in all_dates:
        j=i.inner_text()
        if(j==target_date):
            i.click()
            break


# HERE THE CALENDER TYPE IS DIFFERENT ITS COMES DROPDOWN
def test_jquery_datepicker_approach_003(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    date_picker_01=page.locator(".hasDatepicker").nth(1)
    date_picker_01.scroll_into_view_if_needed()
    date_picker_01.click()

    is_future=True
    year="2028"
    month="Oct"
    date="26"

    select_option_001(page,year,month,date,is_future)
    print(date_picker_01.input_value())
    page.wait_for_timeout(3000)

def select_option_001(page, target_year,target_month,target_date,is_future):
    while True:
        current_month=page.locator(".ui-datepicker-month option:checked").text_content().strip()
        current_year=page.locator(".ui-datepicker-year option:checked").text_content().strip()
        if current_month==target_month and current_year==target_year:
            break
        if is_future==True:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    all_dates=page.locator(".ui-datepicker-calendar td").all()
    print(all_dates)
    for i in all_dates:
        j=i.inner_text()
        if(j==target_date):
            i.click()
            break



