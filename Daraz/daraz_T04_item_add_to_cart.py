from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://www.daraz.com.bd/")
print(driver.title)

driver.find_element(By.ID,"q").send_keys("Phone")
driver.find_element(By.XPATH,"//*[@id='topActionHeader']/div/div[2]/div/div[2]/form/div/div[2]/button").click()
driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/img").click()
driver.find_element(By.XPATH,"//*[@id='module_add_to_cart']/div/button[2]/span/span").click()
time.sleep(3)