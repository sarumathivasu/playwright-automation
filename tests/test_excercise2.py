from playwright.sync_api import sync_playwright, Page, expect

def test_excercise(page: Page):

    page.goto("https://bstackdemo.com/")
    page.wait_for_timeout(100)

# Verify whether the sorting dropdown is enabled

    a = page.locator('.sort')
    b = a.is_enabled()

    a.click()

    print("Dropdown is enabled")

# Select the sorting option as 'Lowest to highest'

    page.locator('.sort select').select_option("Lowest to highest")

# Fetch all product titles from the product cards

    a = page.locator('.shelf-item__title')

    b = [i.strip() for i in a.all_text_contents()]

    print(b)

# Fetch all product prices and convert them into integer values

    c = page.locator('.shelf-item__price .val')

    d = [int(j.strip().replace("$", "").replace(".00", "")) for j in c.all_text_contents()]

    print(d)

# Print the maximum and minimum product prices

    print("maximum value is", max(d))

    print("minimum value is", min(d))

    page.wait_for_timeout(5000)

# Map and print each product title with its corresponding price

    for k, l in zip(b, d):

        print("title is", k, "price is", l)

