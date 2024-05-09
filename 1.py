from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Firefox()
driver.get("https://forms.gle/PQLgTzymUaygEViM8")
times = 4

# time.sleep(5)

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")                          #kebawah
        # textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")    #isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")    #kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")    #checkbox

        if len(testcheck) < 5:
            print("Error: Not enough radio buttons on the page")
            print(len(testcheck))
            break

        temp = random.choice([1,2,3,4])
        if temp != 2 :
            checkboxes[0].click()
            driver.implicitly_wait(4)

        random_item = random.sample([1,2,3,4], temp)
        
        for i in random_item :
           checkboxes[i].click()

        driver.implicitly_wait(4)
        radio = random.choice([1,2,3])
        radiobuttons[radio].click()

        p1 = 1
        p2 = 2
        p3 = 3
        p4 = 4
        bag1 = 17
        while bag1 :
            soal = 2
            check1 = 0
            while soal :
                if check1 == 0 :
                    check1 = random.choice([p1,p2,p3,p4])
                    testcheck[check1].click()
                    p1+=5
                    p2+=5
                    p3+=5
                    p4+=5
                    soal -=1
                elif check1 == (p1-5) :
                    check1 = random.choice([p1,p2])
                    testcheck[check1].click()
                    p1+=5
                    p2+=5
                    p3+=5
                    p4+=5
                    soal -=1
                elif check1 == (p2-5) :
                    check1 = random.choice([p1,p2,p3])
                    testcheck[check1].click()
                    p1+=5
                    p2+=5
                    p3+=5
                    p4+=5
                    soal -=1
                else :
                    check1 = random.choice([p3,p4])
                    testcheck[check1].click()
                    p1+=5
                    p2+=5
                    p3+=5
                    p4+=5
                    soal -=1
            bag1 -= 1


        # driver.find_elements("css selector", ".e19J0b").click()
        # driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # driver.find_element_by_xpath("//*[contains(text(), 'Kirim')]").click()



        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "l4V7wb"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/PQLgTzymUaygEViM8")
        times-=1
        print(times)
finally:
	driver.quit()	
