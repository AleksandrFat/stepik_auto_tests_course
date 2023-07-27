from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    url = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(url)
    button_book = browser.find_element(By.CSS_SELECTOR, '#book')
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))
    button_book.click()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = calc(int(x))
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, '#solve')
    button.click()
finally:
    sleep(10)
    browser.quit()