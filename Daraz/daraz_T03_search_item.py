from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.daraz.com.bd/")
print(driver.title)

driver.find_element(By.ID,"q").send_keys("Phone")
driver.find_element(By.XPATH,"//*[@id='topActionHeader']/div/div[2]/div/div[2]/form/div/div[2]/button").click()
time.sleep(3)