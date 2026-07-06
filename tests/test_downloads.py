from playwright.sync_api import Playwright,Page,expect

def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("My name is sarumathi_vasu and i want download text files")
    page.locator("#generateTxt").click()
    page.on("download", lambda download: download.save_as("downloads/text_file1.txt"))
    page.locator("#txtDownloadLink").click()
    page.wait_for_timeout(5000)
    


def test_download_way2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("My name is sarumathi_vasu and i want download text files")
    page.locator("#generateTxt").click()
    with page.expect_download() as downloaded_file:
        page.locator("#txtDownloadLink").click()
    downloaded_files=downloaded_file.value
    downloaded_files.save_as("downloads/text_file2.txt")


