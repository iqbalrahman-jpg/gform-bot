from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import random
import time

firefox_options = Options()
firefox_options.add_argument('-headless')
firefox_options.add_argument('--disable-extensions')
firefox_options.add_argument('--disable-popup-blocking')
firefox_options.add_argument('--profile-directory=Default')
firefox_options.add_argument('--disable-plugins-discovery')
firefox_options.add_argument('--disable-save-password-bubble')
firefox_options.add_argument('--disable-blink-features=AutomationControlled')

firefox_driver_path = '/geckodriver' 
firefox_service = Service(executable_path=firefox_driver_path)
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

driver.get("https://forms.gle/P2URQH7hBU9wMRsUA")
times = 1

driver.implicitly_wait(10)
time.sleep(5)

try:
    while times:
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", "docssharedWizToggleLabeledContainer")
        # textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
        # testcheck = driver.find_elements_by_class_name("freebirdMaterialScalecontentColumn")
        checkboxes = driver.find_elements("css selector", "docssharedWizToggleLabeledContainer")

        if len(radiobuttons) < 5:
            print("Error: Not enough radio buttons on the page")
            print(len(radiobuttons))
            break

        check1 = random.choice([0,1,2,3,4])
        radiobuttons[check1].click()

        check2 = random.choice([5,6,7,8,9])
        radiobuttons[check2].click()

        c1 = random.choice([0,1])
        checkboxes[c1].click()
        c2 = random.choice([2,3])
        checkboxes[c2].click()
        driver.implicitly_wait(4)
        checkboxes[4].click()
        driver.implicitly_wait(7)
        driver.find_element_by_xpath("//*[contains(text(), 'Kirim')]").click()
        driver.implicitly_wait(4)
        driver.get("https://forms.gle/P2URQH7hBU9wMRsUA")
        times-=1
        print(times)
finally:
	driver.quit()	



