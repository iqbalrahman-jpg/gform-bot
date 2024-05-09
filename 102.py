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

profil = ["Profile 9"]

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
]

domisili = [
    "surabaya",
    "surabaya",
    "Surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "sidosermo",
    "surabaya",
    "surabaya",
    "sidoarjo",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "sidoarjo",
    "surabaya",
    "gresik",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",
    "surabaya",

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

# perusahaan ===============================
induk = [
    "CV. Tunjang Langit",
    "CV. Wisma Podo Rukun",
    "Vennyma CV",
    "Bank Bumi Daya Tower",
    "CV. Simo Gunung Indah CV",
    "CV. Palung Buana",
    "CV. Dwi Putra Karya",
    "CV. Prima Cipta",
    "CV. Lintas Lautan",
    "PT Mulia Mukti",
    "Terus Jaya .CV",
    "Digahayu Manufacturing CO. CV",
    "Bumi Persada CV",
    "CV. De Bough Indonesia",
    "CV Bina Laut Pangan",
    "Sabrahamas CV.",
    "CV. Yala Pinasti",
    "PT Kusuma Jaya",
    "Bintang Jaya CV.",
    "CV. Bina Persada Timur",
    "CV. Bina Usaha",
    "Seger Abadi Utama. CV",
    "Modern CV",
    "Indradhanu. CV",
    "Koesno & Son. CV",
    "Alfa Retailindo, PT. Tbk",
    "CV. Mitra Usaha",
    "CV. Sertindo Utama",
    "PT. Purnomo Sejati",
    "PT. Purnomo Sejati",
]

# 0 pt, 1 cv, 2 firma
bentukinduk = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

bidanginduk = [
    "Media Cetak",
    "konstruksi dan material bangunan",
    "industri tembakau",
    "makanan ternak",
    "usaha manufaktur dan perdagangan rokok",
    "industri tembakau",
    "makanan ternak",
    "properti",
    "makanan ternak",
    "industri es krim",
    "Media Cetak",
    "media",
    "industri baja",
    "konstruksi dan material bangunan",
    "properti",
    "logam",
    "Industri galangan kapal",
    "industri suku cadang sepeda motor",
    "media",
    "industri tembakau",
    "perdagangan kayu",
    "pengolahan dan pengemasan makanan daging",
    "Media Cetak",
    "konveksi",
    "Industri galangan kapal",
    "makanan ternak",
    "perdagangan kayu",
    "industri es krim",
    "media",
    "Industri galangan kapal",
]

tahuninduk = [
    "1949",
    "1962",
    "1962",
    "2006",
    "1930",
    "1962",
    "2006",
    "1982",
    "2006",
    "1972",
    "1949",
    "2014",
    "1976",
    "1962",
    "1982",
    "1989",
    "1939",
    "1983",
    "2014",
    "1962",
    "1998",
    "2005",
    "1949",
    "2008",
    "1939",
    "2006",
    "1998",
    "1972",
    "2014",
    "1939",
]

anak = [
    "desain grafis",
    "mebel dan funiture",
    "toko kelontong",
    "frozen food",
    "kiraishop",
    "toko kelontong",
    "toko buah",
    "loolly Store",
    "online shop",
    "toko serba ada",
    "pentol kabul",
    "mapple management",
    "the floriest",
    "mebel dan funiture",
    "Café N Resto",
    "Texa Kriya Logam",
    "online shop",
    "ossvariasi, online shop",
    "desain grafis",
    "toko klontong",
    "mebel dan funiture",
    "Moi Kitchen and Frozen Food",
    "toko kelontong",
    "Resto Ayam Penyet",
    "kedai mie ayam - gofood",
    "frozen food",
    "mebel dan funiture",
    "toko serba ada",
    "desain grafis",
    "online shop",
]

# 0 PT, 1 CV, 2 FIRMA, 3 PERORANGAN
bentukanak = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]

