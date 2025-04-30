from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/radio-button')

# print("✅ WebDriver is working correctly!")

# click yes on the radio button
yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
yes.click

time.sleep(5)

print("(display) : You have clicked \'Yes\' : You like the site")

# close browser
driver.quit()
