from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")

driver.maximize_window()

driver.get("https://chaldal.com/")
print(driver.title)


driver.find_element(By.NAME,"search_term_string").click()
time.sleep(1)
driver.find_element(By.NAME,"search_term_string").send_keys("egg")
time.sleep(1)



