from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = 'https://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    answer = calc(int(x))

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(answer)

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input_robotCheckbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    input_robotCheckbox.click()

    input_robotsRule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    input_robotsRule.click()

    button.click()

finally:
    sleep(10)
    browser.quit()