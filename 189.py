from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_189
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSet_8ZpTl0QFKIt2XwFVkJuaDNjs0IvSMlVNh9PGj-eaFSeMg/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_189.times
index = data_189.index

soal = data_189.soal

try:
    while times:
        time.sleep(2)
        kelamin = list_baru.kelamin[index]
        usia = data.hitungUsia(4,5)
        pendidikan = data.hitungUsia(8,9)
        pekerjaan = data.hitungUsia(13,15)
        
        darimana = data.hitungUsia(0,3)
        banyak = data.hitungUsia(5,8)

        tipeJawab = data.pilihTipe(data_189.kategori[0])
        data_189.kategori[0][tipeJawab] -= 1

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.email[index])
        isian[1].send_keys(list_baru.nama[index])

        time.sleep(1)
        bawah[0].click()
        bawah[2].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        bawah[kelamin].click()
        bawah[usia].click()
        bawah[pendidikan].click()
        bawah[pekerjaan].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        bawah[darimana].click()
        bawah[banyak].click()
        bawah[10].click()

        data.pindahHalaman(driver)

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(3)
            samping = data.tombol(3, driver)

            data.polaJawab2(0, tipeJawab, soal[i], 5, samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_189.kategori[0]))
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