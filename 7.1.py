from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Firefox()
driver.get("https://forms.gle/fuXrDK1dms28hYft5")
times = 10

instagram = [
    "@cynaranafs",
    "@monahadfinna_",
    "@mahendrarhejaa",
    "@fryshtaekanabilla",
    "@yanuarsuryadi_",
    "@rayhanadiwicasa",
    "@sutisnaayuni_",
    "@ayuyulistyan",
    "@mputrasusanto_",
    "@ardyantorizki",
]

nama = [
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
]

index = 0
try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[0].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "l4V7wb"))
        )

        submit_button.click()

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[0].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
 
        submit_button.click()

        time.sleep(5)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(instagram[index])

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
 
        submit_button.click()

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[0].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
 
        submit_button.click()

        time.sleep(5)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        umur = random.choice([0,0,0,0,1,2,3])
        radiobuttons[umur].click()

        if umur == 0:
            pekerjaan = random.choice([4,4,4,4,5,6,7])
            radiobuttons[pekerjaan].click()
        else : 
            pekerjaan = random.choice([4,5,5,5,6,6,6,7,7])
            radiobuttons[pekerjaan].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
 
        submit_button.click()

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        p2 = 1
        p3 = 2
        p4 = 3
        p5 = 4
        soal = 7
        while soal :
            jawab = random.choice([p3,p3,p4,p4,p4,p4,p5,p5,p5,p5,p5])
            testcheck[jawab].click()
            p1 += 5
            p2 += 5
            p3 += 5
            p4 += 5
            p5 += 5
            soal -=1

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
 
        submit_button.click()

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        p2 = 1
        p3 = 2
        p4 = 3
        p5 = 4
        soal = 7
        while soal :
            jawab = random.choice([p3,p3,p4,p4,p4,p4,p5,p5,p5,p5,p5])
            testcheck[jawab].click()
            p1 += 5
            p2 += 5
            p3 += 5
            p4 += 5
            p5 += 5
            soal -=1

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/fuXrDK1dms28hYft5")
        times-=1
        index+=1
        print(times)
finally:
    # print("berhasil")
	driver.quit()
