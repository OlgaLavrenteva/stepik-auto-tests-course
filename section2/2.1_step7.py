from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    x_element = browser.find_element_by_id("treasure")
    x_value = x_element.get_attribute("valuex")
    result_value = calc(x_value)
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(result_value)
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_radio.click()
    submit_button = browser.find_element_by_css_selector("[type='submit']")
    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
