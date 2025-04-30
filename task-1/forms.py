from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Setup
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Remove ads
try:
    driver.execute_script("document.querySelector('#fixedban').remove();")
    driver.execute_script("document.querySelector('footer').remove();")
except:
    pass

# Fill required fields
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.ID, "userNumber").send_keys("1234567890")

# Date of Birth
driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1995")
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("May")
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='15']").click()

# Subject
subject_input = driver.find_element(By.ID, "subjectsInput")
subject_input.send_keys("Maths")
subject_input.send_keys(Keys.ENTER)

# Hobbies
driver.find_element(By.XPATH, "//label[text()='Reading']").click()

# Upload a file
sample_path = os.path.abspath("sample.jpg")  # Put your sample.jpg in the same folder
driver.find_element(By.ID, "uploadPicture").send_keys(sample_path)

# Current Address
driver.find_element(By.ID, "currentAddress").send_keys("123  Street, nakuru")

# State and City
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)
driver.find_element(By.ID, "react-select-4-input").send_keys("Nairobi")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

# Submit
driver.find_element(By.ID, "submit").click()

# Wait and print confirmation
wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
print("Form submitted successfully.")

time.sleep(3)
driver.quit()
