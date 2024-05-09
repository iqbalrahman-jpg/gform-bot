from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

import data
import time
import random
import list_baru

link = "https://docs.google.com/forms/d/e/1FAIpQLSdKW1qetypfBSdBDPCaZu2mwj1iSl1KNe6NbP110htVb7bSvA/viewform?fbzx=7410127517196114550"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

kategori = [
    7,0,0,43,0
]

times = 50
index = 50
        
try:
    while times:
        time.sleep(3)
        tipeKategori = data.pilihTipe(kategori)
        kategori[tipeKategori] -= 1

        time.sleep(3)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        textboxes[0].send_keys(list_baru.email[index])

        time.sleep(2)
        p = tipeKategori
        data.polaJawab2(0, p, 29, 5, testcheck)
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        usia = random.choice([2,3,3,3,3,4,4,4,4,4,5])
        
        if usia == 2 :
            pendidikan = random.choice([6,7])
            posisi = random.choice([11,11,11,12])
        elif usia == 3 :
            pendidikan = random.choice([7,8,8,8,9])
            posisi = random.choice([11,12,12])
        else :
            pendidikan = random.choice([7,8,9,9,9,9,9])
            posisi = random.choice([11,11,11,12,12,12,12,13])
        
        time.sleep(2)
        if posisi == 11 :
            lama = random.choice([15,16])
        elif posisi == 12 :
            lama = random.choice([15,16,16,16,16,17])
        else :
            lama = random.choice([16,17,17,17,17,18,18,18,18])

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[list_baru.kelamin[index]].click()
        radiobuttons[usia].click()
        radiobuttons[pendidikan].click()
        radiobuttons[posisi].click()
        radiobuttons[lama].click()

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")

        kirims1[len(kirims1)-1].click()

        driver.implicitly_wait(4)
        driver.get(link)

        index += 1
        times -= 1
        print("==================")
        print("times : " + str(times))
        print("index : " + str(index))
        print("")
        print("kateogir = " + str(kategori))
        
    # driver.quit()
finally:
    print("berhasil")