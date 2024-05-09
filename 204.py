from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_204
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSfN-ovrGXkGj5qYXo5AsLwtrCS_RkFWKqenT-ix5F9VobsFsQ/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_204.times
index = data_204.index

soal = data_204.soal

try:
    while times:
        time.sleep(2)
        pekerjaan = data_204.pekerjaan()
        pendidikan = data_204.pendidikan()

        pola = data.pilihTipe(data_204.jawaban)
        data_204.jawaban[pola] -= 1

        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        bawah = data.tombol(2, driver)
        isian = data.tombol(0, driver)
        dropdown = data.tombol(6, driver)

        bawah[list_baru.kelamin[index]].click()

        time.sleep(1)
        dropdown[0].click()
        data.pilihDropdown(pendidikan, driver)

        time.sleep(1)
        dropdown[1].click()
        data.pilihDropdown(pekerjaan, driver)

        time.sleep(1)
        isian[0].send_keys("zxc")

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(2)
            samping = data.tombol(3, driver)

            data.polaJawab3((3 if pola == 0 else 2), pola, soal[i], 5, samping)

        # data.kirim(driver)
        # driver.implicitly_wait(4)
        # driver.get(link)

        index+=1
        print("==================")
        print("jawaban = " + str(data_204.jawaban))
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