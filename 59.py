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
driver.get("https://forms.gle/QHp2HzVQp1YLjwYE8")

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
    "Yuli Ayunda Dewi",
    "Bayu Danang Merta",
    "Bellanda Clara Ayunda", 
    "Budi Suryanto",
    "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Attaka Majid",
    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
]

#0 cowo 1 cewe
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,]

car = 12
motor = 8

times = 20
index = 5

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0
        
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        for i in range(5):
            checkboxes[i].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        usia = random.choice([2,3,4,5,6,7])

        if usia == 2:
            pendidikan = random.choice([8,9])
            pekerjaan = 13
        elif usia == 3:
            pendidikan = random.choice([9,10])
            pekerjaan = random.choice([13,13,13,14])
        elif usia == 4:
            pendidikan = random.choice([9,10,11])
            pekerjaan = random.choice([14,15,17])
        else:
            pendidikan = random.choice([10,11])
            pekerjaan = random.choice([14,15,16,17])

        time.sleep(2)
        if pekerjaan == 13:
            pendapatan = 18
        elif pekerjaan == 14:
            pendapatan = random.choice([18,19])
        elif pekerjaan == 15:
            pendapatan = random.choice([18,19,20,20,20,21,22])
        elif pekerjaan == 16:
            pendapatan = random.choice([20,21,22])
        else:
            pendapatan = 18

        time.sleep(2)
        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        time.sleep(2)
        radiobuttons[usia].click()
        radiobuttons[pendidikan].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[pendapatan].click()
        radiobuttons[usia].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        if car != 0 and motor != 0:
            pil = random.choice([0,1])
            if pil == 0:
                car -= 1
            else:
                motor -= 1
        elif car != 0 and motor == 0:
            pil = 0
            car -= 1
        elif car == 0 and motor != 0:
            pil = 1
            motor -= 1

        radiobuttons[pil].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        s1 = []
        s1.append(random.choice([0,1,2]))
        s1.append(3)
        s1.append(random.choice([5,6,7]))
        s1.append(random.choice([9,10,11]))

        temp = random.randint(1,3)
        look = random.sample([0,1,2], temp)

        time.sleep(2)
        for i in range(4):
            radiobuttons[s1[i]].click()

        for i in look:
            checkboxes[i].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 2
        soal = 16
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

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
            )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/QHp2HzVQp1YLjwYE8")

        index+=1
        print("==================")
        print("car   : " + str(car))
        print("motor : " + str(motor))

        times-=1
        print("")
        print("times : " + str(times))
        print("index : " + str(index))
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