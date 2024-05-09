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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfFMsSVLwK4CK6UZo_F1oKtvepfncmxhf17NwBXJEsP6EB01A/viewform?usp=pp_url")

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

    "ekawahy0099@gmail.com",
    "yulisetiawan746@gmail.com",
    "ekow05047@gmail.com",
    "yuninafisah9@gmail.com",
    "agustinaprita304@gmail.com",
    "naufalardiansyah651@gmail.com",
    "bagusrahmad262@gmail.com",
    "hanaanissa33@gmail.com",
    "heraldygunawan@gmail.com",
    "budisantos0@gmail.com",
    "bagushari931@gmail.com",
    "dwipancaa65@gmail.com",
    "oktonadevi@gmail.com",
    "ooliviya96@gmail.com",
    "yahhszid@gmail.com",
    "f.ninadilaa@gmail.com",
    "shabirmaulana23@gmail.com",
    "srhhusaini@gmail.com",
    "anindya.riri@gmail.com",
    "erfinpp34@gmail.com",
    "argopraz@gmail.com",
    "azizahsalma237@gmail.com",
    "faradillaaulia62@gmail.com",
    "dimaswahyu4769@gmail.com",
    "reginacantika663@gmail.com",
    "agisprasetya171@gmail.com",
    "arddyriski@gmail.com",
    "fadlaanm24@gmail.com",
    "kurniaseptinia@gmail.com",
    "damarek099@gmail.com",
    "freddinan35@gmail.com",
    "manndabeel99@gmail.com",
    "bambang.suhatmoyo@gmail.com",
    "aliesakairaini@gmail.com",
    "lika.arletta@gmail.com",
    "arjuna.gh9@gmail.com",
    "dhafidzuann@gmail.com",
    "listakamila299@gmail.com",
    "sadivapratiwi0@gmail.com",
    "hermantocaisar@gmail.com",
    "windycantika13@gmail.com",
    "stephaniamanda67@gmail.com",
    "ardyantoputra43@gmail.com",
    "maryldaputri_@gmail.com",
    "saputranabil157@gmail.com",
    "azzahrakhansa006@gmail.com",
    "naufalazwin85@gmail.com",
    "riskarahmawati400@gmail.com",
    "rohmatubaidillah3@gmail.com",
    "setiawannugraha372@gmail.com",
]

nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Bagas Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Yuli Ayunda Dewi",
    "Bayu Danang Merta",
    "Bella Clara Nur Ayunda", 
    "Budi Suryanto",
    "Miranda Nella Safitri",
    "Sadewa Lingga Budiantoro",
    "M. Alffianto Kuntoro",
    "Annisa Chania Salsabila",
    "Fattahilah Bagas Nurahmad",
    "Diah Ayu Cindy",
    "Attaka Majid",
    "Azzahra Risti Nabila",
    "Fabian Nadeo Putra",
    "Nia Eka Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Angga Siregar Putra",
    "Putri Keancana Adisti",
    "Raja Putra Rahman",
    "Affifah Rahman Nabila",
    "Shaka Kurnia Ramadhan",
    "Cynara Nafisah",
    "Mona Nur Hadfinna",
    "Muhammad Mahendra Fadilah",
    "Friska Sabil Nabilla",
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
    "Marylda Putri Sentosa",
    "Nabil Saputra",
    "Khansa Azzahra",
    "Naufal Azwin",
    "Riska Rahmawati",
    "Rohmat Ubaidillah",
    "Setiawan Nugraha",
]

dom = [7,5,12,0,1]

sudah = 50
belum = 50

times = 100
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0
        domisili = []

        for i in range(5):
            if dom[i] != 0:
                domisili.append(i+5)

        time.sleep(2)
        wilayah = random.choice(domisili)
        dom[wilayah-5] -= 1

        usia = random.choice([0,1,2,3,4])

        if usia == 0:
            pekerjaan = random.choice([11,13,13,13])
        else:
            pekerjaan = random.choice([10,11,12])

        time.sleep(2)
        if sudah != 0 and belum != 0:
            pil = random.choice([15,16])
            if pil == 15:
                sudah -= 1
            else:
                belum -= 1
        elif sudah != 0 and belum == 0:
            pil = 15 
            sudah -= 1 
        elif sudah == 0 and belum != 0:
            pil = 16
            belum -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(email[index])
        textboxes[1].send_keys(nama[index])
        driver.implicitly_wait(4)

        radiobuttons[usia].click()
        radiobuttons[wilayah].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[pil].click()
        radiobuttons[random.choice([17,18,19,20])].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 2
        soal = 6
        while soal:
            s1 = random.choice([p,p+1])
            testcheck[s1].click()
            p += 4
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 2
        soal = 20
        while soal:
            s1 = random.choice([p,p+1])
            testcheck[s1].click()
            p += 4
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfFMsSVLwK4CK6UZo_F1oKtvepfncmxhf17NwBXJEsP6EB01A/viewform?usp=pp_url")

        times-=1
        index+=1
        print("==================")
        print("dom : " + str(dom))
        print("")
        print("sudah : " + str(sudah))
        print("belum : " + str(belum))
        print("")
        
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