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
driver.get("https://shorturl.at/suQUX")

nim = [
    "2301907763",
    "2301906962",
    "2301894552",
    "2301891046",
    "2301903935",
    "2301934871",
    "2301853344",
    "2301903790",
    "2301934796",
    "2301931535",
    "2301871012",
    "2301929852",
    "2301908835",
    "2301862582",
    "2301863351",
    "2301899471",
    "2301887295",
    "2301891986",
    "2301935256",
    "2301866744",
    "2301879053",
    "2301892300",
    "2301934360",
    "2301909951",
    "2301908186",
    "2301930886",
    "2301900795",
    "2301933881",
    "2301912832",
    "2301933591",
]

telp = [
    "084624253733",
    "",
    "",
    "088070442682",
    "",
    "",
    "080103002233",
    "086659262105",
    "",
    "080640301967",
    "083806763847",
    "",
    "084985961237",
    "",
    "089843988039",
    "",
    "",
    "087788078906",
    "",
    "089474988296",
    "088530547344",
    "085109243357",
    "",
    "083273198985",
    "",
    "081211906212",
    "081212784008",
    "",
    "081264718461",
    "",
]

jurusan = [7,7,12,12,12,7,12,12,7,7,12,7,7,12,12,12,12,12,7,12,12,12,7,7,7,7,12,7,7,7]

kelamin = [5,6,6,6,5,5,5,6,5,5,6,5,5,5,6,6,5,5,5,6,5,5,6,6,5,5,5,5,6,5]

baik = 25
jelek = 5

times = 30
index = 0


try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        pilihan = driver.find_elements("css selector", ".Hvn9fb")#isian

        textboxes[0].send_keys(nim[index])
        textboxes[1].send_keys(telp[index])
        driver.implicitly_wait(4)

        radiobuttons[0].click()
        radiobuttons[kelamin[index]].click()

        if jurusan[index] == 12:
            radiobuttons[jurusan[index]].click()
            pilihan[1].send_keys("Marketing Communication")
        else:
            radiobuttons[jurusan[index]].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if baik != 0 and jelek !=0 :
            pil = random.choice([1,2])
            if pil == 1:
                baik -= 1
            else:
                jelek -= 1
        elif baik != 0 and jelek ==0 :
            pil = 1 
            baik -= 1
        elif baik == 0 and jelek !=0 :
            pil = 2
            jelek -= 1


        if pil == 1:
            a = 2
        else:
            a = 0

        p = a
        soal = 5
        while soal:
            s1 = random.choice([p,p+1,p+2])
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

        p = a
        soal = 8
        while soal:
            s1 = random.choice([p,p+1,p+2])
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

        p = a
        soal = 12
        while soal:
            s1 = random.choice([p,p+1,p+2])
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

        p = a
        soal = 6
        while soal:
            s1 = random.choice([p,p+1,p+2])
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

        p = a
        soal = 3
        while soal:
            s1 = random.choice([p,p+1,p+2])
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

        p = a
        soal = 3
        while soal:
            s1 = random.choice([p,p+1,p+2])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://shorturl.at/suQUX")

        index+=1
        print("==================")
        print("Baik  : " + str(baik))
        print("Jelek : " + str(jelek))

        times-=1
        # print("")
        print("index : " + str(index))
        print("")
        print("times : " + str(times))
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