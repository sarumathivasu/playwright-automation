import csv
import pytest
from playwright.sync_api import Page

test_data = []

with open("test_data_DDT\input.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        test_data.append(tuple(row))

@pytest.mark.parametrize("username,password", test_data)
def test_login(page: Page, username, password):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.locator("#username").fill(username)
    page.locator("#password").fill(password)

    page.locator("#submit").click()