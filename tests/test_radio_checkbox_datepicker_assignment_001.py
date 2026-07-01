from playwright.sync_api import Playwright,Page,expect


def calendar_type(page,year,month,day,is_future):
    while True:
        current_month=page.locator(".ui-datepicker-month option:checked").text_content().strip()
        current_year=page.locator(".ui-datepicker-year option:checked").text_content().strip()
        if current_month==month and current_year==year:
            break
        if is_future is True:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

    all_dates=page.locator(".ui-datepicker-calendar td").all()
    print(all_dates)
    for i in all_dates:
        j=i.inner_text()
        if(j==day):
            i.click()
            break


def test_assessment_001(page:Page):
    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")


# verify the radio button is checked by default
    page.wait_for_timeout(5000)
    # default_radio_button=page.locator(".product-item").nth(0)
    # default_radio_button.check()
    # expect(default_radio_button).to_be_checked()

# fill the first and last name

    first_name=page.get_by_placeholder("first and middle name as on passport")
    first_name.scroll_into_view_if_needed()
    first_name.click()
    first_name.fill("Sarumathi")

    last_name=page.get_by_placeholder("last name as on passport")
    last_name.click()
    last_name.fill("Vasu")

#  ADDING THE ADDITIONAL NOTES.
    ORDER_NOTES=page.get_by_placeholder("Notes about your order, e.g. special notes for delivery.")
    ORDER_NOTES.click()
    ORDER_NOTES.fill("u receive a lotz bbe its just an beginning")

    dob=page.locator("input[id='dob'][name='dob']")
    dob.click()
    page.wait_for_timeout(5000)
    calendar_type(page,"2025","Oct","26",is_future=False)
    print(dob.input_value())
    expect(dob).to_have_value("26/10/2025")

    # cancel_ai_popup = page.locator("#jivo_close_button").click()
    # page.wait_for_timeout(5000)
    sex=page.locator("input[id='sex_1'][name='sex']")
    page.wait_for_timeout(5000)
    sex.check()
    expect(sex).to_be_checked()

    trip_type=page.get_by_label(" Round trip")
    trip_type.check()
    expect(trip_type).to_be_checked()

    From_city=page.locator("input[id='fromcity'][name='fromcity']")
    From_city.click()
    From_city.fill("Thiruvannamalai")

    To_city=page.locator("input[id='tocity'][name='tocity']")
    To_city.click()
    To_city.fill("Coimbatore")

    Departure_Date=page.locator("input[id='departon'][name='departon']")
    Departure_Date.click()
    calendar_type(page,"2026","Oct","26",is_future=True)
    expect(Departure_Date).to_have_value("26/10/2026")

    Return_date=page.locator("input[name='returndate'][id='returndate']")
    Return_date.click()
    calendar_type(page,"2026","Oct","28",is_future=True)
    expect(Return_date).to_have_value("28/10/2026")


    additional_information=page.get_by_placeholder("Enter any additional information that you like us to keep in mind.")
    additional_information.click()
    additional_information.fill("I am arrived at 10:00 PM ")


    Purpose_of_dummy_ticket=page.locator("#select2-reasondummy-container").click()
    a=page.get_by_role("option",name=" Proof of return at airport")
    a.click()
    

    Departure_Date_from_homecountry=page.locator("input[name='proofdate'][id='proofdate']").click()
    calendar_type(page,"2026","Oct","28",is_future=True)
    # expect(Departure_Date_from_homecountry).to_have_value("28/10/2026")

    Receive_dummy_ticket=page.locator("input[id='deliverymethod_2'][name='deliverymethod']")
    Receive_dummy_ticket.check()
    expect(Receive_dummy_ticket).to_be_checked()

    Bill_name=page.locator("input[name='billname'][id='billname']")
    Bill_name.click()
    Bill_name.fill("sarumathi_vasu")

    Email_address=page.locator("input[id='billing_email'][name='billing_email']")
    Email_address.click()
    Email_address.fill("saruintegra@gmail.com")

    Country=page.locator("#select2-billing_country-container").click()
    page.wait_for_timeout(6000)
    c=page.locator('.select2-results li:has-text("Canada")')
    c.click()

    




