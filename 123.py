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

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://forms.gle/VREgVUFBXgVH793z5")

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

#0 cowo 1 cewe
kelamin = [ 1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,
    1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
    0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,
    ]

soal = [8,5,5,5]

usia = 77
usialain = 14

positif = 0
negatif = 91

times = 91
index = 59

try:
    while times:
        time.sleep(5)
        #Hardcoded logic

        if usia != 0 and usialain != 0 :
            pil = random.choice([0,1])
        elif usia != 0 and usialain == 0 :
            pil = 0
        elif usia == 0 and usialain != 0 :
            pil = 1

        if pil == 0:
            umur = random.choice([5,6,7])
            usia -= 1
        else:
            umur = random.choice([2,3,4])
            usialain -= 1

        time.sleep(2)
        if umur == 2:
            pekerjaan = 8
            kategori = 19
        elif umur == 3:
            pekerjaan = 8
            kategori = random.choice([18,19,19,19])
        elif umur == 4:
            pekerjaan = 8
            kategori = 18
        elif umur == 5:
            pekerjaan = random.choice([8,9,9])
            kategori = 18
        elif umur == 6:
            pekerjaan = random.choice([9,9,9,10,12])
            kategori = 18
        elif umur == 7 and kelamin[index] == 1:
            pekerjaan = random.choice([9,10,11,12])
            kategori = random.choice([18,18,18,20])
        else :
            pekerjaan = random.choice([9,10,11,12])
            kategori = random.choice([18,18,18,20])

        time.sleep(2)
        if kategori == 18:
            genre = random.choice([13,14,15,16,13,14,15,16,13,14,15,16,13,14,15,16,17])
        elif kategori == 19:
            genre = random.choice([17,17,17,14,15])
        else:
            genre = random.choice([13,14,15,16,17])

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])

        time.sleep(2)
        radiobuttons[kelamin[index]].click()
        radiobuttons[umur].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[genre].click()
        radiobuttons[kategori].click()

        time.sleep(2)
        if positif != 0 and negatif != 0 :
            pil1 = random.choice([0,1])
        elif positif != 0 and negatif == 0 :
            pil1 = 0
        elif positif == 0 and negatif != 0 :
            pil1 = 1

        if pil1 == 0:
            for i in range(len(soal)):

                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

                time.sleep(3)
                radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

                p = 2
                for i in range(soal[i]):
                    s1 = random.choice([p,p,p,p,p,p,p+1,p+2])
                    time.sleep(1)
                    radiobuttons[s1].click()
                    p += 5

            positif -= 1
        else:
            for i in range(len(soal)):

                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

                time.sleep(3)
                radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

                p = 0
                for i in range(soal[i]):
                    s1 = random.choice([p,p,p,p,p,p,p+1,p+1,p+1,p+1,p+1,p+1,p+2])
                    time.sleep(1)
                    radiobuttons[s1].click()
                    p += 5

            negatif -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/VREgVUFBXgVH793z5")

        index+=1
        print("==================")
        print("usia     : " + str(usia))
        print("usialain : " + str(usialain))
        print("")
        print("positif : " + str(positif))
        print("negatif : " + str(negatif))
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