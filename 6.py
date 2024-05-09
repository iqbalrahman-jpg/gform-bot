from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Firefox()
driver.get("http://bit.ly/SurveyOnlineTransport")
times = 25

domisili = []
lain = []
alasan = []
tarif = []
promosi = []
keunggulan = []
kelemahan = []
sederhana = []
uiux = []
fitur = []

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

        gender = random.choice([0,1])
        radiobuttons[gender].click()

        usia = random.choice([2,3,4,5,6,7])
        radiobuttons[usia].click()

        textboxes[0].send_keys(domisili[index])

        grab = random.choice([2,3,4])
        gojek = random.choice([5,6])
        indriver = random.choice([8,9,9,10,10,11])
        maxim = random.choice([12,13,13,14,15])
        testcheck[grab].click()
        testcheck[gojek].click()
        testcheck[indriver].click()
        testcheck[maxim].click()

        textboxes[1].send_keys(lain[index])

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "l4V7wb"))
        )

        submit_button.click()

        time.sleep(1)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#isian
 
        radiobuttons[0].click()

        textboxes[0].send_keys(alasan[index])
        textboxes[1].send_keys(tarif[index])
        textboxes[2].send_keys(promosi[index])
        textboxes[3].send_keys(keunggulan[index])
        textboxes[4].send_keys(kelemahan[index])

        kepuasan = random.choice([0,1,2,3,4])
        testcheck[kepuasan].click()

        textboxes[5].send_keys(sederhana[index])
        textboxes[6].send_keys(uiux[index])
        textboxes[7].send_keys(fitur[index])

        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        # )

        # submit_button.click()

        # driver.implicitly_wait(4)
        # driver.get("http://bit.ly/SurveyOnlineTransport")
        times-=1
        index+=1
        print(times)
finally:
	# driver.quit()
    print("berhasil")
