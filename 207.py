from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from data.data_qualtrics import dataQualtrics
from data.enumList import dataPilihan
import data_207
# import list
import random
import time

link = "https://qualtricsxmkm5x82nbl.qualtrics.com/jfe/form/SV_79YVipIsrLKJrDM"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

data = dataQualtrics(driver)

times = data_207.times
index = data_207.index

soal = data_207.soal

try:
    while times:
        time.sleep(1)
        negara = data.hitungUsia(0,1)
        gender = random.choice([2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,5])
        usia = data.hitungUsia(6,9)

        tipeJawab = data.pilihTipe(data_207.kategori)
        data_207.kategori[tipeJawab] -= 1

        jawab = tipeJawab if tipeJawab == 0 else 3

        dagingJawab = data.pilihTipe(data_207.daging)
        data_207.daging[dagingJawab] -= 1

        time.sleep(3)
        bawah = data.tombol(dataPilihan.KEBAWAH)

        bawah[0].click()

        data.pindahHalaman()

        time.sleep(2)
        bawah = data.tombol(dataPilihan.KEBAWAH)

        bawah[negara].click()
        bawah[gender].click()
        bawah[usia].click()

        data.pindahHalaman()
        data.pindahHalaman()
        data.pindahHalaman()

        time.sleep(2)
        bubble = data.tombol(dataPilihan.BUBBLE)

        data.polaJawab4(2, 3, 10, 7, bubble)

        data.pindahHalaman()

        time.sleep(2)
        bawah = data.tombol(dataPilihan.KEBAWAH)

        bawah[dagingJawab].click()

        data.pindahHalaman()

        time.sleep(2)
        bubble = data.tombol(dataPilihan.BUBBLE)

        data.polaJawab4(2 if jawab == 0 else 4, 0 if jawab == 3 else 3, 1, 7, bubble)
        time.sleep(1)
        data.polaJawab4(4 if jawab == 0 else 2, jawab + 7, 9, 7, bubble)

        data.pindahHalaman()

        time.sleep(2)

        bawah = data.tombol(dataPilihan.KEBAWAH)

        bawah[0].click()

        data.pindahHalaman()

        data.pindahHalaman()
        time.sleep(3)
        driver.get(link)

        index+=1
        print("==================")
        print("kategori = " + str(data_207.kategori))
        print("daging = " + str(data_207.daging))
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
