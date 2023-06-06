from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
print(driver.title)
time.sleep(2)