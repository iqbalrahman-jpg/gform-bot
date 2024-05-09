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

profil = ["Profile"]

nama = [

]

domisili = [

]

telp = [

]

# perusahaan ===============================
induk = [

]

# 0 pt, 1 cv, 2 firma
bentukinduk = []

bidanginduk = [

]

tahuninduk = [

]

jabataninduk = [

]

anak = [

]

# 0 PT, 1 CV, 2 FIRMA, 3 PERORANGAN
bentukanak = []

bidanganak = [

]

tahunanak = [

]

alasananak = [

]

#0 cowo 1 cewe
kelamin = []

page1 = [
    [5,5,2,3,3,4,5,5,5,5,5,5,3,5,3,5,4,4,5,5,4,4,3,4,5],
    [4,4,3,4,2,3,4,5,5,4,5,4,4,4,4,4,4,4,5,5,4,3,2,4,5],
    [5,5,2,4,2,4,4,4,5,5,5,5,3,4,4,4,4,3,5,5,4,3,2,4,5],
    [5,5,2,3,2,4,5,5,5,5,4,5,5,4,3,4,4,4,5,5,4,3,2,4,5],
    [5,4,2,3,2,4,4,4,5,5,5,5,5,5,3,4,4,3,5,5,4,5,2,4,5],
    [5,5,2,4,3,4,5,5,5,5,5,5,3,5,4,5,4,4,5,5,4,4,3,4,5],
]
page2 = [
    [4,5,3,4,2,4,5,4,4,5,5,5,5,4,4,4,4,4,5,5,4,4,2,4,5],
    [5,5,3,4,3,5,4,5,5,4,5,4,4,5,4,5,4,4,5,5,4,4,3,4,5],
    [5,4,3,4,2,5,4,4,4,4,4,4,4,4,4,5,4,4,5,5,4,3,2,4,5],
    [4,4,3,4,3,3,5,3,4,5,5,5,4,4,4,4,4,3,5,5,3,4,3,4,5],
    [5,5,3,4,3,5,4,5,5,4,5,4,4,5,4,5,4,4,5,5,4,4,3,4,5],
]
page3 = [
    [4,3,3,4,2,5,4,4,4,5,4,5,4,4,4,5,4,3,5,5,4,3,2,4,4],
    [5,5,2,3,2,4,5,5,5,5,4,5,5,4,3,4,4,4,5,5,4,3,2,4,5],
    [4,5,3,4,2,4,5,4,4,5,5,5,5,4,4,4,4,4,5,5,4,4,2,4,5],
    [4,4,3,4,2,3,4,5,5,4,5,4,4,4,4,4,4,4,5,5,4,3,2,4,5],
]
page4 = [
    [4,4,3,4,3,3,5,3,4,5,5,5,4,4,4,4,4,3,5,5,3,4,3,4,5],
    [4,5,3,4,2,4,5,4,4,5,5,5,5,4,4,4,4,4,5,5,4,4,2,4,5],
    [5,4,3,4,2,5,4,4,4,4,4,4,4,4,4,5,4,4,5,5,4,3,2,4,5],
    [5,5,2,3,2,4,5,5,5,5,4,5,5,4,3,4,4,4,5,5,4,3,2,4,5],
]
page5 = [
    [4,5,3,4,2,4,5,4,4,5,5,5,5,4,4,4,4,4,5,5,4,4,2,4,5],
    [5,5,3,3,2,5,4,5,4,4,5,4,5,4,3,4,4,3,5,5,4,4,2,4,5],
    [4,5,2,4,3,4,5,4,5,5,5,5,4,5,4,4,4,4,5,5,4,5,3,4,5],
]
page6 = [
    [5,5,2,3,3,4,5,5,5,5,5,5,3,5,3,5,4,4,5,5,4,4,3,4,5],
    [4,4,4,3,2,4,5,5,4,4,5,4,5,4,3,4,4,4,5,5,4,4,2,4,4],
    [4,3,3,4,2,5,4,4,4,5,4,5,4,4,4,5,4,3,5,5,4,3,2,4,4],
    [5,5,2,3,3,4,5,5,5,5,5,5,3,5,3,5,4,4,5,5,4,4,3,4,5],
    [5,5,3,3,2,5,4,5,4,4,5,4,5,4,3,4,4,3,5,5,4,4,2,4,5],
    [4,5,2,4,2,4,5,4,5,5,5,5,4,4,4,3,4,3,5,5,4,4,2,4,5],
]
page7 = [
    [5,5,2,3,3,4,5,5,5,5,5,5,3,5,3,5,4,4,5,5,4,4,3,4,5],
    [5,5,2,3,2,4,5,5,5,5,4,5,5,4,3,4,4,4,5,5,4,3,2,4,5],
    [5,5,2,4,3,4,5,5,5,5,5,5,3,5,4,5,4,4,5,5,4,4,3,4,5],
    [5,5,2,3,2,4,5,5,5,5,4,5,5,4,3,4,4,4,5,5,4,3,2,4,5],
    [4,4,4,3,2,4,5,5,4,4,5,4,5,4,3,4,4,4,5,5,4,4,2,4,4],
]
page8 = [
    [5,4,3,4,2,5,4,4,4,4,4,4,4,4,4,5,4,4,5,5,4,3,2,4,5],
    [5,5,2,4,3,4,5,5,5,5,5,5,3,5,4,5,4,4,5,5,4,4,3,4,5],
    [4,5,2,4,3,4,5,4,5,5,5,5,4,5,4,4,4,4,5,5,4,5,3,4,5],
    [4,5,2,4,2,4,5,4,5,5,5,5,4,4,4,3,4,3,5,5,4,4,2,4,5],
    [5,5,3,3,2,5,4,5,4,4,5,4,5,4,3,4,4,3,5,5,4,4,2,4,5],
]

