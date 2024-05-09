from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

import data
import data_203
import list_baru
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLScAcua3ZnWAxEzRpDKg2jUPFUleiS45TBs5-JNE48-UWHMeVQ/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_203.times
index = data_203.index

soal = data_203.soal

try:
    while times:
        time.sleep(2)
        kelamin = 0 if list_baru.kelaminTaufiq[index] == 1 else 1

        univ = data_203.univ()
        desa = data_203.desa()

        usia = data.hitungUsia(0,2)
        penghasilan = data_203.penghasilan(usia)

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        bawah[usia].click()
        isian[0].send_keys(list_baru.namaTaufiq[index])
        isian[1].send_keys(univ)

        time.sleep(1)
        bawah[penghasilan].click()
        bawah[usia].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)

            time.sleep(3)
            bawah = data.tombol(2, driver)

            if i == 1 :
                bawah[7].click()
                bawah[5].click()

            data.polaJawab2(0, 0, soal[i], 5, bawah)

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