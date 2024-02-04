from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

book = input("book name: ")
url = f"https://www.google.com/search?q={book}+filetype%3Apdf"

driver.get(url)
time.sleep(5)

# Find all <a> tags with the specific jsname attribute
elements = driver.find_elements(By.CSS_SELECTOR, 'a[jsname="UWckNb"]')

# Iterate through all elements and print their href attributes
for element in elements:
    url_link = element.get_attribute('href')
    print(url_link)

driver.quit()
