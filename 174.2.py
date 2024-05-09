from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_174
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdXcrzAsikHWFV55PeoNf1PMNgFwe12rnXJV7pwjGnUeRctWw/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_174.times
index = data_174.index

soal = [3, 3, 3, 3, 3, 3 ]

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(0,3)

        tipeDomisili = data.pilihTipe(data_174.domisili)
        domisili = 4 if tipeDomisili == 0 else data.hitungUsia(5,10)

        data_174.domisili[tipeDomisili] -= 1

        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list.nama[index])

        time.sleep(2)

        bawah[usia].click()
        bawah[domisili].click()

        data_174.jawaban(bawah)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)
        # driver.get(link)

        index+=1
        print("==================")
        print("domisili = " + str(data_174.domisili))
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