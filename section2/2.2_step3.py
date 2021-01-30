from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

url = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    num1_element = browser.find_element_by_id("num1")
    num2_element = browser.find_element_by_id("num2")
    select = Select(browser.find_element_by_class_name("custom-select"))
    submit = browser.find_element_by_css_selector("[type='submit']")
    num1 = num1_element.text
    num2 = num2_element.text
    res_sum = str(int(num1) + int(num2))
    select.select_by_value(res_sum)
    submit.click()
finally:
    time.sleep(20)
    browser.quit()
