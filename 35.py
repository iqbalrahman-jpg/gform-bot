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
driver.get("https://bit.ly/Skripsi_Chrisen")

nama = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
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
]

telp = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
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

email = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
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
]

perusahaan = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "Traveloka",
    "Tokopedia",
    "Gojek",
    "Sale Stock",
    "Zilingo",
    "Kredivo",
    "Sayurbox",
    "KliknKlin",
    "Fore Coffee",
    "BliBli",
    "DANA",
    "Kopi Kenangan",
    "Advotics",
    "Qoala",
    "Zenius",
    "Sayurbox",
    "Traveloka",
    "Ruangguru",
    "Gojek",
    "BliBli",
    "CekAja",
    "Kopi Kenangan",
    "Warung Pintar",
    "Kedai Sayur",
    "Belibeli",
    "Kedai Sayur",
    "Gojek",
    "Tokopedia",
    "Traveloka",
    "Traveloka",

]

domisili = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    
    "Jakarta Selatan",
    "Jakarta Pusat",
    "Jakarta Selatan, DKI Jakarta",
    "Jakarta Selatan",
    "Jakarta Pusat, DKI Jakarta",
    "Jakarta Pusat, DKI Jakarta",
    "Jakarta Selatan",
    "Jakarta Pusat",
    "Jakarta Selatan, DKI Jakarta",
    "Tangerang, Banten",
    "DKI Jakarta",
    "Tangerang, Banten",
    "Jakarta Selatan",
    "Jakarta Pusat",
    "Jakarta Selatan, DKI Jakarta",
    "Jakarta Selatan",
    "Tangerang, Banten",
    "Tangerang",
    "Tangerang",
    "Tangerang",
    "Tangerang",
    "Tangerang",
    "Bogor, Jawa Barat",
    "Bekasi",
    "Bekasi, Jawa Barat",
    "Bekasi",
    "Tangerang",
    "Jakarta Pusat",
    "Tangerang",
    "Tangerang, Banten",

]

#0 perempuan 1 laki
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,]

p = [[4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5,4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5],
     [5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4],
     [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5],
     [4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4,4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4],
     [5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4,5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4],
     [4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4],
     [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5],
     [4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5],
     [4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5,4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5],
     [4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5,4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5],
     [5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5],
     [5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4],
     [4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5,4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5],
     [5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4],
     [5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4],
     [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5],
     [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5],
     [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5],
     [5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4],
     [4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5],
     [5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5],
     [5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4]]

k = [[2,1,2,2,2,1,2,3,1,1,1,2,2,1,2,2,3,1,2,1,1,1,2,4,1,1,1,1,2,1,2,1,2,2,2,1,2,3,1,1,1,2,2,1,2,2,3,1,2,1,1,1,2,4,1,1,1,1,2,1],
     [1,2,1,1,1,1,3,2,1,2,2,2,2,1,2,3,4,1,3,2,2,2,2,3,1,1,1,2,2,2,1,2,1,1,1,1,3,2,1,2,2,2,2,1,2,3,4,1,3,2,2,2,2,3,1,1,1,2,2,2],
     [1,1,3,2,1,1,2,3,1,1,2,2,2,1,2,3,3,1,2,2,1,2,1,4,1,1,1,1,2,1,1,1,3,2,1,1,2,3,1,1,2,2,2,1,2,3,3,1,2,2,1,2,1,4,1,1,1,1,2,1],
     [2,2,2,1,2,2,2,2,2,1,3,2,2,1,2,2,4,2,3,2,2,2,1,3,2,1,3,1,2,2,2,2,2,1,2,2,2,2,2,1,3,2,2,1,2,2,4,2,3,2,2,2,1,3,2,1,3,1,2,2],
     [2,1,2,3,1,1,3,2,1,2,3,2,2,1,2,2,4,1,2,2,2,2,2,3,1,1,2,2,3,2,2,1,2,3,1,1,3,2,1,2,3,2,2,1,2,2,4,1,2,2,2,2,2,3,1,1,2,2,3,2],
     [2,2,1,2,2,1,2,2,1,1,2,2,2,1,2,2,4,1,2,1,2,2,2,3,1,1,1,1,2,1,2,2,1,2,2,1,2,2,1,1,2,2,2,1,2,2,4,1,2,1,2,2,2,3,1,1,1,1,2,1],
     [2,2,2,3,3,2,3,3,1,2,2,2,3,1,3,2,3,1,3,1,2,2,2,3,1,1,2,1,2,1,2,2,2,3,3,2,3,3,1,2,2,2,3,1,3,2,3,1,3,1,2,2,2,3,1,1,2,1,2,1],
     [1,1,3,2,1,1,3,3,1,1,2,2,2,1,2,2,3,1,2,2,1,2,1,4,1,1,1,1,2,1,1,1,3,2,1,1,3,3,1,1,2,2,2,1,2,2,3,1,2,2,1,2,1,4,1,1,1,1,2,1],
     [1,2,2,1,2,2,2,2,1,1,3,2,2,1,2,2,4,2,2,2,2,2,1,3,1,1,2,2,2,2,1,2,2,1,2,2,2,2,1,1,3,2,2,1,2,2,4,2,2,2,2,2,1,3,1,1,2,2,2,2],
     [2,1,2,2,2,1,3,1,1,1,2,2,3,1,2,2,4,1,3,3,2,2,3,4,1,1,1,1,1,1,2,1,2,2,2,1,3,1,1,1,2,2,3,1,2,2,4,1,3,3,2,2,3,4,1,1,1,1,1,1],
     [1,1,2,1,1,1,2,2,1,1,2,2,2,1,2,2,3,1,2,1,1,2,1,3,1,1,1,2,3,2,1,1,2,1,1,1,2,2,1,1,2,2,2,1,2,2,3,1,2,1,1,2,1,3,1,1,1,2,3,2],
     [1,1,1,2,2,2,3,3,1,2,1,2,2,1,2,3,4,1,3,3,1,1,2,4,1,1,2,1,2,2,1,1,1,2,2,2,3,3,1,2,1,2,2,1,2,3,4,1,3,3,1,1,2,4,1,1,2,1,2,2],
     [1,1,3,2,1,1,2,3,1,1,2,2,2,1,2,3,3,1,2,2,1,2,1,4,1,1,1,1,2,1,1,1,3,2,1,1,2,3,1,1,2,2,2,1,2,3,3,1,2,2,1,2,1,4,1,1,1,1,2,1],
     [1,1,1,2,1,1,2,2,1,2,3,2,2,1,2,3,4,2,2,2,2,2,2,4,1,1,1,1,2,1,1,1,1,2,1,1,2,2,1,2,3,2,2,1,2,3,4,2,2,2,2,2,2,4,1,1,1,1,2,1],
     [1,2,1,1,1,1,3,2,1,2,2,2,2,1,2,3,4,1,3,2,2,2,2,3,1,1,1,2,2,2,1,2,1,1,1,1,3,2,1,2,2,2,2,1,2,3,4,1,3,2,2,2,2,3,1,1,1,2,2,2],
     [2,2,1,2,2,1,2,2,1,1,2,2,2,1,2,2,4,1,2,1,2,2,2,3,1,1,1,1,2,1,2,2,1,2,2,1,2,2,1,1,2,2,2,1,2,2,4,1,2,1,2,2,2,3,1,1,1,1,2,1],
     [1,1,3,2,1,1,3,3,1,1,2,2,2,1,2,2,3,1,2,2,1,2,1,4,1,1,1,1,2,1,1,1,3,2,1,1,3,3,1,1,2,2,2,1,2,2,3,1,2,2,1,2,1,4,1,1,1,1,2,1],
     [1,2,2,1,2,2,2,2,1,1,3,2,2,1,2,2,4,2,2,2,2,2,1,3,1,1,2,2,2,2,1,2,2,1,2,2,2,2,1,1,3,2,2,1,2,2,4,2,2,2,2,2,1,3,1,1,2,2,2,2]]
     

