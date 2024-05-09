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

link = "https://forms.gle/pW2pts1p4BhMX9WaA"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

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

kantor = [
    "KANTOR JASA AKUNTAN PETTARANI MAKASSAR",
    "Kantor Akuntan Publik Kusnadi Purnomo & Rekan",
    "KAP Kumalahadi, Kuncara, Sugeng Pamudji & Rekan Cab. Makassar",
    "KAP Kumalahadi, Kuncara, Sugeng Pamudji & Rekan Cab. Makassar",
    "Kantor Pelayanan Pajak Pratama - Makassar Barat",
    "Kantor Akuntan Publik Drs Blasius Mangande Msi",
    "KAP BTFD",
    "Kantor Akuntan Publik Drs Rusman Thoeng, M.Com, Bap",
    "Kantor Akuntan Publik Usman & Rekan",
    "Pt. Interpan Pasific Futures",
    "Kantor Konsultan Pajak 'Hams'",
    "Kap Drs. Ida Bagus Djagera",
    "KAP Yaniswar & Rekan",
    "KAP JOJO SUNARJO & REKAN Cabang Makassar",
    "Burake Jaya Consultant",
    "Kantor Akuntan Publik A Salam Rauf & Rekan",
    "Kantor Akuntan Publik Drs Thomas",
    "Kantor Panwascam Tallo",
    "Kantor Akuntan Publik Kusnadi Purnomo & Rekan",
    "Bahana Solution",
    "Kantor Akuntan Publik Drs Abdul Aziz Bolong",
    "Kantor Akuntan Publik Drs Blasius Mangande MSi",
    "Kantor Akuntan Publik Mansyur Sain & Rekan",
    "Kpp Pratama Makassar Selatan",
    "Kantor Akuntan Fredy Tjoei Yanto",
    "Kantor Akuntan Bernardi Drs",
    "Kantor Akuntan Publik Ellya Noorlisyati & Rekan",
    "Dm Konsultan",
    "Akuntan Publik Isak Saleh Suwondo & Rekan",
    "KAP Kumalahadi, Kuncara, Sugeng Pamudji & Rekan Cab. Makassar",
    "Kantor Akuntan Publik A Salam Rauf & Rekan",
    "Kantor Akuntan Publik Drs. Thomas Blasius Widartoyo & Rekan",
    "Kantor Konsultan Pajak Ezra Palisungan",
    "Karya Artha Bakti Group",
    "Kantor Akuntan Publik Drs Abdul Aziz Bolong",
    "KANTOR AKUNTAN PUBLIK ASRI",
    "Kantor Akuntan Fredy Tjoei Yanto",
    "Kjpp Wiratno, Achmanan, Armansyah & Rekan",
    "Kantor Akuntan Publik Rudi Kartamulya BU",
    "Zahir Accounting",
    "Kantor Akuntan Publik Drs Blasius Mangande MSi",
    "Kpp Madya Makassar",
    "Kantor Akuntan Publik Thomas Blasius Widartoyo & Rekan",
    "KAP Yakub Ratan dan Rekan",
    "Kantor Akuntan Publik (KAP) Drs. Rusman Thoeng, M.Com, BAP",
    "Kantor Pelayanan Pajak Pratama - Makassar Barat",
    "KAP Yakub Ratan dan Rekan",
    "Kantor Konsultan Pajak Karya Artha Bhakti Group",
    "KAP BTFD",
    "Kantor Akuntan Publik Rusman Thoeng Bap",
]

kelamin = [
    1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,
]

positif = 42
negatif = 4

soal = [10, 10]

times = 46
index = 4

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(kantor[index])

        radiobuttons[2].click()
        radiobuttons[kelamin[index]].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        if positif != 0 and negatif != 0:
            pil = random.choice([0,0,1])
        elif positif != 0 and negatif == 0:
            pil = 0
        elif positif == 0 and negatif != 0:
            pil = 1
        
        if pil == 0:
            p = 2
            for i in range(soal[0]) :
                s1 = random.choice([p, p+1, p+1, p+1, p+2, p+2, p+2])
                radiobuttons[s1].click()
                p += 5
            
            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            p = 2
            for i in range(soal[1]) :
                s1 = random.choice([p, p+1, p+1, p+1, p+2, p+2, p+2])
                radiobuttons[s1].click()
                p += 5

            positif -= 1
        else:
            p = 0
            for i in range(soal[0]) :
                s1 = random.choice([p, p, p+1, p+1, p+1, p+2])
                radiobuttons[s1].click()
                p += 5
            
            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            p = 0
            for i in range(soal[1]) :
                s1 = random.choice([p, p, p+1, p+1, p+1, p+2])
                radiobuttons[s1].click()
                p += 5

            negatif -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("positif = " + str(positif))
        print("negatif = " + str(negatif))
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