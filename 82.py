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
driver.get("https://forms.gle/jMkWCwq22Ne4Jxq99")

cowo = 24
cewe = 76

positif = 88
negatif = 12

times = 100
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        umur = random.choice([2,3,4])

        time.sleep(2)
        if umur == 2:
            pekerjaan = 5
        elif umur == 3:
            pekerjaan = random.choice([5,6,7,8])
        else:
            pekerjaan = random.choice([6,7,8])

        if cowo != 0 and cewe != 0:
            kelamin = random.choice([0,1])
            if kelamin == 0:
                cewe -= 1
            else:
                cowo -= 1
        elif cowo != 0 and cewe == 0:
            kelamin = 1 
            cowo -= 1
        elif cowo == 0 and cewe != 0:
            kelamin = 0 
            cewe -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[kelamin].click()
        radiobuttons[umur].click()
        radiobuttons[pekerjaan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        if positif != 0 and negatif != 0:
            pil = random.choice([1,2])
            if pil == 1:
                positif -= 1
            else:
                negatif -= 1
        elif positif != 0 and negatif == 0:
            pil = 1
            positif -= 1
        elif positif == 0 and negatif != 0:
            pil = 2
            negatif -= 1

        time.sleep(2)
        if pil == 1:
            p = 2
        else:
            p = 0

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        soal = 30
        while soal:
            s1 = random.choice([p,p+1,p+1,p+1,p+2])
            testcheck[s1].click()
            p += 5
            soal -= 1

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
        driver.get("https://forms.gle/jMkWCwq22Ne4Jxq99")

        index+=1
        print("==================")
        print("cowo : " + str(cowo))
        print("cewe : " + str(cewe))
        print("")
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