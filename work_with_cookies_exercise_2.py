from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Здесь добавь свой предыдущий код для добавления куки
new_cookie = {"name": "my_first_cookie", "value": "15"}
driver.add_cookie(new_cookie)

cookie = driver.get_cookie("my_first_cookie")
assert cookie['value'] == '15'

# А теперь измени значение куки
driver.delete_cookie("my_first_cookie")

new_cookie = {"name": "my_first_cookie", "value": "25"}
driver.add_cookie(new_cookie)

# Проверь новое значение поля value для добавленной куки
cookie = driver.get_cookie("my_first_cookie")
assert cookie['value'] == '25'

driver.quit()