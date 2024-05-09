from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Firefox()
driver.get("https://bit.ly/KuesionerAplikasiPemesananTiketEvent")
times = 8

nama = [
    "Salma Azizah",
    "Faradilla Aulia",
    "Regina April",
    "Muhammad Fadlan",
    "Ardy Riski",
    "Amanda Bella Putri",
    "Arjuna Ghafur",
    "Sadiva Pratiwi"
]

email = [
    "salmaazizahh@gmail.com",
    "@faradillaaulia02",
    "085694967112",
    "Mfadlan57@gmail.com",
    "087771034388",
    "085691005874",
    "081316619265 ",
    "sadivapratiw1@gmail.com"
]

kelamin = [1,1,1,0,0,1,0,1]

masalah =[
    "Berdesak-desakan",
    "Kehilangan barang",
    "Sesak karena terlalu banyak orang",
    "Gerah karena ac dan kipasnya cuma sedikit",
    "Bingung, tidak tau harus kemana terlebih dahulu",
    "Telat karena informasi rute shuttle bus tidak ada",
    "Terinjak-injak karena yang nonton brutal",
    "Antrian yang panjang terutama jika event populer atau hanya ada sedikit pintu masuk",
    "Barang dicuri"
]

saran = [
    "Aplikasi harus dapat dengan mudah digunakan",
    "Keamanan data privasi wajib untuk dijaga agar tidak bocor",
    "Banyak metode pembayarannya",
    "",
    "",
    "Tampilan aplikasinya harus lebih menarik",
    "Semoga di aplikasi ini menjual tiket jauh lebih mudah dan tidak ribet",
    ""
]
index = 0
try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(email[index])
        radiobuttons[kelamin[index]].click()
        usia = random.randint(18,30)
        textboxes[2].send_keys(usia)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "l4V7wb"))
        )

        submit_button.click()

        time.sleep(5)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#isian
 
        temp = random.choice([1,2,3])
        random_item = random.sample([0,1,2], temp)
        
        for i in random_item :
           checkboxes[i].click()

        driver.implicitly_wait(4)

        temp = random.choice([1,2,3,4,5])
        random_item = random.sample([5,6,7,8,9,10], temp)
        
        for i in random_item :
           checkboxes[i].click()

        driver.implicitly_wait(4)

        textboxes[0].send_keys(masalah[index])
        check1 = random.choice([1,2,3,3,3,4,4,4])
        testcheck[check1].click()
        check2 = random.choice([6,7,8,8,8,9,9,9])
        testcheck[check2].click()
        check3 = random.choice([11,12,13,13,13,14,14,14])
        testcheck[check3].click()
        check4 = random.choice([16,17,18,18,19,19])
        testcheck[check4].click()
        check5 = random.choice([21,22,23,23,24,24])
        testcheck[check5].click()
        check6 = random.choice([26,27,28,28,29,29])
        testcheck[check6].click()
        check7 = random.choice([31,32,33,33,34,34])
        testcheck[check7].click()

        driver.implicitly_wait(4)

        checkboxes[12].click()
        if check3 == 14:
            checkboxes[14].click()
        if check4 == 19:
            checkboxes[13].click()
        if check5 == 24:
            checkboxes[15].click()
        if check6 == 29:
            checkboxes[16].click()
        if check7 == 34:
            checkboxes[17].click()

        driver.implicitly_wait(4)

        textarea[0].send_keys(saran[index])

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "l4V7wb"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://bit.ly/KuesionerAplikasiPemesananTiketEvent")
        times-=1
        index+=1
        print(times)
finally:
	driver.quit()
