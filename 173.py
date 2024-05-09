from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_173
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSekA0OMsfEiomjVT9qjhtkyk6FGX4ZtsFNWbD-uAcZelvQ8GQ/formResponse"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_173.times
index = data_173.index

soal = [3, 3, 3, 3, 3, 3 ]

try:
    while times:
        time.sleep(2)
        tipeJawab = data.pilihTipe(data_173.kategori)

        data_173.kategori[tipeJawab] -= 1

        siapa = data.hitungUsia(2,4)
        sampai = data.hitungUsia(7,9)

        surat = data.pilihanCheckbox(0, 5, 1) if sampai == 7 else data.pilihanCheckbox(0, 5, random.randint(2,5))
        hal = data.pilihanCheckbox(7, 10, random.randint(1,4))

        isian = data.tombol(0, driver)
        buble = data.tombol(7, driver)

        time.sleep(2)
        isian[0].send_keys(list.email[index])
        isian[1].send_keys(list.nama[index])

        time.sleep(1)
        buble[tipeJawab].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        bawah = data.tombol(2, driver)
        checkbox = data.tombol(4, driver)
        samping = data.tombol(3, driver)

        time.sleep(1)
        bawah[0].click()
        bawah[siapa].click()
        bawah[sampai].click()
        bawah[10].click()
        bawah[12].click()

        time.sleep(1)
        for i in surat : 
            checkbox[i].click()
        
        for j in hal :
            checkbox[j].click()
        
        data.polaJawab3(1, 2, 1, 5, samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("kategori = " + str(data_173.kategori))
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