from playwright.sync_api import Playwright,Page,expect

def test_frames_approach_01(page:Page):

    # Navigate to the Frames Demo page
    page.goto("https://ui.vision/demo/webtest/frames/")

    # -----------------------------
    # FRAME 1 - Using page.frame()
    # -----------------------------

    # Switch to Frame 1 using its URL
    frames = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1")

    # Locate the text field inside Frame 1
    a = frames.locator("input[name='mytext1']")

    # Click and enter text
    a.click()
    a.fill("Saru's frame")

    # Pause for demonstration
    frames.wait_for_timeout(1000)


    # -----------------------------------------
    # FRAME 2 - Using page.frame_locator()
    # -----------------------------------------

    # Locate Frame 2 using frame_locator
    frame_002 = page.frame_locator("frame[src='frame_2.html']")

    # Fill the textbox inside Frame 2
    b = frame_002.locator("input[name='mytext2']")
    b.fill("saru's second frame")

    # Pause for demonstration
    page.wait_for_timeout(1000)


    # -----------------------------------------
    # FRAME 3 - Using page.frame()
    # -----------------------------------------

    # Switch to Frame 3 using its URL
    frame_003 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")

    # Fill the textbox inside Frame 3
    c = frame_003.locator("input[name='mytext3']")
    c.fill("saru's third frame")

    # Pause for demonstration
    page.wait_for_timeout(1000)


    # -----------------------------------------
    # CHILD FRAME (Google Form)
    # -----------------------------------------

    # Get the first child frame (Google Form iframe)
    child = frame_003.child_frames[0]


    # Click the "I am a human" checkbox
    question_001 = child.locator("div[aria-label='I am a human']")
    question_001.click()


    # Select "Web Testing"
    question_002 = child.locator("div[aria-label='Web Testing']").click()


    # Select "Form Autofilling"
    question_003 = child.locator("div[aria-label='Form Autofilling']").click()


    # Click the Next button in the Google Form
    button = child.locator(".YhQJj").click()


    # Fill the first text field
    question_004 = child.locator(".whsOnd").fill("nothing to say!!")


    # Fill the multiline text area
    question_005 = child.locator("textarea[aria-label='Your answer']").fill("noob")


    # Submit the Google Form
    child.get_by_role("button", name="Submit").click()

    # Pause to observe the submission
    page.wait_for_timeout(5000)


    # Print the child frame object
    print(child)


    # -----------------------------------------
    # FRAME 4 - Using frame_locator()
    # -----------------------------------------

    # Locate Frame 4
    frame_004 = page.frame_locator("frame[src='frame_4.html']")

    # Fill the textbox inside Frame 4
    d = frame_004.locator("input[name='mytext4']")
    d.fill("saru's fourth frame")

    # Pause for demonstration
    page.wait_for_timeout(1000)


    # -----------------------------------------
    # FRAME 5 - Using frame_locator()
    # -----------------------------------------

    # Locate Frame 5
    frame_005 = page.frame_locator("frame[src='frame_5.html']")

    # Fill the textbox inside Frame 5
    e = frame_005.locator("input[name='mytext5']")
    e.fill("saru's fifth frame")

    # Pause for demonstration
    page.wait_for_timeout(1000)