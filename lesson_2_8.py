from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = browser.find_element_by_xpath("//input[@name='firstname']")
    first_name.send_keys("Rita")
    
    last_name = browser.find_element_by_xpath("//input[@name='lastname']")
    last_name.send_keys("Molodec")
    
    email = browser.find_element_by_xpath("//input[@name='email']")
    email.send_keys("Molodec@mail.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'some_text_file.txt')    
    send_file = browser.find_element_by_xpath("//input[@type='file']")
            
    send_file.send_keys(file_path)
    
    button = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    button.click()
    
    time.sleep(3)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
