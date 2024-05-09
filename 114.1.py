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

profil = []
idx = []

nama = [

]

negara = [
    "Colombia",
    "Colombia",
    "Colombia",
    "Colombia",
    "Colombia",
    "Colombia",
    "Colombia",
    "Colombia",
    "Colombia",
    "Filipina",
    "Filipino",
    "Filipino",
    "Filipino",
    "Filipina",
    "Filipino",
    "Malaysian",
    "Malaysian",
    "Malaysian",
    "Malaysian",
    "Mexican",
    "Mexican",
    "Mexican",
    "Mexican",
    "Tokelauan",
    "New Zealander",
    "Tokelauan",
    "New Zealander",
    "Tokelauan",
    "New Zealander",
    "New Zealander",
    "new Zealander",
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa",
    "South Africa",
    "Thai",
    "Thai",
    "Thai",
    "Thai",
    "Thai",
    "Thai",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "Zimbabwean",
    "Zimbabwean",
    "Zimbabwean",
    "Zimbabwean",
    "Zimbabwean",
]

bahasa = [
    "Spanish",
    "Spanish",
    "Spanish",
    "Spanish",
    "Spanish",
    "Spanish",
    "Spanish",
    "Spanish",
    "Spanish",
    "Filipino/Tagalog",
    "Filipino/Tagalog",
    "Filipino/Tagalog",
    "Filipino/Tagalog",
    "Filipino/Tagalog",
    "Filipino/Tagalog",
    "Mandarin ",
    "Mandarin ",
    "Mandarin ",
    "Mandarin ",
    "Spanish",
    "Spanish",
    "Spanish",
    "Spanish",
    "Tokelauan",
    "English",
    "Tokelauan",
    "maori",
    "Tokelauan",
    "maori",
    "English",
    "English",
    "Zulu",
    "Zulu",
    "Afrikaans",
    "Afrikaans",
    "Xhosa",
    "Afrikaans",
    "Thai",
    "Thai",
    "Thai",
    "Thai",
    "Thai",
    "Thai",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "English",
    "Shona",
    "Shona",
    "Ndebele",
    "Shona",
]

kelamin = [1,0,0,0,1,0,1,0,1,1, 0,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,0,1,0]

usia = [5,5,5,6,5,5,6,5,6,5, 5,5,6,6,6,6,6,6,5,6, 5,6,5,5,5,5,5,5,6,6, 6,5,5,6,5,6,6,5,5,5, 6,6,6,6,6,6,6,6,6,5, 6,5,5,6]

work = [11,11,11,11,11,11,11,11,11,10, 10,10,11,11,11,11,11,11,11,10, 10,10,10,10,10,10,10,10,10,11, 11,10,10,10,10,10,10,10,10,10, 10,10,10,10,10,10,10,10,10,12, 12,12,12,12]

lama = [
    "2 - 3 months",
    "3 - 3 months",
    "4 - 3 months",
    "5 - 3 months",
    "6 - 3 months",
    "7 - 3 months",
    "8 - 3 months",
    "9 - 3 months",
    "10 - 3 months",
    "17",
    "17",
    "17",
    "16",
    "16",
    "16",
    "2 - 3 months",
    "3 - 3 months",
    "4 - 3 months",
    "5 - 3 months",
    "7 - 12 months",
    "8 - 12 months",
    "9 - 12 months",
    "10 - 12 months",
    "18",
    "18",
    "18",
    "17",
    "17",
    "17",
    "1-3 months",
    "1-3 months",
    "18",
    "18",
    "17",
    "17",
    "17",
    "17",
    "18",
    "18",
    "17",
    "17",
    "17",
    "17",
    "17",
    "1 - 3 months",
    "1 - 3 months",
    "1 - 3 months",
    "17",
    "17",
    "1.5 year",
    "2 year",
    "2 year",
    "1 year",
    "1 year",
]

