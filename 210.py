from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from data.data import dataGoogleForm
from data.enumList import dataPilihan as pil
import data_210 as datas
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
        kelaminJawab = data.hitungUsia(0,1)

        usiaJawab = data.pilihTipe(datas.usia)
        datas.usia[usiaJawab] -= 1
        usiaJawab += 2

        ident0 = data.pilihTipe(datas.kat1[0])
        ident1 = data.pilihTipe(datas.kat1[1])
        ident2 = data.pilihTipe(datas.kat1[2])

        datas.kat1[0][ident0] -= 1
        datas.kat1[1][ident1] -= 1
        datas.kat1[2][ident2] -= 1

        ident0 += 7
        ident1 += 9
        ident2 += 11

        bookJawab = 0
        check1 = []
        check2 = []
        checkno = []

        time.sleep(1)
        if ident2 == 11 :
            book = data.pilihTipe(datas.kat2)
            datas.kat2[book] -= 1
            bookJawab = 0 if book == 0 else data.hitungUsia(1,3)

            check1 = datas.hitungCheck1()
            check2 = datas.hitungCheck2()
        else :
            checkno = datas.hitungCheckNo()

        time.sleep(2)
        bawah = data.tombol(pil.KEBAWAH)

        bawah[kelaminJawab].click()
        bawah[usiaJawab].click()
        bawah[ident0].click()
        bawah[ident1].click()
        bawah[ident2].click()

        data.pindahHalaman()

        if ident2 == 11 :
            time.sleep(3)
            bawah = data.tombol(pil.KEBAWAH)
            checkbox = data.tombol(pil.CHECKBOX)
            samping = data.tombol(pil.KESAMPING)

            bawah[bookJawab].click()

            time.sleep(1)
            if len(check1) != 0 :
                for i in check1 :
                    checkbox[i].click()
            else :
                checkbox[4].click()

            if len(check2) != 0 :
                for j in check2 :
                    checkbox[j].click()
            else :
                checkbox[6].click()

            time.sleep(1)
            samping[random.choice([2,2,2,2,2,2,2,3,4])].click()

        else :
            time.sleep(3)
            checkbox = data.tombol(pil.CHECKBOX)

            if len(check2) != 0 :
                for i in checkno :
                    checkbox[i].click()
            else :
                checkbox[1].click()

        data.kirim()
        driver.implicitly_wait(4)
        data.kirimJawaban()
        # driver.get(link)

        index+=1
        print("==================")
        print("usia = " + str(datas.usia))
        print("kat1 = " + str(datas.kat1))
        print("kat2 = " + str(datas.kat2))
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
