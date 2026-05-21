from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect

# =========================================================
# SINGLE DROPDOWN HANDLING
# =========================================================

def test_single_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select by visible text
    page.locator("#country").select_option("United Kingdom")
    page.locator("#country").select_option(label="United Kingdom")

    # select by label
    page.locator('#country').select_option("australia")
    page.locator('#country').select_option(value="australia")

    # select by index
    page.locator('#country').select_option(index=9)

    # =====================================================
    # GET ALL DROPDOWN OPTIONS
    # =====================================================

    dropdown_options=page.locator('#country>option')

    # =====================================================
    # ASSERTION
    # VERIFY DROPDOWN OPTION COUNT
    # =====================================================

    expect(dropdown_options).to_have_count(10)

    # =====================================================
    # GET ALL DROPDOWN TEXT VALUES
    # all_text_contents() returns list with spaces/newlines | EG: [['\n        United States\n      ', ......]]
    # =====================================================

    a=dropdown_options.all_text_contents() 
    print(a)

    # =====================================================
    # REMOVE SPACES USING strip()
    # FOR MULTIPLE VALUES WE USE LOOP/LIST COMPREHENSION
    # =====================================================

    # in 37 line u can see the output with spaces,  so we can remove the space by using the strip if we want to use strip in list means we have use loop if single value no issues if we are using multiple values then we goahed with for loop - without loop it runs like [' India ', ' USA '].strip()
    b=[t.strip() for t in dropdown_options.all_text_contents()]
    print(b)

    # =====================================================
    # PRINT DROPDOWN VALUES LINE BY LINE
    # =====================================================

    for i in a:
       print(i.strip())

    # =====================================================
    # ASSERTION
    # VERIFY "Canada" EXISTS IN DROPDOWN
    # =====================================================

    assert "Canada" in b,"canada is not presented"   # Verifies when value is in dropdown
    page.wait_for_timeout(1500)

# =========================================================
# MULTIPLE DROPDOWN HANDLING
# =========================================================

def test_multiple_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

     # =====================================================
    # SELECT MULTIPLE VALUES
    # =====================================================

    # page.locator('#colors').select_option(["Red", "Green", "White"])
    page.locator('#colors').select_option(label=["Red", "Green", "White"])
    page.wait_for_timeout(8000)

    # =====================================================
    # SAME CAN BE DONE USING
    # VALUES AND INDEXES
    # =====================================================

    # =====================================================
    # GET MULTIPLE DROPDOWN OPTION COUNT
    # =====================================================

    multipleoption_count=page.locator('#colors>optios')

    # =====================================================
    # ASSERTION
    # VERIFY DROPDOWN OPTION COUNT
    # =====================================================

    expect(multipleoption_count).to_have_count(7)

    # =====================================================
    # GET ALL DROPDOWN TEXT VALUES
    # all_text_contents() returns list with spaces/newlines
    # =====================================================

    a= multipleoption_count.all_text_contents()
    print(a)

# =========================================================
# VERIFY DROPDOWN IS SORTED
# =========================================================

def test_sortedlist(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    a=page.locator('#colors>option')
    b=[i.strip() for i in a.all_text_contents()]
    c=b.copy()
    d=sorted(b)

    print("original",c)
    print("sorted",d)

    # =====================================================
    # VERIFY WHETHER DROPDOWN IS SORTED
    # =====================================================

    if c==d:
        print("sorted")

        assert True

    else:
        print("unsorted")

        assert False