bidanganak = [
    "media cetak",
    "properti",
    "toko ritel",
    "makanan",
    "industri makanan",
    "ritel",
    "ritel",
    "Kerajinan Tangan",
    "online shop",
    "bisnis ritel",
    "makanan",
    "media informasi dan promosi",
    "toko bunga",
    "properti",
    "industri kuliner",
    "industri dan kerajinan logam",
    "online shop",
    "otomotif",
    "media",
    "ritel",
    "kerajinan kayu",
    "makanan",
    "ritail",
    "kuliner",
    "industri makanan",
    "makanan",
    "kerajinan kayu",
    "bisnis ritel",
    "media",
    "online shop",
]

tahunanak = [
    "2016",
    "2021",
    "2020",
    "2018",
    "2017",
    "2020",
    "2022",
    "2020",
    "2021",
    "2002",
    "2021",
    "2022",
    "2017",
    "2020",
    "2012",
    "2008",
    "2021",
    "2019",
    "2018",
    "2020",
    "2020",
    "2020",
    "2020",
    "2013",
    "2021",
    "2018",
    "2020",
    "2002",
    "2018",
    "2021",
]

alasananak = [
    "keahlian yang ada dapat dimanfaatkan untuk membuka bisnis yang dapat dikerjakan paruh waktu",
    "membuka cabang bisnis di bidang yang sama",
    "membuka bisnis yang dapat dijalankan oleh keluarga sendiri",
    "dengan bantuan supply bahan dari teman menjadi reseller dirumah dan mengisi waktu luang",
    "ingin berbisnis dengan ikuti trend yang viral sekarang",
    "franchies ",
    "membuat toko yang mudah dikelola sendiri dengan pegawai",
    "adanya pandemi akhirnya membuka usaha baru secara online",
    "ingin mencoba mengembangkan bisnis ke ranah online",
    "usaha yang mudah dan aman dilakukan dan dapat dijaga oleh keluarga",
    "franchies yang murah dan mudah di buka dan dikelola",
    "bisnis yang dapat dijalankan secara online dan dapat dilakukan di waktu senggang",
    "mencoba bisnis tanpa turun tangan langsung, hanya memantau dan menggunakan pegawai",
    "membuka cabang bisnis di bidang yang sama, namun dalam skala yang lebih kecil",
    "ingin mencoba bisnis dibidang lain, dengan ilmu yang ada",
    "bahan awal berasal dari bisnis sendiri, sehingga lebih mudah untuk memulai dan mengembangkan bisnis",
    "ingin mencoba bisnis pada ranah online, dan juga sekaligus mengembangkan bisnis",
    "menyalurkan hobi dan keinginan berbisnis",
    "menyalurkan hobi yang sekaligus dapat menghasilkan",
    "bisnis yang dijalankan dari jauh tanpa harus datang / menjaga setiap saat",
    "dengan bakat yang dimiliki mmebuka bisnis sampingan untuk menambah penghasilan",
    "bisnis online yang dapat dilakukan oleh ibu rumah tangga ",
    "adayang wabah pandemi yang akhirnya membuat keuangan sulit dan harus mencari jalan keluar lainnya dengan membuka bisnis toko ",
    "mengembangkan bisnis ke ranah lain dengan modal resep keluarga",
    "menambah penghasilan melalui keahlian",
    "dengan bantuan supply bahan dari teman menjadi reseller dirumah dan mengisi waktu luang",
    "dengan bakat yang dimiliki mmebuka bisnis sampingan untuk menambah penghasilan",
    "usaha yang mudah dan aman dilakukan dan dapat dijaga oleh keluarga",
    "menyalurkan hobi yang sekaligus dapat menghasilkan",
    "ingin mencoba bisnis pada ranah online, dan juga sekaligus mengembangkan bisnis",
]

#0 cowo 1 cewe
kelamin = [0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0]

