from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    input_value = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robots_radio = browser.find_element_by_id("robotsRule")
    submit = browser.find_element_by_css_selector("[type='submit']")
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    x = input_value.text
    result = calc(x)
    answer.send_keys(result)
    robot_checkbox.click()
    robots_radio.click()
    submit.click()

finally:
    time.sleep(30)
    browser.quit()



