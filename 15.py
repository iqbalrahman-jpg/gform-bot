from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# driver = webdriver.Firefox()
driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://forms.gle/NQ7r5gbiSUXCzQrK8")

nama = [
    "Yahya Nugraha",
    "Putra Agung Dewantoro",
    "Nanda Bagas Kurniawan",
    "Yudi Pradanawan",
    "Yuli Putra Senopati",
    "Bayu Danang Merta",
        "Bellanda Clara Ayunda", 
]

email = [
    "yahyanugraha87@gmail.com",
    "putradewantoro90@yahoo.com",
    "nandakurniawan91@hotmail.com",
    "yudipradana22@outlook.com",
    "yulisenopati77@gmail.com",
    "bayudanangmerta99@protonmail.com",
    "bellaclaraayunda@gmail.com",
]

kelamin = [0,0,0,0,0,0,1]

times = 7
index = 0


try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(email[index])

        radiobuttons[kelamin[index]].click()

        if kelamin[index] == 1:
            time.sleep(2)
            usia = random.choice([2,3,4,5])
            radiobuttons[usia].click()
            if usia == 2:
                time.sleep(2)
                pendidikan = random.choice([7,8,9,10])
                radiobuttons[pendidikan].click()
            else:
                time.sleep(2)
                pendidikan = random.choice([8,9,10,11])
                radiobuttons[pendidikan].click()
        else:
            time.sleep(2)
            usia = random.choice([3,4,5])
            radiobuttons[usia].click()
            pendidikan = random.choice([8,9,10])
            radiobuttons[pendidikan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        soal = 4
        while soal:
            s1 = random.choice([p1+1,p1+2,p1+3,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4,p1+4])
            testcheck[s1].click()
            soal -= 1
            p1 += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        soal = 8
        while soal:
            s1 = random.choice([p1+1,p1+2,p1+3,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4,p1+4])
            testcheck[s1].click()
            soal -= 1
            p1 += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        soal = 3
        while soal:
            s1 = random.choice([p1+1,p1+2,p1+3,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4,p1+4])
            testcheck[s1].click()
            soal -= 1
            p1 += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 0
        soal = 3
        while soal:
            s1 = random.choice([p1+1,p1+2,p1+3,p1+3,p1+3,p1+3,p1+4,p1+4,p1+4,p1+4])
            testcheck[s1].click()
            soal -= 1
            p1 += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/NQ7r5gbiSUXCzQrK8")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        print("times : " + str(times))
finally:
	# driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()