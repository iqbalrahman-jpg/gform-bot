from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_166
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLScKIVTTlPV02rGemx-Omf2jayW-UtpoiBRJfsDhEQoBNMJhRA/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_166.times
index = data_166.index

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(0,2)
        kelamin = data_166.kelamin[index] + 3
        domisili = data.hitungUsia(5,10)

        pekerjaan = data_166.pekerjaan(usia, kelamin)
        pendidikan = data_166.pendidikan(pekerjaan, usia)

        pernah = data_166.pernah()
        rata = data.hitungUsia(29,31)
        terakhir = data_166.terakhir(rata)

        lainnya = data_166.lainnya(pernah)
        
        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        isian = data.tombol(0, driver)
        kebawah = data.tombol(2, driver)
        checkbox = data.tombol(4, driver)

        isian[0].send_keys(data_166.nama[index])

        time.sleep(1)
        kebawah[usia].click()
        kebawah[kelamin].click()
        kebawah[domisili].click()
        kebawah[pekerjaan].click()
        kebawah[pendidikan].click()
        kebawah[pernah].click()
        kebawah[rata].click()
        kebawah[terakhir].click()

        time.sleep(1)
        for i in lainnya : 
            checkbox[i].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        checkbox = data.tombol(4, driver)
        kebawah = data.tombol(2, driver)

        alasan1 = data.pilihanCheckbox(0, 2, 3)
        alasan2 = data.pilihanCheckbox(4, 7, 4)

        time.sleep(1)
        for i in alasan1 : 
            checkbox[i].click()
        
        time.sleep(2)
        for j in alasan2 : 
            checkbox[j].click()
        
        kebawah[1].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        kesamping = data.tombol(3, driver)

        data.polaJawab3(1, 2, 30, 5, kesamping)

        data.pindahHalaman(driver)

        time.sleep(3)
        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

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
