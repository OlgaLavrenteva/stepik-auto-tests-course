from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    x_element = browser.find_element_by_id("input_value")
    answer_element = browser.find_element_by_id("answer")
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_radio = browser.find_element_by_id("robotsRule")
    submit_button = browser.find_element_by_css_selector("[type='submit']")
    x = x_element.text
    result = calc(x)
    browser.execute_script("return arguments[0].scrollIntoView(true)", answer_element)
    answer_element.send_keys(result)
    browser.execute_script("return arguments[0].scrollIntoView(true)", robot_checkbox)
    robot_checkbox.click()
    browser.execute_script("return arguments[0].scrollIntoView(true)", robot_radio)
    robot_radio.click()
    browser.execute_script("return arguments[0].scrollIntoView(true)", submit_button)
    submit_button.click()
finally:
    time.sleep(20)
    browser.quit()
