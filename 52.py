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
driver.get("https://forms.gle/tWiU4FfLNwMQRC7x8")

bantuan = [
    "pinjaman modal yang mudah, dan juga ringan cicilan",
    "Bantuan pinjaman modal dengan bunga rendah",
    "Modal tambahan berupa pinjaman yang dicicil",
    "Bantuan modal yang diberikan oleh pemerintah",
    "Mengikuti pelatihan yang diadakan secara gratis oleh pemerintah",
    "edukasi gratis tentang wirausaha oleh pemerintah",
]

pernah = 0
tidak = 2
idxb = 5

times = 2
index = 11

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        domisili = 0
        lokasi = random.randint(9,16)
        usia = random.choice([18,19,19,19,19,20,20, 20,21,22,23,24])
        jenis = random.randint(25,35)
        karyawan = random.choice([37,38,38,39,39,39,40,41])
        toko = lokasi + 35
        modal = random.randint(53,57)
        pendidikan = random.choice([66,67,68,68,68,68,68,69])
        lama = random.choice([71,72,73,73,73,74,75,76])

        if karyawan == 37 :
            omset = 61
        elif karyawan == 38:
            omset = random.choice([61,62])
        elif karyawan == 39:
            omset = random.choice([62,63,64])
        else:
            omset = random.choice([62,63,64,65])

        if pernah != 0 and tidak != 0:
            pil = random.choice([1,2])
            if pil == 1:
                pernah -= 1
            else:
                tidak -= 1
        elif pernah != 0 and tidak == 0:
            pil = 1
            pernah -= 1
        elif pernah == 0 and tidak != 0:
            pil = 2
            tidak -= 1

        time.sleep(2)
        radiobuttons[domisili].click()
        radiobuttons[lokasi].click()
        radiobuttons[usia].click()
        radiobuttons[jenis].click()
        radiobuttons[karyawan].click()
        radiobuttons[42].click()
        radiobuttons[toko].click()
        radiobuttons[modal].click()
        radiobuttons[omset].click()
        radiobuttons[pendidikan].click()
        radiobuttons[lama].click()

        time.sleep(2)
        if pil == 1:
            radiobuttons[59].click()
            driver.implicitly_wait(4)
            textboxes[0].send_keys(bantuan[idxb])
            idxb += 1

        else:
            radiobuttons[60].click()
            driver.implicitly_wait(4)
            textboxes[0].send_keys("-")

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 13
        while soal:
            s1 = random.choice([p,p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 4
        while soal:
            s1 = random.choice([p,p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 10
        while soal:
            s1 = random.choice([p,p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 4
        while soal:
            s1 = random.choice([p,p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/tWiU4FfLNwMQRC7x8")

        index+=1
        print("==================")
        print("index  : " + str(index))
        print("")
        print("pernah  : " + str(pernah))
        print("tidak  : " + str(tidak))
        print("idxb  : " + str(idxb))

        times-=1
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