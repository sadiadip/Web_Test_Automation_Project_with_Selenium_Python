from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.daraz.com.bd/")
print(driver.title)

driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[1]/div[1]/input").send_keys("01xxxxxxxxx")
driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[1]/div[2]/input").send_keys("123@23")
driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[2]/div[1]/button").click()
time.sleep(3)
driver.find_element(By.ID,"q").send_keys("Phone")
driver.find_element(By.XPATH,"//*[@id='topActionHeader']/div/div[2]/div/div[2]/form/div/div[2]/button").click()
time.sleep(3)