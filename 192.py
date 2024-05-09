from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_192
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/1tMkH-vHCYIWX5ukd3Z1f97rM6WAOsYOErhuSrbSwoj8/viewform?edit_requested=true"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_192.times
index = data_192.index

soal = data_192.soal

try:
    while times:
        time.sleep(2)
        instansi = data_192.pilihanInstansi()

        time.sleep(3)
        isian = data.tombol(0, driver)

        isian[0].send_keys(list_baru.email[index])
        isian[1].send_keys(list_baru.nama[index])
        isian[2].send_keys(instansi)

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)

        p = 0

        for i in range(len(soal)-1) :
            bawah[p].click() if soal[i] == 2 else bawah[data.hitungUsia(p,p+1)].click()
            p += soal[i]

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