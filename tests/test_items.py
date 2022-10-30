from selenium.webdriver.common.by import By


def test_add_to_basket_btn_exists(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_button = (By.CSS_SELECTOR, "button.btn-add-to-baskets")

    els = browser.find_elements(*add_button)
    
    assert len(els), "No element satisfying specified locator"
    assert len(els) == 1 , "Element is not unique"
