from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_188
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSftalDGaNjR6XpaxWUETJyDZbJk8UW2kaUhRGhHk2dPNopKrQ/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_188.times
index = data_188.index

soal = data_188.soal

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(0,7)
        kelamin = list.kelamin[index] + 8
        domisili = data.hitungUsia(10,14)
        pendidikan = data_188.pendidikan(usia)
        pekerjaan = data_188.pekerjaan(usia)

        tipeEtnis = data.pilihTipe(data_188.kategori[0])
        data_188.kategori[0][tipeEtnis] -= 1

        etnis = random.randint(23,31) if tipeEtnis == 2 else tipeEtnis + 21
        agama = data_188.agama(etnis)

        jawa = data.hitungUsia(48,51)
        tionghoa = data.hitungUsia(52,55)

        time.sleep(2)
        bawah = data.tombol(2, driver)
        bawah[0].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)
        samping = data.tombol(3, driver)

        time.sleep(1)
        isian[0].send_keys(list.inisial[index])

        time.sleep(1)
        bawah[usia].click()
        bawah[kelamin].click()
        bawah[domisili].click()
        bawah[pendidikan].click()
        bawah[etnis].click()
        bawah[agama].click()
        bawah[pekerjaan].click()
        bawah[jawa].click()
        bawah[tionghoa].click()

        time.sleep(2)
        s1 = data.hitungUsia(0,4)
        samping[s1].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        samping = data.tombol(3, driver)

        data.polaJawab3(2, 2, 5, 5, samping) if tipeEtnis != 1 else data.polaJawab3(5, 0, 5, 5, samping)
        samping[13].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        samping = data.tombol(3, driver)

        s1 = random.choice([0,0,0,1,1,1,2]) if tipeEtnis != 1 else random.choice([2,3,3,3,4,4,4])
        s2 = random.choice([7,8,8,8,9,9,9]) if tipeEtnis != 1 else random.choice([5,5,5,6,6,6,7])

        samping[s1].click()
        samping[s2].click()

        data.pindahHalaman(driver)

        data.kirim(driver)
        driver.implicitly_wait(4)
        data.kirimJawaban(driver)

        index+=1
        print("==================")
        print("kategori = " + str(data_188.kategori[0]))
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