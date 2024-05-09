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
driver.get("https://forms.gle/MAdN9u2obNTbfeGV7")

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
]

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
]

#0 laki, 1 perempuan
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1]

times = 15
index = 0

baik = 12
jelek = 3

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        if kelamin[index] == 0:
            kelamin1 = random.choice(["laki","Laki","pria","Pria","cowo","Cowo","laki-laki","Laki-laki","Laki - Laki"])
        else:
            kelamin1 = random.choice(["perempuan","Perempuan","Cewe","cewe","Wanita","wanita"])

        fakultas = random.choice([1,2,3,4,5,6,7])

        if fakultas == 1:
            f1 = "Syariah dan Hukum"
            f2 = random.choice([
                "Hukum Keluarga Islam",
                "Hukum Pidana Islam",
                "Hukum Ekonomi Syariah",
                "Ilmu Falak",
                "Ilmu Hukum",
                ])
        elif fakultas == 2:
            f1 = "Ushuludin dan Humaniora"
            f2 = random.choice([
                "Aqidah Dan Filsafat Islam",
                "Studi Agama-Agama",
                "Ilmu Al-Qur'an Dan Tafsir",
                "Tasawuf Dan Psikoterapi",
                "Ilmu Seni Dan Arsitektur Islam",
                ])
        elif fakultas == 3:
            f1 = "Ilmu Tarbiyah dan Keguruan"
            f2 = random.choice([
                "Pendidikan Agama Islam",
                "Pendidikan Bahasa Arab",
                "Manajemen Pendidikan Isam",
                "Pendidikan Bahasa Inggris",
                "Pendidikan Guru Madrasah Ibtidaiyah (PGMI)",
                "Pendidikan Islam Anak Usia Dini (PIAUD",
                ])
        elif fakultas == 4:
            f1 = "Dakwah dan Komunikasi"
            f2 = random.choice([
                "Bimbingan Dan Penyuluhan Islam",
                "Komunikasi Dan Penyiaran Islam",
                "Manajemen Dakwah",
                "Pengembangan Masyarakat Islam",
                "Manajemen Haji Dan Umrah",
                ])
        elif fakultas == 5:
            f1 = "Ekonomi Dan Bisnis Islam"
            f2 = random.choice([
                "Ekonomi Islam",
                "Perbankan Syari'ah",
                "Akuntansi Syari'ah",
                "Manajemen",
                ])
        elif fakultas == 6:
            f1 = "Ilmu Sosial Dan Politik"
            f2 = random.choice([
                "Sosiologi",
                "Ilmu Politik",
                ])
        else:
            f1 = "Sains Dan Teknologi"
            f2 = random.choice([
                "Pendidikan Matematika",
                "Pendidikan Fisika",
                "Pendidikan Kimia",
                "Pendidikan Biologi",
                "Matematika",
                "Kimia",
                "Biologi",
                "Teknologi Informasi",
                "Teknik Lingkungan",
                ])

        awal = random.choice(["","Fakultas "])
        konjungsi = random.choice([", "," dan jurusan ",", jurusan "," jurusan "," dan prodi "," prodi ",", prodi "])
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(kelamin1)
        textboxes[2].send_keys(awal)
        textboxes[2].send_keys(f1)
        textboxes[2].send_keys(konjungsi)
        textboxes[2].send_keys(f2)
        textboxes[3].send_keys(telp[index])
        textboxes[4].send_keys(email[index])
        driver.implicitly_wait(4)
        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if baik != 0 and jelek != 0:
            time.sleep(2)
            s1 = random.choice([1,2])
            if s1 == 1:
                p1 = 0
                soal = 3
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                j1 = random.choice([13,14,14,14,15])
                testcheck[j1].click()

                p1 = 16
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                j1 = random.choice([26,27])
                testcheck[j1].click()
                j1 = random.choice([29,30,31])
                testcheck[j1].click()

                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

                time.sleep(2)
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

                p1 = 2
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 8
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 18
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 24
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 34
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                j1 = random.choice([40,41])
                testcheck[j1].click()

                p1 = 46
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 52
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                j1 = random.choice([62,63])
                testcheck[j1].click()

                j1 = random.choice([66,67])
                testcheck[j1].click()

                p1 = 70
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 76
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                baik -= 1
            else:
                p1 = 0
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                j1 = random.choice([8,9,10,11])
                testcheck[j1].click()
                j1 = random.choice([12,13])
                testcheck[j1].click()

                p1 = 18
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                j1 = random.choice([24,25])
                testcheck[j1].click()
                j1 = random.choice([28,29])
                testcheck[j1].click()

                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

                time.sleep(2)
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

                p1 = 0
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 10
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 16
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 26
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 32
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                j1 = random.choice([42,43])
                testcheck[j1].click()

                p1 = 44
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 54
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                j1 = random.choice([61,62])
                testcheck[j1].click()

                j1 = random.choice([66,67])
                testcheck[j1].click()

                p1 = 68
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                p1 = 78
                soal = 2
                while soal:
                    j1 = random.choice([p1,p1+1])
                    testcheck[j1].click()
                    soal -= 1
                    p1 += 4

                jelek -= 1
        elif baik != 0 and jelek == 0:
            time.sleep(2)
            p1 = 0
            soal = 3
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            j1 = random.choice([13,14,14,14,15])
            testcheck[j1].click()

            p1 = 16
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            j1 = random.choice([26,27])
            testcheck[j1].click()
            j1 = random.choice([29,30,31])
            testcheck[j1].click()

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p1 = 2
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 8
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 18
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 24
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 34
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            j1 = random.choice([40,41])
            testcheck[j1].click()

            p1 = 46
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 52
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            j1 = random.choice([62,63])
            testcheck[j1].click()

            j1 = random.choice([66,67])
            testcheck[j1].click()

            p1 = 70
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 76
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            baik -= 1
        else:
            time.sleep(2)
            p1 = 0
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            j1 = random.choice([8,9,10,11])
            testcheck[j1].click()
            j1 = random.choice([12,13])
            testcheck[j1].click()

            p1 = 18
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            j1 = random.choice([24,25])
            testcheck[j1].click()
            j1 = random.choice([28,29])
            testcheck[j1].click()

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p1 = 0
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 10
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 16
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 26
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 32
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            j1 = random.choice([42,43])
            testcheck[j1].click()

            p1 = 44
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 54
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            j1 = random.choice([61,62])
            testcheck[j1].click()

            j1 = random.choice([66,67])
            testcheck[j1].click()

            p1 = 68
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4

            p1 = 78
            soal = 2
            while soal:
                j1 = random.choice([p1,p1+1])
                testcheck[j1].click()
                soal -= 1
                p1 += 4
            jelek -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/MAdN9u2obNTbfeGV7")

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