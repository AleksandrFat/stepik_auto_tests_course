from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button_window1 = browser.find_element(By.TAG_NAME, 'button')
    button_window1.click()
    browser.switch_to.window(browser.window_handles[-1])  # переход на новую вкладку
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = calc(int(x))
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(answer)
    button_new_window = browser.find_element(By.CSS_SELECTOR, 'button')
    button_new_window.click()
finally:
    sleep(10)
    browser.quit()