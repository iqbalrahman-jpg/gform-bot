from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://forms.gle/WC7fu5uBXoudoUGF7")


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
]

#laki 0 perempuan 1
kelamin = [1,0,1,0,0,1,0,1,1,0,]

times = 5
index = 5



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
        p = 0
        radiobuttons[p].click()
        radiobuttons[p+2].click()
        radiobuttons[p+4].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
        
        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(nama[index])
        radiobuttons[kelamin[index]].click()
        umur = random.choice([2,3,4,5])
        radiobuttons[umur].click()
        if umur <3:
            pendidikan = 6
            pekerjaan = random.choice([9,9,9,9,11,12])
        else:
            pendidikan = random.choice([7,8,8,8])
            pekerjaan = random.choice([10,11,12])
        
        radiobuttons[pendidikan].click()
        radiobuttons[pekerjaan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        p = 0
        soal = 3
        while soal:
            jawab = random.choice([p,p+1,p,p+1,p+2,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 15
        indikator = random.choice([1,2])
        if indikator == 1:
            soal = 3
            while soal:
                jawab = random.choice([p,p+1])
                testcheck[jawab].click()
                soal -= 1
                p += 5
        else:
            soal = 3
            while soal:
                jawab = random.choice([p+2,p+3,p+4,p+3,p+4])
                testcheck[jawab].click()
                soal -= 1
                p += 5
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        p = 0
        soal = 5
        while soal:
            jawab = random.choice([p+2,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        p = 0
        soal = 4
        while soal:
            jawab = random.choice([p+1,p+1,p+2,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/WC7fu5uBXoudoUGF7")

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