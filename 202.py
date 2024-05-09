from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_202
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSe3zgwtm42ayFd18ZIQJkKUlXkfI7Fs3qUT46dZqwGvzlW0GA/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_202.times
index = data_202.index

soal = data_202.soal

try:
    while times:
        time.sleep(2)
        kelamin = 0 if list_baru.kelamin[index] == 1 else 1

        univ = data_202.univ()
        desa = data_202.desa()

        usia = data.hitungUsia(2,4)
        penghasilan = data_202.penghasilan(usia)

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.email[index])
        isian[1].send_keys(list_baru.nama[index])
        isian[2].send_keys(univ)
        isian[3].send_keys(desa)

        time.sleep(1)
        bawah[kelamin].click()
        bawah[usia].click()
        bawah[penghasilan].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(3)
            bawah = data.tombol(2, driver)

            data.polaJawab2(0, 0, soal[i], 5, bawah)

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