from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_196_1
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSfeCxqEteZtpfxu_jdUhVwtsfiXx6iaBs5XVfo-TOdDKud4ZA/formResponse"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_196_1.times
index = data_196_1.index

soal = data_196_1.soal

try:
    while times:
        time.sleep(2)
        tipeJawab = data.pilihTipe(data_196_1.kategori)
        data_196_1.kategori[tipeJawab] -= 1

        kelamin = 4 if list_baru.kelaminTaufiq[index] == 1 else 5

        umur = data.hitungUsia(6,8)
        pekerjaan = data_196_1.pekerjaan(umur)
        penghasilan = data_196_1.penghasilan(pekerjaan)
        
        kali = data.hitungUsia(13,15)
        domisili = random.choice([19,19,19,20,20,20,21])

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.emailTaufiq[index])

        time.sleep(1)
        bawah[0].click()
        bawah[2].click()
        bawah[kelamin].click()
        bawah[umur].click()
        bawah[pekerjaan].click()
        bawah[kali].click()
        bawah[penghasilan].click()
        bawah[domisili].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)
        
        bawah[2].click()
        data.polaJawab3(2 if tipeJawab == 2 else 4, tipeJawab, soal[0], 5, bawah)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_196_1.kategori))
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