from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
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

email = [
    "email@gmail.com",
]

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

soal = [
    6,4,7
]

pertanyaan = [
    "Bagaimana pendapat Anda ketika di dorong untuk menggunakan aplikasi telemedicine terbaru?",
    "Menurut Anda, Bagaimana media sosial dapat mendorong atau mempengaruhi Anda dalam melakukan sesuatu?",
    "Apa faktor yang membuat Anda percaya bahwa layanan telemedicine yang Anda gunakan dapat diandalkan?",
    "Dalam pengalaman Anda, bagaimana perbandingan nilai dan biaya dari layanan aplikasi telemedicine dibandingkan dengan kunjungan langsung ke dokter atau fasilitas kesehatan?",
    "Apa yang memotivasi Anda untuk lebih sering menggunakan layanan telemedicine?",
    "Bisakah Anda menceritakan tentang pengalaman terakhir menggunakan layanan telemedicine dan bagaimana ini memenuhi kebutuhan Anda?",
]

jawaban = [
    [
        "1",
    ],
    [
        "2",
    ],
    [
        "3",
    ],
    [
        "4",
    ],
    [
        "5",
    ],
    [
        "6",
    ],
]

kategori = [
    11,0,89
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

def berikutnya() :
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

def polaJawab3(pola: int, awal: int, banyakSoal: int, kelipatan: int, jawab: list[WebElement]) :
    p = awal
    for i in range(banyakSoal) :
        if pola == 0 :
            s1 = random.choice([p,p,p,p+1,p+1,p+1,p+2])
        elif pola == 2 :
            s1 = random.choice([p,p+1,p+1,p+1,p+2,p+2,p+2])
        else :
            s1 = random.choice([p,p+1,p+2])

        jawab[s1].click()
        p += kelipatan

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
            tipeJawab = pilihTipe(kategori)
            kategori[tipeJawab] -= 1

            time.sleep(2)
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian

            textboxes[0].send_keys(email[index])

            berikutnya()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            radiobuttons[kelamin[index]].click()

            # disini
            #
            #

            for i in range(6) :
                berikutnya()

                time.sleep(3)
                textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

                polaJawab3(tipeJawab, tipeJawab, 3, 5, testcheck)

                time.sleep(1)
                textarea[0].send_keys(jawaban[i][index])

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
            print("")
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
