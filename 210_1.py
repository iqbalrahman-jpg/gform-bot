from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from data.data import dataGoogleForm
from data.enumList import dataPilihan as pil
import data_210_1 as datas
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSf7EGFvF5qdEa0YZl8wrj8HvVRJpbJxV5iY7ugHDoy6AA5rwQ/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

data = dataGoogleForm(driver=driver)

times = datas.times
index = datas.index

soal = datas.soal

try:
    while times:
        time.sleep(2)
        kelaminJawab = datas.kelamin[index]

        usiaJawab = datas.usia[index]

        ident0 = 8
        ident1 = 10
        ident2 = 12

        time.sleep(2)
        bawah = data.tombol(pil.KEBAWAH)

        bawah[kelaminJawab].click()
        bawah[usiaJawab].click()
        bawah[ident0].click()
        bawah[ident1].click()
        bawah[ident2].click()

        data.pindahHalaman()

        time.sleep(3)
        checkbox = data.tombol(pil.CHECKBOX)

        for i in datas.check[index] :
            checkbox[i].click()

        data.kirim()
        driver.implicitly_wait(4)
        data.kirimJawaban()
        # driver.get(link)

        index+=1
        print("==================")
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
