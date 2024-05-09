from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_198
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSe-eLqB6S8769tSMdU4_-6UbS-mKT2cBk0fatKGxL2-dazp9A/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_198.times
index = data_198.index

soal = data_198.soal

try:
    while times:
        time.sleep(2)
        tipeKategori = data.pilihTipe(data_198.kategori[0])
        data_198.kategori[0][tipeKategori] -= 1

        usia = data.hitungUsia(19,20) if tipeKategori == 0 else data.hitungUsia(20,21)
        matkul = 0 if tipeKategori == 0 else data.hitungUsia(0,3)

        data.pindahHalaman(driver)

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)
        check = data.tombol(4, driver)

        isian[0].send_keys(list_baru.nama[index])
        isian[1].send_keys(usia)

        time.sleep(1)
        bawah[list_baru.kelamin[index]].click()
        bawah[tipeKategori + 2].click()

        time.sleep(1)
        check[matkul].click()

        data.pindahHalaman(driver)
        
        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(3)
            samping = data.tombol(3, driver)

            data_198.jawab(soal[i], 5, samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("katefori = " + str(data_198.kategori[0]))
        print("")
        
        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    # driver.quit()
    print("berhasil")

        # radiobuttons = data.tombol("kebawah", driver)
        # textboxes = data.tombol("isian", driver)
        # checkboxes = data.tombol("checkbox", driver)
        # testcheck = data.tombol("kesamping", driver)
        # textarea = data.tombol("textarea", driver)
        # pilihan = data.tombol("bubble", driver)
        # lainnya = data.tombol("lainnya", driver)

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")