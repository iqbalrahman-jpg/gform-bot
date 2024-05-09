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
driver.get("https://forms.gle/5kRW9JdFfVkeVBET6")

nama = [
    "Bagas Anugrah",
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
]

domisili = [
    "surabaya",
    "jawa timur",
    "gresik",
    "banyuwangi",
    "Bali",
    "Surabaya",
    "Yogyakarta",
    "jakarta",
    "Jakarta",
    "Bandung",
    "semarang",
    "DKI Jakarta",
    "surabaya",
    "Bekasi",
    "Bandung",
]

#0 laki, 1 perempuan
kelamin = [0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,]

times = 1
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(domisili[index])
        umur = random.choice([0,1])
        radiobuttons[umur].click()
        if umur == 0:
            pengeluaran = random.choice([4,5])
        else:
            pengeluaran = random.choice([2,3])

        radiobuttons[pengeluaran].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[0].click()
        time.sleep(1)
        radiobuttons[2].click()
        time.sleep(1)
        radiobuttons[5].click()
        p = 6
        soal = 4
        while soal:
            radiobuttons[p].click()
            soal -= 1
            p += 2

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
       
        # strategi = random.choice([0,1])
        radiobuttons[1].click()
        time.sleep(1)
        radiobuttons[7].click()
        time.sleep(1)
        radiobuttons[8].click()
        time.sleep(1)
        radiobuttons[12].click()
        p = 0
        soal = 6
        while soal:
            jawab = random.choice([p,p+1])
            testcheck[jawab].click()
            soal -= 1
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        pesan = random.choice([2,3])
        radiobuttons[pesan].click()
        p = 0
        soal = 14
        while soal:
            jawab = random.choice([p+3,p+2])
            testcheck[jawab].click()
            soal -= 1
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/5kRW9JdFfVkeVBET6")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")

        times-=1
        print("times : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()