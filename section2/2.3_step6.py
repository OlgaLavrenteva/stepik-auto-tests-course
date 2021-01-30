from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    submit = browser.find_element_by_css_selector("[type='submit']")
    x = x_element.text
    answer.send_keys(calc(x))
    submit.click()

finally:
    time.sleep(20)
    browser.quit()
