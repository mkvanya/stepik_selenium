from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    answer = calc(x.text)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(10)
    browser.quit()

