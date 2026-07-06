from playwright.sync_api import expect,Page

# def test_singleupload(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     single_upload=page.locator("#singleFileInput")
#     single_upload.scroll_into_view_if_needed()
#     single_upload.set_input_files("uploads\PAY-2026-05387 (1).pdf")
#     page.get_by_role("button",name='Upload Single File').click()
#     page.wait_for_timeout(5000)


#     multipleuploads=["uploads\INV-2026-05331.pdf","uploads\PAY-2026-05387 (1).pdf"]
#     multiple_uploads=page.locator("#multipleFilesInput")
#     multiple_uploads.scroll_into_view_if_needed()
#     multiple_uploads.set_input_files(multipleuploads)
#     page.get_by_role("button",name='Upload Multiple Files').click()
#     page.wait_for_timeout(5000)



def test_assignment_single_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")
    single_upload_files=page.locator("input[name='filesToUpload'][id='filesToUpload']")
    single_upload_files.set_input_files("uploads/INV-2026-05331.pdf")
    page.wait_for_timeout(5000)
    expect(page.locator("#fileList")).to_have_text("INV-2026-05331.pdf")

def test_assignment_multiple_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")
    single_upload_files=page.locator("input[name='filesToUpload'][id='filesToUpload']")
    multiple_files=["uploads\Bloom 365 - Customer Site Menu - PRD Document (1).pdf","uploads\company_sj_Alabama_INV-2026-05331.pdf","uploads\INV-2026-05331.pdf"]
    single_upload_files.set_input_files(multiple_files)
    page.wait_for_timeout(5000)
    expect_value1=page.locator("#fileList li")
    expect(expect_value1.nth(0)).to_have_text("Bloom 365 - Customer Site Menu - PRD Document (1).pdf")
    expect(expect_value1.nth(1)).to_have_text("company_sj_Alabama_INV-2026-05331.pdf")
    expect(expect_value1.nth(2)).to_have_text("INV-2026-05331.pdf")




