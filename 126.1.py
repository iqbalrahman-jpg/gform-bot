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

profil = ["Profile 7", "Profile 8", "Profile 9", "Profile 10"]

nama = [
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Mutia Ayu Nur",

    "Bayu Danang Merta",
    "Bellanda Clara Ayunda ",
    "Budi Suryanto",
    "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Yuli Ayunda Dewi",

    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Attaka Majid",

    "Putri Keancana",
    "Raja Putra Wardanawan",
    "Affifah Rahman Nabila",
]

umur = [17,15,16,17,14,17,14,18,18,13,17,16,18,15,16,15,17,15,14,18,16,16,13,15,17,13,16,17,13,18,14,13,15,]

kelamin = [0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,]

pendidikan = [3,2,3,3,2,3,2,3,3,2,3,3,3,2,3,2,3,2,2,3,3,3,2,2,3,2,3,3,2,3,2,2,2,]

page = [
    [1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1],
    [3,3,3,1,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3],
    [0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2],
    [1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1],
    [1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1],
    [1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,2,1,1,1],
    [3,3,3,3,3,2,2,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,2,3,3,3,3,3],
    [1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1],
    [3,3,2,3,3,3,3,2,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3],
    [1,0,0,0,0,0,0,3,0,0,0,0,0,1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0],
]

alasan = [
    "Animasi nya lumayan bagus",
    "ada beberapa scene yang kurang natural tapi overall bagus",
    "dapat menjadi cerminan sejarah tragedi rengat berdarah",
    "butuh peningkatan di bagian mayat nya ",
    "penyampaian cerita di animasi nya cukup jelas dan dapat dipahami",
    "karakter nya banyak yang mirip, mungkin bisa dirubah",
    "ada greenscreen yang masih kelihatan di bagian meledak nya mungkin bisa di perbaiki lagi",
    "mantabbb",
    "suara nya kuraang besar",
    "animasi nya mudah dipahami",
    "mirip GTA san andreas tekstur animasi nya ",
    "Film pendek animasi nya bagus dijadikan bahan pembelajaran sejarah khusus nya warga lokal rengat karena animasinya mudah di pahami dan visualisasi yang ditampilkan lumayan bagus",
    "film nya bagus cerita nya menarik",
    "lagu nya terlalu besar suara nya mungkin bisa  dikecilkan lagi tapi bagus",
    "film yang membuat kita harus mengingat perjuangan pahlawan yang ada di rengat dan mendoakan untuk mereka",
    "saya baru tau cerita kematian bupati tulus difilm ini saya hanya tau nama jalan saja dulu, film ini bagus untuk menambah ilmu",
    "film pendek animasi ini bisa dijadikan media edukasi untuk masyarakat rengat",
    "cukup menarik",
    "perlu sedikit variasi di latar nya karena terasa sedikit ulang-ulang gitu, tapi bagus animasi nya",
    "editing lumayan bagus Cuma grading nya agak kurang",
    
    "menambah ilmu baru tentang sejarah kota rengat dulu ",
    "jarang ada yang buat konten animasi tentang rengat gini jadi perlu diperbanyak lagi seperti ini ",
    "suasana saat pembantaian warga rengat sangat menyedihkan ",
    "banyak pesan moral yang di dapatkan dari animasi ini semoga dapat lebih baik lagi kedepan nya",
    "pentempuran nya keren",
    "ada beberapa bagian yang harus nya ditambahkan pergerakan nya supaya bisa lebih sempurna animasinya",
    "gak ada ",
    "inspiratif",
    "agak kaku di beberapa bagian tapi ceritanya bagus",
    "bisa mengenang jasa para pahlawan yg telah gugur",
    "dapat dijadikan sebuah motivasi,agar remaja-remaja Rengat tetap mengenang sejarah Tragedi Rengat berdarah",
    "dapat meningkatkan awareness akan sejarah yang ada di rengat",
    "Semoga tidak terulang lagi",
]

index = 1
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://bit.ly/PostTestAnimasiRengatBerdarah")

        idx = 1

        if i == len(profil) - 1 :
            times = 3
        elif i == 0:
            times = 9
            idx = 2
        else:
            times = 10

        idxx = 1

        while times:
            time.sleep(2)

            if idx == 10:
                idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(10)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[idx].click()

            time.sleep(10)
            # ================================================================================

            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

            checkboxes[0].click()

            time.sleep(2)
            textarea[0].send_keys(alasan[index])

            time.sleep(2)
            textboxes[0].send_keys(nama[index])
            textboxes[1].send_keys(umur[index])

            time.sleep(2)
            radiobuttons[pendidikan[index]].click()
            radiobuttons[kelamin[index]].click()

            p = 4
            for i in range(10) :
                s1 = page[i][index] + p
                radiobuttons[s1].click()
                p += 4

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
            driver.get("https://bit.ly/PostTestAnimasiRengatBerdarah")

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))

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