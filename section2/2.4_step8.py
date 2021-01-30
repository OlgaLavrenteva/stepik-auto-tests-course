from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(url)
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x_element = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    submit = browser.find_element_by_css_selector("[type='submit']")
    x = x_element.text
    answer.send_keys(calc(x))
    submit.click()

finally:
    time.sleep(20)
    browser.quit()
