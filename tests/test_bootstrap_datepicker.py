from playwright.sync_api import Playwright , expect , Page

def test_bootstrap_datepicker01(page:Page):
    page.goto("https://www.booking.com/")
    cancel_inital_popup=page.get_by_label("Dismiss sign-in info.").click()
    start_end_date=page.locator(".ed9f289288").click()
    page.wait_for_timeout(2000)

    checkin_date(page,"2026","July","5")
    checkout_date(page,"2026","October","5")
    page.wait_for_timeout(3000)

    check_in=page.locator("[data-testid='date-display-field-start']").inner_text()
    check_out=page.locator("[data-testid='date-display-field-end']").inner_text()

    print(check_in)
    print(check_out)

    expect(page.locator("[data-testid='date-display-field-start']")).to_contain_text(check_in)
    expect(page.locator("[data-testid='date-display-field-end']")).to_contain_text(check_out)



def checkin_date(page,year,month,date):
    while True:
        start_month_year=page.locator(".af236b7586").nth(0).inner_text()
        current_month,current_year = start_month_year.split(" ")
        if current_month==month and current_year == year:
            break
        else:
            page.get_by_label("Next month").click()

    all_dates=page.locator("table.b8fcb0c66a").nth(0).locator("td").all()
    print(all_dates)
    for i in all_dates:
        if i.inner_text()==date:
            i.click()
            break


def checkout_date(page,year,month,date):
    while True:
        start_month_year=page.locator(".af236b7586").nth(1).inner_text()
        current_month,current_year = start_month_year.split(" ")
        if current_month==month and current_year == year:
            break
        else:
            page.get_by_label("Next month").click()

    all_dates=page.locator("table.b8fcb0c66a").nth(1).locator("td").all()
    print(all_dates)
    for i in all_dates:
        if i.inner_text()==date:
            i.click()
            break
        