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
driver.get("https://forms.gle/xMkGEKmXoGhjprZr8")

times = 47
index = 3

page1 = [
    [5,4,5,4,4,5,5,5,4,3,5,4,5,5,3,4,4,4,4,4,4,4,4,4,5,4,5,2,4,5,5,4,4,5,5,5,3,5,3,2,5,5,4,4,4,4,5,4,5,3],
    [5,4,5,4,4,5,5,5,5,3,5,5,5,5,4,5,5,5,5,4,4,5,3,4,4,4,5,3,4,3,5,4,5,5,5,5,2,5,4,3,5,5,5,4,3,5,5,5,3,2],
    [4,4,4,4,4,4,4,4,5,4,3,5,5,4,3,4,4,4,5,4,4,4,4,4,5,3,5,2,4,4,4,3,5,4,5,4,3,5,4,2,3,4,4,4,4,5,4,4,4,3],
    [5,4,5,4,4,4,5,5,5,4,5,5,5,5,3,5,4,5,5,3,4,4,4,4,4,3,5,2,4,3,5,3,4,5,5,5,2,5,4,2,5,5,4,4,4,5,5,4,3,2],
    [5,4,5,4,4,5,4,5,4,4,4,4,5,5,4,5,4,5,4,3,4,4,4,4,3,3,5,2,4,4,4,3,4,5,5,5,3,5,3,2,4,5,4,4,4,4,5,4,4,3],
    [5,4,4,4,4,5,5,5,4,3,5,5,5,5,4,5,5,5,4,4,4,5,4,4,4,3,5,2,4,5,5,3,4,5,5,5,2,5,4,2,5,5,4,4,4,5,4,4,5,2],
]

page2 = [
    [4,5,3,3,4,5,5,3,5,3,4,3,5,3,4,5,5,3,5,3,4,3,4,4,4,4,5,3,4,4,5,5,4,4,4,4,5,5,4,4,5,3,5,5,4,4,3,4,4,4],
    [4,5,4,2,4,4,5,4,5,4,4,2,5,4,5,5,4,4,4,4,4,5,4,4,5,4,5,4,5,5,4,4,4,4,4,3,4,5,4,4,5,4,5,5,4,4,4,4,4,4],
    [4,5,4,3,5,4,5,4,5,3,5,3,5,4,5,5,5,2,5,3,5,5,4,4,3,5,5,2,3,5,5,5,4,5,5,4,4,5,5,5,5,3,5,5,4,4,4,5,5,5],
    [4,5,5,2,5,4,4,4,5,4,5,2,5,4,4,4,4,3,5,4,5,4,3,4,4,5,4,3,4,4,4,5,3,4,5,4,4,5,4,4,5,4,5,4,4,4,4,4,4,4],
    [4,5,4,2,5,3,5,3,5,3,4,2,5,3,5,5,5,2,5,5,3,4,4,5,4,5,5,2,4,5,5,5,4,4,4,4,3,5,5,5,5,5,5,5,4,4,4,4,5,5],
    [4,5,5,2,5,4,4,4,5,4,5,2,5,4,4,4,4,3,5,4,5,4,3,4,4,5,4,3,4,4,4,5,3,4,5,4,4,5,4,4,5,4,5,4,4,4,4,4,4,4],
]

page3 = [
    [2,5,4,4,4,5,4,5,5,4,4,3,5,5,3,4,5,5,3,3,2,5,4,5,4,3,5,5,5,5,2,4,4,5,5,5,3,4,4,5,4,5,2,5,5,3,5,5,4,5],
    [2,5,5,4,5,4,5,5,3,4,4,4,5,5,4,4,5,5,3,4,2,5,4,5,5,4,5,5,4,5,2,5,4,5,4,4,4,4,4,5,5,5,2,4,5,4,5,3,5,4],
    [3,5,5,4,5,5,5,5,4,5,4,4,5,3,4,5,5,5,3,3,2,5,4,5,5,4,5,5,5,5,3,5,5,5,4,5,4,4,4,5,5,3,2,5,5,3,5,4,5,4],
    [2,5,5,4,5,4,5,5,3,4,4,4,5,5,4,4,5,5,3,4,2,5,4,5,5,4,5,5,4,5,2,5,4,5,4,4,4,4,4,5,5,5,2,4,5,4,5,3,5,4],
    [2,5,5,4,4,5,5,5,4,4,4,4,5,5,4,4,5,5,3,4,3,5,4,4,5,3,4,5,4,4,2,4,4,5,4,5,3,4,5,5,5,5,3,4,5,4,4,4,5,4],
    [3,5,5,4,5,5,5,5,4,5,4,4,5,3,4,5,5,5,4,3,2,5,4,5,5,3,5,5,5,5,3,5,5,5,4,5,4,4,4,5,5,3,2,5,5,3,5,4,5,4],
]

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        domisili = random.choice([0,1,2,3,4])
        kelamin = random.choice([5,6])
        pendidikan = random.choice([9,10,11])

        time.sleep(2)
        if pendidikan == 9:
            pekerjaan = random.choice([12,13,14])
            pendapatan = random.choice([15,16])
        else:
            pekerjaan = random.choice([12,13,14])
            pendapatan = random.choice([15,16,17])

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        time.sleep(2)
        radiobuttons[2].click()
        radiobuttons[domisili].click()
        radiobuttons[kelamin].click()
        radiobuttons[pendidikan].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[pendapatan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = -1
        for i in range(6):
            s1 = page1[i][index] + p
            testcheck[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = -1
        for i in range(6):
            s1 = page2[i][index] + p
            testcheck[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = -1
        for i in range(6):
            s1 = page3[i][index] + p
            testcheck[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/xMkGEKmXoGhjprZr8")

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