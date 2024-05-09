from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_186
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdXOWjKReNLDVEk5ynnQmh5_OSBMmmDTb-vEVIFhUvUNrtPmA/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_186.times
index = data_186.index

soal = data_186.soal

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(2,5)
        kelamin = list_baru.kelamin[index]

        tipePendidikan = data.pilihTipe(data_186.kategori[0])
        data_186.kategori[0][tipePendidikan] -= 1

        pendidikan = 8 if tipePendidikan == 0 else random.choice([6,7,7,7,7])

        tipeKerja = data.pilihTipe(data_186.kategori[1])
        data_186.kategori[1][tipeKerja] -= 1

        kerja = 11 if tipeKerja == 0 else random.choice([10,10,12,12,13])

        nikah = random.choice([14,14,15]) if usia <= 3 else random.choice([14,15,15,15,16])

        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[kelamin].click()
        bawah[pendidikan].click()
        bawah[usia].click()
        bawah[kerja].click()
        bawah[nikah].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(2)
            bawah = data.tombol(2, driver)
            
            p = -1
            for j in range(soal[i]) :
                s1 = data_186.listJawab[i][index][j] + p
                bawah[s1].click()

                p += 5

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_186.kategori[0]))
        print("         = " + str(data_186.kategori[1]))
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