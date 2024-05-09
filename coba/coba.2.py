from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options with remote debugging address
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")

# Connect to the existing Chrome browser
driver = webdriver.Chrome(options=chrome_options)

# Use the driver to interact with the opened Chrome browser
driver.get("https://www.youtube.com")
# Add more actions as needed

# Close the driver when done
# driver.quit()