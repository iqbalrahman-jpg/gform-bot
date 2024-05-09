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

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("profile-directory=Profile 14")

driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)

driver.get("https://forms.gle/q2UsVzNTQhfP8ZK47")

nama = [
    "Alreno Fahrurozi",
    "Achmad Maulana",
    "Cintya Ayu",
    "Bella Rahma",
    "Budiman Laksana Satria",
    "Cila Ayu Cianta",
    "Ruli Juliansyah Tan",
    "Renofal Nugraha",
    "Bagas Reno Ramadhan",
    "",
]

#0 cewe 1 cowo
kelamin = [1,1,0,0,1,0,1,1,1]

mahasiswa = 3
tidak = 5

bone = 2
bbone = 6

range2 = 0
range3 = 8

tertarik = 6
ttertarik = 2

k10 = 4
k20 = 4

times = 8
index = 0
idx = 1
idxx = 1

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if idx == 10:
            idx = 0

        option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

        option[0].click()

        time.sleep(20)
        driver.switch_to.window(driver.window_handles[idxx])
        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
        radiobuttons[idx].click()

        time.sleep(20)
        # =====================================================================================

        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        if mahasiswa != 0 and tidak != 0 :
            pil = random.choice([1,2])
            if pil == 1:
                mahasiswa -= 1
            else:
                tidak -= 1
        elif mahasiswa != 0 and tidak == 0 :
            pil = 1
            mahasiswa -= 1
        elif mahasiswa == 0 and tidak != 0 :
            pil = 2
            tidak -= 1

        time.sleep(2)
        if bone != 0 and bbone != 0:
            domisili = random.choice([1,2])
            if domisili == 1:
                bone -= 1
            else:
                bbone -= 1
        elif bone != 0 and bbone == 0:
            domisili = 1
            bone -= 1
        elif bone == 0 and bbone != 0:
            domisili = 2
            bbone -= 1

        time.sleep(2)
        if pil == 1:
            usia = random.choice([2,3,3,4,4,4,5])
            pekerjaan = 30
        else:
            usia = random.choice([4,5])
            pekerjaan = random.choice([31,32,33])

        time.sleep(2)
        if domisili == 1:
            kab = 20
        else:
            kab = random.choice([6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29])

        time.sleep(2)
        checkboxes[0].click()

        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        radiobuttons[usia].click()
        radiobuttons[kab].click()
        radiobuttons[pekerjaan].click()

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

        if k10 != 0 and k20 != 0:
            jawabu = random.choice([2,3])
            if jawabu == 2:
                k10 -= 1
            else:
                k20 -= 1
        elif k10 != 0 and k20 == 0:
            jawabu = 2 
            k10 -= 1
        elif k10 == 0 and k20 != 0:
            jawabu = 3
            k20 -= 1

        time.sleep(2)
        if tertarik != 0 and ttertarik != 0 :
            jawabt = random.choice([0,1])
            if jawabt == 0:
                tertarik -= 1
            else:
                ttertarik -= 1
        elif tertarik != 0 and ttertarik == 0 :
            jawabt = 0 
            tertarik -= 1
        elif tertarik == 0 and ttertarik != 0 :
            jawabt = 1
            ttertarik -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[jawabt].click()
        radiobuttons[random.choice([2,3,4])].click()
        radiobuttons[jawabu + 3].click()
        radiobuttons[random.choice([10,11,11,12,13])].click()

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
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if range2 != 0 and range3 != 0:
            p = random.choice([1,2])
            if p == 1:
                range2 -= 1
            else:
                range3 -= 1
        elif range2 != 0 and range3 == 0:
            p = 1
            range2 -= 1
        elif range2 == 0 and range3 != 0:
            p = 2
            range3 -= 1

        time.sleep(2)
        soal = 6
        while soal:
            s1 = random.choice([p,p+1,p+2])
            testcheck[s1].click()
            p += 5
            soal -= 1

        radiobuttons[jawabt].click()
        radiobuttons[jawabu].click()

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
        driver.get("https://forms.gle/q2UsVzNTQhfP8ZK47")

        index+=1
        idx += 1
        idxx += 1
        print("==================")
        print("times : " + str(times))
        print("index : " + str(index))
        print("idx   : " + str(idx))
        print("idxx  : " + str(idxx))
        print("")
        print("mahasiswa : " + str(mahasiswa))
        print("tidak     : " + str(tidak))
        print("")
        print("bone  : " + str(bone))
        print("bbone : " + str(bbone))
        print("")
        print("range2 : " + str(range2))
        print("range3 : " + str(range3))
        print("")
        print("tertarik : " + str(tertarik))
        print("ttertarik : " + str(ttertarik))
        print("")
        print("k10  : " + str(k10))
        print("k20  : " + str(k20))

        times-=1
        print("")
finally:
    # driver.quit()
    print("berhasil")

        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()