from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/dragabble')

# print("✅ WebDriver is working correctly!")


drag_element = driver.find_element(By.ID, "dragBox")
ActionChains(driver).drag_and_drop_by_offset(drag_element, 100, 100).perform()

time.sleep(3)

driver.quit()