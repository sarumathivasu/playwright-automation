from playwright.sync_api import Playwright , Page,expect
from datetime import datetime

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
    expect(date_picker_01).to_have_value("26/10/2028")
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

# Rule to remember automation:

# type="text" date fields (like jQuery UI Datepicker): Use the application's expected format (e.g. MM/DD/YYYY).
# type="date" HTML5 inputs: Always use YYYY-MM-DD with Playwright's fill(), regardless of how the date is displayed on the page.

def test_datepicker_003(page:Page):
    start_date="2026-10-10"
    end_date="2027-10-10"
    print(type(start_date))
    print(type(end_date))


    page.goto("https://testautomationpractice.blogspot.com/")
    datepicker_03=page.locator("#start-date")
    datepicker_03.fill(start_date)
    page.wait_for_timeout(1000)
    print(datepicker_03.input_value())

    datepicker_0003=page.locator("#end-date")
    datepicker_0003.fill(end_date)
    page.wait_for_timeout(1000)
    print(datepicker_0003.input_value())


    page.locator(".submit-btn").click()

    result=page.locator("#result")

    # Convert the start and end date strings into datetime objects so we use strptime,
    # What does %Y-%m-%d mean? 2026-10-10 Break it
                        # 2026
                        # │
                        # Year

                        # 10
                        # │
                        # Month

                        # 10
                        # │
                        # Day

                        # Format codes

                        # %Y
                        # ↓

                        # 4-digit year

                        # 2026
    # subtract them to get the date difference,
    # extract the total number of days using .days, if we dont use .days then we got an o/p as  'You selected a range of 365 days, 0:00:00 days.' but we only want days so we use .days
    # and use abs() to ensure the result is always positive.

    days=abs((datetime.strptime(start_date,"%Y-%m-%d") - datetime.strptime(end_date,"%Y-%m-%d")).days)
    to_have_texts=f"You selected a range of {days} days."
    page.wait_for_timeout(1000)

    expect(result).to_have_text(to_have_texts)



    



