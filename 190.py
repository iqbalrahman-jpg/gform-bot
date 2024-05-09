from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_190
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdP2heuxRxY354vrguWhnIs9VzOCddE4DrDC1dgvv65wZHb7g/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_190.times
index = data_190.index

soal = data_190.soal

try:
    while times:
        time.sleep(2)
        kelamin = 1 if list_baru.kelamin[index] == 0 else 0
        umur = data.hitungUsia(2,4)
        pekerjaan = data_190.pekerjaan(umur)
        kali = data.hitungUsia(10,12)
        penghasilan = data_190.penghasilan(pekerjaan)
        domisili = data.hitungUsia(17,19)

        tipeJawab = data.pilihTipe(data_190.kategori[0])
        data_190.kategori[0][tipeJawab] -= 1

        time.sleep(3)
        bawah = data.tombol(2, driver)

        bawah[0].click()
        bawah[2].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        bawah[kelamin].click()
        bawah[umur].click()
        bawah[pekerjaan].click()
        bawah[kali].click()
        bawah[penghasilan].click()
        bawah[domisili].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(3)
            bawah = data.tombol(2, driver)

            bawah[1].click() if tipeJawab == 0 else bawah[3].click()
            data.polaJawab3(2, tipeJawab, soal[i], 5, bawah) if tipeJawab == 2 else data.polaJawab3(4, tipeJawab, soal[i], 5, bawah)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_190.kategori[0]))
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