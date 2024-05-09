from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# driver = webdriver.Firefox()
driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://forms.gle/4C1G3oB2AWenZYDm9")

email = [
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
"anggasiregarp@gmail.com",
"putrikeancana@gmail.com",
"rajawardanawan@gmail.com",
"affifahh7@gmail.com",
"shakapwijaya@gmail.com",
"cynnarafisa@gmail.com",
"monahfnna87@gmail.com",
"mahendrejaa@gmail.com",
"fryshta.eka823@gmail.com",
"yanrasuryad@gmail.com",
"rahannadi1@gmail.com",
"sutisnayun@gmail.com",
"ayulistyaan@gmail.com",
"muhh.santosoo@gmail.com",
"ardyantoputra43@gmail.com",
"puttr.wirawan@gmail.com",
"agungnugrh1@gmail.com",
"daniramadhan1982@gmail.com",
"dimapurb0@gmail.com",
"nabillasyaqila.q@gmail.com"

]

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
    "Nabilla Syaqila Qolbi "
]

#3 laki, 4 perempuan
kelamin = [4,3,4,3,3,4,3,4,4,3,4,3,4,3,4,3,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,4,3,4,3,3,4,4,3,3,3,3,3,3,4]

times = 1
index = 49


try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        usia = random.choice([0,1,2])
        domisili = random.choice([5,6,7,8,9])

        textboxes[0].send_keys(email[index])
        textboxes[1].send_keys(nama[index])

        time.sleep(2)
        radiobuttons[usia].click()

        radiobuttons[kelamin[index]].click()
        radiobuttons[domisili].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 4
        while soal:
            s1 = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[s1].click()
            soal -= 1
            p += 5

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 14
        while soal:
            s1 = random.choice([p+1,p+2,p+3,p+3,p+3,p+3,p+4,p+4,p+4,p+4])
            testcheck[s1].click()
            soal -= 1
            p += 5

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 4
        while soal:
            s1 = random.choice([p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[s1].click()
            soal -= 1
            p += 5

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 6
        while soal:
            s1 = random.choice([p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[s1].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/4C1G3oB2AWenZYDm9")

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

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()