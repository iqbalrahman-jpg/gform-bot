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
driver.get("https://docs.google.com/forms/d/1Udfuo414Hdev8TZzgewji1Rw-dhi0oxSNhso-y9FB_8")

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
    "Eka Wahyu",
    "Yuli Setiawan",
    "Eko Wijaya",
    "Yuni Nafisah",
    "Prita agustina",
    "Naufal Ardiansyah",
    "Bagus Rahmad",
    "Hana Anissa Herian",
    "Heraldy Gunawan",
    "Budi Santoso",
    "Bagus Hariawan",
    "Dwi Panca",
    "Okto Devano",
    "Olivia Niken",
    "Yazid Hasbilluh Kurniawan",
    "faradilla nina",
    "Shabir Maulana",
    "Sarah Husaini",
    "Anindya Riri",
    "Erfina Pratiwi",
    "Argo Prasetyawan",
    "Salma Azizah",
    "Faradilla Aulia",
    "Dimas Wahyu",
    "Regina Cantika Subandini",
    "Agis Prasetya",
    "Ardy Riski",
    "Muhammad Fadlan",
    "Septinia Kurniawan",
    "Damar Eka",
    "Fredinan Puan",
    "Amanda Bella Putri",
    "Bambang Suhatmoyo",
    "Kairaini Aliesa",
    "Lika Arletta",
    "Arjuna Ghafur",
    "Damar Hafidzhuan",
    "Lista Kamilla",
    "Sadiva Pratiwi",
    "Hermanto Caisar",
    "Windy Cantika",
    "Stephani Amanda Safitri",
    "Ardyanto Putra Wardhana",
    "Windy Putri Sentosa",
    "Nabil Saputra",
    "Khansa Azzahra",
    "Naufal Azwin",
    "Riska Rahmawati",
    "Rohmat Ubaidillah",
    "Setiawan Nugraha",
]

times = 78
index = 22

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        radiobuttons[random.choice([0,1,1,1,1,2])].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 10
        while soal :
            s1 = random.choice([p,p+1,p+2,p+3,p+4])
            if s1 < p+2:
                l = p+5
                s2 = random.choice([l,l+1])
            elif s1 > p+2:
                l = p+8
                s2 = random.choice([l,l+1])
            else:
                l = p+5
                s2 = random.choice([l,l+1,l+2,l+3,l+4])

            testcheck[s1].click()
            testcheck[s2].click()
            p += 10
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 10
        while soal :
            s1 = random.choice([p,p+1,p+2,p+3,p+4])
            if s1 < p+2:
                l = p+5
                s2 = random.choice([l,l+1])
            elif s1 > p+2:
                l = p+8
                s2 = random.choice([l,l+1])
            else:
                l = p+5
                s2 = random.choice([l,l+1,l+2,l+3,l+4])

            testcheck[s1].click()
            testcheck[s2].click()
            p += 10
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/1Udfuo414Hdev8TZzgewji1Rw-dhi0oxSNhso-y9FB_8")

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