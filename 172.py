from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_172
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSeZVHodTC3spJ0pSWwvGnT6SNNlhU66vN5JH4WmiyRKEBa0Qg/viewform?usp=pp_url"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_172.times
index = data_172.index

try:
    while times:
        time.sleep(2)
        usia = data.hitungUsia(21,45)
        domisili = data_172.domisili()
        profesi = data_172.profesi(usia)

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)
        checkbox = data.tombol(4, driver)
        
        time.sleep(2)
        checkbox[list.kelamin[index]].click()

        isian[0].send_keys(list.nama[index])
        isian[1].send_keys(usia)
        isian[2].send_keys(domisili)

        time.sleep(1)
        bawah[profesi].click()
        bawah[5].click()

        for i in range(5) :
            data.pindahHalaman(driver)

            time.sleep(2)
            bawah = data.tombol(2, driver)

            if i == 0 or i == 2 or i == 3 :
                data.polaJawab2(0, 3, 4, 5, bawah)
            else :
                data.polaJawab4(0, 1, 4, 5, bawah)
                

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

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