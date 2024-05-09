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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeiP95BMZVafjpFV1pVEFRKUcyp8DmbjmF9J5Z33AF74m1Aeg/viewform?usp=sf_link")

nama = [
    "Hesty - Suryopranoto",
    "Ridhansyah - Tanah Abang",
    "Nia - Ujung Menteng",
    "Fani - Wiladatika",
    "Hadit - Cikarang",
    "Marendra - Karawang",
    "Ratino - Subang",
    "Anneke - Gading Serpong",
    "Bayu - Cipanas",
    "Irene - Cinere",
    "Robert",
    "Noviana - Asia Afrika",
    "Wahyu - matraman",
    "Dandy - Melawai",
    "Menara Global",
    "Pangeran jayakarta",
    "eko - batam",
    "tedi",
    "jambi",
    "Balikpapan",
    "Banjarmasin",
    "Pontianak",
    "Samarinda",
    "Lily - kupang",
    "Sherly - lampung",
    "napoleon",
    "Ishaq",
    "Nanda",
    "Medan",
    "Palembang",
    "christin - pangkalpinang",
    "pekanbaru",
    "riani - semarang",
    "hendry - surabaya",
    "teguh - hr muhammad",
    "Bitung",
    "Inny - makassar",
    "ivanda - manado",
    "indra - kpo sudirman",
    "debby - kpo sudirman",
    "riza - kpo sudirman",
    "Ayu -  BEI",
    "Septi - Semarang",
    "Rosita - SAM",
    "Fazri - SAM",
    "Kemas - SAM",
    "Fenty - Cokroaminoto",
    "fahrina - artha gading",
    "virgin - Dit. Bisni",
]

bagian = [2,16,8,7,23,16,4,26,23,14,14,4,3,22,8,8,18,2,23,2,2,23,16,3,5,18,13,9,13,23,9,1,20,3,22,10,13,6,12,8,6,14,20,23,9,10,22,3,2]

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0
        count = 1

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(nama[index])

        time.sleep(2)
        while count != 27:
            print(count)
            time.sleep(2)
            if count == bagian[index] :
                radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

                p = 2
                for i in range(10):
                    s1 = random.choice([p,p+1])
                    radiobuttons[s1].click()
                    p += 5

                time.sleep(2)

            count += 1    
            if count != 27 :
                time.sleep(3)
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )

                submit_button.click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeiP95BMZVafjpFV1pVEFRKUcyp8DmbjmF9J5Z33AF74m1Aeg/viewform?usp=sf_link")

        index+=1
        print("==================")
        # print("  : " + str())
        # print("")
        
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