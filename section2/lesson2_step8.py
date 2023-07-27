from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'stepic.txt')

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.CSS_SELECTOR, '.form-group>.form-control:nth-child(2)')
    input_name.send_keys('!')

    input_last_name = browser.find_element(By.CSS_SELECTOR, '.form-group>.form-control:nth-child(4)')
    input_last_name.send_keys('!')

    input_email = browser.find_element(By.CSS_SELECTOR, '.form-group>.form-control:nth-child(6)')
    input_email.send_keys('!')

    input_file = browser.find_element(By.CSS_SELECTOR, '#file')
    input_file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    sleep(10)
    browser.quit()