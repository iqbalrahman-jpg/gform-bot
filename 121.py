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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc0HS9TGn_gI8KpTFmSbLvLDqFvGw_uLENHcGUIKjiRI84OQw/viewform?usp=pp_url")

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
    "nabilla.s.qolbi@gmail.com",
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

p = [0,1,1,2,2,2,2,2,2,2,]

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(email[index])
        textboxes[1].send_keys(nama[index])

        time.sleep(2)
        radiobuttons[random.choice([0,1,2,3])].click()
        radiobuttons[random.choice([5,6,7,8,9])].click()
        radiobuttons[11].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p2 = 0
        for i in range(3) :
            p1 = p[i] + p2
            s1 = random.choice([p1,p1+1])
            testcheck[s1].click()
            p2 += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p2 = 0
        for i in range(3) :
            p1 = p[i+3] + p2
            s1 = random.choice([p1,p1+1])
            testcheck[s1].click()
            p2 += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p2 = 0
        for i in range(4) :
            p1 = p[i+6] + p2
            s1 = random.choice([p1,p1+1])
            testcheck[s1].click()
            p2 += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[random.choice([0,1,2])].click()

        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc0HS9TGn_gI8KpTFmSbLvLDqFvGw_uLENHcGUIKjiRI84OQw/viewform?usp=pp_url")

        index+=1
        print("==================")
        # print("  : " + str())
        # print("")
        
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