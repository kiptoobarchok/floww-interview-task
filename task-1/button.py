from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
actions = ActionChains(driver)
time.sleep(2)

# Remove ad if present
try:
    driver.execute_script("""
        let ad = document.querySelector("#adplus-anchor");
        if (ad) { ad.remove(); }
    """)
except:
    pass

# 1. Double Click
double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
actions.double_click(double_click_btn).perform()
time.sleep(1)

# 2. Right Click
right_click_btn = driver.find_element(By.ID, "rightClickBtn")
actions.context_click(right_click_btn).perform()
time.sleep(1)

# 3. Dynamic Click (third button with no ID, use XPath)
dynamic_click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
dynamic_click_btn.click()
time.sleep(2)


# Cleanup
driver.quit()
