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
driver.get("https://forms.gle/JhhvzSKsoXtb69kt8")

nama = [
	   "Mutia Ayu Nur",
    "Ali Hasanudin",
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
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
        "Annisa Chania",
    "Fattahilah Sadewa",
    "Attaka Majid",
        "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Bayu Dwiganara",
        "Diah Ayu Cindy",
    "Aditya Derdinand",
    "Reyhan Utomowa",
        "Salma Arowaya",
    "Angga Siregar Putra",
    "Raja Putra Wardanawan",
    "Shaka Kurnia Wijaya",
    "Mahendra Rhejaa Fadilah",
    "Yanuar Suryadi",
        "Miranda Nella",
    "Rayhan Adi Wicasa",
    "M. Putra Susanto",
    "Ardyanto Rizki Putra",
    "Putra Wirawan",
    "Agung Nugroho",
        "Riskia Ayu Febrianti",
    "Dani Ramadhan",
    "Dimas Purbo",
        "Syifa Radifah",
    "Rio Fajar Pratama",
    "Agung Kusuma Jaya",
        "Siti Fauziyah",
    "Rizki Pratama Nugraha",
    "Dwi Prasetya Utama",
    "Arif Rahman Hakim",
        "Nia EKa Yuliana",
    "Ananda Dwi Wicaksono",
    "Rama Aditya Wardhana",
    "Ade Kurniawan Saputra",
]

#0 laki 1 perempuan
kelamin = [1,0,0,0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0]

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        usia = random.choice([1,2,3])

        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(4)

        radiobuttons[usia].click()
        radiobuttons[kelamin[index]+4].click()
        radiobuttons[6].click()
        radiobuttons[random.choice([8,9])].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 2
        soal = 5
        while soal:
            s1 = random.choice([p,p+1])
            testcheck[s1].click()
            soal -= 1
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        bag = 2
        while bag:
            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p = 2
            soal = 3
            while soal:
                s1 = random.choice([p,p+1])
                testcheck[s1].click()
                soal -= 1
                p += 4

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()
            bag -= 1

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 2
        soal = 5
        while soal:
            s1 = random.choice([p,p+1])
            testcheck[s1].click()
            soal -= 1
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/JhhvzSKsoXtb69kt8")

        index+=1
        print("==================")
        print("index  : " + str(index))
        print("")

        times-=1
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