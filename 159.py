from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_159
import list
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSduiY_7Nd8kvkHVw1qe2fG9MA8TxAA5aShSkwCnq7Opz63VWg/viewform"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_159.times
index = data_159.index

soal = [3, 3, 3, 3, 3, 3 ]

try:
    while times:
        time.sleep(2)
        kategoris = data_159.pilihKategori()
        data_159.kategori[kategoris] -= 1

        data.pindahHalaman(driver)
        
        for i in range(len(soal)) :
            time.sleep(3)
            testcheck = data.tombol("kesamping", driver)

            if i == 4 :
                tipe = 0 if kategoris == 2 else 2
                data_159.jawab1(testcheck, soal[i], tipe)
            else :
                data_159.jawab1(testcheck, soal[i], kategoris)
            
            data.pindahHalaman(driver)
        
        time.sleep(3)
        radiobuttons = data.tombol("kebawah", driver)
        textboxes = data.tombol("isian", driver)
        textarea = data.tombol("textarea", driver)

        textboxes[0].send_keys(list.nama[index])
        textboxes[1].send_keys(data_159.hitungPegawai())
        textboxes[2].send_keys(data_159.jenisQris())
        textboxes[3].send_keys(data_159.lamaPakai())
        textboxes[4].send_keys(data_159.jumlahTransaksi())

        time.sleep(2)
        radiobuttons[data_159.hitungRandint(0,21)].click()
        radiobuttons[data_159.hitungRandint(22,29)].click()
        radiobuttons[data_159.hitungRandint(30,34)].click()
        radiobuttons[data_159.hitungRandint(35,41)].click()
        radiobuttons[data_159.hitungRandint(42,50)].click()
        radiobuttons[data_159.hitungRandint(51,58)].click()

        time.sleep(3)
        textarea[0].send_keys(data_159.alasan[index])

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("kategori = " + str(data_159.kategori[0]) + "," + str(data_159.kategori[1]) + "," + str(data_159.kategori[2]))
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


        

