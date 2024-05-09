from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfNEVVu8MF9LzTdTLyWzD7zICZerhVYYQFUmaNAUCQqfwkCwQ/viewform?usp=sf_link")

times = 14
index = 29

s = 7
ss = 7
try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if s != 0 and ss != 0:
            arah = random.choice([3,4])
            if arah == 3:
                s -= 1
            else :
                ss -= 1
        elif s != 0 and ss == 0:
            arah = 3
            s -= 1
        elif s == 0 and ss != 0:
            arah = 4
            ss -= 1
        
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        radiobuttons[0].click()
        banyak = random.choice([1,2,3,4])

        random_item = random.sample([0,1,2,3], banyak)
        
        for i in random_item :
           checkboxes[i].click()

        kali = random.choice([2,3,4])
        radiobuttons[kali].click()

        kali = random.choice([6,7,8,9])
        radiobuttons[kali].click()

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        gender = random.choice([0,1])
        radiobuttons[gender].click()
        usia = random.choice([2,3,4,5,6])
        radiobuttons[usia].click()

        if gender == 0:
            time.sleep(2)

            if usia == 2:
                time.sleep(2)
                radiobuttons[7].click()
                radiobuttons[12].click()
            elif usia == 3 or usia == 4:
                time.sleep(2)
                pekerjaan = random.choice([7,9,10])
                radiobuttons[pekerjaan].click()
                penghasilan = random.choice([13,14,15])
                radiobuttons[penghasilan].click()
            elif usia == 5 or usia == 6:
                time.sleep(2)
                pekerjaan = random.choice([9,10])
                radiobuttons[pekerjaan].click()
                penghasilan = random.choice([14,15])
                radiobuttons[penghasilan].click()

        else :
            time.sleep(2)

            if usia == 2:
                time.sleep(2)
                radiobuttons[7].click()
                radiobuttons[12].click()
            elif usia == 3 or usia == 4:
                time.sleep(2)
                pekerjaan = random.choice([7,8,9,10])
                radiobuttons[pekerjaan].click()
                penghasilan = random.choice([13,14,15])
                radiobuttons[penghasilan].click()
            elif usia == 5 or usia == 6:
                time.sleep(2)
                pekerjaan = random.choice([8,9,10])
                radiobuttons[pekerjaan].click()
                penghasilan = random.choice([14,15])
                radiobuttons[penghasilan].click()
        

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = arah
        soal = 4
        while soal:
            testcheck[p1].click()
            p1 += 5
            soal -= 1

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = arah
        soal = 3
        while soal:
            testcheck[p1].click()
            p1 += 5
            soal -= 1

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = arah
        soal = 3
        while soal:
            testcheck[p1].click()
            p1 += 5
            soal -= 1

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = arah
        soal = 7
        while soal:
            testcheck[p1].click()
            p1 += 5
            soal -= 1

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = arah
        soal = 4
        while soal:
            testcheck[p1].click()
            p1 += 5
            soal -= 1

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = arah
        soal = 5
        while soal:
            testcheck[p1].click()
            p1 += 5
            soal -= 1


        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfNEVVu8MF9LzTdTLyWzD7zICZerhVYYQFUmaNAUCQqfwkCwQ/viewform?usp=sf_link")

        print("==================")
        print("index : " + str(index))
        print("s : " + str(s))
        print("ss : " + str(ss))

        index+=1
        times-=1
finally:
	# driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox