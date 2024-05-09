from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import random

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("profile-directory=Profile 7")

driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
driver.get("https://forms.gle/rUi7fnjKPzLsSB7t5")

nama = [
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Mutia Ayu Nur",
]

times = 10
index = 0
idx = 1
idxx = 1
umur15 = 3
umur18 = 7

# ada kak, request jawaban di page 1
# - Apakah anda sudah mengetahui layanan bank digital: Iya
# - Apakah anda sudah menggunakan layanan bank digital: Tidak

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if idx == 10:
            idx = 0

        option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

        option[0].click()

        time.sleep(20)
        driver.switch_to.window(driver.window_handles[idxx])
        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
        radiobuttons[idx].click()

        time.sleep(20)
        #Hardcoded logic

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        pilihan = driver.find_elements("css selector", ".Hvn9fb")#pilihan

        checkboxes[0].click()
        radiobuttons[0].click()

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        
        textboxes[0].send_keys(nama[index])
        if umur15 != 0 and umur18 != 0:
            umur = random.choice([1,2])
            if umur == 1:
                umur15 -= 1
            else:
                umur18 -= 1
        elif umur15 == 0 :
            umur = 2
            umur18 -= 1
        elif umur18 == 0 :
            umur = 1
            umur15 -= 1

        radiobuttons[umur].click()
        radiobuttons[5].click()

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 5
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+3,p+3,p+4,p+4])
            testcheck[jawab].click()
            p += 5
            soal -= 1


        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 5
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+3,p+3,p+4,p+4])
            testcheck[jawab].click()
            p += 5
            soal -= 1

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 3
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+3,p+3,p+4,p+4])
            testcheck[jawab].click()
            p += 5
            soal -= 1

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 4
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+3,p+3,p+4,p+4])
            testcheck[jawab].click()
            p += 5
            soal -= 1

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 5
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+3,p+3,p+4,p+4])
            testcheck[jawab].click()
            p += 5
            soal -= 1

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 3
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+3,p+3,p+4,p+4])
            testcheck[jawab].click()
            p += 5
            soal -= 1

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 4
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+3,p+3,p+4,p+4])
            testcheck[jawab].click()
            p += 5
            soal -= 1


        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
            )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/rUi7fnjKPzLsSB7t5")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        idx += 1
        idxx += 1
        print("times : " + str(times))
        print("umur15 : " + str(umur15))
        print("umur18 : " + str(umur18))
        
finally:
	# driver.quit()
    print("berhasil")

    # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
    # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
    # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox