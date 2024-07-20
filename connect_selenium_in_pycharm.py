from selenium import webdriver
import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()

driver.maximize_window() # полноэкранный режим

driver.get('https://ya.ru/')

# сделаем паузу
time.sleep(5)

# закроем браузер
driver.quit()
