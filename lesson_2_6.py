from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    number_element = browser.find_element_by_id("input_value")
    x = number_element.text
    y = calc(x)
    
    
    browser.execute_script("window.scrollBy(0, 200);")
    
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    checkbox_first = browser.find_element_by_id("robotCheckbox")
    checkbox_first.click()
    
    radio_first = browser.find_element_by_id("robotsRule")
    radio_first.click()
    
    button.click()
    
    time.sleep(3)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    

