from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/select-menu')


select_value = driver.find_element(By.ID, "withOptGroup")
select_value.click()
time.sleep(1)

option = driver.find_element(By.XPATH, '//div[text()="Group 1, option 2"]')
option.click()

time.sleep(5)

driver.quit()
