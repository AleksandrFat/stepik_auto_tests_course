from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)
    answer = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(answer)

    input_robotCheckbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    input_robotCheckbox.click()

    input_robotsRule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    input_robotsRule.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    sleep(10)
    browser.quit()
