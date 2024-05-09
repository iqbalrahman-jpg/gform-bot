from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_166_1
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLScI6w6Op-Lpr9xVK7bYeBDi_NkWIMzLe6ucjxL_tig1R1VCWw/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_166_1.times
index = data_166_1.index

try:
    while times:
        time.sleep(2)
        kelamin = data_166_1.kelamin[index] + 3
        domisili = data.hitungUsia(5,9)

        tipeUsia = data.pilihTipe(data_166_1.kategori[0])
        usia = 0 if tipeUsia == 0 else 1
        data_166_1.kategori[0][tipeUsia] -= 1

        pekerjaan = 12 if usia == 0 else data_166_1.pekerjaan(usia, kelamin)
        tipePekerjaan = 0 if pekerjaan == 12 else 1
        data_166_1.kategori[1][tipePekerjaan] -= 1

        pendidikan = 22 if pekerjaan == 12 else data_166_1.pendidikan(pekerjaan, usia, data_166_1.kategori[2][1])
        tipePendidikan = 0 if pendidikan == 22 else 1
        data_166_1.kategori[2][tipePendidikan] -= 1

        pernah = 26
        tipeRata = data.pilihTipe(data_166_1.kategori[3])
        rata = 29 if tipeRata == 0 else data.hitungUsia(30,31)
        data_166_1.kategori[3][tipeRata] -= 1

        terakhir = data_166_1.terakhir(rata)
        lainnya = data_166_1.lainnya(pernah)
        
        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        isian = data.tombol(0, driver)
        kebawah = data.tombol(2, driver)
        checkbox = data.tombol(4, driver)

        isian[0].send_keys(data_166_1.nama[index])
        isian[1].send_keys(list.telp[index])

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
        print("usia = " + 
              str(data_166_1.kategori[0]))
        print("usia = " + 
              str(data_166_1.kategori[1]))
        print("usia = " + 
              str(data_166_1.kategori[2]))
        print("usia = " + 
              str(data_166_1.kategori[3]))
        print("")
        
        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    # driver.quit()
    print("berhasil")

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")
