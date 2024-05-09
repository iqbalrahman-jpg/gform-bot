from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://forms.gle/2RPRpcieGG9Uh1C67")

nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
]

kritik = [
    "Tambahkan tombol pesan di persewaan bis",
    "Web terasa sedikit lambat",
    "Tampilan bisa lebih diperbagus",
    "sewa kendaraan sedikit membingungkan",
]

kelamin = [1,0,1,0,0,1,0,1,1,0,]

page = [
    [2,4,4,4,2,4,3,4,4,4],
    [3,5,5,4,3,5,2,4,4,3],
    [2,5,3,4,2,4,3,4,4,4],
    [2,4,3,4,2,4,2,4,4,4],
    [3,5,3,3,4,5,4,5,5,5],
    [3,4,3,3,4,5,4,5,4,3],
    [2,3,2,2,2,4,3,4,3,2],
    [2,4,3,2,4,5,4,5,4,4],
]

pernah = 1
belum = 9

saran = 4
tsaran = 6
idxsaran = 0

times = 10
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if pernah != 0 and belum != 0 :
            pil = random.choice([2,3])
        elif pernah != 0 and belum == 0 :
            pil = 2
        elif pernah == 0 and belum != 0 :
            pil = 3

        if pil == 2:
            pernah -= 1
        else:
            belum -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])

        time.sleep(2)
        radiobuttons[kelamin[index]].click()
        radiobuttons[pil].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        if pil == 2:
            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()
        else:
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            radiobuttons[random.choice([0,0,0,1])].click()

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = -1
        for i in range(8):
            s1 = page[i][index] + p
            testcheck[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)

        if saran != 0 and tsaran != 0:
            pil3 = random.choice([0,1])
        elif saran != 0 and tsaran == 0:
            pil3 = 0
        elif saran == 0 and tsaran != 0:
            pil3 = 1

        time.sleep(2)
        if pil3 == 0:
            time.sleep(2)
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

            textarea[0].send_keys(kritik[idxsaran])

            idxsaran += 1
            saran -= 1
        else:
            tsaran -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/2RPRpcieGG9Uh1C67")

        index+=1
        print("==================")
        print("Pernah : " + str(pernah))
        print("Belum : " + str(belum))
        print("")
        print("saran : " + str(saran))
        print("tsaran : " + str(tsaran))
        print("idxsaran : " + str(idxsaran))
        print("")

        times-=1
        print("index  : " + str(index))
        print("times  : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()