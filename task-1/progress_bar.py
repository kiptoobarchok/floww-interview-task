from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/progress-bar')

start_button = driver.find_element(By.ID, "startStopButton")
start_button.click()
time.sleep(5) 
start_button.click() 

driver.quit()
