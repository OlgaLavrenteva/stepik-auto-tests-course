from selenium import webdriver
import time
import os

url = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_to_upload = os.path.join(current_dir, 'test.txt')

try:
    browser = webdriver.Chrome()
    browser.get(url)
    firstname_element = browser.find_element_by_name("firstname")
    lastname_element = browser.find_element_by_name("lastname")
    email_element = browser.find_element_by_name("email")
    file_upload_element = browser.find_element_by_css_selector("[type='file']")
    submit_button = browser.find_element_by_css_selector("button[type='submit']")
    firstname_element.send_keys("Olga")
    lastname_element.send_keys("Lavrenteva")
    email_element.send_keys("test@test.ru")
    file_upload_element.send_keys(file_to_upload)
    submit_button.click()
finally:
    time.sleep(20)
    browser.quit()
