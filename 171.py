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

link = "https://forms.gle/wtvsozue6sbPWyfh7"

profil = ["Default"]

nama = [
    "nama",
]

telp = [
    "telp",
]

kelamin = [
    0
]

soal = [5,7,5,5,5,5]

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

            for i in range(4) :
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
            banyak = random.randint(1,7)
            usia = random.randint(1,2)
            domisili = random.randint(6,9)
            olshop = random.choice([26,26,26,27,28,28,28,29])
            produk = 33 if banyak >= 6 else random.choice([31,32,33,33,34,35])
            
            if usia == 1 and kelamin[index] == 1:
                pekerjaan = random.choice([10,11,11,11,12,12,12,13,13,14])
            elif usia == 1 :
                pekerjaan = random.choice([10,11,11,11,12,12,12,13,13])
            elif usia == 2 and kelamin[index] == 1 :
                pekerjaan = random.choice([11,11,11,12,12,12,13,13,14])
            else :
                pekerjaan = random.choice([11,11,11,12,12,12,13,13])

            time.sleep(1)
            if pekerjaan == 10 :
                pendidikan = 23
                penghasilan =  random.choice([16,17])
            elif pekerjaan == 11 :
                pendidikan = random.choice([22,23])
                penghasilan =  random.choice([17,18,18,18,19])
            else :
                pendidikan = random.choice([22,23,23,23])
                penghasilan =  random.choice([17,18,18,19])

            time.sleep(1)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian

            textboxes[0].send_keys(nama[index])
            textboxes[1].send_keys(telp[index])
            textboxes[2].send_keys(banyak)

            time.sleep(2)
            radiobuttons[usia].click()
            radiobuttons[kelamin[index] + 3].click()
            radiobuttons[domisili].click()
            radiobuttons[pekerjaan].click()
            radiobuttons[penghasilan].click()
            radiobuttons[pendidikan].click()
            radiobuttons[olshop].click()
            radiobuttons[produk].click()

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

            for i in range(len(soal)) :
                time.sleep(2)
                radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

                p = 2
                for i in range(soal[i]) :
                    s1 = random.choice([p,p+1,p+1,p+1,p+2,p+2,p+2])
                    radiobuttons[s1].click()

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