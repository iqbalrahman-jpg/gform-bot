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
driver.get("https://forms.gle/wnRTvpUBF7ekTgLE9")

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
]

#0 laki 1 perempuan
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,]

orang2 = 7
orang4 = 8

times = 15
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        radiobuttons[2].click()
        radiobuttons[8].click()
        radiobuttons[16].click()
        radiobuttons[19].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        if orang2 != 0 and orang4 != 0 :
            pil = random.choice([1,2])
            if pil == 1:
                orang2 -= 1
            else:
                orang4 -= 1
        elif orang2 != 0 and orang4 == 0 :
            pil = 1
            orang2 -= 1
        elif orang2 == 0 and orang4 != 0 :
            pil = 2
            orang4 -= 1

        if pil == 1:
            bag = 2
            while bag:
                time.sleep(2)
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

                p = 1
                soal = 4
                while soal:
                    s1 = random.choice([p,p+2])
                    testcheck[s1].click()
                    p += 5
                    soal -= 1

                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()
                bag -= 1

            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p = 1
            soal = 3
            while soal:
                s1 = random.choice([p,p+2])
                testcheck[s1].click()
                p += 5
                soal -= 1

        else:
            bag = 2
            while bag:
                time.sleep(2)
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

                p = 3
                soal = 4
                while soal:
                    s1 = random.choice([p,p+1])
                    testcheck[s1].click()
                    p += 5
                    soal -= 1

                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()
                bag -= 1

            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p = 3
            soal = 3
            while soal:
                s1 = random.choice([p,p+1])
                testcheck[s1].click()
                p += 5
                soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/wnRTvpUBF7ekTgLE9")

        index+=1
        print("==================")
        print("index  : " + str(index))
        print("")
        print("orang2 : " + str(orang2))
        print("orang4 : " + str(orang4))

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