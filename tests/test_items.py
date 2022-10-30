from selenium.webdriver.common.by import By


def test_shop_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_button = (By.CSS_SELECTOR, "button.btn-add-to-baskets")

    els = browser.find_elements(*add_button)
    
    assert len(els), "No element satisfying specified locator"
    assert len(els) == 1 , "Element is not unique"
