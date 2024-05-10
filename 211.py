from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from data.data import dataGoogleForm
from data.enumList import dataPilihan as pil
import data_211 as dat
import list_baru
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSeYafb5k6cAluHJdZ8c1e-kOPqVtkUMfaBlr0e0X7hfpreqFA/viewform"

driver = webdriver.Firefox()
# driver.set_window_position(0, 0)
# driver.set_window_size(1024, 768)
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

data = dataGoogleForm(driver=driver)

times = dat.times
index = dat.index

soal = dat.soal

try:
    while times:
        time.sleep(2)
        pekerjaan = data.pilihTipe(dat.pekerjaan)
        dat.pekerjaan[pekerjaan] -= 1
        pekerjaan += 2

        waktu = dat.waktu(pekerjaan)

        # time.sleep(dat.jeda[index])
        if times != dat.times :
            time.sleep(random.randint(10,200))

        data.pindahHalaman()

        time.sleep(2)
        isian = data.tombol(pil.ISIANPENDEK)
        bawah = data.tombol(pil.KEBAWAH)

        isian[0].send_keys(dat.email[index])

        time.sleep(1)
        bawah[dat.kelamin[index]].click()
        bawah[pekerjaan].click()
        bawah[waktu].click()

        time.sleep(1)
        for i in range(len(soal)) :
            data.pindahHalaman()

            time.sleep(2)
            samping = data.tombol(pil.KESAMPING)

            p = -1
            for j in range(soal[i]) :
                s1 = dat.jawaban[i][index][j] + p
                samping[s1].click()
                p += 5

        data.kirim()
        time.sleep(1)
        data.kirimJawaban()

        index+=1
        print("==================")
        print("pekerjaan = " + str(dat.pekerjaan))
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
