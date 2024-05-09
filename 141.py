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

profil = ["Profile 7", "Profile 8", "Profile 9"]

nama = [
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Mutia Ayu Nur",

    "Bayu Danang Merta",
    "Bellanda Clara Ayunda ",
    "Budi Suryanto",
    "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Yuli Ayunda Dewi",

    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Attaka Majid",
]

notelp = [
    "085719303458",
    "085694967112",
    "087771034388",
    "085691005874",
    "081316619265",
    "081807757031",
    "087884291109",
    "087734232521",
    "083831978961",
    "085817281922",

    "085772067944",
    "085780272919",
    "085711503322",
    "083899226851",
    "081296660892",
    "083879828932",
    "085328666691",
    "085716463668",
    "081310967642",
    "089602615268",

    "085740420953",
    "085786378946",
    "089929069068",
    "082299476447",
    "083870192449",
    "087730874992",
    "081381810073",
    "085777737195",
    "081219725497",
    "082310667325",
]

kelamin = [0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0]

positif = 23
negatif = 0

index = 7
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeVSFj_1C1Mjj8-k4YWJheb68R26lzoY69Fyyy0Q4tgBcuncQ/viewform")

        if i == 0:
            idx = 8
            times = 3
        else:
            idx = 1
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
            radiobuttons[idx].click()

            time.sleep(10)
            # ================================================================================

            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            textboxes[0].send_keys(nama[index])
            radiobuttons[kelamin[index]].click()
            usia = random.randint(22,37)
            textboxes[1].send_keys(usia)
            if usia <= 25 :
                radiobuttons[2].click()
            elif usia <= 32 :
                lama = random.choice([2,3,3,3,4])
                radiobuttons[lama].click()
            else :
                lama = random.choice([3,4,4])
                radiobuttons[lama].click()

            posisi = random.choice(["Staff Accounting", "Staff Finance", "Staff", "Staff accounting", "Staff finance", "staff", "staff accounting", "staff finance"])
            textboxes[2].send_keys(posisi)
            textboxes[3].send_keys(notelp[index])
            checkboxes[0].click()

            if positif != 0 and negatif != 0 :
                jawaban = random.choice([1,1,1,2])
                if jawaban == 1 :
                    indikator = 1
                    soal = 60
                    p = 0
                    while soal :
                        jawab = random.choice([p+1,p+2,p+3,p+2,p+3,p+2,p+3])
                        testcheck[jawab].click()
                        soal -= 1
                        p += 4
                    positif -= 1
                else :
                    indikator = 2
                    soal = 60
                    p = 0
                    while soal :
                        jawab = random.choice([p,p+1,p+2,p+1,p+2])
                        testcheck[jawab].click()
                        soal -= 1
                        p += 4
                    negatif -= 1
            elif positif == 0 :
                indikator = 2
                soal = 60
                p = 0
                while soal :
                    jawab = random.choice([p,p+1,p+2,p+1,p+2])
                    testcheck[jawab].click()
                    soal -= 1
                    p += 4
                    negatif -= 1
            elif negatif == 0 :
                indikator = 1
                soal = 60
                p = 0
                while soal :
                    jawab = random.choice([p+1,p+2,p+3,p+2,p+3,p+2,p+3])
                    testcheck[jawab].click()
                    soal -= 1
                    p += 4
                positif -= 1

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
            driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeVSFj_1C1Mjj8-k4YWJheb68R26lzoY69Fyyy0Q4tgBcuncQ/viewform")

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))
            print("")
            print("positif = " + str(positif))
            print("negatif = " + str(negatif))

        driver.quit()
        
finally:
    # driver.quit()
    print("berhasil")

            # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
            # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
            # textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            # textpil = driver.find_elements("css selector", ".whsOnd")#isianpilihan

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