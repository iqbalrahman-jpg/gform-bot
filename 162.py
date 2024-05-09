from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_162
import list
import random
import time

link = "https://forms.gle/npUEKybLYcrHXM2y9"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_162.times
index = data_162.index
soal = data_162.soal

try:
    while times:
        time.sleep(2)
        semester = data_162.pilihanSemester()
        jabatan = data.hitungUsia(6,7)

        tipe = data_162.pilihTipe()

        data_162.listSemester[semester] -= 1
        data_162.kategori[tipe] -= 1

        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[list.kelamin[index]].click()
        bawah[semester].click()
        bawah[jabatan].click()

        for i in range(len(soal)) :
            data.pindahHalaman(driver)
            
            time.sleep(2)
            samping = data.tombol(3, driver)

            data.polaJawab3(1, tipe, soal[i], 5, samping) if tipe == 0 else data.polaJawab3(3, tipe, soal[i], 5, samping)

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("semester = " +
              str(data_162.listSemester[2]) + "," +
              str(data_162.listSemester[3]) + "," +
              str(data_162.listSemester[4]) + "," +
              str(data_162.listSemester[5])
              )
        print("kategori = " +
              str(data_162.kategori[0]) + "," +
              str(data_162.kategori[1]) + "," +
              str(data_162.kategori[2])
              )
        print("")
        
        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    # driver.quit()
    print("berhasil")

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")
