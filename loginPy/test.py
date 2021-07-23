from selenium import webdriver

drive = webdriver.Chrome(executable_path='')
drive.get('https://www.google.com')