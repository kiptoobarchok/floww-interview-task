from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")
driver.maximize_window()
time.sleep(2)

# Remove ad that may block UI
try:
    driver.execute_script("""
        let ad = document.querySelector("#adplus-anchor");
        if (ad) { ad.remove(); }
    """)
except:
    pass

# 1. Click "Add" to add a new user
driver.find_element(By.ID, "addNewRecordButton").click()
time.sleep(1)

# 2. Fill in user data
driver.find_element(By.ID, "firstName").send_keys("kiptoo")
driver.find_element(By.ID, "lastName").send_keys("caleb")
driver.find_element(By.ID, "userEmail").send_keys("caleb@demo.com")
driver.find_element(By.ID, "age").send_keys("30")
driver.find_element(By.ID, "salary").send_keys("60000")
driver.find_element(By.ID, "department").send_keys("IT")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# 3. Locate and click Edit button for the new user (by unique email)
rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
for row in rows:
    if "caleb@demo.com" in row.text:
        edit_button = row.find_element(By.CSS_SELECTOR, "span[title='Edit']")
        edit_button.click()
        break

time.sleep(1)
# Clear and update salary
salary_input = driver.find_element(By.ID, "salary")
salary_input.clear()
salary_input.send_keys("100000")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# 4. Locate and delete the user
rows = driver.find_elements(By.CLASS_NAME, "rt-tr-group")
for row in rows:
    if "alice@example.com" in row.text:
        delete_button = row.find_element(By.CSS_SELECTOR, "span[title='Delete']")
        delete_button.click()
        break

time.sleep(2)
driver.quit()

print("action items : add user, update field and delete user done.")
