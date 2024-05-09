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
driver.get("https://forms.gle/9WauDyHf8ztPd9DT8")

nama = [
    "Eka Wahyu",
    "Yuli Setiawan",
    "Eko Wijaya",
    "Yuni Nafisah",
    "Prita agustina",
    "Naufal Ardiansyah",
    "Bagus Rahmad",
    "Hana Anissa Herian",
    "Heraldy Gunawan",
    "Budi Santoso",

    "Bagus Hariawan",
    "Dwi Panca",
    "Okto Devano",
    "Olivia Niken",
    "Yazid Hasbilluh Kurniawan",
    "faradilla nina",
    "Shabir Maulana",
    "Sarah Husaini",
    "Anindya Riri",
    "Erfina Pratiwi",

    "Argo Prasetyawan",
    "Salma Azizah",
    "Faradilla Aulia",
    "Dimas Wahyu",
    "Regina Cantika Subandini",
    "Agis Prasetya",
    "Ardy Riski",
    "Muhammad Fadlan",
    "Septinia Kurniawan",
    "Damar Eka",

    "Fredinan Puan",
    "Amanda Bella Putri",
    "Bambang Suhatmoyo",
    "Kairaini Aliesa",
    "Lika Arletta",
    "Arjuna Ghafur",
    "Damar Hafidzhuan",
    "Lista Kamilla",
    "Sadiva Pratiwi",
    "Hermanto Caisar",

    "Windy Cantika",
    "Stephani Amanda Safitri",
    "Ardyanto Putra Wardhana",
    "Marylda Putri Sentosa",
    "Nabil Saputra",
    "Khansa Azzahra",
    "Naufal Azwin",
    "Riska Rahmawati",
    "Rohmat Ubaidillah",
    "Setiawan Nugraha",
    
    "Yanto Wibowo",
    "Nina Anggraini",
    "Yoga Putra Wijaya",
    "Dini Cahyani",
    "Raka Triyana",
    "Maya Dewi Utami",
    "Indra Kusuma",
    "Devi Puspitasari",
    "Bima Aditya Nugraha",
    "Rina Anggraini Sari",
]

# laki 0 perempuan 1
kelamin = [
	0,0,0,1,1,0,0,1,0,0, 0,0,0,1,0,1,1,1,1,1, 0,1,1,0,1,0,0,0,1,0, 0,1,0,1,1,0,0,1,1,0, 
    1,1,0,1,0,1,0,1,0,0, 0,1,0,1,0,1,1,1,0,1,
	]

positif = 48
negatif = 12

times = 60
index = 0

soal = [5, 4, 4, 6, 4]

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        usia = random.choice([2,3,3,3,3,4,4,4,4,5,6])

        if usia == 2 :
            pendidikan = 7
        elif usia == 3:
            pendidikan = random.randint(7,9)
        else :
            pendidikan = random.choice([7,8,8,8,9,9,9,9,10,10,10,10,10,11])
            
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])

        time.sleep(2)
        radiobuttons[usia].click()
        radiobuttons[kelamin[index]].click()
        radiobuttons[pendidikan].click()

        time.sleep(2)
        if positif != 0 and negatif != 0:
            pil = random.choice([0,1])
        elif positif != 0 and negatif == 0:
            pil = 0
        elif positif == 0 and negatif != 0:
            pil = 1

        time.sleep(2)
        if pil == 0:
            for i in range(len(soal)) :
                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

                time.sleep(2)
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
                p = 2
                x = soal[i]
                while x :
                    s1 = random.choice([p, p+1, p+1, p+1, p+1, p+1, p+1, p+1, p+2, p+2, p+2, p+2, p+2, p+2, p+2])
                    testcheck[s1].click()
                    p += 5
                    x -= 1

            positif -= 1
        else:
            for i in range(len(soal)) :
                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

                time.sleep(2)
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
                p = 0
                x = soal[i]
                while x :
                    s1 = random.choice([p, p, p, p, p, p, p+1, p+1, p+1, p+1, p+1, p+1, p+2])
                    testcheck[s1].click()
                    p += 5
                    x -= 1

            negatif -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/9WauDyHf8ztPd9DT8")

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