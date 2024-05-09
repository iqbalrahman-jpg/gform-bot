from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_156
import list
import random
import time

link = "https://forms.gle/oErQagjzmNrj2LV78"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_156.times
index = data_156.index

try:
    while times:
        time.sleep(5)

        data.pindahHalaman(driver)

        radiobuttons = data.tombol("kebawah", driver)

        radiobuttons[0].click()
        radiobuttons[2].click()
        radiobuttons[4].click()
        radiobuttons[random.choice([6,7,7,8,9])].click()
        radiobuttons[random.choice([11,11,12])].click()
        radiobuttons[2].click()

        data.pindahHalaman(driver)

        time.sleep(3)
        radiobuttons = data.tombol("kebawah", driver)
        textboxes = data.tombol("isian", driver)

        usia = data_156.countUsia()
        pekerjaan = data_156.countPekerjaan(usia)
        pendapatan = data_156.countPendapatan(pekerjaan)

        textboxes[0].send_keys(list.nama[index])

        radiobuttons[usia].click()
        radiobuttons[list.kelamin[index]].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[pendapatan].click()

        data.pindahHalaman(driver)
        time.sleep(2)

        pil = data_156.pilihJawab()
        if pil == 0 :
            data_156.negatif -= 1
        else:
            data_156.positif -= 1

        for i in range(len(data_156.soal)) :
            data.pindahHalaman(driver)            
            time.sleep(2)
            testcheck = data.tombol("kesamping", driver)
            data_156.jawab1(pil, data_156.soal[i], testcheck)

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("positif = " + str(data_156.positif))
        print("negatif = " + str(data_156.negatif))
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

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()


        

