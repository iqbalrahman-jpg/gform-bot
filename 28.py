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
driver.get("https://forms.gle/9SLbApPKoRrV3FGJ8")

nama = [
        "Mutia Ayu Nur",
    "Ali Hasanudin",
        "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
        "Nana Annisa",
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
]

kelamin = [1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1]

#1. Orang yang bekerja secara jarak jauh, atau pekerja remote working.
# 2. Pekerja remote working yang berusia 23-43 tahun.
# 3. Pekerja remote working yang bekerja di kota Yogyakarta, Daerah Istimewa Yogyakarta.
times = 1
index = 15

try:
    while times:
        time.sleep(2)
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

        textboxes[0].send_keys(nama[index])
        radiobuttons[kelamin[index]].click()
        usia = random.choice([2,4,4,4,5,5,6])
        radiobuttons[usia].click()
        radiobuttons[7].click()
        radiobuttons[8].click()
        time.sleep(2)
        pekerjaan = random.choice([9,9,9,10,11,12,12,13,14,15])
        radiobuttons[pekerjaan].click()



        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 7
        while soal:
            jawab = random.choice([p,p,p+1,p+1,p+2])
            radiobuttons[jawab].click()
            soal -= 1
            p += 5

        p = 35
        soal = 7
        while soal:
            jawab = random.choice([p,p+1,p+2,p+3])
            radiobuttons[jawab].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        cermat = random.choice([0,0,0,1,1,1,2,3])
        radiobuttons[cermat].click()
        std = random.choice([5,5,6,6,7])
        radiobuttons[std].click()
        p = 10
        soal = 3
        while soal:
            jawab = random.choice([p,p,p+1,p+1,p+2])
            radiobuttons[jawab].click()
            soal -= 1
            p += 5

        p = 25
        soal = 5
        while soal:
            jawab = random.choice([p,p,p,p+1,p+1,p+1,p+2,p+3])
            radiobuttons[jawab].click()
            soal -= 1
            p += 5
        
        p = 50
        peralatan = random.choice([p,p,p+1,p+1,p+2])
        radiobuttons[peralatan].click()
        p = 55
        merasa = random.choice([p,p,p+1,p+1,p+2,p+3])
        radiobuttons[merasa].click()
        p = 60
        if merasa < 61:
            jawab = random.choice([p,p+1])
            radiobuttons[jawab].click()
        else:
            jawab = random.choice([p,p,p+1,p+1,p+2])
            radiobuttons[jawab].click()
        
        p = 65
        soal = 2
        while soal:
            jawab = random.choice([p,p,p,p+1,p+1,p+1,p+2])
            radiobuttons[jawab].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        waktusepakat = random.choice([0,0,0,1,1,1,2])
        radiobuttons[waktusepakat].click()
        waktulibur = random.choice([5,5,5,6,6,6,7,8,9])
        radiobuttons[waktulibur].click()

        p = 10
        soal = 4
        while soal:
            jawab = random.choice([p,p,p,p+1,p+1,p+1])
            radiobuttons[jawab].click()
            soal -= 1
            p += 5
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/9SLbApPKoRrV3FGJ8")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        print("times : " + str(times))
        
        
finally:
	# driver.quit()
    print("berhasil")