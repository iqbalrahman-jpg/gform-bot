from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_185
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdUNA8-PvblojaB1ZRkmOxGsKwInD0nf8uhoZIj09egn5UWqg/formResponse"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_185.times
index = data_185.index

soal = data_185.soal

try:
    while times:
        time.sleep(2)
        tipeKelamin = data.pilihTipe(data_185.kategori[0])
        data_185.kategori[0][tipeKelamin] -= 1
        kelamin = tipeKelamin + 4

        tipeJawab = data.pilihTipe(data_185.kategori[1])
        data_185.kategori[1][tipeJawab] -= 1

        time.sleep(2)
        bawah = data.tombol(2, driver)
        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        bawah[data_185.dataJawab[0][index]].click()
        bawah[kelamin].click()
        bawah[data_185.dataJawab[1][index]].click()
        bawah[data_185.dataJawab[2][index]].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(2)
            samping = data.tombol(3, driver)

            data.polaJawab2(0, tipeJawab, soal[i], 5, samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_185.kategori[0]))
        print("         = " + str(data_185.kategori[1]))
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