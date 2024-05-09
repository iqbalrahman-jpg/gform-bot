from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_193
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSedleBnLBCOrzQsdyB3HKYb5BJzOoeGc8m04Be3BNBgEt6JRQ/formResponse"

custom_width = 1400
custom_height = 950

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.set_window_size(custom_width, custom_height)
driver.get(link)

times = data_193.times
index = data_193.index

listJawaban = data_193.listJawaban

soal = data_193.soal

try:
    while times:
        time.sleep(2)
        tipeUltah = data_193.ultah()
        ultah = str(tipeUltah[0]) + " " + tipeUltah[1] + " " + str(tipeUltah[2])

        tipeDomisili = data.hitungUsia(0, len(data_193.listKota) - 1)
        domisili = data_193.listKota[tipeDomisili]

        lamaKerja = data_193.lamaKerja(tipeUltah[2])

        kelamin = list_baru.kelaminInisial[index]
        pendidikan = data_193.pendidikan(tipeUltah[2])
        status = random.choice([10,11,11,11,11,11])
        jabatan = data_193.jabatan(tipeUltah[2], status)
        sektor = data.hitungUsia(16,27)

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.namaInisial[index])
        isian[1].send_keys(ultah)
        isian[2].send_keys(domisili)
        isian[3].send_keys(lamaKerja)

        time.sleep(3)
        bawah[kelamin].click()
        bawah[pendidikan].click()
        bawah[status].click()
        bawah[jabatan].click()
        bawah[sektor].click()

        data.pindahHalaman(driver)

        for i in range(len(soal)) :
            time.sleep(3)
            bawah = data.tombol(2, driver)

            time.sleep(1)
            bawah[0].click()
            
            p = -1
            for j in range(soal[i]) :
                s1 = listJawaban[i][index][j] + p
                bawah[s1].click()

                p = p + 4 if i == 2 else p + 5

            data.pindahHalaman(driver)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        # print(" = " + str())
        # print("")
        
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