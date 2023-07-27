from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    for element in elements:
        element.send_keys('.')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    sleep(30)
    browser.quit()
