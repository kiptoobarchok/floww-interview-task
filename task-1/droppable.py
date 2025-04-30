from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/droppable')


source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
ActionChains(driver).drag_and_drop(source, target).perform()
time.sleep(5)

driver.quit()