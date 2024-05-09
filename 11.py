from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfO8WA_K1HCG2YCwQyM8T5RoTQZpa0r3z6WxaD_thJ6khCGTQ/viewform?usp=send_form")

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
]

kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0]

memajukan = [
    "Memastikan akses ke air terjun mudah dijangkau",
    "jaga jalan menuju air terjun dalam kondisi baik",
    "perbaiki jalan yang rusak",
    "tambahkan berbagai macam fasilitas tambahan",
    "sediakan tempat parkir, kamar mandi, dan area bersantai agar pengunjung merasa nyaman",
    "pastikan keamanan di air terjun",
    "Sediakan informasi yang jelas dan mudah dimengerti mengenai air terjun",
    "bisa tambahan area tentang sejarahnya, keunikan, dan daya tariknya",
    "coba jalin kemitraan dengan pelaku industri wisata, hotel, restoran, dan agen perjalanan",
    "Manfaatkan media sosial untuk menarik minat calon pengunjung.",
    "Tawarkan pengalaman yang berbeda dan menarik ",
    "Jaga kebersihan dan kelestarian lingkungan sekitar air terjun",
    "berikan kualitas pelayanan yang baik dan ramah kepada pengunjung",
    "Tingkatkan promosi dengan memasang iklan di media sosial, media massa, atau ikut pameran wisata",
    "perbaiki jalan menuju lokasi air terjun",
    "Adakan event khusus seperti festival atau kompetisi fotografi",
    "Manfaatkan media sosial seperti Instagram, Facebook, dan Twitter untuk mempromosikan air terjun dan menarik minat pengunjung.",
    "tambahkan kegiatan olahraga air, atau paket wisata kuliner lokal.",
    "Jaga keamanan di lokasi, sehingga tidak ada yang takut",
    "promosikan di tempat yang luas untuk menarik lebih banyak pengunjung",
    "perbaiki akses jalan yang masih kurang",
    "jaga kebersihan yang ada",
    "Perbanyak event atau acara yang di gelar disana",
    "jaga kebersihan dan ketertiban, serta peralatan yang ada",
    "perbaiki akses menuju air terjun",
]

kunjungan = [
    "Cukup ramai",
    "Ramai, penuh dengan keluarga",
    "ramai",
    "hari biasa sepi",
    "relative ramai",
    "sepi",
    "tidak terlalu ramai",
    "tidak sepi",
    "ramai",
    "rame",
    "tinggi",
    "banyak pengunjung",
    "banyak wisatawan",
    "ramai pengunjung",
    "weekend penuh dengan pengunjung",
    "relative ramai namun tidak terlalu",
    "tidak terlalu rame",
    "padat",
    "banyak kunjungan ",
    "ramai pengunjung",
    "cukup ramai",
    "banyak",
    "tinggi",
    "tinggi, ramai ",
    "tinggi pengunjung waktu weekend",
]

potensi = [
    "buat area bermain anak",
    "tambahkan area untuk foto dan berkumpul",
    "aktifkan media sosial yang aktif, agar orang lain dapat melihat",
    "Adakan event event yang berkaitan",
    "Buat acara festival sesekali, bisa tahunan atau bulanan",
    "pendidikan untuk anak sd hingga sma",
    "bikin area atau tempat yang berisikan informasi dan sejarah mengenai air terjun",
    "tidak hanya foto, tapi ada area untuk menikmati air terjun secara langsung",
    "kegiatan olahraga air juga bisa diadakan",
    "arum jeran",
    "acara kuliner lokal, yang di selenggarakan oleh masyarakat lokal",
    "area bermain / khusus anak",
    "tempat atau view yang menarik untuk berfoto",
    "pengenalan lingkungan alam yang lebih",
    "pameran wisata, kunjungan industri, atau bahkan kuliner",
    "suatu yang khas dan unik dari tempat wisata air terjun ini",
    "adakan event kompetisi fotografi bertemakan air terjun kanto lampo",
    "festival yang dapat didatangi oleh masyarakat umum",
    "kegiatan olahraga air seperti arum jeram, dsb",
    "tambahkan area untuk foto foto",
    "tempat budidaya tanaman yang berkaitan",
    "bisa juga dijadikan sarana pendidikan tentang keanekaragaman hayati",
    "olahraga air",
    "objek budaya yang mengenalkan tradisi, adat, maupun kesenian lokal",
    "area olahraga air, seperti arum jeram",
]

times = 25
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(nama[index])

        radiobuttons[kelamin[index]].click()

        domisili = random.choice([2,3])
        radiobuttons[domisili].click()

        usia = random.choice([4,5,6,7,8])
        radiobuttons[usia].click()

        if usia == 4:
            pendidikan = random.choice([9,10])
            radiobuttons[pendidikan].click()
            radiobuttons[13].click()
        else:
            pendidikan = random.choice([10,11,12])
            radiobuttons[pendidikan].click()
            if pendidikan == 10:
                radiobuttons[13].click()
            elif pendidikan != 10 and kelamin[index] == 1:
                pekerjaan = random.choice([14,15,16,17])
                radiobuttons[pekerjaan].click()
            else: 
                pekerjaan = random.choice([15,16,17])
                radiobuttons[pekerjaan].click()

        akses = random.choice([18,18,18,19])
        radiobuttons[akses].click()

        Fasilitas = random.choice([20,20,20,21,21,22])
        radiobuttons[Fasilitas].click()

        org = random.choice([23,23,24,25,25])
        radiobuttons[org].click()

        sdm = random.choice([26,26,26,27])
        radiobuttons[sdm].click()

        saingan = random.choice([28,29,30])
        radiobuttons[saingan].click()

        hubungan = random.choice([31,32])
        radiobuttons[hubungan].click()

        pemasaran = random.choice([33,34,35])
        radiobuttons[pemasaran].click()

        keamanan = random.choice([36,36,36,37])
        radiobuttons[keamanan].click()

        kebersihan = random.choice([38,38,39,40])
        radiobuttons[kebersihan].click()

        sudah = random.choice([41,42])
        radiobuttons[sudah].click()

        textboxes[1].send_keys(memajukan[index])
        textboxes[2].send_keys(kunjungan[index])
        textboxes[3].send_keys(potensi[index])


        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfO8WA_K1HCG2YCwQyM8T5RoTQZpa0r3z6WxaD_thJ6khCGTQ/viewform?usp=send_form")

        print("==================")
        print("index : " + str(index))

        index+=1
        times-=1
        print("times : " + str(times))
finally:
	# driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox