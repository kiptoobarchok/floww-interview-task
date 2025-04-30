from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/auto-complete')
time.sleep(3)
# print("✅ WebDriver is working correctly!")


# multicolour input

inputs = driver.find_element(By.ID, "autoCompleteMultipleInput")

for color in ["black", "grey", "white"]:
    inputs.send_keys(color)
    time.sleep(3)
    inputs.send_keys(Keys.ENTER)


# input single color
single_color = driver.find_element(By.ID, "autoCompleteSingleInput")
single_color.send_keys("black")
time.sleep(3)
single_color.send_keys(Keys.ENTER)


time.sleep(5)

driver.quit()
