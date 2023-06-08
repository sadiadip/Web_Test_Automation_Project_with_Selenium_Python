from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")

driver.maximize_window()

driver.get("https://www.rokomari.com/login")
print(driver.title)
driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/div[3]/div/div[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='js--login-form']/div[2]/div/div/input[2]").send_keys("01521437957")
driver.find_element(By.ID,"js--btn-next").click()
time.sleep(1)
driver.find_element(By.NAME,"j_password").send_keys("Dip12345")
driver.find_element(By.XPATH,"//*[@id='login-form']/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/footer/div[1]/div/div[2]/div/div[1]/div[3]/ul/li[1]/a").click()
time.sleep(4)
dropdown = Select(driver.find_element(By.ID, "subject"))
dropdown.select_by_index(3)
time.sleep(5)

