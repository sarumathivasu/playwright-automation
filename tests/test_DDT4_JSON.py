import json
import pytest
from playwright.sync_api import Page

test_data=[]

with open("test_data_DDT\LoginData.json","r") as file:
    data=json.load(file)

for row in data:
    test_data.append(
        (
            row["username"],
            row["password"]
        )
    )

@pytest.mark.parametrize("username,password",test_data)

def test_login(page:Page,username,password):

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username",username)
    page.fill("#password",password)

    page.click("#submit")