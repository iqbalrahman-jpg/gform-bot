from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_170
import list
import random
import time

link = "https://forms.gle/LwSdUwTYw1KncLVM6"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_170.times
index = data_170.index
idxIsi = data_170.idxIsian

try:
    while times:
        time.sleep(2)
        posisi = data.hitungUsia(0,1)
        jumlah = data.hitungUsia(16,18)
        pernah = data.hitungUsia(20,21)
        ingin1 = data.hitungUsia(28,30)
        ingin2 = data.hitungUsia(35,37)
        ingin3 = data.hitungUsia(38,40)

        tipeSistem = data.pilihTipe(data_170.kategori[1])
        sistem = 4 if tipeSistem == 0 else data.hitungUsia(5,7)

        data_170.kategori[1][tipeSistem] -= 1

        pilihan = data.pilihanCheckbox(0, 2, 3)
        pilihan2 = data.pilihanCheckbox(3, 8, 4)

        tipe_isian = data.pilihTipe(data_170.kategori[0])
        isianJawab = "" if tipe_isian == 0 else data_170.isian[idxIsi]

        data_170.kategori[0][tipe_isian] -= 1
        data_170.idxIsian += tipe_isian

        time.sleep(2)
        kebawah = data.tombol(2, driver)
        checkbox = data.tombol(4, driver)
        essay = data.tombol(1, driver)

        kebawah[posisi].click()
        kebawah[2].click()
        kebawah[sistem].click()
        kebawah[8].click()
        kebawah[13].click()
        kebawah[jumlah].click()
        kebawah[pernah].click()
        kebawah[25].click()
        kebawah[ingin1].click()
        kebawah[33].click()
        kebawah[ingin2].click()
        kebawah[ingin3].click()

        time.sleep(1)
        for i in pilihan : 
            checkbox[i].click()
        
        for j in pilihan2 : 
            checkbox[j].click()
        
        time.sleep(2)
        essay[0].send_keys(isianJawab)

        time.sleep(2)
        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("idxIsian = " + str(data_170.idxIsian))
        print("kategori = " + str(data_170.kategori[0]))
        print("sistem = " + str(data_170.kategori[1]))
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