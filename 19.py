from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://bit.ly/SKRIPSI_FAJAR")

nama = [
    "Ali Hasanudin",
    "Rizki Bagas Febri",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Yahya Nugraha",
    "Nanda Nurahmad",
    "Yudi Pradanawan",
    "Bayu Danang Merta",
    "Budi Suryanto",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Fattahilah Sadewa",
    "Attaka Majid",
    "Fabian Nadeo Putra",
    "Bayu Dwiganara",
    "Aditya Derdinand",
    "Reyhan Utomowa",
    "Angga Siregar Putra",
    "Raja Putra Wardanawan",
    "Shaka Kurnia Wijaya",
    "Mahendra Rhejaa Fadilah",
    "Yanuar Suryadi",
    "Muhammad Hafidz",
    "Ahmad Syahrul",
    "Dian Agus",
    "Irfan Hakim",
    "Rizky Maulana",
    "Rian Pratama",
    "Fajar Gunawan",
    "Alvin Aditya",
]

telp = [
    "084624253733",
    "088565440513",
    "083626799003",
    "088070442682",
    "083435047182",
    "089579629094",
    "080103002233",
    "086659262105",
    "087136378661",
    "080640301967",
    "083806763847",
    "088509885576",
    "084985961237",
    "086137328130",
    "089843988039",
    "086738422620",
    "089045039379",
    "087788078906",
    "088159431881",
    "089474988296",
    "088530547344",
    "085109243357",
    "080470592685",
    "083273198985",
    "081850592479",
    "081211906212",
    "081212784008",
    "081250284950",
    "081264718461",
    "081280281529",

]

times = 30
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(telp[index])

        driver.implicitly_wait(4)

        usia = random.choice([0,1,2,3,4])
        time.sleep(1)
        radiobuttons[usia].click()
        radiobuttons[5].click()

        if usia == 0 or usia == 1:
            time.sleep(2)
            pendidikan = random.choice([7,8])
            radiobuttons[pendidikan].click()
        else:
            time.sleep(2)
            pendidikan = random.choice([7,8,8,8,9,9,9,10])
            radiobuttons[pendidikan].click()

        time.sleep(1)
        radiobuttons[13].click()
        radiobuttons[14].click()
        radiobuttons[15].click()
        pengguna = random.choice([17,18])
        radiobuttons[pengguna].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p1 = 0
        soal = 6
        while soal:
            s1 = random.choice([p1,p1,p1,p1+1,p1+1,p1+1,p1+1,p1+2])
            radiobuttons[s1].click()
            soal -= 1
            p1 += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        bag = 2
        while bag:
            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            p1 = 0
            soal = 4
            while soal:
                s1 = random.choice([p1,p1,p1,p1+1,p1+1,p1+1,p1+1,p1+2])
                radiobuttons[s1].click()
                soal -= 1
                p1 += 4
            bag -= 1
            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p1 = 0
        soal = 3
        while soal:
            s1 = random.choice([p1,p1,p1,p1+1,p1+1,p1+1,p1+1,p1+2])
            radiobuttons[s1].click()
            soal -= 1
            p1 += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p1 = 0
        soal = 5
        while soal:
            s1 = random.choice([p1,p1,p1,p1+1,p1+1,p1+1,p1+1,p1+2])
            radiobuttons[s1].click()
            soal -= 1
            p1 += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p1 = 0
        soal = 8
        while soal:
            s1 = random.choice([p1,p1,p1,p1+1,p1+1,p1+1,p1+1,p1+2])
            radiobuttons[s1].click()
            soal -= 1
            p1 += 4

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
        driver.get("https://bit.ly/SKRIPSI_FAJAR")

        index+=1
        print("==================")
        print("index : " + str(index))
        

        times-=1
        print("times : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()