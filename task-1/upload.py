import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the download directory
download_dir = os.path.abspath("downloads")
os.makedirs(download_dir, exist_ok=True)

# Configure Chrome options to auto-download without prompt
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_dir}
chrome_options.add_experimental_option("prefs", prefs)

# Start WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demoqa.com/upload-download")
driver.maximize_window()
time.sleep(2)

# Remove ad 
try:
    driver.execute_script("""
        let ad = document.querySelector("#adplus-anchor");
        if (ad) { ad.remove(); }
    """)
except:
    pass

# 1. Click Download Button
download_button = driver.find_element(By.ID, "downloadButton")
download_button.click()
time.sleep(3)  # Wait for file to download

# Find the downloaded file
downloaded_file = None
for filename in os.listdir(download_dir):
    if filename.endswith(".jpeg"):  # Default file is "sampleFile.jpeg"
        downloaded_file = os.path.join(download_dir, filename)
        break

if downloaded_file and os.path.exists(downloaded_file):
    print("Downloaded:", downloaded_file)

    # 2. Upload the same file
    upload_input = driver.find_element(By.ID, "uploadFile")
    upload_input.send_keys(downloaded_file)
    time.sleep(2)
else:
    print("File not downloaded.")

# Optional: close browser
driver.quit()
