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
driver.get("https://qfreeaccountssjc1.az1.qualtrics.com/jfe/form/SV_eFj7cSqeV5ZC9bU")

times = 1
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        nextb = driver.find_elements("css selector", ".NextButton")
        nextb[0].click()

        time.sleep(2)
        selection = driver.find_elements("css selector", ".Selection")

        selection[0].click()
        selection[2].click()
        selection[7].click()
        selection[11].click()
        selection[13].click()
        selection[18].click()
        selection[21].click()
        selection[24].click()

        time.sleep(2)
        isian = driver.find_elements("css selector", ".InputText")

        isian[0].send_keys("nama")

        time.sleep(2)
        nextb = driver.find_elements("css selector", ".NextButton")
        nextb[0].click()

        time.sleep(2)
        pilihan = driver.find_elements("css selector", ".ResultsInput")
        print(len(pilihan))

        for i in pilihan :
            driver.execute_script("arguments[0].setAttribute('value','7')", i)

        time.sleep(2)
        nextb = driver.find_elements("css selector", ".NextButton")
        nextb[0].click()

        time.sleep(2)
        pilihan = driver.find_elements("css selector", ".ResultsInput")
        print(len(pilihan))

        for i in pilihan :
            driver.execute_script("arguments[0].setAttribute('value','7')", i)

        time.sleep(2)
        nextb = driver.find_elements("css selector", ".NextButton")
        nextb[0].click()








        










        

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        # )

        # submit_button.click()

        # driver.implicitly_wait(4)
        # driver.get("https://qfreeaccountssjc1.az1.qualtrics.com/jfe/form/SV_eFj7cSqeV5ZC9bU")

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