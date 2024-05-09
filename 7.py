from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Firefox()
driver.get("https://forms.gle/fuXrDK1dms28hYft5")
times = 25

instagram = [
"@mutiaayunur_",
"@ali.hasanudin",
"@riskiaayu.feb",
"@budiprasetyo.w",
"@aryonugraha_",
"@nanaannisa_",
"@yahya.nugraha",
"@putrikirana.d",
"@nandamarsa.ayu",
"@yudipradana_",
"@yuliayunda.d",
"@bayudanangm",
"@bellandaclara_",
"@budisuryantoo",
"@mirandane11a",
"@sadewalingga_",
"@alffiantok",
"@annisachaniia",
"@fattahilah.s",
"@diahayucindy_",
"@attakamajid_",
"@azzarinristia",
"@fabianadeop",
"@niaekayuliana_",
"@bayudwiganara_",
]

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
    "Annisa Chania"
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",

    "Attaka Majid",
    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
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
            jawab = random.choice([p1,p2,p3,p4,p4,p4,p4,p5,p5,p5,p5,p5])
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
            jawab = random.choice([p1,p2,p3,p4,p4,p4,p4,p5,p5,p5,p5,p5])
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