index = 0
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf0QFF5TzDiPnbs_YnCZ-RbWZidEK_2q9bA_jWBLxs3xmDo2w/viewform?usp=sf_link")

        if i == len(profil) - 1:
            times = 5
        else:
            times = 10

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
            # ================================================================================

            usia = random.randint(30,45)

            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            textboxes[0].send_keys(nama[index])
            textboxes[1].send_keys(usia)
            textboxes[2].send_keys(domisili[index])
            textboxes[3].send_keys(telp[index])
            driver.implicitly_wait(4)

            checkboxes[kelamin[index]].click()

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
            omset = random.choice([4,5,6])

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            textpil = driver.find_elements("css selector", ".Hvn9fb")#isianpilihan
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

            textboxes[0].send_keys(induk[index])
            textboxes[1].send_keys(bidanginduk[index])
            textboxes[2].send_keys(tahuninduk[index])
            textboxes[3].send_keys(jabataninduk[index])
            textboxes[4].send_keys("1")
            textboxes[5].send_keys(anak[index])
            textboxes[6].send_keys(bidanganak[index])
            textboxes[7].send_keys(tahunanak[index])
            driver.implicitly_wait(4)
            
            textarea[0].send_keys(alasananak[index])
            driver.implicitly_wait(4)

            radiobuttons[bentukinduk[index]].click()
            radiobuttons[omset].click()

            time.sleep(2)
            if bentukanak[index] == 0:
                s1 = 7
            elif bentukanak[index] == 1:
                s1 = 8
            elif bentukanak[index] == 2:
                s1 = 9
            else:
                s1 = 10
                textpil[1].send_keys("perorangan")

            time.sleep(2)
            radiobuttons[s1].click()

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

            p = -1
            for i in range(6):
                s1 = page1[i][index] + p
                testcheck[s1].click()
                p += 5

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

            p = -1
            for i in range(5):
                s1 = page2[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(4):
                s1 = page3[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(4):
                s1 = page4[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(3):
                s1 = page5[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(6):
                s1 = page6[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(5):
                s1 = page7[i][index] + p
                testcheck[s1].click()
                p += 5

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
            
            p = -1
            for i in range(5):
                s1 = page8[i][index] + p
                testcheck[s1].click()
                p += 5

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
            driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf0QFF5TzDiPnbs_YnCZ-RbWZidEK_2q9bA_jWBLxs3xmDo2w/viewform?usp=sf_link")

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))

        driver.quit()
        
finally:
    # driver.quit()
    print("berhasil")

            # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
            # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
            # textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            # textpil = driver.find_elements("css selector", ".whsOnd")#isianpilihan

            # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

            # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
            # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

            # time.sleep(3)
            # kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            # kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            # if len(kirims1) != 0 :
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            #     )
            # else:
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            #     )

            # submit_button.click()