import subprocess
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
subprocess.Popen(chrome_path)

# Set Chrome options to connect to the existing instance
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

# Start the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Find an element using the desired method (e.g., by ID)
option = driver.find_elements(By.XPATH, "//span[contains(text(), 'Majid Ata')]")

# element = driver.find_element_by_id("element_id")

# Perform actions on the element
element.click()


times.sleep(2)
# option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

