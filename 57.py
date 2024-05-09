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
driver.get("https://forms.gle/A84oSk2yX3hH3AF79")

cowo = 20
cewe = 21

usia1 = 23
usia2 = 9
usia3 = 9

pekerjaan1 = 12
pekerjaan2 = 16
pekerjaan3 = 7
pekerjaan4 = 5
pekerjaan5 = 1

penghasilan1 = 25
penghasilan2 = 12
penghasilan3 = 1
penghasilan4 = 3

page1 = [
    [4,2,1,4,5,3,2,2,4,2,3,2,1,4,1,1,4,1,5,4,1,1,2,4,3,1,2,3,3,3,1,2,2,3,2,1,4,2,2,3,3,1,1,1,5,3,4,5,1,2],
    [3,1,2,3,3,5,1,1,3,2,4,2,1,5,1,2,4,2,4,4,1,1,1,4,4,1,1,5,1,4,3,1,1,2,2,2,3,1,3,5,5,1,2,3,3,4,4,3,1,1],
    [4,2,2,3,3,5,1,1,3,1,4,1,2,4,1,1,5,2,3,5,1,1,1,3,3,1,2,3,1,5,1,2,1,2,1,2,4,2,2,4,4,2,2,1,3,4,5,4,2,1],
    [5,1,2,4,5,4,3,3,4,2,4,1,3,5,3,1,4,3,5,4,3,2,2,4,5,3,3,5,3,4,3,3,3,2,1,1,4,1,3,3,5,3,3,1,4,3,4,4,3,3],
    [4,4,4,5,4,5,4,4,4,4,4,4,2,4,1,4,4,3,5,5,4,4,2,4,5,4,3,5,2,5,3,1,2,2,2,4,5,3,3,5,5,4,1,1,5,5,5,4,4,2],
    [4,2,1,4,4,5,1,1,4,2,3,2,1,5,1,3,4,3,3,4,2,3,3,4,5,3,1,5,1,5,3,1,1,1,3,1,5,1,1,4,5,1,2,2,5,5,4,3,2,2],
    [3,1,2,5,5,4,3,2,4,2,4,2,2,4,3,1,3,3,5,3,1,3,2,4,3,2,3,4,1,4,1,2,2,3,1,1,3,2,3,3,4,1,2,3,3,5,4,4,2,1],
    [5,2,1,3,5,4,3,3,4,3,4,3,2,5,3,3,5,3,4,4,2,1,2,4,4,1,3,5,3,5,3,1,2,2,2,3,4,3,1,3,5,3,3,2,4,4,4,5,2,2],
    [5,4,2,4,5,4,4,4,5,2,4,1,4,4,1,4,5,4,5,5,4,4,4,5,5,2,2,4,3,4,4,3,2,3,4,4,4,3,1,4,5,2,2,4,5,5,5,4,3,4],
    [3,3,1,5,4,3,2,1,5,3,5,2,2,3,3,2,3,3,3,3,3,3,2,3,4,1,3,3,2,5,3,1,1,1,3,3,5,2,1,4,3,2,3,1,4,3,4,4,1,3],
    [5,1,1,5,4,5,2,1,5,3,5,4,2,5,1,3,4,4,5,4,4,2,1,5,5,3,3,5,3,5,4,3,3,3,2,2,5,1,2,5,5,2,3,3,4,5,5,4,1,2],
    [5,1,3,4,5,4,3,2,3,2,3,1,3,4,1,3,4,1,5,4,2,2,3,4,5,1,2,5,3,4,3,3,1,1,1,2,4,3,3,4,5,2,3,1,3,5,3,4,1,1],
    [3,2,2,3,3,4,1,3,4,2,3,1,1,3,1,3,5,1,3,5,2,1,2,4,5,3,2,5,1,5,2,3,3,2,2,3,4,1,3,5,5,1,2,2,3,4,3,5,2,2],
    [4,3,3,4,5,5,3,4,5,4,5,3,1,5,3,4,4,2,4,4,2,3,4,4,5,3,2,4,3,4,1,2,4,4,2,4,4,2,4,4,4,2,3,1,5,4,5,4,1,3],
]

