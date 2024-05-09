from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_158
import list
import random
import time

link = "https://forms.gle/hpc6Lbbqgd3v9gPN9"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_158.times
index = data_158.index

try:
    while times:
        time.sleep(2)
        usia = data_158.countUsia()
        pekerjaan = data_158.countPekerjaan(usia)

        time.sleep(2)
        textboxes = data.tombol("isian", driver)

        textboxes[0].send_keys(list.nama[index])
        textboxes[1].send_keys(usia)
        textboxes[2].send_keys(pekerjaan)

        data.pindahHalaman(driver)

        time.sleep(2)
        testcheck = data.tombol("kesamping", driver)

        data_158.jawab(testcheck)

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

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

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()


        

