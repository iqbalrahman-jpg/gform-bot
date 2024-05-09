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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSefM25h_AzR555ekjAtL-HGwWPf793r3S0dgzQDkLkSWPVwug/viewform")


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

# laki 0 perempuan 1
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,]

times = 50
index = 0
mahasiswa = 8
bukan = 42
ya = 15
tidak = 35


try:
    while times:
        time.sleep(21)
        #Hardcoded logic
        test = 0
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        temp = random.choice([1,1,1,2])
        apk = random.sample([0,1],temp)
        apk = random.choice([0,1])
        checkboxes[apk].click()
        radiobuttons[kelamin[index]].click()
        if mahasiswa != 0 and bukan != 0:
            jawab = random.choice([7,10])
            if jawab == 7:
                bukan -= 1
            else:
                mahasiswa -=1
        elif mahasiswa == 0:
            jawab = 7
        elif bukan == 0:
            jawab = 10

        if mahasiswa == 10:
            umur = random.randint(20, 24)
        else:
            umur = random.randint(27, 60)

        textboxes[0].send_keys(umur)
        if mahasiswa == 10:
            pendapatan = 2
        else:
            pendapatan = random.choice([2,3,3,3,4,5])

        radiobuttons[pendapatan].click()
        if mahasiswa == 10:
            pendidikan = 7
        else:
            pendidikan = random.choice([7,8,8,8,9,9,9])
        
        radiobuttons[pendidikan].click()
        if mahasiswa == 10:
            pekerjaan = 15
        else:
            pekerjaan = random.choice([10,10,11,11,12,12,14])
        
        radiobuttons[pekerjaan].click()

        if mahasiswa == 10:
            jangka= random.choice([17,18])
        else:
            jangka = random.choice([17,18,19,20])
        
        radiobuttons[jangka].click()

        rata = random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14])
        textboxes[1].send_keys(rata)
        

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        #setuju = 1 tidak = 2
        jawaban = random.choice([0,1])
        if jawaban == 0 :
            p = 0
            soal = 4
            while soal:
                jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
                testcheck[jawab].click()
                soal -= 1
                p += 5
        else:
            p = 0
            soal = 4
            while soal:
                jawab = random.choice([p,p,p+1,p+1,p+1,p+2,])
                testcheck[jawab].click()
                soal -= 1
                p += 5
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        jawaban = random.choice([0,1])
        if jawaban == 0 :
            p = 0
            soal = 4
            while soal:
                jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
                testcheck[jawab].click()
                soal -= 1
                p += 5
        else:
            p = 0
            soal = 4
            while soal:
                jawab = random.choice([p,p,p+1,p+1,p+1,p+2,])
                testcheck[jawab].click()
                soal -= 1
                p += 5


        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        
        jawaban = random.choice([0,1])
        if jawaban == 0 :
            p = 0
            soal = 6
            while soal:
                jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
                testcheck[jawab].click()
                soal -= 1
                p += 5
        else:
            p = 0
            soal = 6
            while soal:
                jawab = random.choice([p,p,p+1,p+1,p+1,p+2,])
                testcheck[jawab].click()
                soal -= 1
                p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        jawaban = random.choice([0,1])
        if jawaban == 0 :
            p = 0
            soal = 4
            while soal:
                jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
                testcheck[jawab].click()
                soal -= 1
                p += 5
        else:
            p = 0
            soal = 4
            while soal:
                jawab = random.choice([p,p,p+1,p+1,p+1,p+2,])
                testcheck[jawab].click()
                soal -= 1
                p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        if ya != 0 and tidak != 0:
            jawab = random.choice([0,1])
            if jawab == 0:
                ya -= 1
            else:
                tidak -=1
        elif ya == 0:
            jawab = 1
        elif tidak == 0 :
            jawab = 0
        checkboxes[jawab].click()
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSefM25h_AzR555ekjAtL-HGwWPf793r3S0dgzQDkLkSWPVwug/viewform")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        print("times : " + str(times))
        print("mahasiswa : " + str(mahasiswa))
        print("bukan: " + str(bukan))
        print("ya : " + str(ya))
        print("tidak : " + str(tidak))
        
        
finally:
	# driver.quit()
    print("berhasil")

    # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
    # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
    # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox