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
driver.get("http://bit.ly/46QuCtG")

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
    "bella.rahhma@gmail.com",
    "ptrawiraw.an@gmail.com",
    "agungnugh@gmail.com",
    "dn.ramadhan@gmail.com",
    "cyntttayu@gmail.com",
    "nabilla.s.qolbi@gmail.com",
]

nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Nur Indah Budi Pratiwi",
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
    "Febi Putri Nadeo",
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
    "Shakira Putri Wijaya Kusuma",
    "Cynara Nafisah",
    "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
    "Fryshta Eka Nabilla",
    "Yaniar Ayunda Surya",
    "Rayhan Adi Wicasa",
    "Sutisna Ayuni",
    "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Bella Clarissa Rahma",
    "Putri Awirsya Rawadianti",
    "Agung Nugroho",
    "Dani Ramadhan",
    "Cintya Ayu Dewi",
    "Nabilla Syaqila Qolbi",
]

kelamin = [
    1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,1,
]

pekerjaan = [10, 20, 5, 5, 0, 5, 5]

positif = 45
negatif = 5

times = 50
index = 0

try:
    while times:
        time.sleep(2)
        samples = []
        print(samples)

        for i in range(len(pekerjaan)) :
            if pekerjaan[i] != 0 :
                samples.append(i)
            
        jobs = random.sample(samples, 1)
        for i in jobs :
            jobs = i
            jobsIdx = i + 2

        pekerjaan[jobs] -= 1

        time.sleep(2)

        if jobsIdx == 2:
            usia = random.randint(17, 19)
        elif jobsIdx == 3:
            usia = random.randint(18, 24)
        elif jobsIdx == 4:
            usia = random.randint(21, 27)
        elif jobsIdx == 5:
            usia = random.randint(22, 27)
        elif jobsIdx == 6:
            usia = random.randint(24, 27)
        elif jobsIdx == 7:
            usia = random.randint(20, 27)
        else:
            usia = random.randint(17, 27)
        
        if jobsIdx == 5 :
            kali = 9
        else:
            kali = random.randint(9, 12)

        time.sleep(2)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(email[index])
        textboxes[1].send_keys(nama[index])
        textboxes[2].send_keys(usia)

        checkboxes[kelamin[index]].click()
        checkboxes[jobsIdx].click()
        checkboxes[kali].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if positif != 0 and negatif != 0 :
            pil = random.choice([0, 1])
        elif positif != 0 and negatif == 0 :
            pil = 0
        elif positif == 0 and negatif != 0 :
            pil = 1

        time.sleep(2)
        p = 2
        for i in range(13) :
            s1 = random.choice([p, p+1, p+1, p+1, p+2, p+2, p+2])
            testcheck[s1].click()
            p += 5
        
        if pil == 0 :
            positif -= 1
        else:
            testcheck[31].click()
            testcheck[36].click()
            negatif -= 1
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 2
        for i in range(11) :
            s1 = random.choice([p, p+1, p+1, p+1, p+2, p+2, p+2])
            testcheck[s1].click()
            p += 5
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 2
        for i in range(8) :
            s1 = random.choice([p, p+1, p+1, p+1, p+2, p+2, p+2])
            testcheck[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("http://bit.ly/46QuCtG")

        index+=1
        print("==================")
        print("positif = " + str(positif))
        print("negatif = " + str(negatif))
        print("")
        print("pekerjaan = " + str(pekerjaan))
        print("")

        times-=1
        print("index  : " + str(index))
        print("times  : " + str(times))
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