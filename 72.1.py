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

profil = ["Default"]

email = [
    "zakkyrahman1131@gmail.com",
    "kristianiliviadg@gmail.com",
    "gizelaptriyaa@gmail.com",
    "muhmadputra15@gmail.com",
]

# laki 0 perempuan 1
kelamin = [
1,0,1,0,
]
# tasik 8
# cirebon 9
domisili = [
7,7,5,7,
]

kategori = [
9,11,9,9
]

s1n1 = [
 4,5,2,2,
]

s1n2 = [
3,2,3,3,
]

s1n3 = [
3,4,5,3
]

s1n4 = [
3,4,5,3
]

s2n1 = [
3,2,3,3 
]

s2n2 = [
4,4,5,5
]

s2n3 = [
4,4,5,5
]

s2n4 = [
5,4,4,5
]

s3n1 = [
4,4,5,4
]

s3n2 = [
4,4,5,5
]

s3n3 = [
4,5,4,5
]

s4n1 = [
4,5,4,5
]

s4n2 = [
4,5,3,2
]

s4n3 = [
4,5,3,2
]

s4n4 = [
4,5,3,2
]

s5n1 = [
4,5,3,2
]

s5n2 = [
5,4,4,3
]

s5n3 = [
5,4,4,5
]


index = 0
genz = 4
geny = 0
genx = 0
        
try:
    for i in range(7):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://forms.gle/D2tRgWhzwkizJduMA")

        times = 3
        idx = 1
        idxx = 1

        while times:
            time.sleep(2)

            if idx == 10:
                idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(10)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[idx].click()

            time.sleep(10)

            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
            pilihan = driver.find_elements("css selector", ".Hvn9fb")#pilihan

            checkboxes[0].click()
            
            if genz != 0 and geny != 0 and genx != 0:
                generasi = random.choice([0,1,2])
                if generasi == 0:
                    genz -= 1
                elif generasi == 1:
                    geny -= 1
                elif generasi == 2:
                    genx -= 1
            elif genz == 0 and geny != 0 and genx != 0:
                generasi = random.choice([1,2])
                if generasi == 1:
                    geny -= 1
                elif generasi == 2:
                    genx -= 1
            elif genz != 0 and geny == 0 and genx != 0:
                generasi = random.choice([0,2])
                if generasi == 0:
                    genz -= 1
                elif generasi == 2:
                    genx -= 1
            elif genz != 0 and geny != 0 and genx == 0:
                generasi = random.choice([0,1])
                if generasi == 0:
                    genz -= 1
                elif generasi == 1:
                    geny -= 1
            elif genz == 0 and geny == 0 and genx != 0:
                generasi = 2
                genx -= 1
            elif genz != 0 and geny == 0 and genx == 0:
                generasi = 0
                genz -= 1
            elif genz == 0 and geny != 0 and genx == 0:
                generasi = 1
                geny -= 1

            radiobuttons[generasi].click()
            
            if domisili[index] == 8:
                pilihan[1].send_keys("Tasikmalaya")
            elif domisili[index] == 9:
                pilihan[1].send_keys("Cirebon")
            else:
                radiobuttons[domisili[index]].click()

            radiobuttons[kategori[index]].click()

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
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            
            textboxes[0].send_keys(email[index])
            radiobuttons[kelamin[index]].click()
            time.sleep(2)
            pendidikan = random.choice([2,3,3,4,4,4,5])
            radiobuttons[pendidikan].click()
            income = random.choice([7,8,9,10])
            radiobuttons[income].click()
            time.sleep(2)
            radiobuttons[11].click()

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
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            
            testcheck[s1n1[index]-1].click()
            testcheck[s1n2[index]+4].click()
            testcheck[s1n3[index]+9].click()
            testcheck[s1n4[index]+14].click()

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
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            
            testcheck[s2n1[index]-1].click()
            testcheck[s2n2[index]+4].click()
            testcheck[s2n3[index]+9].click()
            testcheck[s2n4[index]+14].click()

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
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            
            testcheck[s3n1[index]-1].click()
            testcheck[s3n2[index]+4].click()
            testcheck[s3n3[index]+9].click()

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
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            
            testcheck[s4n1[index]-1].click()
            testcheck[s4n2[index]+4].click()
            testcheck[s4n3[index]+9].click()
            testcheck[s4n4[index]+14].click()

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
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            
            testcheck[s5n1[index]-1].click()
            testcheck[s5n2[index]+4].click()
            testcheck[s5n3[index]+9].click()

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
            driver.get("https://forms.gle/D2tRgWhzwkizJduMA")

            index += 1
            idx += 1
            idxx += 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))

            times -= 1
            print("genz : " + str(genz))
            print("geny : " + str(geny))
            print("genx : " + str(genx))

        driver.quit()
        
finally:
    # driver.quit()
    print("berhasil")

    # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
    # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
    # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox