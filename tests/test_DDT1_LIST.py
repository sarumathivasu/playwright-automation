from playwright.sync_api import Playwright,Page,expect
import pytest

# ==========================================================
# Assignment 1 - Multiplication using Parametrization
# ==========================================================

# Test data contains:
# (First Number, Second Number, Expected Multiplication Result)

test_data_001=[
    (2,3,6),
    (4,5,20),
    (10,10,100),
    (8,7,56),
    (9,5,45),
    (6,5,30)
]

# Pass each tuple one by one into the test function.
@pytest.mark.parametrize("a,b,expected",test_data_001)

def test_multiplication(a,b,expected):
    # Verify multiplication result
    assert a*b == expected
    print(a*b)



# ==========================================================
# Assignment 2 - Even / Odd Number Validation
# ==========================================================

# Each tuple contains:
# (Number, Expected Result)

test_data_002=[
    (10,"Even"),
    (25,"Odd"),
    (100,"Even"),
    (77,"Odd")
]

# Executes the same test for every number.
@pytest.mark.parametrize("number,expected",test_data_002)

def test_is_even(number,expected):

#     # Check whether the number is Even or Odd
    if (number%2==0):
        result="Even"
    else:
        result="Odd"

#     # Compare actual result with expected result
    assert result == expected
    print(result)



# ==========================================================
# Assignment 3 - Login Logic without UI
# ==========================================================

# Test Data:
# (Username, Password, Expected Output)

test_data_003=[
            ("admin","admin123","Login Success"),
            ("admin","123","Login Failed"),
            ("user","admin123","Login Failed"),
            ("abc","xyz","Login Failed")
            ]

# Helper function that simulates login validation.
def is_passed(Username,Password):

#     # Valid Credentials
    if Username=="admin" and Password=="admin123":
        return "Login Success"

#     # Invalid Credentials
    else:
        return "Login Failed"

# Execute the function for every login combination.
@pytest.mark.parametrize("Username,Password,Expected",test_data_003)

def test_login(Username,Password,Expected):

#     # Verify actual login result with expected result.
    assert is_passed(Username,Password)==Expected



# ==========================================================
# Assignment 4 - UI Login Automation using Playwright
# ==========================================================

# Test data contains:
# (Username, Password)

test_data_004=[
            ("student","Password123"),
            ("student","wrong"),
            ("wrong","Password123"),
            ("abcd","12345")
            ]

# Run UI login test for every username/password pair.
@pytest.mark.parametrize("Username,Password",test_data_004)

def test_assignment_004(page:Page,Username,Password):

#     # Open login page
    page.goto("https://practicetestautomation.com/practice-test-login/")

#     # Enter Username
    page.locator("input[id='username'][name='username']").fill(Username)

#     # Enter Password
    page.locator("input[id='password'][name='password']").fill(Password)

#     # Click Login button
    page.locator("button[id='submit']").click()

#     # Scenario 1 : Valid Login
    if Username=="student" and Password == "Password123":

#         # Print current URL
        print(page.url)

#         # Verify successful navigation
        expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")

#         # Verify success heading
        expect(page.locator(".post-title")).to_contain_text("Logged In Successfully")

#         # Verify Logout link is visible
        expect(page.get_by_role("link", name="Log out")).to_be_visible()

#         # Capture success message
        success=page.locator(".post-title").text_content()
        print(f"Application result:{success}")

#     # Scenario 2 : Invalid Username
    elif Username !="student":

#         # Verify username error message
        expect(page.locator("div[id='error']")).to_have_text("Your username is invalid!")

        # Capture error message
        error = page.locator("div[id='error']").text_content()
        print(f"Application Result: {error}")

#     # Scenario 3 : Invalid Password
    else:

#         # Verify password error message
        expect(page.locator("div[id='error']")).to_have_text("Your password is invalid!")

#         # Capture error message
        error = page.locator("div[id='error']").text_content()
        print(f"Application Result: {error}")



# ==========================================================
# Assignment 5 - Simple Parametrization Example
# ==========================================================

# Test Data:
# (Product Name, Price)

test_data_005=[
    ("Apple", 100),
    ("Samsung", 200),
    ("OnePlus", 300),
    ("Nothing", 400)
]

# Pytest executes test_sample() four times,
# once for each tuple in test_data5.
@pytest.mark.parametrize("Product,Price",test_data_005)

def test_sample(Product,Price):

    # Print Product Name and its Price.
    print(f"Product:{Product} price:{Price}")