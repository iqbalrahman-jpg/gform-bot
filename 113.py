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
driver.get("https://forms.gle/V19LF6LXVzbGz1mVA")

nama = [
    "I Komang Putra Adi",
    "Made Kusuma",
    "I Gede Putra Jaya Wijaya",
    "I Gusti Bagus Agung",
    "Ni Ketut Gede Sariati Dewi",
    "Ni Ayu Made Pradanawati",
    "Gede Made Putra",
    "I Wayan Kadek Wijaya",
    "I Gede Putra Bagus Jaya",
    "I Wayan Kadek Wijayanto",
    "I Gusti Bagus Jaya Putra",
    "Kadek Komang Sari",
    "Ni Nyoman Kadek Ratnasari",
    "Putri Dewi",
    "Putu Gede Wijaya",
    "I Made Ayu Wijaya",
    "I Komang Putra Wijaya Gede",
    "Nyoman Kadek Sari",
    "Ni Wayan Putri Sari",
    "Gede Putri",
    "I Gede Made Pradana",
    "Ni Ketut Ayu Dewi",
    "Ni Ketut Gede Ratnasari",
    "Wayan Suardika",
    "Nyoman Ketut Wijaya",
    "I Gusti Ngurah",
    "Ni Ketut Gede Ratnawati",
    "Ayu Ketut Wijaya",
    "Ayu Ketut Sari",
    "Wayan Susanto",
    "Ayu Nyoman Sari",
    "Ni Ketut Gede Wijayanti",
    "I Wayan Putra Surya",
    "Komang Sari",
    "I Gede Made Pradana Jaya",
    "Ni Nyoman Kadek Pratiwi",
    "Ketut Surya",
    "Ni Kadek Komang Dewi",
    "I Gede Putra Jaya",
    "Ni Ayu Made Puspitasari",
    "Ni Ketut Gede Sariati",
    "I Made Ayu Wijaya Putra",
    "Nyoman Ketut Sari",
    "I Komang Putra Wijaya",
    "Ayu Novianti",
    "Ketut Wijaya",
    "Kadek Komang Sariati",
    "Ni Wayan Putri Rama Gede",
    "I Wayan Putra Gede Sari",
    "Ni Kadek Komang Sari",
    "Komang Putra Jaya",
    "Ni Ketut Gede Sariati Dewi Sari",
    "Ni Ketut Agung Wijaya",
    "Nyoman Wijaya",
    "I Gusti Bagus Jaya",
    "Ni Ketut Ayu Made Rama",
    "Ni Nyoman Ketut Sari",
    "Ni Ketut Gede Sari",
    "I Komang Putra Aditya",
    "Nyoman Sariati",
    "I Nyoman Gede Wijaya Kusuma",
    "Ni Ketut Agung Nugraha",
    "Ni Ayu Made Pradana",
    "I Nyoman Gede Wijaya Putra",
    "Ni Ayu Made Pradana Jaya",
    "Ni Nyoman Ketut Sariati Dewi",
    "Ni Ayu Made Puspita",
    "Ni Kadek Komang Sri Sari",
    "I Made Agung Kusuma",
    "Ni Nyoman Kadek Ayu Dewi",
    "I Gede Agung Nugraha",
    "Ni Ayu Made Rama Sari",
    "Kadek Santika",
    "Ni Ayu Made Rama",
    "I Gusti Bagus Agus",
    "Made Putra",
    "I Wayan Kadek Wijaya Gede",
    "Ni Kadek Komang Sari Wijaya",
    "Ayu Dewi",
    "Ni Luh Sari",
    "Ni Ayu Ketut Sari",
    "Ni Nyoman Ketut Sari Ayu",
    "Made Ayu Novi",
    "I Gusti Bagus",
    "I Wayan Putra Jaya",
    "Wayan Kadek Wijaya",
    "Ni Luh Ayu",
    "I Komang Made Pradana Jaya",
    "Made Ayu Dewi",
    "Putu Jaya",
    "I Gede Agung Wijaya",
    "Putu Gede Sariati",
    "I Komang Made Prasetyo",
    "I Wayan Putra Prasetya",
    "I Made Ayu Sri Dewi",
    "I Made Ayu Dewi",
    "I Komang Made Pradana",
    "Ni Wayan Putri Rama",
    "I Gusti Eka Bagus Jaya",
    "Komang Sariati",
    "Gede Putra Jaya",
    "Wayan Komang Sariati",
    "I Nyoman Gede Wijaya",
    "Wayan Putri Rama",
    "Ketut Gede Sari",
    "Ni Nyoman Kadek Sari",
    "I Made Ayu Sri Rahayu",
    "Ni Ayu Ketut Sariati Dewi",
    "I Made Agung Putra Wijaya",
    "Ni Ayu Ketut Utami",
]

kelamin = [0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,
            0,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,1,0,1
]

positif = 94
negatif = 16

times = 110
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        usia = random.randint(18,50)

        if usia <= 20 :
            pekerjaan = random.choice(["Pelajar", "SMA", "Siswa"])
        elif usia <= 26 :
            pekerjaan = random.choice(["Mahasiswa", "Kuliah"])
        else:
            pekerjaan = random.choice(["Bekerja", "Kerja"])

        time.sleep(2)
        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(usia)
        textboxes[2].send_keys(pekerjaan)

        time.sleep(2)
        temp = random.randint(1,2)

        if temp == 1:
            alamat = random.choice([
                    "Renon",
                    "Sanur",
                    "Sesetan",
                    "Padangsambian",
                    "Panjer",
                    "Tegal Harum",
                    "Ubung",
                    "Pemogan",
                    "Kuta",
                    "Jimbaran",
                    "Sidakarya",
                    "Kesiman",
                    "Teuku Umar",
                    "Dauh Puri",
                    "Denpasar",
                ])
            alamat1 = ""
        else:
            alamat = random.choice([
                    "Renon",
                    "Sanur",
                    "Sesetan",
                    "Padangsambian",
                    "Panjer",
                    "Tegal Harum",
                    "Ubung",
                    "Pemogan",
                    "Kuta",
                    "Jimbaran",
                    "Sidakarya",
                    "Kesiman",
                    "Teuku Umar",
                    "Dauh Puri",
                ])
            alamat1 = ", Denpasar"

        textarea[0].send_keys(alamat)    
        textarea[0].send_keys(alamat1)     

        time.sleep(2)
        radiobuttons[kelamin[index]].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        if positif != 0 and negatif != 0:
            p = random.choice([0,2])
        elif positif != 0 and negatif == 0:
            p = 2
        elif positif == 0 and negatif != 0:
            p = 0

        if p == 0 :
            negatif -= 1
        else:
            positif -= 1

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        t = p
        for i in range(6):
            s1 = random.choice([t,t+1,t+2])
            testcheck[s1].click()
            t += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        t = p
        for i in range(5):
            s1 = random.choice([t,t+1,t+2])
            testcheck[s1].click()
            t += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        t = p
        for i in range(4):
            s1 = random.choice([t,t+1,t+2])
            testcheck[s1].click()
            t += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        t = p
        for i in range(4):
            s1 = random.choice([t,t+1,t+2])
            testcheck[s1].click()
            t += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/V19LF6LXVzbGz1mVA")

        index+=1
        print("==================")
        print("positif : " + str(positif))
        print("negatif : " + str(negatif))
        print("")
        
        times-=1
        print("index  : " + str(index))
        print("times  : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()