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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeTi5tHcu63tYy_2UynyNxgJBHxAfK4V7WLzB5lr1gj8j8q3Q/viewform")

namaPerusahaan = [
    "INDAH",
    "PT. Istana Tiara",
    "TIMBUL JAYA",
    "PT. HM Sampoerna Tbk",
    "PT. Wismilak Inti Makmur Tbk",
    "SIDO LUHUR",
    "MUDJIYO",
    "PT. Pakuwon Jati Tbk",
    "PT. Gunawan Dianjaya Steel Tbk",
    "PT. Darmi Bersaudara Tbk",
    "ASRI",
    "SUMBER REJEKI",
    "PT. Campina Ice Cream Industry Tbk",
    "BINTANG IDOLA",
    "SEKAR GEMILANG",
    "Ispat Indo",
    "PGS",
    "IDN Media",
    "Unilever Indonesia",
    "Jawa Pos",
    "ANTIK BARU ",
    "LESTARI",
    "MUSLIH",
    "REJEKI",
    "SIDODADI",
    "MITRA ABADI",
    "PAL Indonesia",
    "SANTOSA",
    "LIMA DEWA",
    "RUKUN JAYA",
]

email = [
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
]

times = 30
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        tunjangan = random.choice([5,6,7])

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(namaPerusahaan[index])
        textboxes[1].send_keys(email[index])
        driver.implicitly_wait(4)

        radiobuttons[random.choice([0,1])].click()
        radiobuttons[tunjangan].click()

        p = 8
        soal = 2
        while soal:
            s1 = random.choice([p,p+1,p+2,p+3,p+4])
            radiobuttons[s1].click()
            p += 5
            soal -= 1

        time.sleep(2)
        if tunjangan == 5:
            pernah = random.choice([18,19,20])
            membantu = random.choice([23,24,25])
            jelas = random.choice([28,28,28,29])
        elif tunjangan == 6:
            pernah = 21
            membantu = 27
            jelas = 30
        else:
            pernah = 22
            membantu = 27
            jelas = 30

        fitur = random.choice([31,32,33,34])
        mobile = random.choice([36,37,38,39,40])

        time.sleep(2)
        radiobuttons[pernah].click()
        radiobuttons[membantu].click()
        radiobuttons[jelas].click()
        radiobuttons[fitur].click()
        radiobuttons[mobile].click()
        driver.implicitly_wait(4)

        temp = random.randint(1,5)
        check1 = random.sample([0,1,2,3,4,5], temp)

        for i in check1:
            checkboxes[i].click()

        time.sleep(2)

        temp2 = random.randint(1,5)
        check2 = random.sample([6,7,8,9,10], temp2)

        for i in check2:
            checkboxes[i].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeTi5tHcu63tYy_2UynyNxgJBHxAfK4V7WLzB5lr1gj8j8q3Q/viewform")

        index+=1
        print("==================")
        # print("  : " + str())
        # print("")
        
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