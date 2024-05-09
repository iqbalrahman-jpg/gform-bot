from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from data.data import dataGoogleForm
from data.enumList import dataPilihan as pil
import data_ganti
import list_baru
import random
import time

link = ""

driver = webdriver.Firefox()
# driver.set_window_position(0, 0)
# driver.set_window_size(1024, 768)
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

data = dataGoogleForm(driver=driver)

times = data_ganti.times
index = data_ganti.index

soal = data_ganti.soal

try:
    while times:
        time.sleep(2)











        data.kirim()
        time.sleep(1)
        data.kirimJawaban()

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
