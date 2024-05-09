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
driver.get("https://forms.gle/qzukhWzYo3osR1uTA")

nama = [
    "Mutia Ayu Nur",
    "Budi Wardanawan",
    "Annisa Chania",
    "Bayu Danang Merta",
    "Bellanda Clara Ayunda", 
    "Affianto Kuntoro",
    "M. Iqbal Ramadhan",
    "Rudi Nurbakti",
    "Rehan Lesmana",
    "Eka Wahyu",
]

univ = [
    "Universitas Pembangunan Negeri Veteran Jatim",
    "ITS",
    "UPN",
    "Unair",
    "Universitas Airlangga",
    "UIN",
    "ITS",
    "UNAIR",
    "UNAIR",
    "UM",
]

laptop = 6
hp = 4

times = 10
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(univ[index])

        time.sleep(2)
        if laptop != 0 and hp != 0 :
            pil1 = random.choice([0,1])
        elif laptop != 0 and hp == 0 :
            pil1 = 0
        elif laptop == 0 and hp != 0 :
            pil1 = 1

        time.sleep(2)
        if pil1 == 0:
            radiobuttons[random.choice([3,4])].click()
            radiobuttons[random.choice([5,6,7])].click()
            laptop -= 1
        else:
            radiobuttons[random.choice([8,9,10,11])].click()
            hp -= 1

        time.sleep(2)
        radiobuttons[pil1].click()
        radiobuttons[random.choice([12,13])].click()
        radiobuttons[random.choice([14,14,14,14,14,14,14,15])].click()
        radiobuttons[random.choice([16,17])].click()
        radiobuttons[random.choice([19,20])].click()
        radiobuttons[22].click()
        radiobuttons[25].click()
        radiobuttons[28].click()
        radiobuttons[31].click()
        radiobuttons[34].click()
        radiobuttons[37].click()
        radiobuttons[40].click()
        radiobuttons[43].click()
        radiobuttons[46].click()
        radiobuttons[49].click()
        radiobuttons[54].click()
        radiobuttons[63].click()
        radiobuttons[72].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/qzukhWzYo3osR1uTA")

        index+=1
        print("==================")
        print("laptop = " + str(laptop))
        print("hp = " + str(hp))
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