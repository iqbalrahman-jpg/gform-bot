from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
from data.data import dataGoogleForm
from data.enumList import dataPilihan as pil
import data_209_2 as imp
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSeTJo8x87oT8XSg-sZRAAo4uXbNEOBgYwWFMeoN5QK6rN5DHQ/viewform"
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

data = dataGoogleForm(driver)

times = imp.times
index = imp.index

soal = imp.soal

nama = imp.nama
nim = imp.nim
kelamin = imp.kelamin

try:
    while times:
        time.sleep(2)
        nimJ = nim[index]
        email = str(nimJ) + "@student.uksw.edu"
        angkatan = str(nimJ)[2:6]

        tipe = data.pilihTipe(imp.kategori)
        imp.kategori[tipe] -= 1

        time.sleep(3)
        isian = data.tombol(pilihan=pil.ISIANPENDEK)
        bawah = data.tombol(pilihan=pil.KEBAWAH)

        isian[0].send_keys(email)
        isian[1].send_keys(nama[index])
        isian[2].send_keys(nim[index])
        isian[3].send_keys(angkatan)

        time.sleep(1)
        bawah[kelamin[index]].click()

        data.pindahHalaman()

        for i in range(len(soal)) :
            time.sleep(3)
            samping = data.tombol(pil.KESAMPING)

            data.polaJawab3((6 if tipe == 0 else 3), tipe, soal[i], 5, samping)

            data.pindahHalaman()

        data.kirim()
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("kategori = " + str(imp.kategori))
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
