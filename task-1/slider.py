from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/slider')
time.sleep(2)

slider = driver.find_element(By.CLASS_NAME, "range-slider")
ActionChains(driver).drag_and_drop_by_offset(slider, 60, 0).perform()


time.sleep(5)

driver.quit()
