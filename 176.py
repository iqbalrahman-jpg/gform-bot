from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_176
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSe79JXhtO6vn_2BtpeJ3vJqbWL7efRUppMONhkuI-keVx7w-g/formResponse"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_176.times
index = data_176.index

soal = [4,3,3,4,4,4]

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(2,3)
        pekerjaan = data.hitungUsia(4,5) if usia == 2 else data.hitungUsia(6,8)
        pendidikan = data_176.pendidikan(pekerjaan)
        domisili = data.hitungUsia(17,21)

        data.pindahHalaman(driver)

        for i in range(3) :
            time.sleep(2)
            bawah = data.tombol(2, driver)

            bawah[0].click()

            data.pindahHalaman(driver)
            data.pindahHalaman(driver)

        time.sleep(2)
        bawah = data.tombol(2, driver)
        bawah[1].click()
        data.pindahHalaman(driver)

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(data_176.nama[index])
        isian[1].send_keys(list.telp[index])

        time.sleep(1)
        bawah[1].click()
        bawah[usia].click()
        bawah[pekerjaan].click()
        bawah[pendidikan].click()
        bawah[domisili].click()

        data.pindahHalaman(driver)
        data.pindahHalaman(driver)

        for i in range(len(soal)) :
            time.sleep(3)
            samping = data.tombol(3, driver)

            data.polaJawab4(2, 3, soal[i], 7, samping)
            data.pindahHalaman(driver)
        
        time.sleep(2)
        isian = data.tombol(0, driver)

        for i in range(5) :
            time.sleep(1)
            isian[i].send_keys(data_176.isian[i][index])
        
        data.pindahHalaman(driver)

        time.sleep(3)
        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)
        # driver.get(link)

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