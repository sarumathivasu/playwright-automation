from playwright.sync_api import Playwright,Page,expect

def test_bootstrap_excercise(page:Page):

    # Task 1: Open Flipkart Website

    page.goto("https://www.flipkart.com/")


    # Task 2: Type Search Query

    a = page.locator(".nw1UBF").first
    a.click()
    a.fill("smart")


    # Task 3: Capture and Print Suggestions

    # Get all suggestion elements

    b = page.locator("li.Swx5kP")

    page.wait_for_timeout(5000)

    # Store all suggestion texts in list

    c = b.all_text_contents()


    # Print number of suggestions

    print("Total suggestions:", len(c))


    # Print 5th suggestion if available

    if len(c) >= 5:
        print("5th suggestion is:", c[4])


    # Print all suggestions one by one

    for index, value in enumerate(c):

        print(value)


        # Task 4: Select Specific Suggestion

        # If suggestion matches "smartphone"
        # click that suggestion

        if value == "smartphone":

            b.nth(index).click()

            break


    # Task 5: Assertion

    # Check at least one suggestion is present

    expect(b.first).to_be_visible()


    page.wait_for_timeout(5000)



