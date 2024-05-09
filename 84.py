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
driver.get("https://forms.gle/sWNqZ7p9CJxNmzL16")

inisial = [
    "AH",
    "RF",
    "BP",
    "AN",
    "NA",
    "YN",
    "PA",
    "NA",
    "YP",
    "MA",
    "BM",
    "BA",
    "BS",
    "NM",
    "SL",
    "AK",
    "AC",
    "FS",
    "DC",
    "YA",
    "RR",
    "FP",
    "NY",
    "BD",
    "SR",
    "AF",
    "SF",
    "RU",
    "SA",
    "AM",
    "PK",
    "RW",
    "AR",
    "SP",
    "CN",
    "MF",
    "RM",
    "FE",
]

#0 cowo 1 cewe
kelamin = [0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1]

times = 38
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
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

        pendidikan = random.choice([2,3,4,5,2,3,4,5,2,3,4,5,2,3,4,5,2,3,4,5,6])

        if pendidikan == 2:
            penghasilan = 10
        elif pendidikan == 3:
            penghasilan = random.choice([10,11])
        elif pendidikan == 4:
            penghasilan = random.choice([11,12])
        else :
            penghasilan = random.choice([11,12,13])

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(inisial[index])
        time.sleep(2)

        radiobuttons[pendidikan].click()
        radiobuttons[kelamin[index]].click()
        radiobuttons[penghasilan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 1
        soal = 3
        while soal:
            s1 = random.choice([p,p+1,p+2,p+2,p+2,p+2,p+3,p+3,p+3,p+3])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 1
        soal = 4
        while soal:
            s1 = random.choice([p,p+1,p+2,p+2,p+2,p+2,p+3,p+3,p+3,p+3])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 1
        soal = 3
        while soal:
            s1 = random.choice([p,p+1,p+2,p+2,p+2,p+2,p+3,p+3,p+3,p+3])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 1
        soal = 3
        while soal:
            s1 = random.choice([p,p+1,p+2,p+2,p+2,p+2,p+3,p+3,p+3,p+3])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 1
        soal = 3
        while soal:
            s1 = random.choice([p,p+1,p+2,p+2,p+2,p+2,p+3,p+3,p+3,p+3])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 1
        soal = 3
        while soal:
            s1 = random.choice([p,p+1,p+2,p+2,p+2,p+2,p+3,p+3,p+3,p+3])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 1
        soal = 3
        while soal:
            s1 = random.choice([p,p+1,p+2,p+2,p+2,p+2,p+3,p+3,p+3,p+3])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/sWNqZ7p9CJxNmzL16")

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