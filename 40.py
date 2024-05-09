from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://forms.gle/dLN8EfqDnaUkuPfj6")

email = [
    "mtianur001@gmail.com",
    "alihasn.01.10@gmail.com",
    "risfebri11@gmail.com",
    "budprasety@gmail.com",
    "aryonugh@gmail.com",
    "nanissa0110@gmail.com",
    "yahnugrah@gmail.com",
    "putriptr0110@gmail.com",
    "nandayundaa1@gmail.com",
    "yudipradan01@gmail.com",
    "yulayund1@gmail.com",
    "byumerta1@gmail.com",
    "Bellandayu01@gmail.com",
    "budsuryant01@gmail.com",
    "nela.mirra@gmail.com",
    "dwa.lingga10@gmail.com",
    "alffiantoro@gmail.com",
    "annicsaa@gmail.com",
    "fataahxdewa@gmail.com",
    "diahcindy03@gmail.com",
    "attakmajid@gmail.com",
    "azzarinrst@gmail.com",
    "fabiannadeo@gmail.com",
    "niaejuliana@gmail.com",
    "bayudwiganara@gmail.com",
    "syifaradifah@gmail.com",
    "aditferdinanda@gmail.com",
    "sitifauziyyahh@gmail.com",
    "reyhanutomowa@gmail.com",
    "salmaarowaya@gmail.com",
    "anggasiregarp@gmail.com",
    "putrikeancana@gmail.com",
    "rajawardanawan@gmail.com",
    "affifahh7@gmail.com",
    "shakapwijaya@gmail.com",
    "cynnarafisa@gmail.com",
    "monahfnna87@gmail.com",
    "mahendrejaa@gmail.com",
    "fryshta.eka823@gmail.com",
    "yanrasuryad@gmail.com",
    "rahannadi1@gmail.com",
    "sutisnayun@gmail.com",
    "ayulistyaan@gmail.com",
    "muhh.santosoo@gmail.com",
    "rudinurbaktii01@gmail.com",
    "ptrawiraw.an@gmail.com",
    "agungnugh@gmail.com",
    "dn.ramadhan@gmail.com",
    "dimas.purbo07@gmail.com",
    "nabilla.s.qolbi@gmail.com"
]

nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Yuli Ayunda Dewi",
    "Bayu Danang Merta",
    "Bellanda Clara Ayunda", 
    "Budi Suryanto",
    "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Attaka Majid",
    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Angga Siregar Putra",
    "Putri Keancana",
    "Raja Putra Wardanawan",
    "Affifah Rahman Nabila",
    "Shaka Kurnia Wijaya",
    "Cynara Nafisah",
    "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
    "Fryshta Eka Nabilla",
    "Yanuar Suryadi",
    "Rayhan Adi Wicasa",
    "Sutisna Ayuni",
    "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Ardyanto Rizki Putra",
    "Putra Wirawan",
    "Agung Nugroho",
    "Dani Ramadhan",
    "Dimas Purbo",
    "Nabilla Syaqila Qolbi",
]

positif = 42
negatif = 8

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        pendidikan = random.choice([0,1,2,0,1,2,0,1,2,3])

        if pendidikan == 0:
            usia = random.choice([17,18])
        elif pendidikan == 1:
            usia = random.choice([18,19,20,21,22,23,24])
        elif pendidikan == 2:
            usia = random.choice([24,25,26])
        else:
            usia = random.choice([25,26,27])

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        textboxes[0].send_keys(email[index])
        textboxes[1].send_keys(nama[index])
        textboxes[2].send_keys(usia)
        driver.implicitly_wait(4)

        radiobuttons[pendidikan].click()
        radiobuttons[5].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        #positif 0 negatif 1
        if positif != 0 and negatif != 0:
            time.sleep(2)
            pil = random.choice([1,2])
            if pil == 1:
                temp = 0
            else:
                temp = 1
        elif positif != 0 and negatif == 0:
            temp = 0
        else:
            temp = 1

        #1,2,3
        t1 = [1,4,5,8,9,11,12,14,18,19,20,22,24,26,27,28,29,34,35,36,38,39,]
        #2,3,4
        t2 = [7,16,32,40]

        idxt1 = 0
        idxt2 = 0

        if temp == 0:
            p = 0
            soal = 39
            nosoal = 1
            while soal:
                if nosoal == t1[idxt1] :
                    s1 = random.choice([p,p+1,p+2])
                    testcheck[s1].click()
                    idxt1 += 1
                elif nosoal == t2[idxt2] :
                    s1 = random.choice([p+1,p+2,p+3])
                    testcheck[s1].click()
                    idxt2 += 1
                else:
                    s1 = random.choice([p+2,p+3,p+4])
                    testcheck[s1].click()

                soal -= 1
                nosoal += 1
                p += 5

            positif -= 1
        else:
            p = 0
            soal = 39
            nosoal = 1
            while soal:
                if nosoal == t1[idxt1] :
                    s1 = random.choice([p+2,p+3,p+4])
                    testcheck[s1].click()
                    idxt1 += 1
                elif nosoal == t2[idxt2] :
                    s1 = random.choice([p+1,p+2,p+3])
                    testcheck[s1].click()
                    idxt2 += 1
                else:
                    s1 = random.choice([p,p+1,p+2])
                    testcheck[s1].click()

                soal -= 1
                nosoal += 1
                p += 5

            negatif -= 1

        time.sleep(2)

        testcheck[65].click()
        testcheck[111].click()
        testcheck[147].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/dLN8EfqDnaUkuPfj6")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")

        times-=1
        print("times : " + str(times))
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