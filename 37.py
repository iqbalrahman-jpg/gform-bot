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
driver.get("https://bit.ly/kuesionermhsrantau")

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
    "nabilla.s.qolbi@gmail.com"
]

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

#jabodetabek
univ = [
    "UI",
    "UGM",
    "Universitas Bina Nusantara",
    "Institut Teknologi Bandung",
    "UNTAR",
    "UPH",
    "Universitas Trisakti",
    "Universitas Pancasila",
    "Universitas Mercu Buana",
    "UAJY",
    "UMN",
    "Universitas Gunadarma",
    "Universitas Kristen Petra",
    "Universitas Katolik Parahyangan",
    "UNAS",
    "UNPAD",
    "Universitas Mercu Buana",
    "Universitas Kristen Maranatha",
    "UMN",
    "UNISBA",
    "Universitas Negeri Jakarta",
    "UAJ",
    "Universitas Kristen Duta Wacana",
    "Universitas Kristen Satya Wacana",
    "UPB",
    "Universitas Paramadina",
    "Universitas Kristen Krida Wacana",
    "UNTIRTA",
    "Universitas Jenderal Soedirman",
    "Universitas Muhammadiyah Jakarta",
    "Universitas Prof. Dr. Moestopo",
    "UPN Veteran",
    "UI",
    "BINUS",
    "Universitas Tarumanagara",
    "Universitas Trisakti",
    "Universitas Pancasila",
    "Universitas Mercu Buana",
    "Universitas Gunadarma",
    "Universitas Kristen Petra",
    "UNPAR",
    "UI",
    "Universitas Bina Nusantara",
    "UNTAR",
    "Universitas Trisakti",
    "Universitas Pancasila",
    "Universitas Mercu Buana",
    "Universitas Gunadarma",
    "UNAS",
    "Universitas Trisakti",
]

# isi prodi sesuai angka

# 2  Akuntansi
# 3  Arsitektur
# 4  Desain Komunikasi Visual
# 5  Desain Produk
# 6  Ilmu Komunikasi
# 7  Manajemen
# 8  Psikologi
# 9  Sistem Informasi
# 10 Teknik Informatika
# 11 Teknik Sipil

#0 laki, 1 perempuan
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,]

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(email[index])
        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        usia = random.randint(18,20)
        pulau = random.randint(13,19)
        prodi = random.randint(2,11)

        if pulau == 13:
            prov = random.choice([
                    "Aceh",
                    "Sumatera Utara",
                    "Sumatera Barat",
                    "Riau",
                    "Kepulauan Riau",
                    "Jambi",
                    "Bengkulu",
                    "Sumatera Selatan",
                    "Lampung",
                    "Bangka Belitung",
                ])
        elif pulau == 14:
            prov = random.choice([
                    "Kalimantan Barat",
                    "Kalimantan Tengah",
                    "Kalimantan Selatan",
                    "Kalimantan Timur",
                    "Kalimantan Utara",
                ])
        elif pulau == 15:
            prov = random.choice([
                    "Sulawesi Utara",
                    "Sulawesi Tengah",
                    "Sulawesi Selatan",
                    "Sulawesi Tenggara",
                    "Sulawesi Barat",
                    "Gorontalo",
                ])
        elif pulau == 16:
            prov = random.choice([
                    "Papua",
                    "Papua Barat"
                ])
        elif pulau == 17:
            prov = "Bali"
        elif pulau == 18:
            prov = random.choice([
                    "Pulau Ambon",
                    "Pulau Seram",
                    "Pulau Ternate",
                    "Pulau Tidore",
                    "Pulau Banda",
                    "Pulau Buru",
                    "Pulau Kai",
                    "Pulau Lease",
                    "Pulau Saparua",
                    "Pulau Nusa Laut",
                ])
        else :
            prov = random.choice([
                    "Nusa Tenggara Barat (NTB)",
                    "NTB",
                    "Nusa Tenggara Timur (NTT)",
                    "NTT",
                ])

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[1].send_keys(nama[index])
        textboxes[2].send_keys(usia)
        textboxes[3].send_keys(univ[index])
        textboxes[4].send_keys(prov)
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        radiobuttons[prodi].click()
        radiobuttons[pulau].click()
        radiobuttons[20].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        #1,2
        t1 = [2,3,4,6,10,11,12,15,16,17,18,24,27,29,32,37]
        #2,3,4
        t2 = [7,8,13,23,37]
        #1,2,3
        t3 = [21,34,37]
        #1,2,3,4
        t4 = [28,37]

        idxt1 = 0
        idxt2 = 0
        idxt3 = 0
        idxt4 = 0

        p = 0
        soal = 36
        nosoal = 1
        while soal:
            if nosoal == t1[idxt1]:
                s1 = random.choice([p,p+1])
                testcheck[s1].click()
                idxt1 += 1
            elif nosoal == t2[idxt2]:
                s1 = random.choice([p+1,p+2,p+3])
                testcheck[s1].click()
                idxt2 += 1
            elif nosoal == t3[idxt3]:
                s1 = random.choice([p,p+1,p+2])
                testcheck[s1].click()
                idxt3 += 1
            elif nosoal == t4[idxt4]:
                s1 = random.choice([p,p+1,p+2,p+3])
                testcheck[s1].click()
                idxt4 += 1
            else:
                s1 = random.choice([p+2,p+3])
                testcheck[s1].click()

            soal -= 1
            nosoal += 1
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        #1,2,3
        k1 = [1,4,6,8,20,21,24,37]
        #2,3,4
        k2 = [7,13,15,16,25,37]
        #1,2,3,4,5
        k3 = [2,3,10,11,18,37]

        idxk1 = 0
        idxk2 = 0
        idxk3 = 0

        p = 0
        soal = 26
        nosoal = 1
        while soal:
            if nosoal == k1[idxk1]:
                s1 = random.choice([p,p+1,p+2])
                testcheck[s1].click()
                idxk1 += 1
            elif nosoal == k2[idxk2]:
                s1 = random.choice([p+1,p+2,p+3])
                testcheck[s1].click()
                idxk2 += 1
            elif nosoal == k3[idxk3]:
                s1 = random.choice([p,p+1,p+2,p+3,p+4])
                testcheck[s1].click()
                idxk3 += 1
            else:
                s1 = random.choice([p+2,p+3,p+4])
                testcheck[s1].click()

            soal -= 1
            nosoal += 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[1].click()

        time.sleep(3)
        submit_button = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")

        submit_button[1].click()

        driver.implicitly_wait(4)
        driver.get("https://bit.ly/kuesionermhsrantau")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")

        times-=1
        print("times : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()