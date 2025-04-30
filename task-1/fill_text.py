from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2) 

# Remove ad overlay 
try:
    driver.execute_script("""
        let ad = document.querySelector("#adplus-anchor");
        if (ad) { ad.remove(); }
    """)
except:
    pass

# Fill in the form fields
driver.find_element(By.ID, "userName").send_keys("John Doe")
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("123 Demo Street, Nairobi")
driver.find_element(By.ID, "permanentAddress").send_keys("456 Permanent Lane, Nakuru")

# Scroll into view and click Submit
submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
time.sleep(1)
submit_btn.click()

# Optional: Wait to see the output
time.sleep(3)

# confirm succes
print("data added to text field successfully")

# Close browser
driver.quit()
