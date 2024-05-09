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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScnBSllHxNb307IxbD-L2jK5cN4_T0KraE-kW56PPNRIOikLQ/viewform?usp=sf_link")

jelek = 5
baik = 45

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        usia = random.choice([0,1,2,3])
        domisili = random.choice([4,4,4,5,6,7])

        radiobuttons[usia].click()
        radiobuttons[domisili].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        if jelek != 0 and baik != 0 :
            time.sleep(2)
            pilih = random.choice([1,2])
            if pilih == 1:
                s1 = random.choice([0,1])
                s2 = random.choice([3,3,3,3,3,4])
                if s2 == 4:
                    s3 = random.choice([6,7])
                    s4 = random.choice([8,9,9,9])
                else :
                    s3 = random.choice([5,6])
                    s4 = 8

                radiobuttons[s1].click()
                radiobuttons[s2].click()
                radiobuttons[s3].click()
                radiobuttons[s4].click()

                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

                time.sleep(3)
                radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

                style = random.choice([2,3,4,4,4,5,5,5])
                applys = random.choice([6,7])
                bahan = random.choice([8,8,8,9,9,9,10])
                p1 = random.choice([12,13])
                p2 = random.choice([14,14,14,15,15,15,16])
                p3 = random.choice([17,18,19,20])
                p4 = random.choice([21,22,23,24])

                radiobuttons[0].click()
                radiobuttons[style].click()
                radiobuttons[applys].click()
                radiobuttons[bahan].click()
                radiobuttons[p1].click()
                radiobuttons[p2].click()
                radiobuttons[p3].click()
                radiobuttons[p4].click()

                baik -= 1
            else:
                s1 = random.choice([1,2])
                s2 = random.choice([3,4])
                if s2 == 4:
                    s3 = random.choice([6,7])
                    s4 = random.choice([8,9,9,9])
                else :
                    s3 = random.choice([5,6])
                    s4 = 8

                radiobuttons[s1].click()
                radiobuttons[s2].click()
                radiobuttons[s3].click()
                radiobuttons[s4].click()

                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

                time.sleep(3)
                radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

                p5 = random.choice([0,1])
                style = random.choice([2,3,4,4,4,5,5,5])
                applys = random.choice([6,7])
                bahan = random.choice([9,10])
                p1 = random.choice([12,13])
                p2 = random.choice([15,16])
                p3 = random.choice([17,18])
                p4 = random.choice([21,22])

                radiobuttons[p5].click()
                radiobuttons[style].click()
                radiobuttons[applys].click()
                radiobuttons[bahan].click()
                radiobuttons[p1].click()
                radiobuttons[p2].click()
                radiobuttons[p3].click()
                radiobuttons[p4].click()

                jelek -= 1
        elif jelek != 0 and baik == 0: 
            s1 = random.choice([1,2])
            s2 = random.choice([3,4])
            if s2 == 4:
                s3 = random.choice([6,7])
                s4 = random.choice([8,9,9,9])
            else :
                s3 = random.choice([5,6])
                s4 = 8

            radiobuttons[s1].click()
            radiobuttons[s2].click()
            radiobuttons[s3].click()
            radiobuttons[s4].click()

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            p5 = random.choice([0,1])
            style = random.choice([2,3,4,4,4,5,5,5])
            applys = random.choice([6,7])
            bahan = random.choice([9,10])
            p1 = random.choice([12,13])
            p2 = random.choice([15,16])
            p3 = random.choice([17,18])
            p4 = random.choice([21,22])

            radiobuttons[p5].click()
            radiobuttons[style].click()
            radiobuttons[applys].click()
            radiobuttons[bahan].click()
            radiobuttons[p1].click()
            radiobuttons[p2].click()
            radiobuttons[p3].click()
            radiobuttons[p4].click()

            jelek -= 1
        elif jelek == 0 and baik != 0: 
            s1 = random.choice([0,1])
            s2 = random.choice([3,3,3,3,3,4])
            if s2 == 4:
                s3 = random.choice([6,7])
                s4 = random.choice([8,9,9,9])
            else :
                s3 = random.choice([5,6])
                s4 = 8

            radiobuttons[s1].click()
            radiobuttons[s2].click()
            radiobuttons[s3].click()
            radiobuttons[s4].click()

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            style = random.choice([2,3,4,4,4,5,5,5])
            applys = random.choice([6,7])
            bahan = random.choice([8,8,8,9,9,9,10])
            p1 = random.choice([12,13])
            p2 = random.choice([14,14,14,15,15,15,16])
            p3 = random.choice([17,18,19,20])
            p4 = random.choice([21,22,23,24])

            radiobuttons[0].click()
            radiobuttons[style].click()
            radiobuttons[applys].click()
            radiobuttons[bahan].click()
            radiobuttons[p1].click()
            radiobuttons[p2].click()
            radiobuttons[p3].click()
            radiobuttons[p4].click()

            baik -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScnBSllHxNb307IxbD-L2jK5cN4_T0KraE-kW56PPNRIOikLQ/viewform?usp=sf_link")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")
        print("baik  : " + str(baik))
        print("jelek : " + str(jelek))
        print("style : " + str(style))

        times-=1
        print("times : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()