from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.daraz.com.bd/")
print(driver.title)

time.sleep(3)