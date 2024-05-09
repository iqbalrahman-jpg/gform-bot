from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import random

profil = ["Default"]

page = [
    [
        [1,2,1,4,2,1,1,2,2,1,1,1,1,1,1,1,2,4,1,2,2,1,3,1,2,1,1,1,3,2,2,2,1,1,2,2,2,1,2,2,2,1,1,1,2,2,1,2,1,2,3,4,2,2,2,2,2,2,1,2,2,1,1,2,1,2,1,1,1,3,1,2,1,2,1,1,2,2,1,1,2,1,1,2,1,1,2,1,2,1,3,2,1,1,4,2,1,2,1,2],
        [2,2,1,3,2,2,1,1,1,2,2,2,1,2,1,1,3,3,2,2,2,2,2,2,3,1,1,1,4,1,2,1,2,1,1,2,1,1,3,2,2,1,2,1,2,1,1,3,2,2,2,3,2,1,1,1,3,1,1,3,1,2,2,3,2,3,2,1,1,2,2,2,1,1,1,2,3,2,2,2,2,1,2,2,2,2,3,2,3,1,4,2,1,2,3,1,1,1,2,3],
        [1,1,1,4,2,2,1,1,3,1,2,2,1,2,1,1,2,4,1,2,2,1,3,2,2,1,1,1,3,1,2,1,2,1,1,2,2,1,2,1,2,1,1,1,2,1,1,2,1,2,3,4,1,1,3,2,3,3,1,2,2,1,2,2,2,3,1,1,1,3,1,2,1,1,1,1,2,2,1,2,1,1,2,2,1,1,3,1,3,1,3,2,1,1,4,3,1,1,1,2],
        [2,2,1,4,2,2,1,1,3,1,2,2,1,3,1,1,2,4,1,2,3,2,2,2,3,1,1,1,4,1,2,2,2,1,2,2,2,1,2,2,2,1,1,1,2,2,1,3,1,2,2,4,2,1,3,2,2,3,1,3,2,1,2,2,2,2,2,1,1,2,1,2,1,1,1,2,2,3,2,2,2,1,3,2,1,1,2,1,2,1,4,3,1,2,4,3,1,2,2,3],
        [2,2,1,3,2,2,1,2,2,2,2,2,1,3,1,1,3,3,1,2,3,2,2,2,2,1,1,1,4,2,2,1,2,1,1,2,3,1,3,2,2,1,2,1,2,1,1,2,1,2,2,3,2,2,2,3,2,2,1,2,3,2,2,3,2,2,2,1,1,2,2,2,1,2,1,2,3,3,2,2,2,1,3,2,1,1,2,2,2,1,4,3,2,2,3,2,1,1,2,2],
    ],[   
        [1,2,1,4,2,2,1,1,1,1,2,2,2,3,1,2,2,4,1,2,2,1,2,2,2,1,1,1,4,1,2,1,2,1,1,2,2,1,2,2,2,1,2,1,2,1,1,2,1,2,2,4,2,1,1,2,3,1,1,2,2,2,2,2,2,3,1,2,1,2,2,2,2,1,1,2,2,2,2,2,2,1,3,2,1,1,3,1,3,1,4,2,1,2,4,1,1,1,2,2],
        [1,2,1,3,3,2,1,2,2,1,1,1,1,2,1,1,3,3,2,3,2,1,3,2,3,1,1,1,3,2,2,3,1,1,3,3,3,2,3,2,3,1,2,2,3,3,1,3,2,2,3,3,2,2,2,3,2,2,1,3,3,2,2,3,2,2,1,1,1,3,2,2,1,2,1,2,3,2,2,1,2,2,2,3,2,2,2,1,2,1,3,2,2,2,3,2,1,3,2,3],
        [1,2,1,2,2,2,2,2,1,2,2,2,1,2,1,1,2,2,2,2,2,1,2,2,2,1,1,1,4,2,2,1,2,2,1,2,2,1,2,2,2,2,2,1,2,1,1,2,2,2,2,2,2,2,1,2,3,1,1,2,2,2,2,2,2,3,1,1,1,2,2,2,1,2,1,2,2,2,2,2,2,1,2,2,2,2,3,2,3,1,4,2,2,2,2,1,2,1,2,2],
        [1,1,1,4,2,2,1,1,3,1,2,2,1,2,1,1,3,4,1,2,2,1,3,2,2,1,1,1,3,1,2,1,2,1,1,2,2,1,3,1,2,1,1,1,2,1,1,2,1,2,3,4,1,1,3,2,2,3,1,2,2,1,2,3,2,2,1,1,1,3,1,2,1,1,1,1,3,2,1,2,1,1,2,2,1,1,2,1,2,1,3,2,1,1,4,3,1,1,1,2],
    ],[   
        [2,1,1,3,2,2,1,1,2,2,2,2,2,3,1,2,2,3,2,2,2,2,2,2,2,1,1,1,4,1,2,2,2,1,2,2,1,2,2,1,2,1,1,2,2,2,1,2,2,2,2,3,1,1,2,1,2,2,1,2,1,1,2,2,2,2,2,2,1,2,1,2,2,1,1,2,2,2,2,2,1,2,3,2,2,2,2,2,2,1,4,2,2,2,3,2,1,2,2,2],
        [1,3,1,4,3,2,1,2,2,1,3,3,1,2,1,1,3,4,1,2,1,1,1,2,3,1,1,1,4,2,2,2,3,1,2,3,2,1,3,3,2,1,1,1,3,2,1,3,1,2,1,4,3,2,2,2,2,2,1,3,2,1,2,3,2,2,1,1,1,1,1,2,1,2,1,2,3,1,2,3,3,1,2,2,1,1,2,1,2,1,4,1,1,2,4,2,1,2,2,3],
        [2,1,1,3,2,2,1,1,2,2,1,1,1,2,1,1,2,3,1,2,3,2,2,2,2,1,1,1,3,1,2,1,1,1,1,2,1,1,2,1,2,1,1,1,2,1,1,2,1,2,2,3,1,1,2,1,2,2,1,2,1,1,2,2,2,2,2,1,1,2,1,2,1,1,1,1,2,3,1,1,1,1,2,2,1,1,2,2,2,1,3,3,1,1,3,2,1,1,1,2],
        [2,2,1,4,2,1,1,1,1,1,3,3,1,1,1,1,3,4,1,2,2,2,3,1,3,1,1,1,4,1,2,2,3,1,2,2,2,2,3,2,2,1,2,2,2,2,1,3,1,2,3,4,2,1,1,2,3,1,1,3,2,2,1,3,1,3,2,1,1,3,2,2,1,1,1,1,3,2,1,3,2,2,1,2,1,1,3,1,3,1,4,2,2,1,4,1,1,2,1,3],
        [1,2,1,4,2,2,1,1,1,1,2,2,2,3,1,2,2,4,1,2,2,1,2,2,2,1,1,1,4,1,2,1,2,1,1,2,2,1,2,2,2,1,2,1,2,1,1,2,1,2,2,4,2,1,1,2,3,1,1,2,2,2,2,2,2,3,1,2,1,2,2,2,2,1,1,2,2,2,2,2,2,1,3,2,1,1,3,1,3,1,4,2,1,2,4,1,1,1,2,2],
    ],[   
        [1,2,1,4,2,2,1,1,1,1,2,2,2,3,1,2,2,4,1,2,2,1,2,2,2,1,1,1,4,1,2,1,2,1,1,2,2,1,2,2,2,1,2,1,2,1,1,2,1,2,2,4,2,1,1,2,3,1,1,2,2,2,2,2,2,3,1,2,1,2,2,2,2,1,1,2,2,2,2,2,2,1,3,2,1,1,3,1,3,1,4,2,1,2,4,1,1,1,2,2],
        [2,2,1,3,2,2,1,1,1,2,2,2,1,2,1,1,3,3,2,2,2,2,2,2,3,1,1,1,4,1,2,1,2,1,1,2,1,1,3,2,2,1,2,1,2,1,1,3,2,2,2,3,2,1,1,1,3,1,1,3,1,2,2,3,2,3,2,1,1,2,2,2,1,1,1,2,3,2,2,2,2,1,2,2,2,2,3,2,3,1,4,2,1,2,3,1,1,1,2,3],
        [1,2,1,3,2,2,1,2,1,1,1,1,1,2,1,1,2,3,2,2,2,1,2,2,2,1,1,1,4,2,2,2,1,1,2,2,2,1,2,2,2,1,1,1,2,2,1,2,2,2,2,3,2,2,1,2,2,1,1,2,2,1,2,2,2,2,1,1,1,2,1,2,1,2,1,2,2,2,2,1,2,1,2,2,2,2,2,1,2,1,4,2,1,2,3,1,1,2,2,2],
        [2,1,1,3,2,2,1,1,2,2,2,2,2,3,1,2,2,3,2,2,2,2,2,2,2,1,1,1,4,1,2,2,2,1,2,2,1,2,2,1,2,1,1,2,2,2,1,2,2,2,2,3,1,1,2,1,2,2,1,2,1,1,2,2,2,2,2,2,1,2,1,2,2,1,1,2,2,2,2,2,1,2,3,2,2,2,2,2,2,1,4,2,2,2,3,2,1,2,2,2],
    ]
]

