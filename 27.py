from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://forms.gle/1g9LRRe4GbCM4QXm8")


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
    "Maya Dara Putri",
    "Rio Fajar Pratama",
    "Dewi Sari Wijaya",
    "Agung Kusuma Jaya",
    "Ratih Suci Lestari",
    "Rizki Pratama Nugraha",
    "Dwi Prasetya Utama",
    "Arif Rahman Hakim",
    "Intan Ayu Lestari",
    "Ananda Dwi Wicaksono",
    "Fira Nur Hidayah",
    "Rama Aditya Wardhana",
    "Cinta Ayu Dewanti",
    "Ade Kurniawan Saputra",
    "Mira Fitriana Wati",
    "Dian Kusuma Wardani",
    "Budi Santoso Putra",
    "Rina Nuraini Sari",
    "Ahmad Fauzi Akbar",
    "Rizky Ananda Pratama",
    "Maya Dewi Sari",
    "Dwi Kusuma Jaya",
    "Agung Santosa Nugroho",
    "Dila Yuliani Wati",
    "Andi Muhammad Rizal",
]

# laki 6 perempuan 7
kelamin = [7,6,7,6,6,7,6,7,7,6,7,6,7,6,7,6,6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7,7,6,7,6,6,7,7,6,6,6,6,6,6,7,7,6,7,6,7,6,6,6,7,6,7,6,7,6,7,7,6,7,6,6,7,6,6,7,6,
]

#kurang 10
times = 8
index = 67

try:
    while times:
        time.sleep(2)
        #Hardcoded logic
        test = 0
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(nama[index])
        umur = random.choice([1,1,2,2,2,3,4,5])
        radiobuttons[umur].click()
        radiobuttons[kelamin[index]].click()
        if umur < 2:
            pendidikan = random.choice([8,9,10])
        else:
            pendidikan = random.choice([9,10,11])
        radiobuttons[pendidikan].click()
        domisili = random.choice([13,14,15,16,17])
        radiobuttons[domisili].click()
        time.sleep(2)
        radiobuttons[19].click()
        kali = random.choice([21,21,21,22,22,23])
        radiobuttons[kali].click()
        time.sleep(2)
        temp = random.choice([1,2,2,2,3,3])
        ecom = random.sample([0,1,2,3,4],temp)
        for i in ecom :
           checkboxes[i].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 4
        while soal:
            jawab = random.choice([p+3,p+4,p+5])
            testcheck[jawab].click()
            soal -= 1
            p += 6


        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 3
        while soal:
            jawab = random.choice([p+2,p+3,p+4,p+5])
            testcheck[jawab].click()
            soal -= 1
            p += 6

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 6
        while soal:
            jawab = random.choice([p+3,p+4,p+5])
            testcheck[jawab].click()
            soal -= 1
            p += 6

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 6
        while soal:
            jawab = random.choice([p+3,p+4,p+5])
            testcheck[jawab].click()
            soal -= 1
            p += 6

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 4
        while soal:
            jawab = random.choice([p+3,p+4,p+5])
            testcheck[jawab].click()
            soal -= 1
            p += 6
        p = 24
        memberitahu = random.choice([p+2,p+3,p+4,p+5])
        testcheck[memberitahu].click()
        p = 30
        berbelanja = random.choice([p+2,p+3,p+4,p+5])
        testcheck[berbelanja].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/1g9LRRe4GbCM4QXm8")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        print("times : " + str(times))
        
        
finally:
	# driver.quit()
    print("berhasil")

    # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
    # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
    # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox