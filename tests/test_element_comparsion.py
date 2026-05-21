from playwright.sync_api import Playwright,Page,expect

def test_comparsions(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    a=page.locator(".product-title")
    b=[i.strip()for i in a .all_text_contents()]  # returns al the titles
    print(b)
    for j in b:
        print(j)

# 1. text_content()

# Gets raw text from FIRST matched element.

# Includes hidden text and extra spaces.

    c=page.locator(".product-title").first.text_content()
    print(c)

# O/p             $25 Virtual Gift Card

# 2. inner_text()

# Gets visible text only from FIRST matched element.

# Removes hidden text and normalizes spaces.

    d=page.locator(".product-title").first.inner_text()
    print(d)

# o/p:$25 Virtual Gift Card

# 3. all_text_contents()

# Gets raw text from ALL matched elements.

# Returns list.

    e=page.locator(".product-title").all_text_contents()
    print(e)

# o/p: ['\n            $25 Virtual Gift Card\n        ', '\n            14.1-inch Laptop\n        ', '\n            Build your own cheap computer\n        ', '\n            Build your own computer\n        ', '\n            Build your own expensive computer\n        ', '\n            Simple Computer\n        ']

# 4. all_inner_texts()

# Gets visible text from ALL matched elements.

# Returns list.

    f=page.locator(".product-title").all_inner_texts()
    print(f)
# O/p: ['$25 Virtual Gift Card', '14.1-inch Laptop', 'Build your own cheap computer', 'Build your own computer', 'Build your own expensive computer', 'Simple Computer']
