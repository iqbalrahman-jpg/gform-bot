from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://bit.ly/ResearchWork-lifeBalanceAkuntanPublik")

times = 20
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        kelamin = random.choice([0,1])
        umur = random.choice([2,3,4,5,6,7])

        if umur == 2 or umur == 3:
            time.sleep(2)
            pernikahan = 9
            kerja = random.choice([10,11])
            jabatan = random.choice([17,18])
        else :
            time.sleep(2)
            pernikahan = random.choice([8,9])
            kerja = random.choice([10,11,12,13,14])
            if kerja == 10 or kerja == 11:
                jabatan = random.choice([17,18])
            elif kerja == 12 or kerja == 13:
                jabatan = random.choice([17,18,18,18,19,19,19,20,21])
            else :
                jabatan = random.choice([18,19,19,20,20,20,21])

        kantor = random.choice([15,15,15,16])

        radiobuttons[kelamin].click()
        radiobuttons[umur].click()
        radiobuttons[pernikahan].click()
        radiobuttons[kerja].click()
        radiobuttons[kantor].click()
        radiobuttons[jabatan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        if jabatan == 17 or jabatan == 18:
            wfa1 = random.choice([1,2])
            wfa2 = random.choice([4,5])
            wfa3 = random.choice([7,8])
        elif jabatan == 19:
            wfa1 = random.choice([0,1,2])
            wfa2 = random.choice([3,4,5])
            wfa3 = random.choice([6,7,8])
        elif jabatan == 20:
            wfa1 = random.choice([1])
            wfa2 = random.choice([4])
            wfa3 = random.choice([7])
        else :
            wfa1 = random.choice([0,1])
            wfa2 = random.choice([3,4])
            wfa3 = random.choice([6,7])

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[wfa1].click()
        radiobuttons[wfa2].click()
        radiobuttons[wfa3].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        mp1 = random.choice([0,0,1,1,2,3,3,4,4])
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        #tidak 
        if mp1 == 0 or mp1 == 1:
            p1 = 0
            soal = 5
            while soal:
                s1 = random.choice([p1,p1,p1+1,p1+1,p1+2])
                testcheck[s1].click()
                soal -= 1
                p1 += 5
        #ya
        elif mp1 == 3 or mp1 == 4:
            p1 = 2
            soal = 5
            while soal:
                s1 = random.choice([p1,p1+1,p1+1,p1+2,p1+2])
                testcheck[s1].click()
                soal -= 1
                p1 += 5
        #netral
        else :
            p1 = 0
            soal = 5
            while soal:
                s1 = random.choice([p1,p1+1,p1+2,p1+3,p1+4])
                testcheck[s1].click()
                soal -= 1
                p1 += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if mp1 == 0 or mp1 == 1:
            p1 = 0
            soal = 3
            while soal:
                s1 = random.choice([p1,p1,p1+1,p1+1,p1+2])
                testcheck[s1].click()
                soal -= 1
                p1 += 5
        #ya
        elif mp1 == 3 or mp1 == 4:
            p1 = 2
            soal = 3
            while soal:
                s1 = random.choice([p1,p1+1,p1+1,p1+2,p1+2])
                testcheck[s1].click()
                soal -= 1
                p1 += 5
        #netral
        else :
            p1 = 0
            soal = 3
            while soal:
                s1 = random.choice([p1,p1+1,p1+2,p1+3,p1+4])
                testcheck[s1].click()
                soal -= 1
                p1 += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        kkk1 = random.choice([0,1,2,3,4])
        kkk4 = kkk1 + 15

        if kkk1 == 0 or kkk1 == 2:
            kkk2 = random.choice([5,6])
            kkk3 = random.choice([10,11])
        elif kkk1 == 3 or kkk1 == 4:
            kkk2 = random.choice([8,9])
            kkk3 = random.choice([13,14])
        else:
            kkk2 = random.choice([5,6,7,8,9])
            if kkk2 == 5 or kkk2 == 6:
                kkk3 = random.choice([10,11,12])
            else :
                kkk3 = random.choice([12,13,14])

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        testcheck[kkk1].click()
        testcheck[kkk2].click()
        testcheck[kkk3].click()
        testcheck[kkk4].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        soal = 11
        while soal:
            s1 = random.choice([p1,p1+1,p1+2,p1+3,p1+3,p1+4,p1+4])
            testcheck[s1].click()
            soal -= 1
            p1 += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://bit.ly/ResearchWork-lifeBalanceAkuntanPublik")

        index+=1
        print("==================")
        print("index : " + str(index))
        

        times-=1
        print("times : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()