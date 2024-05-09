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

profil = ["Profile 7", "Profile 8", "Profile 9", "Profile 10", "Profile 11"]

nama = [
    "Naniša Ognjenović",
    "Budimir Prasetić",
    "Arjan Ugarov",
    "Yudi Pradana Fernandez",
    "Angela Yunda Cruz",
    "Yana Santos Nugh",
    "John Reyes Pertiwi",
    "Ali Hasanović",
    "Rista Febrić",
    "Maria Tiana Lopez",

    "Bence Yumerta",
    "Bella Ndayu",
    "Nela Mirra",
    "Dora Langga",
    "Fatah Dewa",
    "Anisah Cha",
    "Bence Suryanto",
    "Diah Cindy",
    "Alfiyan Tori",
    "Yulia Yund",

    "Syifa Radifa",
    "Amelia Scott Arowaya",
    "Nia Julieta",
    "Jacob Reyson Utomo",
    "Azzarina Rosita",
    "Isabella Sitpatel",
    "Bayu Diaz Ganara",
    "Liam Ferdinand Thompson",
    "Fabiano De La Cruz",
    "Oliv Atta Majid",

    "Afifa Mhlongo",
    "Nomsa Warda Nawan",
    "Putri Keanca Na Siphiwe",
    "Mahendra Tran Quang Huy",
    "Shaka Pwijaya Dlamini",
    "Bongani Cynna Rafisa",
    "Mona Phan Minh Trang",
    "Yan Ra Pham Tuan",
    "Le Thi Frys Eknh",
    "Nguyen Thanh Ang",

    "Nahi Chau Mutasa",
    "Tinashe Suti Surya",
    "Ariestya Delima Rashida",
    "Rucul Lee Thompson",
    "Ayu Listya Chirisa",
    "Fadil Jaidun Campbell",
    "Ndlovu Moh Santos",
    "Tendai Rudi Nurba Dube",
    "Raafni Johnson Williams",
    "Shanice Rahan Nadi",
]

negara = [
    "Croatian",
    "Croatian",
    "Croatian",
    "Filipino",
    "Filipino",
    "Filipino",
    "Filipino",
    "Croatian",
    "Croatian",
    "Filipino",

    "Hungarian",
    "Hungarian",
    "Hungarian",
    "Hungarian",
    "Malaysia",
    "Malaysia",
    "Hungarian",
    "Malaysia",
    "Malaysia",
    "Malaysia",

    "Mexican",
    "New Zealander",
    "Mexican",
    "New Zealander",
    "Mexican",
    "New Zealander",
    "Mexican",
    "New Zealander",
    "Mexican",
    "New Zealander",

    "South Africa",
    "South Africa",
    "South Africa",
    "Vietnam",
    "South Africa",
    "South Africa",
    "Vietnam",
    "Vietnam",
    "Vietnam",
    "Vietnam",

    "Zimbabwean ",
    "Zimbabwean ",
    "Jamaican",
    "Jamaican",
    "Zimbabwean ",
    "Jamaican",
    "Zimbabwean ",
    "Zimbabwean ",
    "Jamaican",
    "Jamaican",
]

bahasa = [
    "Croatian",
    "Croatian",
    "Croatian",
    "Filipino",
    "Filipino",
    "Filipino/Tagalog",
    "tagalog",
    "Croatian",
    "Croatian",
    "Filipino",

    "Hungarian",
    "Hungarian",
    "Hungarian",
    "Hungarian",
    "Malay",
    "Malay",
    "Hungarian",
    "Malay",
    "Malay",
    "Malay",

    "Spanish",
    "Maori",
    "Spanish",
    "English",
    "Spanish",
    "English",
    "Spanish",
    "English",
    "Spanish",
    "Maori",

    "Zulu",
    "Zulu",
    "Afrikaans",
    "Vietnamese",
    "Afrikaans",
    "Xhosa",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",
    "Vietnamese",

    "Shona",
    "English",
    "JamaicanPatois",
    "JamaicanPatois",
    "Shona",
    "JamaicanPatois",
    "Shona",
    "Ndebele",
    "JamaicanPatois",
    "JamaicanPatois",
]

kelamin = [1,0,0,0,1,0,1,0,1,1, 0,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,0,1,0]

usia = [5,5,5,6,5,5,6,5,6,5, 5,5,6,6,6,6,6,6,5,6, 5,6,5,5,5,5,5,5,6,6, 6,5,5,6,5,6,6,5,5,5, 6,6,6,6,6,6,6,6,6,6]

work = [10,10,10,10,11,10,11,11,11,11, 11,10,11,11,11,10,10,11,11,10, 10,11,11,11,10,10,10,11,10,10, 10,10,10,10,11,11,11,11,10,10, 12,12,12,12,12,12,12,12,12,12]

lama = [17,16,17,16,17,16,17,17,16,17, 16,18,18,17,16,17,16,17,16,16, 16,18,17,17,18,16,18,17,17,16, 16,17,16,16,16,17,16,17,16,17, 19,19,19,19,19,19,19,19,19,19]

idx = [5,3,4,9,8,6,7,1,2,0, 1,2,4,5,8,7,3,9,6,0, 5,9,3,8,1,7,4,6,2,0, 3,2,1,7,4,5,6,9,8,0, 4,1,9,7,2,8,3,5,6,0]

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

            if lama[index] == 19 :
                s1 = random.choice(["2 year", "1.5 year"])
                lainnya[1].send_keys(s1)
            else:
                radiobuttons[lama[index]].click()

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

            p = 2
            for i in range(10):
                s1 = random.choice([p,p+1,p+1,p+1,p+2,p+2,p+2])
                testcheck[s1].click()

                p += 3
                s1 = random.choice([p,p,p,p+1,p+1,p+1,p+2])
                testcheck[s1].click()
                p += 7

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