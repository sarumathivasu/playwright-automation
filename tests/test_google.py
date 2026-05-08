from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect


# =========================================================
# PLAYWRIGHT MAIN CATEGORIES
# =========================================================

# | Category   | Purpose                        |
# | ---------- | ------------------------------ |
# | Locator    | Find elements                  |
# | Action     | Perform operations             |
# | Assertion  | Verify expected result         |
# | Navigation | Move/open pages                |
# | Waits      | Handle loading/synchronization |


def test_automation_checkbox(page: Page):

    # =====================================================
    # NAVIGATION
    # =====================================================

    page.goto("https://practice-automation.com/form-fields/")
    print(page.title())

    # =====================================================
    # ASSERTION
    # Verify page title
    # =====================================================

    expect(page).to_have_title("Form Fields | Practice Automation")

    # =====================================================
    # LOCATOR + ACTION
    # Fill input fields
    # =====================================================

    page.get_by_test_id("name-input").fill("SarumathiVasu")

    page.get_by_label("Password").fill("V_saru2002@")


    # =====================================================
    # SINGLE CHECKBOX OPERATIONS
    # =====================================================

    a = page.get_by_label("Water")     # locator
    a.check()                          # action
    expect(a).to_be_checked()          # assertion

    b = page.get_by_label("Milk")
    b.check()

    c = page.get_by_label("Coffee")
    c.check()

    page.get_by_test_id("name-input").clear()

    a.uncheck()
    expect(a).not_to_be_checked()



    # =====================================================
    # CHECK CURRENTLY SELECTED CHECKBOXES
    # =====================================================

    counts = ["Water", "Milk", "Coffee", "Wine", "Ctrl-Alt-Delight"]

    checkboxes = []

    for count in counts:

        checkbox = page.get_by_label(count)   # locator

        # verify whether checkbox selected or not
        if checkbox.is_checked():

            # store selected checkbox name
            checkboxes.append(count)

    print("tcs:", checkboxes)

    print("tcs:", len(checkboxes))

    page.wait_for_timeout(2000)


    # =====================================================
    # SELECT ALL CHECKBOXES
    # =====================================================

    counts = ["Water", "Milk", "Coffee", "Wine", "Ctrl-Alt-Delight"]

    checkboxes = []

    for count in counts:

        checkbox = page.get_by_label(count)   # locator

        checkbox.check()                      # action

        expect(checkbox).to_be_checked()      # assertion

    page.wait_for_timeout(2000)


    # =====================================================
    # UNCHECK LAST 3 CHECKBOXES
    # counts[-3:] → Coffee, Wine, Ctrl-Alt-Delight
    # =====================================================

    counts = ["Water", "Milk", "Coffee", "Wine", "Ctrl-Alt-Delight"]

    checkboxes = []

    for count in counts[-3:]:

        checkbox = page.get_by_label(count)   # locator

        checkbox.uncheck()                    # action

        expect(checkbox).not_to_be_checked()  # assertion

        page.wait_for_timeout(2000)

    # =====================================================
    # check the radio button
    # =====================================================

    d=page.get_by_test_id("color1")
    d.check()
    expect(d).to_be_checked()
    page.wait_for_timeout(2000)

    e=page.get_by_test_id("color3")
    e.check()
    expect(d).not_to_be_checked()
    page.wait_for_timeout(2000)

    # =====================================================
    # check the dropdown button
    # =====================================================

    f=page.get_by_test_id("automation")
    f.select_option('yes')
    expect(f).to_have_value('yes')
    page.wait_for_timeout(2000)

    g=page.locator("#automation")
    g.select_option('no')
    expect(g).to_have_value("no")
    page.wait_for_timeout(2000)






    
