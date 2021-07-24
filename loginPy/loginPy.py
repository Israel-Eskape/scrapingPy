from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = ''#url de la página a la que desea acceder
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(url)

user = ""#usuario del formulario
password = ""#password del formulario

input_user = driver.find_element_by_name("email")
input_user.send_keys(user)

input_password =driver.find_element_by_name("password")
input_password.send_keys(password)

time.sleep(2)

input_password.send_keys(Keys.ENTER)