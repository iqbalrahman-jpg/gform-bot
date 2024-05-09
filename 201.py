from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_201
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdRuuqR00Aq5B8N0SIn11s2oYn1xibgz9Z1PelD9bpX5KB3nA/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_201.times
index = data_201.index

soal = data_201.soal

try:
    while times:
        time.sleep(2)
        tipeJawab = data.pilihTipe(data_201.kategori[0])
        data_201.kategori[0][tipeJawab] -= 1

        time.sleep(3)
        bawah = data.tombol(2, driver)
        samping = data.tombol(3, driver)

        data.polaJawab3(4 if tipeJawab == 0 else 2, tipeJawab, 7, 5, samping)

        bawah[2].click()
        if tipeJawab == 0:
            bawah[data.hitungUsia(0,1)].click()
            bawah[data.hitungUsia(5,6)].click()
            bawah[data.hitungUsia(7,8)].click()
            bawah[data.hitungUsia(9,10)].click()
        else :
            bawah[0].click()
            bawah[5].click()
            bawah[7].click()
            bawah[9].click()
        
        data.polaJawab3(4 if tipeJawab == 0 else 2, tipeJawab + 35, 2, 5, samping)
        samping[47].click()

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_201.kategori[0]))
        print("")
        
        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    print("berhasil")