kelamin = [0]

soal = [5,4,5,4]

usia1 = 70 
usia2 = 30

index = 0
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScMHWGv7zeAGgGvtH3Cyc0cuP9KGv7ZDlWpbR-To3gXMMRsvg/viewform?usp=sf_link")

        times = 10
        idx = 1
        idxx = 1

        while times:
            time.sleep(2)

            if idx == 10:
                idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(10)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[idx].click()

            time.sleep(10)
            # ================================================================================

            if usia1 != 0 and usia2 != 0:
                pil = random.choice([0,1])
            elif usia1 != 0 and usia2 == 0:
                pil = 0
            elif usia1 == 0 and usia2 != 0:
                pil = 1

            if pil == 0 :
                usia1 -= 1
                umur = random.choice([2,3])
            else:
                umur = random.choice([4,5,6])
                usia2 -= 1

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            checkboxes[0].click()

            time.sleep(2)
            radiobuttons[kelamin[index]].click()
            radiobuttons[umur].click()

            time.sleep(2)
            for i in range(4):
                time.sleep(3)
                kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
                kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

                if len(kirims1) != 0 :
                    submit_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                    )
                else:
                    submit_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                    )

                submit_button.click()

                time.sleep(2)
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

                p = -1
                for x in range(soal[i]):
                    s1 = page[i][x][index] + p
                    testcheck[s1].click()
                    p += 5

                






















            # time.sleep(3)
            # kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
            # kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

            # if len(kirims1) != 0 :
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
            #     )
            # else:
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
            #     )

            # submit_button.click()

            # driver.implicitly_wait(4)
            # driver.get("https://docs.google.com/forms/d/e/1FAIpQLScMHWGv7zeAGgGvtH3Cyc0cuP9KGv7ZDlWpbR-To3gXMMRsvg/viewform?usp=sf_link")

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))

            print("")
            print("usia1 : " + str(usia1))
            print("usia2 : " + str(usia2))

        driver.quit()
        
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
            # kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            # kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            # if len(kirims1) != 0 :
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            #     )
            # else:
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            #     )

            # submit_button.click()