page1 = [
    [4,5,2,3,2,3,2,4,2,4,3,3,4,5,3,4,4,5,4,4,3,3,4,4,4,5,5,4,5,3,4,3,3,4,5,5,5,4,3,4,5,4,3,5,5,5,4,4,4,3,3,2,3,3],
    [2,3,5,3,4,3,3,3,2,2,3,3,2,3,1,2,2,3,1,2,2,2,1,2,2,2,2,1,1,1,2,2,2,1,3,2,2,2,3,3,3,4,2,2,3,1,1,2,1,2,2,1,3,3],
    [4,5,2,3,3,2,3,4,3,4,4,3,5,4,3,4,3,3,3,4,4,5,3,5,4,4,5,3,5,4,5,4,4,4,3,3,4,3,3,3,3,4,4,4,4,4,3,5,5,4,2,4,3,3],
    [3,2,3,3,3,4,4,3,2,2,2,3,3,3,2,4,2,3,3,2,2,1,1,1,2,2,1,1,1,4,2,1,2,2,1,3,2,2,2,3,1,1,3,2,1,2,1,2,1,3,3,1,2,1],
    [4,4,3,2,3,2,3,4,4,4,4,4,3,5,4,3,3,2,3,2,3,3,3,4,2,3,3,3,4,5,4,3,3,4,5,5,4,4,4,5,3,3,5,5,5,4,3,4,3,2,2,3,4,4],
    [2,1,2,3,4,4,3,2,2,2,2,3,2,2,3,2,2,2,1,2,3,2,1,1,2,3,2,1,2,2,2,3,3,2,2,1,3,2,2,1,1,2,3,1,1,1,3,2,2,2,3,3,2,3],
    [5,5,2,3,4,3,4,3,3,4,3,4,3,3,4,4,4,5,5,4,4,5,4,5,4,4,5,4,4,4,5,5,5,3,4,3,3,4,4,4,3,5,3,4,4,4,3,5,5,3,3,4,3,4],
    [1,2,5,4,2,4,3,3,4,2,2,3,2,1,3,2,2,1,2,2,2,2,1,1,2,2,2,1,3,1,2,2,2,1,3,2,2,2,2,1,1,2,2,3,3,1,2,1,1,2,2,1,3,2],
    [4,5,3,2,3,2,3,2,4,5,5,4,4,3,3,4,3,3,4,5,3,4,4,4,5,3,4,4,5,5,5,3,5,5,3,4,5,4,4,4,5,5,5,3,3,4,4,5,5,4,3,3,4,4],
    [1,2,3,5,3,4,3,2,2,2,2,3,1,2,3,2,2,1,1,2,1,1,2,2,2,1,1,2,2,2,2,2,2,2,1,3,2,1,1,2,2,1,1,1,1,1,2,1,1,2,1,2,3,1],
    [5,5,4,3,2,3,5,3,2,5,3,4,4,5,4,2,4,4,2,5,5,3,4,4,5,5,3,4,5,5,2,5,5,2,4,5,4,5,4,4,5,5,4,4,4,3,2,4,4,3,3,3,3,2],
    [1,2,3,3,4,4,3,1,3,2,1,2,2,1,2,1,1,2,3,2,2,1,3,1,2,2,1,3,2,1,2,1,1,2,2,1,3,2,3,3,1,1,2,2,2,3,1,2,1,3,2,1,1,2],
    [5,5,4,2,3,5,4,2,2,3,3,4,5,4,4,5,5,3,3,3,3,4,5,5,3,3,4,5,5,5,3,4,5,5,2,4,5,4,4,2,3,4,4,3,3,4,3,3,3,3,3,2,4,1],
    [3,2,4,2,3,4,4,3,3,2,2,3,2,2,1,2,2,1,2,3,2,2,1,2,3,2,2,1,2,4,3,2,2,1,3,3,3,4,2,2,3,2,2,1,1,1,2,2,1,3,2,1,2,2],
    [5,4,2,2,3,3,3,4,5,3,4,5,4,3,3,4,4,5,3,2,4,4,4,3,2,4,4,4,5,5,4,5,5,2,4,5,4,4,4,3,5,2,4,4,4,5,3,3,5,4,2,3,2,3],
    [1,2,3,3,3,4,3,2,2,2,3,3,4,3,3,2,1,1,2,2,2,1,2,1,2,2,1,2,2,3,2,2,2,2,1,3,3,1,1,2,2,1,2,2,2,2,3,2,2,2,2,1,1,2],
    [4,4,2,3,2,2,5,4,4,3,3,3,4,5,3,3,4,4,5,3,3,4,3,4,2,4,5,4,4,5,2,5,5,2,4,5,4,4,4,5,3,4,4,5,3,3,4,4,4,4,4,3,3,4],
    [2,1,3,2,4,3,3,1,3,2,1,3,2,3,2,2,2,1,1,1,1,2,2,3,2,2,1,3,2,3,4,2,2,2,2,1,3,1,1,1,2,2,2,2,3,2,1,3,1,3,3,2,2,2],
    [4,3,2,2,3,4,5,3,4,4,4,5,4,5,5,2,3,4,5,3,3,4,5,4,4,3,3,2,3,4,5,4,5,5,2,4,5,4,4,5,5,4,5,4,4,4,4,5,5,4,3,2,2,3],
    [1,1,2,3,3,2,3,2,2,4,3,3,2,1,2,2,2,2,1,2,2,1,3,2,2,1,3,1,1,2,2,2,2,1,3,2,2,1,1,2,3,4,1,3,3,3,2,2,3,2,2,3,2,1],
]

index = 1
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://forms.gle/C1TcxrgupSU6htBM8")

        if i == 0:
            times = 9
        else:
            times = 10

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

            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            lainnya = driver.find_elements("css selector", ".Hvn9fb")#lainnya
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            checkboxes[0].click()

            time.sleep(2)
            textboxes[0].send_keys(nama[index])
            textboxes[1].send_keys(negara[index])
            textboxes[2].send_keys(bahasa[index])

            time.sleep(2)
            radiobuttons[kelamin[index]].click()
            radiobuttons[usia[index]].click()
            radiobuttons[work[index]].click()

            if lama[index] == 16 :
                radiobuttons[lama[index]].click()
            elif lama[index] == 17 :
                radiobuttons[lama[index]].click()
            elif lama[index] == 18 :
                radiobuttons[lama[index]].click()
            else:
                lainnya[1].send_keys(lama[index])

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
            for i in range(20):
                s1 = page1[i][index] + p
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
            driver.get("https://forms.gle/C1TcxrgupSU6htBM8")

            index += 1
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
            # lainnya = driver.find_elements("css selector", ".Hvn9fb")#lainnya
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