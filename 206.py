from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_206
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdfY-aTHwk4wLUe8SfvLAFGmG7vJue7T7zOJG0BpSobYvksAg/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_206.times
index = data_206.index

soal = data_206.soal

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(18,27)

        pekerjaan = data_206.pekerjaan(usia)
        time.sleep(1)
        sejak = data_206.sejak(usia)

        frekuensi = random.randint(0,1)
        durasi = random.choice([2,2,3,3,3,3,3])

        tipeJawab = data.pilihTipe(data_206.kategori)
        data_206.kategori[tipeJawab] -= 1

        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.inisialPerempuan[index])
        isian[1].send_keys(usia)
        isian[2].send_keys(pekerjaan)
        isian[3].send_keys(sejak)

        time.sleep(1)
        bawah[frekuensi].click()
        bawah[durasi].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        data.polaJawab2(0, tipeJawab, 10, 4, bawah)

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        data.polaJawab4(0, 0, 20, 4, bawah)

        data.pindahHalaman(driver)

        time.sleep(3)
        samping = data.tombol(3, driver)

        data.polaJawab3(2, 2, 2, 5, samping)

        data.pindahHalaman(driver)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_206.kategori))
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
