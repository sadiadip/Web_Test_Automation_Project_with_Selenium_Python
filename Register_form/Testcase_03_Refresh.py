from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="Webdriver/chromedriver.exe")

driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
print(driver.title)

driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[1]/div[1]/input").send_keys("Sadia")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[1]/div[2]/input").send_keys("Dip")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[2]/div/textarea").send_keys("Dhaka")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='eid']/input").send_keys("wxy@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[4]/div/input").send_keys("011111111111")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[5]/div/label[2]/input").click()
time.sleep(2)
driver.find_element(By.ID,"checkbox2").click()
time.sleep(2)
driver.find_element(By.ID,"checkbox3").click()
time.sleep(2)

dropdown = Select(driver.find_element(By.ID,"Skills"))
dropdown.select_by_value("Python")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[10]/div/span/span[1]/span/span[2]/b").click()
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Bangladesh")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
time.sleep(2)
dropdown = Select(driver.find_element(By.ID,"yearbox"))
dropdown.select_by_value("1998")
time.sleep(2)

dropdown = Select(driver.find_element(By.XPATH,"//*[@id='basicBootstrapForm']/div[11]/div[2]/select"))
dropdown.select_by_index(1)
time.sleep(2)

dropdown = Select(driver.find_element(By.ID,"daybox"))
dropdown.select_by_index("16")
time.sleep(2)
driver.find_element(By.ID, "imagesrc").send_keys("G:\\abc.PNG")
time.sleep(2)
driver.find_element(By.ID,"firstpassword").send_keys("12345678")
time.sleep(2)
driver.find_element(By.ID,"secondpassword").send_keys("12345678")
time.sleep(2)
driver.find_element(By.ID,"Button1").click()
time.sleep(4)