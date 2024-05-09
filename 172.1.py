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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfOCh_5i_TaLCbqfzNTLqkSFJ-DdgTAYhtxoQm3uDXirU2L7A/formResponse?pli=1")


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


]

kelamin = [ 1,0,1,1,0,1,0,1,0,0,
            0,1,1,0,0,1,1,0,1,1,
            0,1,1,0,1,0,0,0,1,0,
            0,1,0,1,1,0,0,1,1,0,
            1,1,0,1,0,1,0,1,0,0,
            
            #50
            1,0,0,0,0,1,1,1,0,0,
            0,0,1,0,0,1,0,1,1,0,
            0,0,1,0,0,1,1,1,0,1,
            1,0,1,0,1,1,1,0,0,1,
            1,1,1,1,1,1,1,1,1,1,

            ]


index  = 49
times  = 51

try:
    while times:
        time.sleep(2)
        #Hardcoded logic
        test = 0

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        textboxes[0].send_keys(nama[index])
        alamat = random.choice(["Anjatan",
        "Anajatan Utara",
        "Anjatanbaru",
        "Bugis",
        "Bugis Tua",
        "Cilandak",
        "Cilandak Lor",
        "Kedungwungu",
        "Kopyah",
        "Lempuyang",
        "Mangunijaya",
        "Salamdarma",
        "Wanguk",
        "Bongas",
        "Cipaat",
        "Cipedang",
        "Kertajaya",
        "Kertamulya",
        "Margamulya",
        "Plawangan",
        "Sidamulya",
        "Babakan Jaya",
        "Drunten Kulon",
        "Drunten Wetan",
        "Kedokan Gabus",
        "Kedung Dawa",
        "Ranca Mulya",
        "Rancahan",
        "Sekar Mulya",
        "Balareja",
        "Bantarwaru",
        "Gantar",
        "Mekarjaya",
        "Mekarwaru",
        "Sanca",
        "Situraja",
        "Cipancuh",
        "Haurkolot",
        "Karangtumaritis",
        "Kertanegara",
        "Mekarjati",
        "Sidodadi",
        "Sukajati",
        "Sumbermulya",
        "Wanakaya",
        "Bulak",
        "Curug",
        "Eratan Kulon",
        "Eretan Wetan",
        "Ilir",
        "Karanganyar",
        "Karangmulya",
        "Kertawinangun",
        "Pareangirang",
        "Pranti",
        "Soge",
        "Wirakanan",
        "Wirapanjunan",
        "Jayamulya",
        "Kroya",
        "Sukaslamet",
        "Sukamelang",
        "Sumberjaya",
        "Sumbon",
        "Tamyangsari",
        "Tanjungkerta",
        "Temiyang",
        "Arjasari",
        "Umpas",
        "Mekarsari",
        "Patrol",
        "Patrol Baru",
        "Patrol Bugel",
        "Patrol Lor",
        "Sukahaji",
        "Bogor",
        "Karang Layung",
        "Sukra",
        "Sukra Wetan",
        "Sumuradem",
        "Sumuradem Timur",
        "Tagal Taman",
        "Ujunggebang"])
        textboxes[1].send_keys(alamat)

        checkboxes[kelamin[index]].click()
        umur = random.choice([2,3,4,2,3,4,2,3,4,5])
        checkboxes[umur].click()
        if umur == 2 :
            pendidikan = random.choice([7,8,9,8,9,9,9])
        else :
            pendidikan = random.choice([8,9,8,9,9,9])

        checkboxes[pendidikan].click()
        

        if pendidikan == 7 :
            pekerjaan = random.choice([13,13,13,14,15])
        elif pendidikan == 8 :
            pekerjaan = random.choice([11,11,11,13,15])
        else :
            pekerjaan = random.choice([12,13,15])

        checkboxes[pekerjaan].click()
        
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
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping



        p = 0
        soal = 12
        while soal :
            jawaban = random.choice([p+3,p+4])
            testcheck[jawaban].click()
            p += 5
            soal -= 1

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
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping



        p = 0
        soal = 8
        while soal :
            jawaban = random.choice([p+3,p+4])
            testcheck[jawaban].click()
            p += 5
            soal -= 1

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
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping



        p = 0
        soal = 6
        while soal :
            jawaban = random.choice([p+3,p+4])
            testcheck[jawaban].click()
            p += 5
            soal -= 1


        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfOCh_5i_TaLCbqfzNTLqkSFJ-DdgTAYhtxoQm3uDXirU2L7A/formResponse?pli=1")

        index+=1
        print("==================")
        
        times-=1
        print("index  = " + str(index))
        print("times  = " + str(times))
        time.sleep(5)





finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # radiobuttons = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

        # time.sleep(1)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()