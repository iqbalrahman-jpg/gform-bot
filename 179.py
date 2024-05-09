from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_179
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSfU01J22hwP_MeHyNmKeP-H-IH8Ma50Qg7vIBfdkBCoQTYHGA/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_179.times
index = data_179.index

soal = [3, 3, 3, 3, 3, 3 ]

try:
    while times:
        time.sleep(1)
        umur = data.hitungUsia(19,24)
        kelamin = "Laki-laki" if list.kelamin[index] == 0 else "Perempuan"

        time.sleep(2)
        isian = data.tombol(0, driver)
        dropdown = data.tombol(6, driver)

        isian[0].send_keys(list.nama[index])
        isian[1].send_keys(umur)

        dropdown[0].click()
        data.pilihDropdown(kelamin, driver)

        data.pindahHalaman(driver)

        time.sleep(3)

        samping = data.tombol(3, driver)

        data.polaJawab3(0, 1, 15, 5, samping)

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