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

link = "https://docs.google.com/forms/d/e/1FAIpQLSfStXPhGGUI9QWNSbFtXVg1Y1eRshCxlAB4nWTZRiILsMEZuw/viewform"

profil = ["Default"]

email = [
    "email@gmail.com",
]

kelamin = [
    0,
]

listJawaban = [
    [4,5,5,4,5,4,5,4,4,4,5,5,4,5,5,5,5,5,5,4,5,5,4,5,5,4,5,5,5,5],
    [5,4,5,4,5,5,5,4,4,4,5,4,5,5,5,5,5,5,4,4,5,4,5,5,5,5,5,5,5,4],
    [4,5,3,4,3,4,5,5,4,5,3,4,4,4,5,5,3,5,5,5,3,4,4,5,3,4,5,3,5,4],
    [4,5,4,5,4,3,4,4,3,4,4,5,4,5,4,4,4,4,5,4,4,5,3,4,4,4,4,4,4,5],
    [4,5,5,4,4,5,5,4,3,5,5,4,4,5,4,5,5,5,5,4,5,4,5,5,5,4,4,5,5,4],
    [5,5,5,4,5,5,5,5,4,5,5,4,5,5,4,5,5,5,5,5,5,4,5,5,5,5,4,5,5,4],
    [4,3,4,4,4,3,4,4,3,4,3,4,3,4,3,4,4,4,3,4,3,4,3,4,3,3,3,4,4,4],
    [3,4,3,4,4,4,4,4,3,4,3,4,5,4,3,4,3,4,4,4,3,4,4,4,3,5,3,3,4,4],
    [5,5,5,4,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,4,5,5,5,4,4,5,4,4,5,5,5,5,4,4,5,4,4,5,5,5,4,4,5,5,4,5,4,5],
    [5,4,4,3,3,3,3,4,4,4,4,3,4,4,5,3,4,3,4,4,4,3,3,3,4,4,5,4,3,3],
    [3,2,3,2,2,2,2,2,3,2,3,2,2,3,2,2,3,2,2,2,3,2,2,2,3,2,2,3,2,2],
    [4,4,4,4,4,4,4,4,3,4,4,4,3,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4],
    [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [4,3,3,4,4,4,3,4,4,3,4,4,4,4,3,3,3,3,3,4,4,4,4,3,4,4,3,3,3,4],
    [3,2,3,2,2,2,2,2,3,2,3,2,2,3,2,2,3,2,2,2,3,2,2,2,3,2,2,3,2,2],
    [5,5,5,4,5,5,4,5,5,5,5,4,5,5,5,4,5,4,5,5,5,4,5,4,5,5,5,5,4,4],
    [4,3,4,3,3,4,4,4,3,4,4,4,3,4,3,4,4,4,3,4,4,4,4,4,4,3,3,4,4,4],
    [5,4,4,4,4,4,4,5,5,4,4,4,3,5,3,4,4,4,4,5,4,4,4,4,4,3,3,4,4,4],
    [5,4,5,4,4,4,4,4,4,4,5,4,4,5,5,4,5,4,4,4,5,4,4,4,5,4,5,5,4,4],
    [5,4,4,4,4,4,4,4,4,4,4,4,4,4,5,4,4,4,4,4,4,4,4,4,4,4,5,4,4,4],
    [4,4,5,5,4,4,4,4,4,4,5,5,3,5,4,4,5,4,4,4,5,5,4,4,5,3,4,5,4,5],
    [2,3,2,3,2,3,2,3,3,4,2,3,2,3,2,2,2,2,3,3,2,3,3,2,2,2,2,2,2,3],
    [5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,5,5,3,5,4,5,5,4,4,5,4,5,5,4,5,5,5,5,5,5,4,4,5,5,5,4,5,5,4],
    [5,4,5,5,5,4,5,5,5,4,5,4,5,4,5,5,5,5,4,5,5,4,4,5,5,5,5,5,5,4],
    [2,3,2,3,2,3,2,3,3,4,2,3,2,3,2,2,2,2,3,3,2,3,3,2,2,2,2,2,2,3],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
]

index = 0
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get(link)

        times = 1
        idx = 1
        idxx = 1

        while times:
            time.sleep(2)

            if idx == 10:
                idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(5)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[idx].click()

            time.sleep(5)
            # ================================================================================

            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            textboxes[0].send_keys(email[index])

            time.sleep(2)
            p = -1
            for i in range(29) :
                s1 = listJawaban[index][i] + p
                testcheck[s1].click()

                p += 5
            
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

            time.sleep(3)
            usia = random.choice([2,3,3,3,3,4,4,4,4,4,5])
            
            if usia == 2 :
                pendidikan = random.choice([6,7])
                posisi = random.choice([11,11,11,12])
            elif usia == 3 :
                pendidikan = random.choice([7,8,8,8,9])
                posisi = random.choice([11,12,12])
            else :
                pendidikan = random.choice([7,8,9,9,9,9,9])
                posisi = random.choice([11,11,11,12,12,12,12,13])
            
            time.sleep(2)
            if posisi == 11 :
                lama = random.choice([15,16])
            elif posisi == 12 :
                lama = random.choice([15,16,16,16,16,17])
            else :
                lama = random.choice([16,17,17,17,17,18,18,18,18])

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            radiobuttons[kelamin[index]].click()
            radiobuttons[usia].click()
            radiobuttons[pendidikan].click()
            radiobuttons[posisi].click()
            radiobuttons[lama].click()

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
            # driver.get(link)

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))

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