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

profil = ["Profile 7"]

kelamin = [0,1,0,0,1,0,1,1,0,1,]

index = 0
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://forms.gle/o17fgSaXHu7PPtMS7")

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

            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            usia = random.choice([2,3,4,5])

            time.sleep(2)
            if usia == 2:
                pekerjaan = random.choice([6,7,8,8,8])
            else:
                pekerjaan = random.choice([6,7])

            time.sleep(2)
            if pekerjaan == 8:
                pendapatan = 10
            else:
                pendapatan = random.choice([10,11,11,12,12,12])

            time.sleep(2)
            radiobuttons[kelamin[index]].click()
            radiobuttons[usia].click()
            radiobuttons[pekerjaan].click()
            radiobuttons[pendapatan].click()

            time.sleep(2)
            p = 13
            soal = 3
            while soal:
                s1 = random.choice([p,p+1,p+2,p+3])
                radiobuttons[s1].click()
                p += 4
                soal -= 1

            time.sleep(2)
            p = 25
            soal = 20
            while soal:
                s1 = random.choice([p,p+1])
                radiobuttons[s1].click()
                p += 4
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
            driver.get("https://forms.gle/o17fgSaXHu7PPtMS7")

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