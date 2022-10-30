from selenium.webdriver.common.by import By
from pytest import mark
import time
import math


@mark.parametrize('url', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
])
def test_guest_should_see_login_link(browser, url):
    browser.get(url)
    answer_field = browser.find_element(By.CSS_SELECTOR, "textarea")
    answer = math.log(int(time.time()))
    answer_field.send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    msg = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    assert msg == "Correct!", f"Unexpected msg: '{msg}'"
