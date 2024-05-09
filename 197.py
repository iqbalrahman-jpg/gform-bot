from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_197
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSddwZwbKPEZuAGRollAiVzmXFEk10cCNQXkUgAB7wVw9gVv3A/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_197.times
index = data_197.index

soal = data_197.soal

try:
    while times:
        time.sleep(2)
        umur = data.hitungUsia(2, 6)

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list_baru.nama[index])

        time.sleep(1)
        bawah[list_baru.kelamin[index]].click()
        bawah[umur].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(3)
            samping = data.tombol(3, driver)

            data.polaJawab4(2, 1, soal[i], 5, samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

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