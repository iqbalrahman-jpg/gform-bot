from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_167_1
import list
import random
import time

link = "https://forms.gle/wVAfYsMpJpTkoUdi6"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_167_1.times
index = data_167_1.index

try:
    while times:
        time.sleep(2)
        kelamin = list.kelamin[index]

        tipePekerjaan = data.pilihTipe(data_167_1.kategori[0])
        pekerjaan = 6 + tipePekerjaan

        data_167_1.kategori[0][tipePekerjaan] -= 1

        usia = random.randint(4,5) if tipePekerjaan == 2 or tipePekerjaan == 3 else tipePekerjaan + 2
        pendidikan = random.randint(10,11) if tipePekerjaan == 2 or tipePekerjaan == 3 else tipePekerjaan + 10

        tipeDomisili = data.pilihTipe(data_167_1.kategori[1])
        domisili = 14 if tipeDomisili == 0 else data.hitungUsia(15,18)

        data_167_1.kategori[1][tipeDomisili] -= 1
        
        tipeKali = data.pilihTipe(data_167_1.kategori[2])
        kali = 24 if tipeKali == 0 else random.choice([23,25,26])

        pendapatan = tipePekerjaan + 19

        data_167_1.kategori[2][tipeKali] -= 1

        time.sleep(2)
        isian = data.tombol(0, driver)

        isian[0].send_keys(list.email[index])

        data.pindahHalaman(driver)

        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[kelamin].click()
        bawah[usia].click()
        bawah[pekerjaan].click()
        bawah[pendidikan].click()
        bawah[domisili].click()
        bawah[pendapatan].click()
        bawah[kali].click()

        data.pindahHalaman(driver)

        tipeJawab = data.pilihTipe(data_167_1.kategori[3])
        data_167_1.kategori[3][tipeJawab] -= 1

        time.sleep(2)
        samping = data.tombol(3, driver)

        data.polaJawab1(0, tipeJawab, 15, 5, samping)

        data.pindahHalaman(driver)

        time.sleep(2)
        samping = data.tombol(3, driver)

        data.polaJawab1(0, tipeJawab, 12, 5, samping)
        
        time.sleep(3)
        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("usia     = " + 
              str(data_167_1.kategori[0]))
        print("domisili = " + 
              str(data_167_1.kategori[1]))
        print("kali     = " + 
              str(data_167_1.kategori[2]))
        print("jawaban  = " + 
              str(data_167_1.kategori[3]))
        print("")

        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    # driver.quit()
    print("berhasil")

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")
