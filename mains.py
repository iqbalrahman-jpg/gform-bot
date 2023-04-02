from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Firefox()
driver.get("https://forms.gle/P2URQH7hBU9wMRsUA")
times = 5

# time.sleep(5)

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")
        # textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
        # testcheck = driver.find_elements_by_class_name("freebirdMaterialScalecontentColumn")
        checkboxes = driver.find_elements("css selector", ".uHMk6b")

        if len(radiobuttons) < 5:
            print("Error: Not enough radio buttons on the page")
            print(len(radiobuttons))
            break

        check1 = random.choice([0,1,2,3,4])
        radiobuttons[check1].click()

        c1 = random.choice([0,1])
        checkboxes[c1].click()
        c2 = random.choice([2,3])
        checkboxes[c2].click()
        driver.implicitly_wait(4)
        checkboxes[4].click()
        driver.implicitly_wait(7)

        check2 = random.choice([5,6,7,8,9])
        radiobuttons[check2].click()
        
        # driver.find_elements("css selector", ".e19J0b").click()
        # driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # driver.find_element_by_xpath("//*[contains(text(), 'Kirim')]").click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "l4V7wb"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/P2URQH7hBU9wMRsUA")
        times-=1
        print(times)
finally:
	driver.quit()	



