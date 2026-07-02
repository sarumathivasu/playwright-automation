from playwright.sync_api import Playwright,Page,expect


# Reusable function to select a date from the jQuery date picker
def calendar_type(page,year,month,day,is_future):
    while True:
        # Get currently displayed month
        current_month=page.locator(".ui-datepicker-month option:checked").text_content().strip()

        # Get currently displayed year
        current_year=page.locator(".ui-datepicker-year option:checked").text_content().strip()

        # Stop when the required month and year are displayed
        if current_month==month and current_year==year:
            break

        # Navigate to next month if selecting a future date
        if is_future is True:
            page.locator(".ui-datepicker-next").click()

        # Navigate to previous month if selecting a past date
        else:
            page.locator(".ui-datepicker-prev").click()

    # Get all date cells from the calendar
    all_dates=page.locator(".ui-datepicker-calendar td").all()
    print(all_dates)

    # Loop through each date and click the required day
    for i in all_dates:
        j=i.inner_text()
        if(j==day):
            i.click()
            break


def test_assessment_001(page:Page):

    # Open the Dummy Ticket website
    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")


    # Wait for page to load
    page.wait_for_timeout(5000)

    # Verify default radio button (optional)
    # default_radio_button=page.locator(".product-item").nth(0)
    # default_radio_button.check()
    # expect(default_radio_button).to_be_checked()


    # ---------------- Personal Information ----------------

    # Enter First Name
    first_name=page.get_by_placeholder("first and middle name as on passport")
    first_name.scroll_into_view_if_needed()
    first_name.click()
    first_name.fill("Sarumathi")

    # Enter Last Name
    last_name=page.get_by_placeholder("last name as on passport")
    last_name.click()
    last_name.fill("Vasu")


    # ---------------- Order Notes ----------------

    # Enter additional order notes
    ORDER_NOTES=page.get_by_placeholder("Notes about your order, e.g. special notes for delivery.")
    ORDER_NOTES.click()
    ORDER_NOTES.fill("u receive a lotz bbe its just an beginning")


    # ---------------- Date of Birth ----------------

    # Open DOB date picker
    dob=page.locator("input[id='dob'][name='dob']")
    dob.click()
    page.wait_for_timeout(5000)

    # Select Date of Birth
    calendar_type(page,"2025","Oct","26",is_future=False)

    # Print selected DOB
    print(dob.input_value())

    # Verify DOB value
    expect(dob).to_have_value("26/10/2025")


    # ---------------- Gender ----------------

    # Select Female radio button
    sex=page.locator("input[id='sex_1'][name='sex']")
    page.wait_for_timeout(5000)
    sex.check()

    # Verify gender selection
    expect(sex).to_be_checked()


    # ---------------- Trip Type ----------------

    # Select Round Trip option
    trip_type=page.get_by_label(" Round trip")
    trip_type.check()

    # Verify Round Trip is selected
    expect(trip_type).to_be_checked()


    # ---------------- Journey Details ----------------

    # Enter From City
    From_city=page.locator("input[id='fromcity'][name='fromcity']")
    From_city.click()
    From_city.fill("Thiruvannamalai")

    # Enter To City
    To_city=page.locator("input[id='tocity'][name='tocity']")
    To_city.click()
    To_city.fill("Coimbatore")


    # ---------------- Departure Date ----------------

    # Open Departure Date picker
    Departure_Date=page.locator("input[id='departon'][name='departon']")
    Departure_Date.click()

    # Select Departure Date
    calendar_type(page,"2026","Oct","26",is_future=True)

    # Verify Departure Date
    expect(Departure_Date).to_have_value("26/10/2026")


    # ---------------- Return Date ----------------

    # Open Return Date picker
    Return_date=page.locator("input[name='returndate'][id='returndate']")
    Return_date.click()

    # Select Return Date
    calendar_type(page,"2026","Oct","28",is_future=True)

    # Verify Return Date
    expect(Return_date).to_have_value("28/10/2026")


    # ---------------- Additional Information ----------------

    # Enter additional travel information
    additional_information=page.get_by_placeholder("Enter any additional information that you like us to keep in mind.")
    additional_information.click()
    additional_information.fill("I am arrived at 10:00 PM ")


    # ---------------- Purpose of Ticket ----------------

    # Open Purpose dropdown
    Purpose_of_dummy_ticket=page.locator("#select2-reasondummy-container").click()

    # Select "Proof of return at airport"
    a=page.get_by_role("option",name=" Proof of return at airport")
    a.click()


    # ---------------- Proof Date ----------------

    # Open Proof Date calendar
    Departure_Date_from_homecountry=page.locator("input[name='proofdate'][id='proofdate']").click()

    # Select Proof Date
    calendar_type(page,"2026","Oct","28",is_future=True)

    # expect(Departure_Date_from_homecountry).to_have_value("28/10/2026")


    # ---------------- Delivery Method ----------------

    # Select Email delivery option
    Receive_dummy_ticket=page.locator("input[id='deliverymethod_2'][name='deliverymethod']")
    Receive_dummy_ticket.check()

    # Verify delivery method
    expect(Receive_dummy_ticket).to_be_checked()


    # ---------------- Billing Information ----------------

    # Enter Billing Name
    Bill_name=page.locator("input[name='billname'][id='billname']")
    Bill_name.click()
    Bill_name.fill("sarumathi_vasu")

    # Enter Email Address
    Email_address=page.locator("input[id='billing_email'][name='billing_email']")
    Email_address.click()
    Email_address.fill("saruintegra@gmail.com")


    # ---------------- Country Selection ----------------

    # Open Country dropdown
    Country=page.locator("#select2-billing_country-container").click()

    # Select Canada
    c=page.locator('.select2-results li:has-text("Canada")')
    c.click()


    # ---------------- Address Details ----------------

    # Enter Street Address
    street_address=page.locator("input[name='billing_address_1'][id='billing_address_1']")
    street_address.click()
    street_address.fill("256, Middlestreet ")

    # Enter Apartment/Unit
    street_address01=page.get_by_placeholder("Apartment, suite, unit, etc. (optional)")
    street_address01.click()
    street_address01.fill("Thiruvannamalai")


    # Enter City
    town_city=page.locator("input[name='billing_city'][id='billing_city']")
    town_city.click()
    town_city.fill("Thiruvannmalai")


    # ---------------- State Selection ----------------

    # Open State dropdown
    state_chatgpt=page.locator("#select2-billing_state-container").click()
    page.wait_for_timeout(1000)

    # Select New Brunswick
    page.locator('li:has-text("New Brunswick")').click()


    # ---------------- Postal Code ----------------

    # Enter Postal Code
    postcode_zip = page.locator("input[name='billing_postcode'][id='billing_postcode']")
    postcode_zip.click()
    postcode_zip.fill("N3A 1R3")


    # ---------------- Phone Number ----------------

    # Enter Phone Number
    phone=page.locator("input[name='billing_phone'][id='billing_phone']")
    phone.click()
    phone.fill("9445116078")


    # ---------------- Order Verification ----------------

    # Verify selected product
    your_order=page.locator(".product-details")
    expect(your_order).to_contain_text("Dummy return ticket")

    # Verify Order Total
    amount=page.locator(".product-total").nth(1)
    expect(amount).to_have_text("₹990")


    # ---------------- Place Order ----------------

    # Click Place Order button
    submit=page.locator("#place_order")
    submit.click()

    # Verify Checkout page is displayed
    expect(page.locator("h1").nth(1)).to_contain_text("Checkout")