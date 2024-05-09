from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_181
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSccjRnxfheE5w47JAoZvGDocMSBvWWBOspB_iprBtZl7xRH2A/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_181.times
index = data_181.index

soal = [5, 3, 3, 4, 4, 2, 4, 2]

jawab = data_181.jawab

try:
    while times:
        time.sleep(2)
        follow = data.hitungUsia(0,1)
        lama = data.hitungUsia(4,6)
        sosmed = data.pilihanCheckbox(0, 4, 3)
        produk = data.pilihanCheckbox(5, 8, 2)

        domisili = data_181.domisili()
        kelamin = list_baru.kelamin[index]
        usia = data.hitungUsia(2,5)
        pendidikan = data_181.pendidikan(usia)
        pekerjaan = data_181.pekerjaan(kelamin, pendidikan, usia)
        pengeluaran = data_181.pengeluaran(pekerjaan)

        time.sleep(2)
        isian = data.tombol(0, driver)

        isian[0].send_keys(list_baru.email[index])

        data.pindahHalaman(driver)

        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        bawah = data.tombol(2, driver)
        check = data.tombol(4, driver)

        bawah[follow].click()
        bawah[2].click()
        bawah[lama].click()

        time.sleep(2)
        for i in sosmed :
            check[i].click()
        
        for i in produk :
            check[i].click()
        
        data.pindahHalaman(driver)

        idxJawab = 0
        for i in range(len(soal)) :
            time.sleep(3)
            samping = data.tombol(3, driver)

            #kuesioner
            p = -1
            for j in range(soal[i]) :
                s1 = jawab[index][idxJawab] + p
                samping[s1].click()

                idxJawab += 1
                p += 6

            data.pindahHalaman(driver)

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[1].send_keys(domisili)

        time.sleep(1)
        bawah[kelamin].click()
        bawah[usia].click()
        bawah[pendidikan].click()
        bawah[pengeluaran].click()
        bawah[pekerjaan].click()

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)
        # driver.get(link)

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