from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_165
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSe3UrrFg1Mg0WB_88S5yG2LtfzpTOh5eDBYx1GySLnGOqgt_w/formResponse"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_165.times
index = data_165.index

try:
    while times:
        time.sleep(2)
        kelamin = 0 if list.kelamin[index] == 1 else 1
        usia = data.hitungUsia(2,5)
        domisili = random.choice([6,6,6,6,6,7])
        pekerjaan = data_165.pilihPekerjaan(usia, kelamin)
        sering = data_165.hitungSering()

        bawah = data.tombol(2, driver)

        bawah[2].click()
        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(list.nama[index])

        time.sleep(1)
        bawah[usia].click()
        bawah[kelamin].click()
        bawah[domisili].click()
        bawah[pekerjaan].click()
        bawah[sering].click()
        bawah[usia].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        samping = data.tombol(3, driver)

        data.polaJawab3(2, 2, 20, 5, samping)
        data.polaJawab3(5, (20*5) + 2, 7, 5, samping)
        data.polaJawab3(2, (27*5) + 2, 7, 5, samping)
        
        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

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
