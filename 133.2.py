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

profil = ["Profile 13", "Profile 14", "Profile 109", "Default",]
indeks = [9,0,1,2,3,4,5,6,9,0,2,3,1,2,3,]
jumlahakun = [2,8,2,3]

nama = [
    "Ariela Putri Abagas",
    "Rihana Asmara Dewi",

    "Rensky Alifia Kuncoro",
    "Fitri Bella Sadisti",
    "Cintya Ayu Dewi",
    "Bella Clarissa Rahma",
    "Jesica Budi Pratiwi",
    "Shella Fransiska",
    "Rina Gista Wardoyo",
    "Renu Harsana Safitri",

    "Putri Delima Ariesta",
    "Fadilla Ida Anugrah",

    "Kristiani Vidya Salsabilla",
    "Gizel Safitri Ningtyas",
    "Aprillia Indah Deviana",

]

kelamin = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

ma = 2
patma = 4
gapatma = 9
wagapatma = 0

index = 0
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://forms.gle/NKzMj1esABsKFzur7")

        times = jumlahakun[i]
        # idx = 1
        idxx = 1

        while times:
            time.sleep(2)

            # if idx == 10:
            #     idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(10)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[indeks[index]].click()

            time.sleep(10)
            # ================================================================================

            usia = random.choice([0,1,2,3])
            domisili = random.choice([6,7,8,9,10])

            time.sleep(2)
            if usia == 0:
                pendidikan = random.choice([11,12,16])
                pekerjaan = random.choice([17,19,21,24])
            elif usia == 1:
                pendidikan = random.choice([11,12,13])
                pekerjaan = random.choice([17,18,19,20,24])
            else:
                pendidikan = random.choice([11,12,13,14])
                if pendidikan == 14 and kelamin[index] == 0:
                    pekerjaan = random.choice([17,18,19,20,22,24])
                elif kelamin[index] == 1:
                    pekerjaan = random.choice([17,18,19,20,22,24])
                else:
                    pekerjaan = random.choice([17,18,19,20,24])

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            time.sleep(2)
            checkboxes[0].click()

            time.sleep(2)
            textboxes[0].send_keys(nama[index])

            time.sleep(2)
            radiobuttons[4].click()
            radiobuttons[usia].click()
            radiobuttons[domisili].click()
            radiobuttons[pendidikan].click()
            radiobuttons[pekerjaan].click()
            radiobuttons[25].click()
            radiobuttons[27].click()

            time.sleep(2)
            if ma != 0 and patma != 0 and gapatma != 0 and wagapatma != 0:
                pil = random.choice([4,3,2,1])
            elif ma != 0 and patma != 0 and gapatma != 0 and wagapatma == 0:
                pil = random.choice([4,3,2])
            elif ma != 0 and patma != 0 and gapatma == 0 and wagapatma != 0:
                pil = random.choice([4,3,1])
            elif ma != 0 and patma == 0 and gapatma != 0 and wagapatma != 0:
                pil = random.choice([4,2,1])
            elif ma == 0 and patma != 0 and gapatma != 0 and wagapatma != 0:
                pil = random.choice([3,2,1])
            elif ma != 0 and patma != 0 and gapatma == 0 and wagapatma == 0:
                pil = random.choice([4,3])
            elif ma != 0 and patma == 0 and gapatma != 0 and wagapatma == 0:
                pil = random.choice([4,2])
            elif ma == 0 and patma != 0 and gapatma != 0 and wagapatma == 0:
                pil = random.choice([3,2])
            elif ma != 0 and patma == 0 and gapatma == 0 and wagapatma != 0:
                pil = random.choice([4,1])
            elif ma == 0 and patma != 0 and gapatma == 0 and wagapatma != 0:
                pil = random.choice([3,1])
            elif ma == 0 and patma == 0 and gapatma != 0 and wagapatma != 0:
                pil = random.choice([2,1])
            elif ma != 0 and patma == 0 and gapatma == 0 and wagapatma == 0:
                pil = 4
            elif ma == 0 and patma != 0 and gapatma == 0 and wagapatma == 0:
                pil = 3
            elif ma == 0 and patma == 0 and gapatma != 0 and wagapatma == 0:
                pil = 2
            elif ma == 0 and patma == 0 and gapatma == 0 and wagapatma != 0:
                pil = 1

            time.sleep(2)
            if pil == 4:

                time.sleep(2)
                p = pil
                for i in range(27):
                    testcheck[p].click()
                    p += 5

                ma -= 1
            elif pil == 3:

                time.sleep(2)
                p = pil
                for i in range(27):
                    s1 = random.choice([p,p+1])
                    testcheck[s1].click()
                    p += 5

                patma -= 1
            elif pil == 2:

                time.sleep(2)
                p = 3
                for i in range(27):
                    s1 = p
                    testcheck[s1].click()
                    p += 5

                gapatma -= 1
            else:

                time.sleep(2)
                p = pil
                for i in range(27):
                    s1 = random.choice([p,p+1,p+2,p+3])
                    testcheck[s1].click()
                    p += 5

                wagapatma -= 1

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
                )

            submit_button.click()

            driver.implicitly_wait(4)
            driver.get("https://forms.gle/NKzMj1esABsKFzur7")

            index += 1
            # idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(indeks[index]))
            print("idxx : " + str(idxx))
            print("")
            print("ma = " + str(ma))
            print("patma = " + str(patma))
            print("gapatma = " + str(gapatma))
            print("wagapatma = " + str(wagapatma))

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