from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_191
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSf_S9cvL8ZxnTynReK0OyIhysvI0czLKQU6a-mjj-JQ-Rj3YQ/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_191.times
index = data_191.index

soal = data_191.soal

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(0,5)
        tipeJawab = data.pilihTipe(data_191.kategori[0])
        data_191.kategori[0][tipeJawab] -= 1

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.nama[index])

        time.sleep(1)
        bawah[usia].click()
        
        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(3)
            samping = data.tombol(3, driver)

            data.polaJawab3(2, tipeJawab, soal[i], 5, samping) if tipeJawab == 2 else data.polaJawab3(4, tipeJawab, soal[i], 5, samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_191.kategori[0]))
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