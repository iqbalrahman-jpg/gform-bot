from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScssvIqvNjNZkN-mt2lHM17v8HSwcfL5IfjZZN17xZIR-LTEQ/viewform?usp=sf_link")

times = 75
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        usia = random.choice([3,3,4,4,5,6])

        time.sleep(2)
        if usia == 3 :
            jabatan = random.choice([10,14,15,16])
        elif usia == 4:
            jabatan = random.choice([7,8,9,10,12,13,14,15,16,17])
        elif usia == 5:
            jabatan = random.choice([7,8,9,10,11,12,13,14,16,17])
        else :
            jabatan = random.choice([7,8,9,10,11,12,13,17])

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()
        radiobuttons[usia].click()
        radiobuttons[jabatan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 17
        while soal:
            time.sleep(2)
            if p == 35:
                s1 = random.choice([p,p+1,p+2])
                testcheck[s1].click()
            elif p == 50:
                s1 = random.choice([p+2,p+3])
                testcheck[s1].click()
            if p == 55:
                s1 = random.choice([p,p+1,p+2])
                testcheck[s1].click()
            else:
                s1 = random.choice([p,p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
                testcheck[s1].click()

            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 8
        while soal:
            time.sleep(2)
            if p == 5:
                s1 = random.choice([p,p+1])
                testcheck[s1].click()
            else:
                s1 = random.choice([p,p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
                testcheck[s1].click()

            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScssvIqvNjNZkN-mt2lHM17v8HSwcfL5IfjZZN17xZIR-LTEQ/viewform?usp=sf_link")

        index+=1
        print("==================")
        # print("  : " + str())
        # print("")
        
        times-=1
        print("index  : " + str(index))
        print("times  : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()