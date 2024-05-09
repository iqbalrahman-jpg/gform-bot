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
driver.get("https://forms.gle/x11Xy62RcCqcc48s6")

times = 90
index = 0

positif = 60
negatif = 30

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        usia = random.choice([0,1,2,3])
        pekerjaan = random.choice([4,5,6,7,8,9,10,11,12,13,14])
        domisili = random.choice([15,16,17,18,19,20])

        time.sleep(2)
        if positif != 0 and negatif != 0 :
            pil = random.choice([0,1])
        elif positif != 0 and negatif == 0 :
            pil = 0
        elif positif == 0 and negatif != 0 :
            pil = 1

        time.sleep(2)
        radiobuttons[usia].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[domisili].click()

        time.sleep(2)
        if pil == 0:
            time.sleep(2)
            radiobuttons[21].click()
            radiobuttons[24].click()
            radiobuttons[25].click()
            radiobuttons[30].click()
            radiobuttons[34].click()

            time.sleep(2)
            checkboxes[0].click()
            checkboxes[1].click()
            checkboxes[4].click()
            checkboxes[5].click()

            positif -= 1
        else:
            time.sleep(2)
            radiobuttons[random.randint(21,22)].click()
            radiobuttons[random.randint(23,24)].click()
            radiobuttons[random.randint(25,29)].click()
            radiobuttons[random.randint(30,31)].click()
            radiobuttons[random.randint(32,35)].click()

            time.sleep(2)
            temp = random.randint(1,2)
            temp1 = random.randint(1,2)

            cheki = random.sample([0,1,2,3], temp)
            cheki1 = random.sample([4,5,6,7], temp1)

            time.sleep(2)
            for x in cheki :
                checkboxes[x].click()

            for x in cheki1 :
                checkboxes[x].click()

            negatif -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/x11Xy62RcCqcc48s6")

        index+=1
        print("==================")
        print("positif : " + str(positif))
        print("negatif : " + str(negatif))
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