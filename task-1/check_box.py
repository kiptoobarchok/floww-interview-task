from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#set up chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the checkbox page
driver.get('https://demoqa.com/checkbox')
time.sleep(2)


# click the "home" checkbox

check_box = driver.find_element(By.XPATH,  '//span[@class="rct-checkbox"]')
check_box.click()


# click button confirmation
print("Check_box clicked successfully!!")

# wait time
time.sleep(3)

driver.quit()