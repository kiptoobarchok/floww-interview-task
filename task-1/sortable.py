from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/sortable')

time.sleep(2)

items = driver.find_elements(By.CSS_SELECTOR, ".vertical-list-container .list-group-item")
ActionChains(driver).click_and_hold(items[5]).move_to_element(items[0]).release().perform()
time.sleep(3)

driver.quit()