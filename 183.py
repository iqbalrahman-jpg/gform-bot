from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_183
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSeDgqX10kpuX7P441-mtI4Kd1Oy06dtesmI-AaXdZVpXEMktQ/formResponse?pli=1"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_183.times
index = data_183.index

soal = data_183.soal

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(0,4)
        bulan = data.hitungUsia(6,7)
        transaksi = data.hitungUsia(9,10)

        tipeJawab = data.pilihTipe(data_183.kategori[0])
        data_183.kategori[0][tipeJawab] -= 1

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        p = 0
        for i in range(3) :
            bawah[p].click()
            p += 2
        
        data.pindahHalaman(driver)

        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[usia].click()
        bawah[bulan].click()
        bawah[transaksi].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(3)
            samping = data.tombol(3, driver)

            data.polaJawab3(1, 2, soal[i], 5, samping) if tipeJawab == 0 else data.polaJawab3(3, 0, soal[i], 5, samping)

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