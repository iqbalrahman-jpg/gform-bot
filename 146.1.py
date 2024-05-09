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

nama = [

]


# laki 0 perempuan 1
kelamin = [
    
]

positif = 48
negatif = 12

times = 60
index = 0

soal = [5, 4, 4, 6, 4]

try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://forms.gle/9WauDyHf8ztPd9DT8")

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
            #Hardcoded logic
            test = 0

            usia = random.choice([2,3,3,3,3,4,4,4,4,5,6])

            if usia == 2 :
                pendidikan = 7
            elif usia == 3:
                pendidikan = random.randint(7,9)
            else :
                pendidikan = random.choice([7,8,8,8,9,9,9,9,10,10,10,10,10,11])
                
            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian

            textboxes[0].send_keys(nama[index])

            time.sleep(2)
            radiobuttons[usia].click()
            radiobuttons[kelamin[index]].click()
            radiobuttons[pendidikan].click()

            time.sleep(2)
            if positif != 0 and negatif != 0:
                pil = random.choice([0,1])
            elif positif != 0 and negatif == 0:
                pil = 0
            elif positif == 0 and negatif != 0:
                pil = 1

            time.sleep(2)
            if pil == 0:
                for i in range(len(soal)) :
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

                    submit_button.click()

                    time.sleep(2)
                    testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
                    p = 2
                    x = soal[i]
                    while x :
                        s1 = random.choice([p, p+1, p+1, p+1, p+1, p+1, p+1, p+1, p+2, p+2, p+2, p+2, p+2, p+2, p+2])
                        testcheck[s1].click()
                        p += 5
                        x -= 1

                positif -= 1
            else:
                for i in range(len(soal)) :
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

                    submit_button.click()

                    time.sleep(2)
                    testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
                    p = 0
                    x = soal[i]
                    while x :
                        s1 = random.choice([p, p, p, p, p, p, p+1, p+1, p+1, p+1, p+1, p+1, p+2])
                        testcheck[s1].click()
                        p += 5
                        x -= 1

                negatif -= 1

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
            driver.get("")

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))
            print("==================")
            print("positif : " + str(positif))
            print("negatif : " + str(negatif))
            print("")
            
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
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()