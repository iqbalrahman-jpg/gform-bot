from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_199
import list_baru
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSfWrSPcyJnyE3ygHcSCiGTgLY7ULpbdTgaYEor2FgL9129kiA/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_199.times
index = data_199.index

soal = data_199.soal
jawab = data_199.jawab

try:
    while times:
        time.sleep(2)
        tipeAsal = data.pilihTipe(data_199.kategori[0])
        data_199.kategori[0][tipeAsal] -= 1

        asal = 0 if tipeAsal == 0 else data.hitungUsia(1,5)

        tipeUsia = data.pilihTipe(data_199.kategori[1])
        data_199.kategori[1][tipeUsia] -= 1

        usia = 7 if tipeUsia == 0 else data.hitungUsia(8,12)

        kelamin = data_199.kelamin[index] + 13

        pekerjaan = data_199.pekerjaan(usia)

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list.telp[index])

        time.sleep(1)
        bawah[asal].click()
        bawah[usia].click()
        bawah[kelamin].click()
        bawah[pekerjaan].click()
        bawah[19].click()

        data.pindahHalaman(driver)

        data.pindahHalaman(driver)

        time.sleep(3)
        samping = data.tombol(3, driver)

        data.polaJawabCustom(-1, jawab[index], 5, samping)
        
        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        bawah[0].click()

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_199.kategori[0]))
        print("           " + str(data_199.kategori[1]))
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