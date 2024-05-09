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
driver.get("https://forms.gle/aJ6WBkzTFyjh97bJ7")

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

#0 cowo 1 cewe
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,]

page1 = [
    [4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5,4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5],
    [5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4],
    [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4],
    [4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4,4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4],
    [5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4,5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4],
]

page2 = [
    [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4],
    [4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5],
    [4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5,4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5],
]

page3 = [
    [4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5,4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4],
    [5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4],
    [5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4],
    [4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5,4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3],
]

page4 = [
    [5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5],
    [5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3],
    [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4],
    [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4],
]

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        usia = random.choice([2,3,4,5,6])

        time.sleep(2)
        if usia == 2:
            pekerjaan = random.choice([7,8,9,10,7,8,9,10,7,8,9,10,11])
        else:
            pekerjaan = random.choice([8,9,10,8,9,10,8,9,10,8,9,10,11])

        time.sleep(2)
        if pekerjaan == 2:
            penghasilan = random.choice([13,13,14])
        else:
            penghasilan = random.choice([14,15,16,17])

        time.sleep(2)
        if penghasilan <= 2:
            pakai = random.choice([18,18,19,20])
        else:
            pakai = random.choice([18,19,20,20,21,21,22])

        time.sleep(2)
        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        radiobuttons[usia].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[penghasilan].click()
        radiobuttons[pakai].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = -1
        for i in range(5):
            s1 = page1[i][index] + p
            radiobuttons[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = -1
        for i in range(3):
            s1 = page2[i][index] + p
            radiobuttons[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = -1
        for i in range(4):
            s1 = page3[i][index] + p
            radiobuttons[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = -1
        for i in range(4):
            s1 = page4[i][index] + p
            radiobuttons[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/aJ6WBkzTFyjh97bJ7")

        index+=1
        print("==================")
        # print("  : " + str())
        # print("")
        
        times-=1
        print("index  : " + str(index))
        print("")
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