from selenium import webdriver

url = "https://www.google.com"

driver = webdriver.Chrome('C:/bin/chromedriver.exe')

driver.get(url)