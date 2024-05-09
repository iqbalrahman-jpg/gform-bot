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

profil = ["Profile 7", "Profile 8", "Profile 9", "Profile 10"]
banyak = [5,4,2,3]

inisial = [
    "AH",
    "RF",
    "BP",
    "AN",
    "YN",
    "PA",
    "BM",
    "BS",
    "AC",
    "DC",
    "SR",
    "SA",
    "PK",
    "AR",
    "SP",
]

usia = [
    "20",
    "23",
    "20",
    "19",
    "19",
    "21",
    "22",
    "22",
    "19",
    "19",
    "23",
    "22",
    "22",
    "20",
    "22",
]

telp = [
    "084624253733",
    "088565440513",
    "083626799003",
    "088070442682",
    "089579629094",
    "080103002233",
    "083806763847",
    "084985961237",
    "089045039379",
    "088159431881",
    "081850592479",
    "081264718461",
    "081290475868",
    "082132447386",
    "087886158249",
]

kelamin = [0,1,0,0,0,1,0,0,1,1,1,1,1,1,0]

domisili = [2,3,4,4,4,5,3,4,3,3,4,6,6,4,2]

idx = [1,2,3,4,6,7,1,3,7,9,5,9,1,3,4]

index = 1
positif = 11
negatif = 3
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://docs.google.com/forms/d/1REgl3ZrJUoDsZF1BFFldidS0y6A-S6vI0FlgABoBQB4/edit")
        
        times = banyak[i]
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
            radiobuttons[idx[index]].click()

            time.sleep(10)
            # ================================================================================

            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            checkboxes[0].click()

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
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            radiobuttons[0].click()

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
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian

            textboxes[0].send_keys(inisial[index])
            textboxes[1].send_keys(usia[index])
            driver.implicitly_wait(4)

            radiobuttons[domisili[index]].click()
            time.sleep(2)
            radiobuttons[kelamin[index]].click()

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
            if positif != 0 and negatif != 0:
                p = random.choice([0,3])
                if p == 0:
                    negatif -= 1
                else:
                    positif -= 1
            elif positif != 0 and negatif == 0:
                p = 3
                positif -= 1
            elif positif == 0 and negatif != 0:
                p = 0
                negatif -= 1

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            soal = 14
            while soal :
                if p == 10 or p == 15:
                    s1 = random.choice([p+3,p+4])
                    radiobuttons[s1].click()
                    p += 5
                    soal -= 1
                elif p == 13 or p == 18:
                    s1 = random.choice([p-3,p-2])
                    radiobuttons[s1].click()
                    p += 5
                    soal -= 1
                else:
                    s1 = random.choice([p,p+1])
                    radiobuttons[s1].click()
                    p += 5
                    soal -= 1

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
            driver.get("https://docs.google.com/forms/d/1REgl3ZrJUoDsZF1BFFldidS0y6A-S6vI0FlgABoBQB4/edit")

            index += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))
            print("positif : " + str(positif))
            print("negatif : " + str(negatif))

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