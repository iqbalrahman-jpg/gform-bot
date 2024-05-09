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

link = "https://docs.google.com/forms/d/e/1FAIpQLScCQF28FhAbRqNfQvp5k8MTO99upazxqS1mRBLLvtBbbF-jbw/viewform"

profil = ["Default"]

nama = [
    "nama",
]

kelamin = [
    0
]

kategori = [
    [ 
        "akuntansi", "Akuntansi",
    ],
    [
        "administrasi Perkantoran", "Administrasi Perkantoran", "administrasi perkantoran", "Admin Perkantoran"
    ],
    [
        "tkj", "TKJ", "Tkj", "Teknik Komputer Jaringan", "Teknik komputer jaringan"
    ],
    [
        "multimedia", "Multimedia", "mulmed", "Mulmed"
    ],
    [
        "perhotelan", "Perhotelan", "PERHOTELAN"
    ],
]

soal = [
    [0,0,2,2,0,1,2,2,0,0,2,0,0,0,2,2,0,0,2,2,0,0,2,2,0,0,1,2,0,0,2,2,0,0,2,2,0,0,2,2,0,0,2,1,],
    [0,0,0,0,0,2,2,2,2,2,0,1,0,0,0,2,1,1,2,2,0,1,0,0,0,2,2,2,2,2,0,0,0,0,0,2,2,2,2,2,1,1,1,1,0,2,0,2,2,2,1,0,0,0,0,2,2,2,2,2,],
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

            umur = random.randint(16,19)
            tipeJurusan = random.randint(0,4)
            jurusan = random.choice(kategori[tipeJurusan])

            if umur == 16 :
                kelas = 2
            elif umur == 17 :
                kelas = random.choice([2,3,3])
            elif umur == 18 :
                kelas = random.choice([2,3,3,3,4])
            else :
                kelas = random.choice([3,4,4,4])

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            time.sleep(1)
            checkboxes[0].click()

            time.sleep(1)
            textboxes[0].send_keys(nama[index])
            textboxes[1].send_keys(umur)
            textboxes[2].send_keys(jurusan)

            time.sleep(2)
            radiobuttons[kelamin[index]].click()
            radiobuttons[kelas].click()

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

                time.sleep(2)
                radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

                p = 0
                for i in range(len(soal[i])) :
                    s = p + soal[i] 
                    s1 = random.choice([p,p+1,p+2,p+3]) if soal[i] == 1 else random.choice([s,s+1])
                    radiobuttons[s1].click()

                    p += 4

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
            driver.get(link)

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