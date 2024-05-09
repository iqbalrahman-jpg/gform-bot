from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Firefox()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfdOzOkP5anOup3aC7_2O1w4_EY55PhxMqm58mbutLOSKcnug/formResponse")
times = 15

nama = [
    "Ali Hasanudin",
    "Rizki Febrianto Putra",
    "Budi Prasetyo",
    "Aryo Nugraha",
    "Yahya Nugraha",
    "Nanda Herlambang",
    "Yudi Pradanawan",
    "Yuli Setyawan",
    "Bayu Danang Merta",
    "Budi Suryanto",
    "Sadewa Lingga Budiantoro",
    "Alfianto Yusuf Kunta Cahya",
    "Fattahilah Sadewa",
    "Attaka Majid",
    "Fabian Bagas Nadeo"
]

index = 0
try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(nama[index])
        radiobuttons[0].click()

        usia = random.choice([2,3,4,5,6])
        radiobuttons[usia].click()

        if usia == 2:
            radiobuttons[8].click()
        elif usia == 3:
            dum = random.choice([7,8,9,11])
            radiobuttons[dum].click()
        else:
            dum = random.choice([7,7,9,10,11])
            radiobuttons[dum].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "l4V7wb"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#isian
 
        p1 = 0
        p2 = 1
        p3 = 2
        bag1 = 10
        while bag1 :
            check1 = random.choice([p1,p1,p1,p2,p2,p2,p3])
            radiobuttons[check1].click()
            p1+=5
            p2+=5
            p3+=5
            bag1-=1

        time.sleep(6)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#isian

        p1 = 0
        p2 = 1
        p3 = 2
        bag1 = 10
        while bag1 :
            check1 = random.choice([p1,p1,p1,p2,p2,p2,p3])
            radiobuttons[check1].click()
            p1+=5
            p2+=5
            p3+=5
            bag1-=1

        driver.implicitly_wait(4)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfdOzOkP5anOup3aC7_2O1w4_EY55PhxMqm58mbutLOSKcnug/formResponse")
        times-=1
        index+=1
        print(times)
finally:
	driver.quit()
    # print("berhasil")
