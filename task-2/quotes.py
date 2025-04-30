from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# set up firefox driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://quotes.toscrape.com/')


#give time page to load
time.sleep(2)

#find all quote elements
quotes = driver.find_elements(By.CLASS_NAME, "quote")

print(driver.title)

five_quotes = []
quotes = driver.find_elements(By.CLASS_NAME, "quote")[:5]
time.sleep(2)

# loop through the quotes
for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    print(f"{text} - {author}")

    # save quotes to a list
    five_quotes.append({
        "text": text,
        "author": author
    })



driver.quit()

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(five_quotes, f, indent=4, ensure_ascii=False)

print(f"Saved {len(five_quotes)} quotes to \'quotes.json\' file")