times = 10
index = 30

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        usia = random.randint(25,41)
        if usia < 29:
            status = random.choice([2,2,2,3,3,3,4])
            lama1 = random.randint(0,usia-23)
            if lama1 == 0:
                lama2 = random.randint(1,12)
            else:
                lama2 = random.randint(0,12)
            nikah = 6
        else :
            status = random.choice([2,3,4,4])
            lama1 = random.randint(0,usia-23)
            if lama1 == 0:
                lama2 = random.randint(1,12)
            else:
                lama2 = random.randint(0,12)

            nikah = random.choice([5,6])

        if lama1 != 0:
            if lama2 != 0:
                konjungsi = random.choice([" Tahun, dan "," Tahun, "," tahun, dan "," tahun, "," Tahun "," tahun "])
                akhir = random.choice([" Bulan"," bulan"])
            else:
                konjungsi = random.choice([" Tahun"," tahun", " Thn", " thn"])
                akhir = ""
        else:
            lama1 = ""
            konjungsi = ""
            akhir = random.choice([" Bulan"," Bulan"," bulan"," bulan"," bln"])

        divisi = random.choice([
                    "Divisi pemasaran dan branding",
                    "Divisi keuangan dan akuntansi",
                    "Divisi sumber daya manusia (SDM)",
                    "Divisi pengembangan produk",
                    "Divisi teknologi informasi (TI)",
                    "Divisi penjualan dan bisnis development",
                    "Divisi pengembangan bisnis",
                    "Divisi riset dan pengembangan",
                    "Divisi pelanggan dan pengalaman pengguna (user experience/UX)",
                    "Divisi keamanan informasi dan privasi",
                    "Divisi operasional dan logistik",
                    "Divisi manajemen produk",
                    "Divisi kemitraan dan strategi",
                    "Divisi pengembangan komunitas",
                    "Divisi legal dan kepatuhan",
                    "Divisi analisis data dan bisnis",
                    "Divisi pengiriman dan logistik",
                    "Divisi teknologi pembayaran",
                    "Divisi hubungan masyarakat (PR)",
                    "Divisi pengembangan bisnis internasional",
                    "Divisi pengembangan aplikasi mobile",
                    "Divisi pengembangan aplikasi web",
                    "Divisi desain grafis dan visual",
                    "Divisi pengujian dan kualitas",
                    "Divisi pengembangan bisnis online/offline",
                    "Divisi keamanan informasi dan privasi",
                    "Divisi analisis data dan bisnis",
                    "Divisi pengembangan komunitas",
                    "Divisi sumber daya manusia",
                    "Divisi keuangan dan akuntansi",
                ])

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(telp[index])
        textboxes[2].send_keys(email[index])
        textboxes[3].send_keys(usia)
        textboxes[4].send_keys(perusahaan[index])
        textboxes[5].send_keys(divisi)
        textboxes[6].send_keys(domisili[index])
        textboxes[7].send_keys(lama1)
        textboxes[7].send_keys(konjungsi)
        textboxes[7].send_keys(lama2)
        textboxes[7].send_keys(akhir)

        radiobuttons[kelamin[index]].click()
        radiobuttons[status].click()
        radiobuttons[nikah].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        temp = -1
        for i in range(22):
            # time.sleep(1)
            temps = temp + p[i][index]
            pilihan[temps].click()
            temp += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        temp = -1
        for i in range(18):
            # time.sleep(1)
            temps = temp + k[i][index]
            pilihan[temps].click()
            temp += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://bit.ly/Skripsi_Chrisen")

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