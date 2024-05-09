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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSewhhXJeZscluH4o-JjhWEd4AF5IGur6pmT2du7uZT1NTKcMg/viewform?vc=0&c=0&w=1&flr=0")

# Mungkin untuk umur diperbanyak yang 18-25 buat jawaban yang lain yang penting bisa menjawab judulnya kalo bisa dibanyakin

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
]

# laki 4 perempuan 5
kelamin = [5,4,5,4,4,5,4,5,5,4,5,4,5,4,5,4,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,5,4,5,4,4,5,5,4,4,4,4,4,4,5,1,0,1,0,1,0,0,0,1,0,]

times = 10
index = 50
cenderung = 7
tidak = 3
y = 8
g = 2



try:
    while times:
        time.sleep(2)
        #Hardcoded logic
        test = 0
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        umur = random.choice([0,1,1,1,1,2,3,])
        checkboxes[umur].click()
        checkboxes[kelamin[index]].click()
        if umur < 2:
            pekerjaan = random.choice([6,6,6,6,6,8])
        else:
            pekerjaan = random.choice([7,7,7,8,8,9])

        checkboxes[pekerjaan].click()
        checkboxes[10].click()
        berpergian = random.choice([12,13,14])
        checkboxes[berpergian].click()
        alasan = random.choice([15,15,15,16,16,17,18])
        checkboxes[alasan].click()
        penting = random.choice([19,19,19,20,20,20,21])
        checkboxes[penting].click()
        sering = random.choice([23,23,23,24,24,24,25])
        checkboxes[sering].click()
        foto = random.choice([27,27,27,28,28,28,29])
        checkboxes[foto].click()
        checkboxes[31].click()
        mudah = random.choice([33,33,33,34,34,34,35])
        checkboxes[mudah].click()
        if cenderung != 0 and tidak != 0:
            jawab = random.choice([37,37,38])
            if jawab == 37:
                cenderung -= 1
            else:
                tidak -=1
        elif cenderung == 0:
            jawab = 38
            bukan -= 1
        elif tidak == 0:
            jawab = 37
            cenderung -= 1

        checkboxes[jawab].click()
        if y != 0 and g != 0:
            jawab = random.choice([39,39,40])
            if jawab == 39:
                y -= 1
            else:
                g -=1
        elif y == 0:
            jawab = 40
            g -= 1
        elif g == 0:
            jawab = 39
            y -= 1
        checkboxes[jawab].click()
        if alasan == 15:
            share = 41
        else:
            share = random.choice([41,42,43])
        checkboxes[share].click()
        checkboxes[45].click()
        mencari = random.choice([47,47,48,48,49])
        checkboxes[mencari].click()
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSewhhXJeZscluH4o-JjhWEd4AF5IGur6pmT2du7uZT1NTKcMg/viewform?vc=0&c=0&w=1&flr=0")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        print("times : " + str(times))
        print("cenderung : " + str(cenderung))
        print("tidak : " + str(tidak))
        print("y : " + str(y))
        print("g : " + str(g))
        
        
finally:
	# driver.quit()
    print("berhasil")

    # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
    # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
    # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox