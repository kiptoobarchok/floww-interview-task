from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")
driver.maximize_window()
time.sleep(2)

# Remove overlay ad if present
try:
    driver.execute_script("""
        let ad = document.querySelector("#adplus-anchor");
        if (ad) { ad.remove(); }
    """)
except:
    pass

# 1. Switch to first frame and get text
driver.switch_to.frame("frame1")
frame1_text = driver.find_element(By.ID, "sampleHeading").text
print("Frame 1 Text:", frame1_text)

# 2. Switch back to main document
driver.switch_to.default_content()

# 3. Switch to second frame and get text
driver.switch_to.frame("frame2")
frame2_text = driver.find_element(By.ID, "sampleHeading").text
print("Frame 2 Text:", frame2_text)

# Cleanup
driver.quit()
