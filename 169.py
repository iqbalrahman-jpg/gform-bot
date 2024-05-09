from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_169
import list
import random
import time

link = "http://bit.ly/KuesionerArdel"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_169.times
index = data_169.index
indexTelp = data_169.indexTelp

soal = data_169.jawaban

try:
    while times:
        time.sleep(2)
        kelamin = data_169.kelamin[index]
        usia = data.hitungUsia(20,40)
        pekerjaan = data_169.pekerjaan(usia)
        tipeNomor = random.choice([0,1])
        nomor = "0" if tipeNomor == 0 else list.telp[indexTelp]

        data_169.indexTelp += tipeNomor

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(data_169.nama[index])
        isian[1].send_keys(usia)
        isian[2].send_keys(pekerjaan)
        isian[3].send_keys(nomor)

        time.sleep(1)
        bawah[kelamin].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        samping = data.tombol(3, driver)

        data_169.jawab(samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        # print(" = " + str())
        # print("")
        
        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
        print("indexTelp = " + str(data_169.indexTelp))
finally:
    # driver.quit()
    print("berhasil")

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")