page2 = [
    [4,4,3,2,5,3,5,3,1,3,4,3,4,2,2,3,1,1,5,5,2,4,5,5,4,1,1,5,3,5,5,2,2,4,4,4,4,5,3,5,5,2,3,4,3,5,4,5,2,4],
    [5,5,1,2,3,4,3,3,2,2,4,1,5,1,1,2,1,2,5,5,2,4,3,3,4,2,2,3,2,5,3,1,2,4,2,3,4,4,3,3,4,2,4,4,2,3,5,3,1,5],
    [5,3,1,1,4,4,3,3,1,3,3,1,4,3,3,1,2,1,5,5,3,3,3,4,4,1,2,4,2,4,4,2,1,3,5,4,4,3,5,3,5,2,3,3,1,4,3,5,1,3],
    [4,4,3,3,5,4,5,5,3,3,4,2,5,1,2,3,2,1,5,5,1,4,5,4,4,3,1,5,3,5,4,2,2,4,5,4,4,4,5,5,4,1,4,4,1,4,5,4,1,5],
    [5,5,2,2,4,5,5,5,2,3,5,1,5,1,1,1,1,2,3,5,1,5,4,5,4,2,3,3,2,4,5,1,2,4,5,5,5,4,5,5,4,3,5,4,3,4,4,5,2,3],
    [4,5,2,2,3,3,4,4,2,1,3,2,3,1,1,1,2,2,5,4,1,3,3,3,4,1,2,4,1,4,5,2,1,4,3,4,3,5,3,5,5,2,4,4,2,3,3,3,1,3],
    [4,5,2,2,3,3,3,4,1,1,5,1,4,2,1,2,3,2,5,4,3,5,4,5,4,1,3,3,1,4,3,2,3,3,4,4,3,4,3,5,5,2,4,4,2,3,3,3,2,5],
    [4,4,2,2,3,3,5,5,2,2,3,3,4,2,2,2,1,1,3,4,2,4,5,4,3,1,2,4,3,5,3,1,2,3,3,5,4,4,5,5,3,2,3,3,1,3,3,5,2,4],
    [4,4,2,2,5,3,3,3,2,2,3,2,3,2,1,1,1,1,3,3,1,4,2,2,4,1,2,4,1,3,3,1,1,3,3,3,4,3,5,4,4,2,5,3,2,3,5,3,2,4],
]

