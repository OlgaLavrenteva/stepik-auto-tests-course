from selenium import webdriver
import time
import math


def calc(x):
    # ln(abs(12*sin(x)))
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    button = browser.find_element_by_css_selector("[type='submit']")
    x = x_element.text
    answer.send_keys(calc(x))
    button.click()
finally:
    time.sleep(20)
    browser.quit()
