from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_164
import list
import random
import time

link = "https://forms.gle/t9PpjMCh6RsusbQL6"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_164.times
index = data_164.index

try:
    while times:
        time.sleep(2)
        kelamin = 0 if data_164.kelamin[index] == 1 else 1
        usia = data.hitungUsia(18, 25)

        isian = data.tombol(0, driver)
        kebawah = data.tombol(2, driver)
        chechbox = data.tombol(4, driver)

        isian[0].send_keys(data_164.nama[index])
        isian[1].send_keys(usia)

        time.sleep(2)
        kebawah[kelamin].click()
        kebawah[2].click()

        data_164.jawab1(chechbox)

        data.pindahHalaman(driver)

        time.sleep(2)
        kebawah = data.tombol(2, driver)

        data.polaJawab2(0, 0, 30, 4, kebawah)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)
        # driver.get(link)

        index+=1
        print("==================")
        # print("")
        
        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    # driver.quit()
    print("berhasil")

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")
