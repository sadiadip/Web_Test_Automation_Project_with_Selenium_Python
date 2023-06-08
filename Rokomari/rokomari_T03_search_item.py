from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.rokomari.com/login")
print(driver.title)
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/div[3]/div/div[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='js--login-form']/div[2]/div/div/input[2]").send_keys("01xxxxxxxxx")
driver.find_element(By.ID,"js--btn-next").click()
time.sleep(1)
driver.find_element(By.NAME,"j_password").send_keys("1234wea")
driver.find_element(By.XPATH,"//*[@id='login-form']/button").click()
time.sleep(1)
driver.find_element(By.ID,"js--search").send_keys("zafor iqbal")
driver.find_element(By.XPATH,"//*[@id='js--main-header']/div/div/div[2]/div/form/div/div[2]/button/i").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='js--browse-sidebar-form']/div[1]/div[2]/div[2]/div/label").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='js--browse-sidebar-form']/div[2]/div[2]/div[2]/div/label").click()
time.sleep(3)