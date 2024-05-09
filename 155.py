from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_155
import list
import random
import time

link = "https://forms.gle/akdruPqTE8UAUBRaA"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_155.times
index = data_155.index

try:
    while times:
        time.sleep(5)
        usia = data_155.countUsia()
        semester = data_155.countSemester(usia)
        status = data_155.countStatus(semester)
        
        pil = data_155.cekTipe()

        time.sleep(2)
        radiobuttons = data.tombol("kebawah", driver)

        radiobuttons[2].click()
        radiobuttons[0].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        radiobuttons = data.tombol("kebawah", driver)
        textboxes = data.tombol("isian", driver)
        checkboxes = data.tombol("checkbox", driver)

        textboxes[0].send_keys(list.inisial[index])
        textboxes[1].send_keys(usia)
        textboxes[2].send_keys(data_155.universitas[index])

        radiobuttons[semester].click()
        checkboxes[status].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        radiobuttons = data.tombol("kebawah", driver)

        if pil == 1 :
            data_155.jawab1(15, radiobuttons)
            data.pindahHalaman(driver)

            checkboxes = data.tombol("checkbox", driver)
            testcheck = data.tombol("kesamping", driver)
            
            data_155.jawabx1(testcheck, checkboxes, 5, 9, 7, 9, status)

            data.pindahHalaman(driver)

            time.sleep(2)
            radiobuttons = data.tombol("kebawah", driver)
            textboxes = data.tombol("isian", driver)
            checkboxes = data.tombol("checkbox", driver)
            testcheck = data.tombol("kesamping", driver)
            lainnya = data.tombol("lainnya", driver)

            data_155.halaman5(checkboxes, textboxes, radiobuttons, testcheck, lainnya, 5, 9, "tidak", "-", 7, 9)

            data.pindahHalaman(driver)
            

            data_155.tipe1 -= 1
        elif pil == 2:
            data_155.jawab2(15, radiobuttons)
            data.pindahHalaman(driver)

            checkboxes = data.tombol("checkbox", driver)
            testcheck = data.tombol("kesamping", driver)
            
            data_155.jawabx1(testcheck, checkboxes, 5, 9, 0, 2, status)
            
            data.pindahHalaman(driver)
            
            time.sleep(2)
            radiobuttons = data.tombol("kebawah", driver)
            textboxes = data.tombol("isian", driver)
            checkboxes = data.tombol("checkbox", driver)
            testcheck = data.tombol("kesamping", driver)            
            lainnya = data.tombol("lainnya", driver)

            data_155.halaman5(checkboxes, textboxes, radiobuttons, testcheck, lainnya, 3, 4, "tidak", "-", 0, 2)

            data.pindahHalaman(driver)

            data_155.tipe2 -= 1
        else:
            data_155.jawab3(15, radiobuttons)
            data.pindahHalaman(driver)

            checkboxes = data.tombol("checkbox", driver)
            testcheck = data.tombol("kesamping", driver)
            
            data_155.jawabx1(testcheck, checkboxes, 3, 6, 8, 9, status)
            
            data.pindahHalaman(driver)
            
            time.sleep(2)
            radiobuttons = data.tombol("kebawah", driver)
            textboxes = data.tombol("isian", driver)
            checkboxes = data.tombol("checkbox", driver)
            testcheck = data.tombol("kesamping", driver)
            lainnya = data.tombol("lainnya", driver)

            data_155.halaman5(checkboxes, textboxes, radiobuttons, testcheck, lainnya, 6, 9, "ya", "bebas", 8, 9)

            data.pindahHalaman(driver)

            data_155.tipe3 -= 1
        
        time.sleep(2)
        textboxes = data.tombol("isian", driver)
        data_155.jawabIsian(pil, textboxes)

        data.pindahHalaman(driver)

        time.sleep(2)
        radiobuttons = data.tombol("kebawah", driver)
        radiobuttons[1].click()

        data.pindahHalaman(driver)

        time.sleep(2)
        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("tipe1 = " + str(data_155.tipe1))
        print("tipe2 = " + str(data_155.tipe2))
        print("tipe3 = " + str(data_155.tipe3))
        print("")
        print("tipe1Idx = " + str(data_155.tipe1Idx))
        print("tipe2Idx = " + str(data_155.tipe2Idx))
        print("tipe3Idx = " + str(data_155.tipe3Idx))
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


        

