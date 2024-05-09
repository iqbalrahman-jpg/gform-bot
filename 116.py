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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfB2J_XG1lPkuODps6lZ1xGy1Oj3rJ-3XADimc_3UAUpqDlpQ/viewform")

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
    
    "Maya Dara Putri",
    "Rio Fajar Pratama",
    "Dewi Sari Wijaya",
    "Agung Kusuma Jaya",
    "Ratih Suci Lestari",
    "Rizki Pratama Nugraha",
    "Dwi Prasetya Utama",
    "Arif Rahman Hakim",
    "Intan Ayu Lestari",
    "Ananda Dwi Wicaksono",
    "Fira Nur Hidayah",
    "Rama Aditya Wardhana",
    "Cinta Ayu Dewanti",
    "Ade Kurniawan Saputra",
    "Mira Fitriana Wati",
    "Dian Kusuma Wardani",
    "Budi Santoso Putra",
    "Rina Nuraini Sari",
    "Ahmad Fauzi Akbar",
    "Rizky Ananda Pratama",
    "Maya Dewi Sari",
    "Dwi Kusuma Jaya",
    "Agung Santosa Nugroho",
    "Dila Yuliani Wati",
    "Andi Muhammad Rizal",
    "Budi Santoso",
    "Rina Permata Sari",
    "Dian Nugroho",
    "Rudi Setiawan",
    "Maya Putri Lestari",
    "Andi Prasetyo",
    "Sinta Utami Sari",
    "Rizky Ramadhan",
    "Eka Puspita Dewi",
    "Dika Setiawan Pratama",
    "Rani Fitriani",
    "Dito Prasetya",
    "Nisa Indah Sari",
    "Rizal Pratama",
    "Tiara Dewi Puspita",
    "Yanto Wibowo",
    "Nina Anggraini",
    "Yoga Putra Wijaya",
    "Dini Cahyani",
    "Raka Triyana",
    "Maya Dewi Utami",
    "Indra Kusuma",
    "Devi Puspitasari",
    "Bima Aditya Nugraha",
    "Rina Anggraini Sari",
]

#0 cowo 1 cewe
kelamin = [
    1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,
    1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1
    ]

page = [
    [
        [4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5,4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5,5,5,4,4,4,4,3,4,5,5,5,3,2,5,4,5,4,5,5,4,5,4,5,5,4,5,5,4,2,4,5,5,4,5,4,5,4,5,4,5],
        [5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,4,4,5,4,5,3,4,4,4,5,5,2,3,5,5,5,4,5,4,3,4,4,5,4,5,5,5,4,3,5,5,5,3,5,4,4,3,5,4,4],
        [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,4,5,5,4,3,3,3,4,4,5,5,3,2,5,4,5,4,5,5,3,5,4,5,5,5,5,5,5,2,5,5,5,4,5,4,5,4,5,4,5],
        [4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4,4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4,4,4,4,4,4,4,4,4,4,4,5,2,3,4,5,5,4,3,5,4,4,4,5,4,4,4,3,5,3,4,4,4,4,5,4,4,3,4,4,5],
        [5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4,5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4,4,4,5,4,3,4,4,4,4,5,5,2,2,5,4,5,4,5,5,4,4,3,5,4,4,5,5,4,2,5,5,5,4,5,4,5,3,5,4,5],
        [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,4,4,5,4,5,3,4,4,4,4,5,2,2,5,4,5,4,5,5,3,5,4,5,5,5,5,5,4,2,5,5,5,4,5,4,5,4,5,4,4],
    ],[
        [4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,5,4,4,4,5,4,4,4,4,5,5,2,3,5,4,5,4,5,5,4,5,4,5,5,4,5,5,4,3,4,5,5,4,5,4,4,4,5,4,5],
        [4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5,4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5,5,4,4,4,4,4,3,3,4,5,5,3,3,4,3,5,3,4,5,4,5,4,5,5,3,5,4,4,3,4,5,4,3,5,3,4,3,5,4,4],
        [4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5,4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5,4,4,4,4,5,3,4,4,4,5,5,2,4,5,4,5,4,4,4,3,5,4,5,5,5,5,4,4,4,4,5,5,4,5,4,4,4,4,4,4],
        [5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,4,4,5,4,4,4,4,4,4,4,5,2,3,4,5,5,4,4,4,4,4,4,5,4,4,5,4,5,3,5,5,4,4,5,4,4,4,5,4,5],
        [4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5,4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5,3,4,4,4,4,4,5,4,4,5,5,2,2,5,4,5,3,5,5,4,5,5,5,5,4,5,5,3,2,4,5,5,3,5,4,5,3,5,4,5],
        [5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4,5,5,5,4,4,4,4,4,4,5,5,3,3,5,5,5,4,5,4,4,4,3,5,4,5,5,5,5,3,5,5,5,4,5,4,5,4,5,4,5],
    ],[ 
        [5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,3,5,5,4,5,3,3,4,5,5,5,2,2,4,4,5,4,4,5,3,4,4,5,4,4,5,4,4,2,5,5,4,3,5,4,5,3,5,4,4],
        [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,4,5,5,4,3,3,3,4,4,5,5,3,2,5,4,5,4,5,5,3,5,4,5,5,5,5,5,5,2,5,5,5,4,5,4,5,4,5,4,5],
        [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,4,4,5,4,5,3,4,4,4,4,5,2,2,5,4,5,4,5,5,3,5,4,5,5,5,5,5,4,2,5,5,5,4,5,4,5,4,5,4,4],
        [5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,4,4,5,4,5,3,4,4,4,5,5,2,3,5,5,5,4,5,4,3,4,4,5,4,5,5,5,4,3,5,5,5,3,5,4,4,3,5,4,4],
        [4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,5,4,4,4,5,4,4,4,4,5,5,2,3,5,4,5,4,5,5,4,5,4,5,5,4,5,5,4,3,4,5,5,4,5,4,4,4,5,4,5],
        [5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,4,4,5,4,4,4,4,4,4,4,5,2,3,4,5,5,4,4,4,4,4,4,5,4,4,5,4,5,3,5,5,4,4,5,4,4,4,5,4,5],
    ]
]

# soal = [6,6,6]

times = 100
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        pendidikan = random.choice([6,7,8,8,8])

        if pendidikan == 8 :
            pekerjaan = random.choice([10,11,13])
        else:
            pekerjaan = random.choice([10,12,13])

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        textboxes[0].send_keys(nama[index])
        time.sleep(2)

        radiobuttons[kelamin[index]].click()
        radiobuttons[pendidikan].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[15].click()

        for i in range(3):
            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            if i == 0 :
                time.sleep(2)
                checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

                checkboxes[0].click()

            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p = -1
            for x in range(6):
                s1 = page[i][x][index] + p
                testcheck[s1].click()
                p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfB2J_XG1lPkuODps6lZ1xGy1Oj3rJ-3XADimc_3UAUpqDlpQ/viewform")

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