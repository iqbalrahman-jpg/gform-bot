from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_160
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdOxzVeOsvOp1cB908M9Yw6Wq_Pmz5CbHGbatWrMqOBHvRLfQ/formResponse"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_160.times
index = data_160.index

soal = [3, 3, 3, 3, 3, 3 ]

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(17,22)
        semester = data_160.hitungSemester(usia)
        tipe = data_160.pilihKategori()
        data_160.kategori[tipe] -= 1
        
        data.pindahHalaman(driver)

        time.sleep(2)
        radiobuttons = data.tombol("kebawah", driver)
        textboxes = data.tombol("isian", driver)
        dropdown = data.tombol("dropdown", driver)

        textboxes[0].send_keys(list.nama[index])
        textboxes[1].send_keys(list.email[index])

        time.sleep(2)
        radiobuttons[list.kelamin[index]].click()
        radiobuttons[2].click()
        radiobuttons[4].click()
        radiobuttons[6].click()

        time.sleep(2)
        dropdown[0].click()
        data.pilihDropdown(str(usia), driver)

        time.sleep(2)
        dropdown[1].click()
        data.pilihDropdown("Universitas Mulawarman", driver)

        time.sleep(2)
        dropdown[2].click()
        print(semester)
        data.pilihDropdown(str(semester), driver)

        data.pindahHalaman(driver)

        time.sleep(2)
        testcheck = data.tombol("kesamping", driver)
        data_160.jawab1(testcheck, tipe)
        data.pindahHalaman(driver)

        time.sleep(2)
        testcheck = data.tombol("kesamping", driver)
        data_160.jawab2(testcheck, tipe, 1)
        data.pindahHalaman(driver)

        time.sleep(2)
        testcheck = data.tombol("kesamping", driver)
        data_160.jawab2(testcheck, tipe, 2)
        data.pindahHalaman(driver)

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("Kategori = " + str(data_160.kategori[0]) + "," + str(data_160.kategori[1]) + "," + str(data_160.kategori[2]))
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
