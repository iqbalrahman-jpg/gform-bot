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
driver.get("https://forms.gle/PDeQqcKmPK1YDnLj7")

email = [
    "muhh.santosoo@gmail.com",
    "rinapermatasari@gmail.com",

]

nama = [
    "M. Putra Susanto",
    "Rina Permata Sari",
]

alamat = [
    "Cimahi",
    "Ciparay",
    "Cimahi",
    "Cibiru Hilir",
    "Lembang",
    "Cibiru Hilir",
    "Dayeuhkolot",
]

telp = [
    "081261234611",
    "081280285159",
]
#0 laki 1 perempuan
kelamin = [0,1,]

times = 1
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(email[index])

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        usia = random.choice([2,2,3,3,3,3,3,4,4,4,5,6])

        if usia == 2:
            pekerjaan = 7
            pendidikan = random.choice([13,14])
            pendapatan = 19
        elif usia == 3:
            pekerjaan = random.choice([7,7,7,7,8,9,10])
            pendidikan = random.choice([14,15,16,17])
            pendapatan = random.choice([19,20,21])
        else:
            pekerjaan = random.choice([8,9,9,10])
            pendidikan = random.choice([14,15,16,17])
            pendapatan = random.choice([19,20,21,21,21])

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        textboxes[1].send_keys(nama[index])
        textboxes[2].send_keys(telp[index])
        driver.implicitly_wait(4)
        textarea[0].send_keys(alamat[index])
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        radiobuttons[usia].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[pendidikan].click()
        radiobuttons[pendapatan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox 

        time.sleep(2)
        radiobuttons[0].click()
        mengenal = random.randint(0,6)
        sering = random.randint(9,11)

        temp = random.randint(1,5)
        random_item = random.sample([0,1,2,3,4], temp)

        time.sleep(2)
        radiobuttons[mengenal].click()
        radiobuttons[sering].click()
        driver.implicitly_wait(4)

        for i in random_item :
           checkboxes[i].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 19
        while soal :
            s1 = random.choice([p,p+1,p+2,p+3,p+3,p+4,p+4,p+2,p+3,p+3,p+4,p+4])
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

        p = 0
        soal = 19
        while soal :
            s1 = random.choice([p,p+1,p+2,p+3,p+3,p+4,p+4,p+2,p+3,p+3,p+4,p+4])
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

        time.sleep(40)

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/PDeQqcKmPK1YDnLj7")

        index+=1
        print("==================")
        print("index : " + str(index))
        # print("")

        times-=1
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