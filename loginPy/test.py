from selenium import webdriver

drive = webdriver.Chrome(executable_path='./chromedriver')
drive.get('https://www.google.com')