page1 = [
    [5,4,4,5,4,5,4,5,5,5,4,5,3,2,5,4,5,4,3,4,5,5,4,4,4,3,2,5,5,4],
    [5,4,3,4,4,4,4,5,5,5,3,4,4,3,4,4,5,4,4,4,5,4,4,3,4,4,3,5,4,3],
    [5,4,4,4,4,5,4,5,5,5,4,5,4,2,5,4,5,4,4,4,5,4,4,3,3,4,2,5,5,3],
    [5,4,4,4,4,5,4,5,5,5,4,4,4,2,4,4,5,4,4,4,5,5,4,4,4,4,2,5,5,4],
    [5,5,3,5,3,4,4,5,4,4,3,4,3,2,4,3,5,4,3,4,5,4,5,4,3,3,2,5,4,4],
    [5,4,3,5,4,5,4,5,5,5,3,5,3,2,5,4,5,4,3,4,5,5,4,4,4,3,2,5,5,4],
]
page2 = [
    [5,4,4,4,5,5,4,5,5,5,4,5,4,3,5,5,5,4,4,4,4,5,4,4,4,4,3,4,5,4],
    [5,4,4,5,5,5,4,5,5,5,4,5,4,3,5,5,5,4,4,4,5,4,4,3,4,4,3,5,5,3],
    [5,4,4,4,4,4,4,5,4,4,4,5,4,3,5,4,5,4,4,4,4,4,4,4,4,4,3,4,4,4],
    [5,4,3,4,5,4,3,5,4,4,3,4,3,3,4,5,5,3,3,3,4,5,4,4,3,3,3,4,4,4],
    [5,4,4,5,5,5,4,5,5,5,4,5,4,3,5,5,5,4,4,4,5,4,4,3,4,4,3,5,5,3],
]
page3 = [
    [4,4,4,4,4,3,4,4,4,4,4,5,4,3,5,4,5,4,4,4,4,4,4,4,3,4,3,4,3,4],
    [5,4,4,4,4,5,4,5,5,5,4,4,4,2,4,4,5,4,4,4,5,5,4,4,4,4,2,5,5,4],
    [5,4,4,4,5,5,4,5,5,5,4,5,4,3,5,5,5,4,4,4,4,5,4,4,4,4,3,4,5,4],
    [5,4,3,4,4,4,4,5,5,5,3,4,4,3,4,4,5,4,4,4,5,4,4,3,4,4,3,5,4,3],
]
page4 = [
    [5,4,3,4,5,4,3,5,4,4,3,4,3,3,4,5,5,3,3,3,4,5,4,4,3,3,3,4,4,4],
    [5,4,4,4,5,5,4,5,5,5,4,5,4,3,5,5,5,4,4,4,4,5,4,4,4,4,3,4,5,4],
    [5,4,4,4,4,4,4,5,4,4,4,5,4,3,5,4,5,4,4,4,4,4,4,4,4,4,3,4,4,4],
    [5,4,4,4,4,5,4,5,5,5,4,4,4,2,4,4,5,4,4,4,5,5,4,4,4,4,2,5,5,4],
]
page5 = [
    [5,4,4,4,5,5,4,5,5,5,4,5,4,3,5,5,5,4,4,4,4,5,4,4,4,4,3,4,5,4],
    [5,4,3,4,4,5,4,5,5,5,3,4,4,3,4,4,5,4,4,4,4,4,4,4,3,4,3,4,5,4],
    [5,5,4,5,5,5,4,5,5,5,4,5,3,2,5,5,5,4,3,4,5,5,5,4,4,3,2,5,5,4],
]
page6 = [
    [5,4,4,5,4,5,4,5,5,5,4,5,3,2,5,4,5,4,3,4,5,5,4,4,4,3,2,5,5,4],
    [5,4,4,4,4,4,4,5,5,5,4,4,4,4,4,4,5,4,4,4,4,5,4,4,4,4,4,4,4,4],
    [4,4,4,4,4,3,4,4,4,4,4,5,4,3,5,4,5,4,4,4,4,4,4,4,3,4,3,4,3,4],
    [5,4,4,5,4,5,4,5,5,5,4,5,3,2,5,4,5,4,3,4,5,5,4,4,4,3,2,5,5,4],
    [5,4,3,4,4,5,4,5,5,5,3,4,4,3,4,4,5,4,4,4,4,4,4,4,3,4,3,4,5,4],
    [5,4,3,4,3,5,4,5,5,5,3,5,5,2,5,3,5,3,5,3,5,5,4,5,3,5,2,5,5,5],
]
page7 = [
    [5,4,4,5,4,5,4,5,5,5,4,5,3,2,5,4,5,4,3,4,5,5,4,4,4,3,2,5,5,4],
    [5,4,4,4,4,5,4,5,5,5,4,4,4,2,4,4,5,4,4,4,5,5,4,4,4,4,2,5,5,4],
    [5,4,3,5,4,5,4,5,5,5,3,5,3,2,5,4,5,4,3,4,5,5,4,4,4,3,2,5,5,4],
    [5,4,4,4,4,5,4,5,5,5,4,4,4,2,4,4,5,4,4,4,5,5,4,4,4,4,2,5,5,4],
    [5,4,4,4,4,4,4,5,5,5,4,4,4,4,4,4,5,4,4,4,4,5,4,4,4,4,4,4,4,4],
]
page8 = [
    [5,4,4,4,4,4,4,5,4,4,4,5,4,3,5,4,5,4,4,4,4,4,4,4,4,4,3,4,4,4],
    [5,4,3,5,4,5,4,5,5,5,3,5,3,2,5,4,5,4,3,4,5,5,4,4,4,3,2,5,5,4],
    [5,5,4,5,5,5,4,5,5,5,4,5,3,2,5,5,5,4,3,4,5,5,5,4,4,3,2,5,5,4],
    [5,4,3,4,3,5,4,5,5,5,3,5,5,2,5,3,5,3,5,3,5,5,4,5,3,5,2,5,5,5],
    [5,4,3,4,4,5,4,5,5,5,3,4,4,3,4,4,5,4,4,4,4,4,4,4,3,4,3,4,5,4],
]

