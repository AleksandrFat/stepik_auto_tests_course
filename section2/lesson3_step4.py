from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button_window = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button_window.click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = calc(int(x))
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(answer)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    sleep(10)
    browser.quit()