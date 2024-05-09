from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_184
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSeahMmj85Ul3srMcVs6FWsJ3mYWkDP3smiIMy1F8hc7n3qgcg/viewform?usp=sf_link"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_184.times
index = data_184.index

soal = data_184.soal

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(2,5)

        tipeJawab = data.pilihTipe(data_184.kategori[0])
        data_184.kategori[0][tipeJawab] -= 1

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.email[index])
        isian[1].send_keys(list_baru.nama[index])

        time.sleep(1)
        bawah[list_baru.kelamin[index]].click()
        bawah[usia].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(2)
            samping = data.tombol(3, driver)

            data.polaJawab2(0, tipeJawab, soal[i], 5, samping)

        time.sleep(1)
        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_184.kategori[0]))
        print("")
        
        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    # driver.quit()
    print("berhasil")