times = 41
index = 9

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0 
        soal = 4
        while soal:
            radiobuttons[p].click()
            p += 2
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        if cowo != 0 and cewe != 0:
            kelamin = random.choice([0,1])
            if kelamin == 0:
                cowo -= 1
            else:
                cewe -= 1
        elif cowo != 0 and cewe == 0:
            kelamin = 0
            cowo -= 1
        elif cowo == 0 and cewe != 0:
            kelamin = 1
            cewe -= 1

        time.sleep(2)
        if usia1 != 0 and usia2 != 0 and usia3 != 0:
            usia = random.choice([2,3,4])
            if usia == 2:
                usia1 -= 1
            elif usia == 3:
                usia2 -= 1
            else:
                usia3 -= 1
        elif usia1 != 0 and usia2 != 0 and usia3 == 0:
            usia = random.choice([2,3])
            if usia == 2:
                usia1 -= 1
            else:
                usia2 -= 1
        elif usia1 != 0 and usia2 == 0 and usia3 != 0:
            usia = random.choice([2,4])
            if usia == 2:
                usia1 -= 1
            else:
                usia3 -= 1
        elif usia1 == 0 and usia2 != 0 and usia3 != 0:
            usia = random.choice([3,4])
            if usia == 3:
                usia1 -= 1
            else:
                usia3 -= 1
        elif usia1 != 0 and usia2 == 0 and usia3 == 0:
            usia = 2
            usia1 -= 1  
        elif usia1 == 0 and usia2 != 0 and usia3 == 0:
            usia = 3
            usia2 -= 1
        elif usia1 == 0 and usia2 == 0 and usia3 != 0:
            usia = 4
            usia3 -= 1

        time.sleep(2)
        if usia == 2:
            if pekerjaan1 != 0 and pekerjaan2 != 0 and pekerjaan5 != 0:
                pekerjaan = random.choice([5,6,9])
            elif pekerjaan1 != 0 and pekerjaan2 != 0 and pekerjaan5 == 0:
                pekerjaan = random.choice([5,6])
            elif pekerjaan1 != 0 and pekerjaan2 == 0 and pekerjaan5 != 0:
                pekerjaan = random.choice([5,9])
            elif pekerjaan1 == 0 and pekerjaan2 != 0 and pekerjaan5 != 0:
                pekerjaan = random.choice([6,9])
            elif pekerjaan1 != 0 and pekerjaan2 == 0 and pekerjaan5 == 0:
                pekerjaan = 5
            elif pekerjaan1 == 0 and pekerjaan2 != 0 and pekerjaan5 == 0:
                pekerjaan = 6
            elif pekerjaan1 == 0 and pekerjaan2 == 0 and pekerjaan5 != 0:
                pekerjaan = 9
        else:
            if pekerjaan2 != 0 and pekerjaan3 != 0 and pekerjaan4 != 0  and pekerjaan5 != 0:
                pekerjaan = random.choice([6,7,8,9])
            elif pekerjaan2 != 0 and pekerjaan3 != 0 and pekerjaan4 != 0  and pekerjaan5 == 0:
                pekerjaan = random.choice([6,7,8])
            elif pekerjaan2 != 0 and pekerjaan3 != 0 and pekerjaan4 == 0  and pekerjaan5 != 0:
                pekerjaan = random.choice([6,7,9])
            elif pekerjaan2 != 0 and pekerjaan3 == 0 and pekerjaan4 != 0  and pekerjaan5 != 0:
                pekerjaan = random.choice([6,8,9])
            elif pekerjaan2 == 0 and pekerjaan3 != 0 and pekerjaan4 != 0  and pekerjaan5 != 0:
                pekerjaan = random.choice([7,8,9])
            elif pekerjaan2 != 0 and pekerjaan3 != 0 and pekerjaan4 == 0  and pekerjaan5 == 0:
                pekerjaan = random.choice([6,7])
            elif pekerjaan2 != 0 and pekerjaan3 == 0 and pekerjaan4 != 0  and pekerjaan5 == 0:
                pekerjaan = random.choice([6,8])
            elif pekerjaan2 == 0 and pekerjaan3 != 0 and pekerjaan4 != 0  and pekerjaan5 == 0:
                pekerjaan = random.choice([7,8])
            elif pekerjaan2 != 0 and pekerjaan3 == 0 and pekerjaan4 == 0  and pekerjaan5 != 0:
                pekerjaan = random.choice([6,9])
            elif pekerjaan2 == 0 and pekerjaan3 != 0 and pekerjaan4 == 0  and pekerjaan5 != 0:
                pekerjaan = random.choice([7,9])
            elif pekerjaan2 == 0 and pekerjaan3 == 0 and pekerjaan4 != 0  and pekerjaan5 != 0:
                pekerjaan = random.choice([8,9])
            elif pekerjaan2 != 0 and pekerjaan3 == 0 and pekerjaan4 == 0  and pekerjaan5 == 0:
                pekerjaan = 6
            elif pekerjaan2 == 0 and pekerjaan3 != 0 and pekerjaan4 == 0  and pekerjaan5 == 0:
                pekerjaan = 7
            elif pekerjaan2 == 0 and pekerjaan3 == 0 and pekerjaan4 != 0  and pekerjaan5 == 0:
                pekerjaan = 8
            elif pekerjaan2 == 0 and pekerjaan3 == 0 and pekerjaan4 == 0  and pekerjaan5 != 0:
                pekerjaan = 9
            else:
                pekerjaan = 5
                pekerjaan1 -= 1

        time.sleep(2)
        if pekerjaan == 5:
            pekerjaan1 -= 1
        elif pekerjaan == 6:
            pekerjaan2 -= 1
        elif pekerjaan == 7:
            pekerjaan3 -= 1
        elif pekerjaan == 8:
            pekerjaan4 -= 1
        else:
            pekerjaan5 -= 1

        time.sleep(2)
        if pekerjaan == 5:
            if penghasilan1 != 0 :
                penghasilan = 10
            elif penghasilan2 != 0:
                penghasilan = 11
            elif penghasilan3 != 0:
                penghasilan = 12
            else:
                penghasilan = 13
        else :
            if penghasilan1 != 0 and penghasilan2 != 0 and penghasilan3 != 0 and penghasilan4 != 0:
                penghasilan = random.choice([10,11,12,13])
            elif penghasilan1 != 0 and penghasilan2 != 0 and penghasilan3 != 0 and penghasilan4 == 0:
                penghasilan = random.choice([10,11,12])
            elif penghasilan1 != 0 and penghasilan2 != 0 and penghasilan3 == 0 and penghasilan4 != 0:
                penghasilan = random.choice([10,11,13])
            elif penghasilan1 != 0 and penghasilan2 == 0 and penghasilan3 != 0 and penghasilan4 != 0:
                penghasilan = random.choice([10,12,13])
            elif penghasilan1 == 0 and penghasilan2 != 0 and penghasilan3 != 0 and penghasilan4 != 0:
                penghasilan = random.choice([11,12,13])
            elif penghasilan1 != 0 and penghasilan2 != 0 and penghasilan3 == 0 and penghasilan4 == 0:
                penghasilan = random.choice([10,11])
            elif penghasilan1 != 0 and penghasilan2 == 0 and penghasilan3 != 0 and penghasilan4 == 0:
                penghasilan = random.choice([10,12])
            elif penghasilan1 == 0 and penghasilan2 != 0 and penghasilan3 != 0 and penghasilan4 == 0:
                penghasilan = random.choice([11,12])
            elif penghasilan1 != 0 and penghasilan2 == 0 and penghasilan3 == 0 and penghasilan4 != 0:
                penghasilan = random.choice([10,13])
            elif penghasilan1 == 0 and penghasilan2 != 0 and penghasilan3 == 0 and penghasilan4 != 0:
                penghasilan = random.choice([11,13])
            elif penghasilan1 == 0 and penghasilan2 == 0 and penghasilan3 != 0 and penghasilan4 != 0:
                penghasilan = random.choice([12,13])
            elif penghasilan1 != 0 and penghasilan2 == 0 and penghasilan3 == 0 and penghasilan4 == 0:
                penghasilan = 10
            elif penghasilan1 == 0 and penghasilan2 != 0 and penghasilan3 == 0 and penghasilan4 == 0:
                penghasilan = 11
            elif penghasilan1 == 0 and penghasilan2 == 0 and penghasilan3 != 0 and penghasilan4 == 0:
                penghasilan = 12
            elif penghasilan1 == 0 and penghasilan2 == 0 and penghasilan3 == 0 and penghasilan4 != 0:
                penghasilan = 13

        time.sleep(2)
        if penghasilan == 10:
            penghasilan1 -= 1
        elif penghasilan == 11:
            penghasilan2 -= 1
        elif penghasilan == 12:
            penghasilan3 -= 1
        else:
            penghasilan4 -= 1



        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[kelamin].click()
        radiobuttons[usia].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[penghasilan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = -1
        for i in range(14):
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
        for i in range(9):
            s1 = page2[i][index] + p
            testcheck[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/A84oSk2yX3hH3AF79")

        index+=1
        print("==================")
        print("cowo : " + str(cowo))
        print("cewe : " + str(cewe))
        print("")
        print("usia1 : " + str(usia1))
        print("usia1 : " + str(usia2))
        print("usia1 : " + str(usia3))
        print("")
        print("pekerjaan1 : " + str(pekerjaan1))
        print("pekerjaan2 : " + str(pekerjaan2))
        print("pekerjaan3 : " + str(pekerjaan3))
        print("pekerjaan4 : " + str(pekerjaan4))
        print("pekerjaan5 : " + str(pekerjaan5))
        print("")
        print("penghasilan1 : " + str(penghasilan1))
        print("penghasilan2 : " + str(penghasilan2))
        print("penghasilan3 : " + str(penghasilan3))
        print("penghasilan4 : " + str(penghasilan4))


        times-=1
        # print("")
        print("index  : " + str(index))
        print("")
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