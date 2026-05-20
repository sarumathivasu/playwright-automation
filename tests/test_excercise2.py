from playwright.sync_api import sync_playwright, Page, expect

def test_excercise(page:Page):
    page.goto("https://bstackdemo.com/")