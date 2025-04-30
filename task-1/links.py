from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/links")
driver.maximize_window()
time.sleep(2)

# Remove potential ad overlay
try:
    driver.execute_script("""
        let ad = document.querySelector("#adplus-anchor");
        if (ad) { ad.remove(); }
    """)
except:
    pass

# Click on the "Home" link
home_link = driver.find_element(By.ID, "simpleLink")
home_link.click()

time.sleep(3)

# Close the browser
driver.quit()
