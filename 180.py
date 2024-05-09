from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_180
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdDSkBWblRfFxHXNMEIBP8yETrvv76SRmQDBdezT4hc8rzInA/viewform?fbzx=-3108080407038215008"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_180.times
index = data_180.index

soal = [
    [
        7
    ],
    [
        6, 5, 6, 5, 6, 6, 
    ]
]

try:
    while times:
        time.sleep(2)
        kelamin = list_baru.kelamin[index]
        umur = data.hitungUsia(17, 32)
        pendidikan = data_180.pendidikan(umur)
        pekerjaan = data_180.pekerjaan(kelamin, umur, pendidikan)
        pengeluaran = data_180.pengeluaran(pekerjaan)

        tipeDom = data.pilihTipe(data_180.kategori[0])
        domisili = data_180.domisili(tipeDom)
        data_180.kategori[0][tipeDom] -= 1

        time.sleep(2)
        isian = data.tombol(0, driver)

        isian[0].send_keys(list_baru.email[index])

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        p = 0
        for i in range(soal[0][0]) :
            bawah[p].click()
            p += 2

        bawah[2].click()
        
        data.pindahHalaman(driver)

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        time.sleep(1)
        bawah[kelamin].click()
        bawah[pendidikan].click()
        bawah[pekerjaan].click()
        bawah[pengeluaran].click()

        time.sleep(2)
        isian[1].send_keys(list_baru.nama[index])
        isian[2].send_keys(umur)
        isian[3].send_keys(domisili)

        for i in range(len(soal[1])) :
            data.pindahHalaman(driver)

            time.sleep(3)
            samping = data.tombol(3, driver)

            data.polaJawab2(0, 3, soal[1][i], 5, samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)
        # driver.get(link)

        index+=1
        print("==================")
        print("kategori = " + str(data_180.kategori))
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