from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://member.daraz.com.bd/user/login?spm=a2a0e.home.header.d5.735212f7ydGWC5&redirect=https%3A%2F%2Fwww.daraz.com.bd%2F")
print(driver.title)

driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[1]/div[1]/input").send_keys("01xxxxxxxxx")
driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[1]/div[2]/input").send_keys("123@23")
driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[2]/div[1]/button").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[1]/div[1]/input").send_keys("01xxxxxxxxx")
driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[1]/div[2]/input").send_keys("123@23")
driver.find_element(By.XPATH,"//*[@id='container']/div/div[2]/form/div/div[2]/div[1]/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='topActionTrack']/span").click()
time.sleep(2)
driver.find_element(By.ID,'topActionTrackEmail').click()
driver.find_element(By.ID,'topActionTrackEmail').send_keys("xyz@gmail.com")
driver.find_element(By.ID,'topActionTrackOrderNumber').click()
driver.find_element(By.ID,'topActionTrackOrderNumber').send_keys("12345")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='topActionTrackForm']/div[2]/button/i").click()
