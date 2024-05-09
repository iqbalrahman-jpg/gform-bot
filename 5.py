from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Firefox()
driver.get("https://forms.gle/frEeYeQa6HowKtwB7")
times = 25

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
    "Annisa Chania"
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
]

kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0]

index = 0
kebutuhan = 12
keinginan = 13
try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='login']")))

        submit_button.click()

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(email[index])

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Selanjutnya')]"))
        )
 
        submit_button.click()

        textboxes[0].send_keys(password[index])


        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(nama[index])
        radiobuttons[kelamin[index]].click() #0 1

        usia = random.choice([2,3])
        radiobuttons[usia].click()

        kampus = random.choice([5,6])
        radiobuttons[kampus].click()

        angk = random.choice([7,8])
        radiobuttons[angk].click()

        studi = random.choice([9,10])
        radiobuttons[studi].click()

        radiobuttons[11].click()
        radiobuttons[18].click()

        if keinginan !=0 and kebutuhan !=0 :
            alasan = random.choice([19,20])
            radiobuttons[alasan].click()
            if alasan == 19:
                keinginan -= 1
            elif alasan == 20:
                kebutuhan -= 1
        elif keinginan == 0:
            radiobuttons[20].click()
            kebutuhan -= 1
        elif kebutuhan == 0:
            radiobuttons[19].click()
            keinginan -= 1

        radiobuttons[23].click()


        if usia == 0:
            pend = random.choice([5,6])
            radiobuttons[pend].click()
        elif usia == 1:
            pend = random.choice([5,6,6,6,7])
            radiobuttons[pend].click()
        elif usia == 2:
            pend = random.choice([5,6,6,7,7,7,8])
            radiobuttons[pend].click()

        asal = random.choice([9,10,11,12,13,14])
        radiobuttons[asal].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "l4V7wb"))
        )

        submit_button.click()

        time.sleep(1)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#isian
 
        radiobuttons[0].click()
        radiobuttons[2].click()
        susah = random.choice([4,5])
        radiobuttons[susah].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
 
        submit_button.click()

        time.sleep(1)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#isian

        radiobuttons[0].click()
        radiobuttons[2].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(1)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#isian

        temp = random.choice([1,2,3,4])
        random_item = random.sample([0,1,2,3], int(temp))
        
        for i in random_item :
           checkboxes[i].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(1)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#isian

        temp = random.choice([1,2,3])
        random_item = random.sample([0,1,2,3], int(temp))
        
        for i in random_item :
           checkboxes[i].click()

        nom = random.choice([0,1,2])
        radiobuttons[nom].click()

        tau = random.choice([3,4,4,4,4])
        radiobuttons[tau].click()

        tau = random.choice([5,6,6,7])
        radiobuttons[tau].click()

        temp = random.choice([1,2,3.4])
        random_item = random.sample([5,6,7,8,9,10], int(temp))
        
        for i in random_item :
           checkboxes[i].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        # )

        # submit_button.click()

        # driver.implicitly_wait(4)
        # driver.get("https://forms.gle/frEeYeQa6HowKtwB7")
        times-=1
        index+=1
        print(times)
finally:
	# driver.quit()
    print("berhasil")