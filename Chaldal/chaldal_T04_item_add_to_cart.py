from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")

driver.maximize_window()

driver.get("https://chaldal.com/")
print(driver.title)

driver.find_element(By.XPATH,"//*[@id='page']/div/div[3]/div/div[1]/div[1]/div[4]/button").click()
driver.find_element(By.XPATH,"//*[@id='page']/div/div[1]/div/div/div/div[2]/div/form/div[1]/div/div[1]/input").send_keys("01xxxxxxxxx")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='page']/div/div[1]/div/div/div/div[2]/div/form/div[3]/button").click()
time.sleep(1)
driver.find_element(By.NAME,"search_term_string").click()
time.sleep(1)
driver.find_element(By.NAME,"search_term_string").send_keys("egg")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='page']/div/div[6]/section/div/div/div/div/section/div[3]/div[2]/div[1]/div/section/p").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='page']/div/div[2]/div/div/section/div[1]").click()
time.sleep(1)
