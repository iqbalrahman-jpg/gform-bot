from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_195
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSf6XpO_sDtQcW7ENmYdKKgdpxClTJ6aU0QCaNoulUVx9gxotg/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_195.times
index = data_195.index

soal = data_195.soal

try:
    while times:
        time.sleep(2)
        umur = data.hitungUsia(23, 42)
        sering = random.choice([0,0,0,1,1,1,1,2])

        tipeJawab = data.pilihTipe(data_195.kategori[0])
        data_195.kategori[0][tipeJawab] -= 1

        indexIsian = data_195.kategori[1][tipeJawab]
        data_195.kategori[1][tipeJawab] += 1

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.nama[index])
        isian[1].send_keys(umur)

        time.sleep(1)
        bawah[sering].click()

        data.pindahHalaman(driver)

        for i in range(len(soal)) :
            time.sleep(3)
            samping = data.tombol(3, driver)

            data.polaJawab2(0, tipeJawab, soal[i], 4, samping)

            data.pindahHalaman(driver)
        
        time.sleep(3)
        essay = data.tombol(1, driver)

        essay[0].send_keys(data_195.jawabIsian[0][tipeJawab][indexIsian])
        essay[1].send_keys(data_195.jawabIsian[1][tipeJawab][indexIsian])

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_195.kategori[0]))
        print("idxIsian = " + str(data_195.kategori[1]))
        
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