from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://forms.gle/cNrgvN41PvCB3rgTA")

nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Bagas Marsha",
    "Yudi Pradanawan",
    "Yulianto Nasution",
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
    "Azzarin Rizki Maulana",
    "Fabian Nadeo Putra",
    "Nis Eko Martahu",
    "Bayu Dwiganara",
    "Radan Syirahano",
]

#0 laki, 1 perempuan
kelamin = [1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,]

times = 3
index = 22

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[0].click()

        time.sleep(1)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[0].click()

        time.sleep(1)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        bag = 3
        while bag:
            time.sleep(3)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
            p1 = 0
            soal = 4
            while soal:
                s1 = random.choice([p1,p1+1,p1+2,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4])
                testcheck[s1].click()
                soal -= 1
                p1 += 5
            bag -= 1
            time.sleep(1)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        soal = 5
        while soal:
            s1 = random.choice([p1+1,p1+2,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4])
            testcheck[s1].click()
            soal -= 1
            p1 += 5

        time.sleep(1)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        bag = 2
        while bag:
            time.sleep(3)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
            p1 = 0
            soal = 4
            while soal:
                s1 = random.choice([p1,p1+1,p1+2,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4])
                testcheck[s1].click()
                soal -= 1
                p1 += 5
            bag -= 1
            time.sleep(1)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        soal = 5
        while soal:
            s1 = random.choice([p1+1,p1+2,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4])
            testcheck[s1].click()
            soal -= 1
            p1 += 5

        time.sleep(1)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        bag = 8
        while bag:
            time.sleep(3)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
            p1 = 0
            soal = 3
            while soal:
                s1 = random.choice([p1+1,p1+2,p1+3,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4,p1+4])
                testcheck[s1].click()
                soal -= 1
                p1 += 5
            bag -= 1
            time.sleep(1)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

        time.sleep(3)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        dropdown = driver.find_elements("css selector", ".ry3kXd")#kebawah

        textboxes[0].send_keys(nama[index])
        usia = random.randint(20,43)
        textboxes[1].send_keys(usia)
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        
        dropdown[0].click()
        domisili = random.choice(["Aceh","Sumatra Utara","Sumatra Barat","Riau","Jambi",
            "Sumatra Selatan","Bengkulu","Lampung","kep. Bangka Belitung","Kep. Riau",
            "DKI Jakarta","Jawa Barat","Jawa Tengah","DI Yogyakarta","Jawa Timur","Banten",
            "Bali","Nusa Tenggara Barat","Nusa Tenggara Timur","Kalimantan Barat","Kalimantan Tengah",
            "Kalimantan Selatan","Kalimantan Timur","Kalimantan Utara","Sulawesi Utara","Sulawesi Tengah",
            "Sulawesi Selatan","Sulawesi Tenggara","Gorontalo","Sulawesi Barat","Maluku","Maluku Utara"])
        print(domisili)
        time.sleep(5)
        # pilih = driver.find_elements("css selector", ".OA0qNb")#kebawah
        option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

        option[1].click()

        time.sleep(5)

        if usia < 25:
            time.sleep(2)
            radiobuttons[2].click()
            dropdown[1].click()

            time.sleep(5)
            options = driver.find_elements(By.XPATH, "//span[contains(text(), 'SMA/Sederajat')]")

            options[1].click()

            driver.implicitly_wait(4)
            radiobuttons[9].click()
        elif usia >= 25 and usia < 30 and kelamin[index] == 0:
            time.sleep(2)
            pekerjaan = random.choice([3,4,5,6])
            radiobuttons[pekerjaan].click()
            pendidikan = random.choice(["Akademi/Diploma","S1"])

            dropdown[1].click()

            time.sleep(5)
            options = driver.find_elements(By.XPATH, "//span[contains(text(), '"+pendidikan+"')]")

            options[1].click()
            penghasilan = random.choice([10,11,12])
            driver.implicitly_wait(4)
            radiobuttons[penghasilan].click()
        elif usia >= 30 and kelamin[index] == 0:
            time.sleep(2)
            pekerjaan = random.choice([3,4,5,6])
            radiobuttons[pekerjaan].click()
            pendidikan = random.choice(["Akademi/Diploma","S1","S2/S3"])

            dropdown[1].click()

            time.sleep(5)
            options = driver.find_elements(By.XPATH, "//span[contains(text(), '"+pendidikan+"')]")

            options[1].click()
            penghasilan = random.choice([10,11,12])
            driver.implicitly_wait(4)
            radiobuttons[penghasilan].click()
        elif usia >= 25 and usia < 30 and kelamin[index] == 1:
            time.sleep(2)
            pekerjaan = random.choice([3,4,5,6,7])
            radiobuttons[pekerjaan].click()
            pendidikan = random.choice(["Akademi/Diploma","S1"])

            dropdown[1].click()

            time.sleep(5)
            options = driver.find_elements(By.XPATH, "//span[contains(text(), '"+pendidikan+"')]")

            options[1].click()
            penghasilan = random.choice([10,11,12])
            driver.implicitly_wait(4)
            radiobuttons[penghasilan].click()
        elif usia >= 30 and kelamin[index] == 1:
            time.sleep(2)
            pekerjaan = random.choice([3,4,5,6,7])
            radiobuttons[pekerjaan].click()
            pendidikan = random.choice(["Akademi/Diploma","S1","S2/S3"])

            dropdown[1].click()

            time.sleep(5)
            options = driver.find_elements(By.XPATH, "//span[contains(text(), '"+pendidikan+"')]")

            options[1].click()
            penghasilan = random.choice([10,11,12])
            driver.implicitly_wait(4)
            radiobuttons[penghasilan].click()

        s1 = random.choice([13,14])
        s2 = random.choice([15,16])
        radiobuttons[s1].click()
        radiobuttons[s2].click()

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
        driver.get("https://forms.gle/cNrgvN41PvCB3rgTA")

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