index = 25
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf0QFF5TzDiPnbs_YnCZ-RbWZidEK_2q9bA_jWBLxs3xmDo2w/viewform?usp=sf_link")

        times = 5

        idx = 6
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

            usia = random.randint(30,45)

            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            textboxes[0].send_keys(nama[index])
            textboxes[1].send_keys(usia)
            textboxes[2].send_keys(domisili[index])
            textboxes[3].send_keys(telp[index])
            driver.implicitly_wait(4)

            checkboxes[kelamin[index]].click()

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
            omset = random.choice([4,5,6])
            jabataninduk = random.choice(["Manager", "CEO", "Pemilik Saham", "Pegawai", "Marketing", "Manajemen"])

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            textpil = driver.find_elements("css selector", ".Hvn9fb")#isianpilihan
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

            textboxes[0].send_keys(induk[index])
            textboxes[1].send_keys(bidanginduk[index])
            textboxes[2].send_keys(tahuninduk[index])
            textboxes[3].send_keys(jabataninduk)
            textboxes[4].send_keys("1")
            textboxes[5].send_keys(anak[index])
            textboxes[6].send_keys(bidanganak[index])
            textboxes[7].send_keys(tahunanak[index])
            driver.implicitly_wait(4)
            
            textarea[0].send_keys(alasananak[index])
            driver.implicitly_wait(4)

            radiobuttons[bentukinduk[index]].click()
            radiobuttons[omset].click()

            time.sleep(2)
            if bentukanak[index] == 0:
                s1 = 7
            elif bentukanak[index] == 1:
                s1 = 8
            elif bentukanak[index] == 2:
                s1 = 9
            else:
                s1 = 10
                textpil[1].send_keys("perorangan")

            time.sleep(2)
            radiobuttons[s1].click()

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

            p = -1
            for i in range(6):
                s1 = page1[i][index] + p
                testcheck[s1].click()
                p += 5

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

            p = -1
            for i in range(5):
                s1 = page2[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(4):
                s1 = page3[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(4):
                s1 = page4[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(3):
                s1 = page5[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(6):
                s1 = page6[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(5):
                s1 = page7[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(5):
                s1 = page8[i][index] + p
                testcheck[s1].click()
                p += 5

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
            driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf0QFF5TzDiPnbs_YnCZ-RbWZidEK_2q9bA_jWBLxs3xmDo2w/viewform?usp=sf_link")

            index += 1
            idx += 1
            idxx += 1
            times -= 1
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
            # textpil = driver.find_elements("css selector", ".whsOnd")#isianpilihan

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