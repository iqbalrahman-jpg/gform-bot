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

link = "https://docs.google.com/forms/d/e/1FAIpQLSe-Omw1EAXl83vNOiSKpflB73iNMpV9gYTgxcJhvRoBdtD7Uw/viewform?pli=1"

profil = ["Profile 106", "Profile 107", "Profile 6"]

nama = [
    "Yuli Setiawan",
    "Eko Wijaya",
    "Yuni Nafisah",
    "Prita agustina",
    "Naufal Ardiansyah",
    "Hana Anissa Herian",
    "Heraldy Gunawan",
    "Eka Wahyu",
    "Bagus Rahmad",
    "Budi Santoso",

    "Dwi Panca",
    "faradilla nina",
    "Erfina Pratiwi",
    "Yazid Hasbilluh Kurniawan",
    "Bagus Hariawan",
    "Josephine Anindya",
    "Sarah Husaini",
    "Shabir Maulana",
    "Olivia Niken",
    "Gita Permata",

    "Argo Prasetyawan",
    "Salma Azizah",
    "Faradilla Aulia",
    "Dimas Wahyu",
    "Regina April",
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
    "Caroline Putri",
    "Nabil Saputra",
    "Khansa Azzahra",
    "Naufal Azwin",
    "Riska Rahmawati",
    "Rohmat Ubaidillah",
    "Setiawan Nugraha",

    "Anastasya Raisha",
    "Rakha Bumi",
    "Fikky Devano Purwanto",
    "Lesmana Dewa",
    "Ilyasa Fadil",
    "Belinda Inggridina Amelia",
    "Putri Bella Kartika",
    "Meydina Margaretha",
    "Muhammad Wawan",
    "Budiman Yahya Pradana",

    "Yahya Budiman",
    "Farhan Nurrahman",
    "Sisca Pratiwi",
    "Ahmad Fioren",
    "Alif Ramadhan",
    "Divani Permatasari",
    "Angga Dewangga",
    "Sasya Putri",
    "Selma Nabila Hayati",
    "Iwan Setiawan",

    "Rafi Fadhil Athalla",
    "Jonathan Putra",
    "Karina Aulia",
    "Diyastra Mahendra",
    "Agung Prasetya",
    "Aulia Lita Hani",
    "Sifa Nada",
    "Hani Salsabila",
    "Denis Prasetya kurniawan",
    "Griska Adelina Septinia",

    "Niara Rahmadhani",
    "Fajar Wijaya",
    "Anissha Fitrianni",
    "Galih Wibowo",
    "Rahma Aulia",
    "Maya Dewi",
    "Dhesy Lestari",
    "Rizky Firdaus",
    "Ditho Prasetyo",
    "Amanda Putri",

    "Karina Tiyas",
    "Abhista Deana",
    "Juana Noelle",
    "Jasmine Hanura",
    "Santiawati Agustina",
    "Pawitri Sari",
    "Yusti Fanggraeni",
    "Pamela Audine",
    "Anisha Pranaya",
    "Keita Pramudya",

    "Haris Cristopher",
    "Sinta Cintia",
    "Toni Sucipto",
    "Hani Baharani",
    "Ruli Abdhi",
    "Vidi Pratama",
    "Azzahra Fitriana",
    "Ilham Maulana",
    "Mayya Fitri",
    "Romadhon Ramzy",
]

kelamin = [
    1,0,1,1,0,1,0,1,0,0,
    0,1,1,0,0,1,1,0,1,1,
    0,1,1,0,1,0,0,0,1,0,
    0,1,0,1,1,0,0,1,1,0,
    1,1,0,1,0,1,0,1,0,0,

    # 50
    1,0,0,0,0,1,1,1,0,0,
    0,0,1,0,0,1,0,1,1,0,
    0,0,1,0,0,1,1,1,0,1,
    1,0,1,0,1,1,1,0,0,1,
    1,1,1,1,1,1,1,1,1,1,


    # 100
    0,1,0,1,0,0,1,0,1,0,
]

kategori = [
    24,0,46
]

jurusan = [
    9,12,11,13,12,13
]

soal = [
    6,4,7
]

index = 0

def pilihanCheck(awal, akhir, banyak) :
    listData = []
    i = awal
    while i <= akhir :
        listData.append(i)
        i += 1

    return random.sample(listData, banyak)

def pilihTipe(data) -> int :
    datar = []
    for i in range(len(data)) :
        if data[i] != 0 :
            datar.append(i)

    return random.sample(datar, 1)[0]

try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\ACER\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\1.KERJOAN\\bot\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get(link)

        if i == 0 :
            times = 10
            idx = 1
        else :
            times = 10
            idx = 1

        idxx = 1

        while times:
            time.sleep(2)

            if idx == 10:
                idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(5)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[idx].click()

            time.sleep(5)
            # ================================================================================
            umur = random.randint(20,36)
            tipeJurusan = pilihTipe(jurusan)
            jurusan[tipeJurusan] -= 1

            jml = random.randint(1,4)
            check = pilihanCheck(0,4,jml)

            tipeJawab = pilihTipe(kategori)
            kategori[tipeJawab] -= 1

            time.sleep(3)
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            checkboxes[0].click()
            checkboxes[1].click()

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            textboxes[0].send_keys(nama[index])
            textboxes[1].send_keys(umur)

            time.sleep(1)
            radiobuttons[kelamin[index]].click()
            radiobuttons[tipeJurusan + 2].click()
            radiobuttons[8].click()
            radiobuttons[random.randint(9,12)].click()
            radiobuttons[13].click()

            time.sleep(1)
            for i in check :
                checkboxes[i].click()

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            radiobuttons[0].click()

            for j in range(len(soal)) :

                time.sleep(3)
                kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
                kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

                if len(kirims1) != 0 :
                    submit_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                    )
                else:
                    submit_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                    )

                submit_button.click()

                time.sleep(2)
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

                i = tipeJawab
                for k in range(soal[j]) :
                    s1 = random.choice([i,i+1])
                    testcheck[s1].click()

                    i += 4

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
            driver.get(link)

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("kategori = " + str(kategori))
            print("jurusan = " + str(jurusan))

            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))

        driver.quit()

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
