from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://forms.gle/FJupEdTzgyCBY4cJ8")

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
]

domisili = [
    "Jawa Timur",
    "Jawa tengah",
    "Jawa timur",
    "DKI Jakarta",
    "jawa timur",
    "DKI Jakarta",
    "Jawa barat",
    "Jawa Barat",
    "Bali",
    "Jawa Timur",
    "jawa tengah",
    "Jawa Timur",
    "Jawa Timur",
    "DKI Jakarta",
    "Yogyakarta"
]

kelamin = [8,7,8,7,7,8,7,8,8,7,8,7,8,7,8]

times = 12
index = 3

temp1 = 7
temp2 = 1
temp3 = 2
try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0
        if temp1 != 0 and temp2 != 0 and temp3 != 0 :
            template = random.choice([1,2,3])
        elif temp1 != 0 and temp2 != 0 and temp3 == 0 :
            template = random.choice([1,2])
        elif temp1 != 0 and temp2 == 0 and temp3 != 0 :
            template = random.choice([1,3])
        elif temp1 != 0 and temp2 == 0 and temp3 == 0 :
            template = random.choice([1])
        elif temp1 == 0 and temp2 != 0 and temp3 != 0 :
            template = random.choice([2,3])
        elif temp1 == 0 and temp2 != 0 and temp3 == 0 :
            template = random.choice([2])
        elif temp1 == 0 and temp2 == 0 and temp3 != 0 :
            template = random.choice([3])

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        
        radiobuttons[0].click()

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        usia = random.choice([0,1,2,3,4,5,6])
        radiobuttons[usia].click()
        textboxes[1].send_keys(domisili[index])
        radiobuttons[kelamin[index]].click()

        if template == 1:
            time.sleep(2)
            lama = random.choice([10,11,12,13])
            radiobuttons[lama].click()
            anggaran = random.choice([16,16,16,17,17,17,18])
            radiobuttons[anggaran].click()
        elif template == 2:
            time.sleep(2)
            lama = random.choice([10,11])
            radiobuttons[lama].click()
            anggaran = random.choice([14,15,16])
            radiobuttons[anggaran].click()
        elif template == 3:
            time.sleep(2)
            radiobuttons[9].click()
            anggaran = random.choice([14,15])
            radiobuttons[anggaran].click()

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        #soal
        time.sleep(5)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if template == 1 :
            temp1 -= 1
            s1 = random.choice([2,3,4])
            testcheck[s1].click()
            s1 = random.choice([7,8,9])
            testcheck[s1].click()
            s1 = random.choice([12,13,14])
            testcheck[s1].click()
            s1 = random.choice([15,16,17,18,19])
            testcheck[s1].click()
            s1 = random.choice([20,20,20,21,21,21,22,23,24])
            testcheck[s1].click()
            s1 = random.choice([25,26,27,28,28,28,29,29,29])
            testcheck[s1].click()
            p1 = 32
            soal = 9
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1 

            s1 = random.choice([78,79])
            testcheck[s1].click()
            s1 = random.choice([83,84])
            testcheck[s1].click()
            s1 = random.choice([87,88,89])
            testcheck[s1].click()
            s1 = random.choice([90,91,92,93,94])
            testcheck[s1].click()
            s1 = random.choice([98,99])
            testcheck[s1].click()
            s1 = random.choice([103,104])
            testcheck[s1].click()
            s1 = random.choice([107,108,109])
            testcheck[s1].click()
            s1 = random.choice([110,111])
            testcheck[s1].click()

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(5)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            s1 = random.choice([0,1,2,3,3,3,4,4,4])
            testcheck[s1].click()
            p1 = 7
            soal = 5
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s1 = random.choice([30,31])
            testcheck[s1].click()
            s1 = random.choice([37,38,39])
            testcheck[s1].click()
            s1 = random.choice([43,44])
            testcheck[s1].click()
            s1 = random.choice([47,48,49])
            testcheck[s1].click()
            s1 = random.choice([53,54])
            testcheck[s1].click()
            s1 = random.choice([57,58,59])
            testcheck[s1].click()
            p1 = 63
            soal = 3
            while soal :
                s1 = random.choice([p1,p1+1])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s1 = random.choice([77,78,79])
            testcheck[s1].click()
            p1 = 83
            soal = 3
            while soal :
                s1 = random.choice([p1,p1+1])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s1 = random.choice([97,98,99])
            testcheck[s1].click()
            p1 = 102
            soal = 2
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s1 = random.choice([110,111,112,113,114])
            testcheck[s1].click()
            s1 = random.choice([118,119])
            testcheck[s1].click()
            s1 = random.choice([123,124])
            testcheck[s1].click()
            s1 = random.choice([125,126,127,128,129])
            testcheck[s1].click()
            s1 = random.choice([133,134])
            testcheck[s1].click()
            s1 = random.choice([137,138,139])
            testcheck[s1].click()
            s1 = random.choice([141,142,143,144])
            testcheck[s1].click()
            s1 = random.choice([148,149])
            testcheck[s1].click()

        elif template == 2 :
            temp2 -= 1
            s2 = random.choice([2,3,4])
            testcheck[s2].click()
            s2 = random.choice([7,8,9])
            testcheck[s2].click()
            s2 = random.choice([10,11,12,13,13,13,14,14,14])
            testcheck[s2].click()
            s2 = random.choice([15,16,17,18,19])
            testcheck[s2].click()
            s2 = random.choice([20,21,22,23,24])
            testcheck[s2].click()
            s2 = random.choice([25,26,27,28,28,28,29,29,29])
            testcheck[s2].click()
            s2 = random.choice([33,34])
            testcheck[s2].click()
            s2 = random.choice([35,36,37,38,39])
            testcheck[s2].click()
            s2 = random.choice([40,41,42,43])
            testcheck[s2].click()
            s2 = random.choice([45,46,47])
            testcheck[s2].click()
            s2 = random.choice([50,51,52,53,54])
            testcheck[s2].click()
            s2 = random.choice([55,56,57,58,59])
            testcheck[s2].click()
            s2 = random.choice([60,61,62,63,64,64,64])
            testcheck[s2].click()
            p1 = 67
            soal = 4
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s2 = random.choice([85,86,87])
            testcheck[s2].click()
            s2 = random.choice([90,91,92,93,94])
            testcheck[s2].click()
            s2 = random.choice([97,98,99])
            testcheck[s2].click()
            s2 = random.choice([102,103,104])
            testcheck[s2].click()
            s2 = random.choice([105,106,107,108,109])
            testcheck[s2].click()
            s2 = random.choice([112,113,114])
            testcheck[s2].click()

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(5)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            s2 = random.choice([0,1,2])
            testcheck[s2].click()
            s2 = random.choice([5,6,7,8,9])
            testcheck[s2].click()
            s2 = random.choice([10,11,12,13,14])
            testcheck[s2].click()
            p1 = 17
            soal = 3
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s2 = random.choice([30,31,32])
            testcheck[s2].click()
            s2 = random.choice([37,38,39])
            testcheck[s2].click()
            s2 = random.choice([43,44])
            testcheck[s2].click()
            p1 = 47
            soal = 4
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s2 = random.choice([68,69])
            testcheck[s2].click()
            s2 = random.choice([73,74])
            testcheck[s2].click()
            s2 = random.choice([77,78,79])
            testcheck[s2].click()
            s2 = random.choice([82,83,84])
            testcheck[s2].click()
            s2 = random.choice([86,87,88,89])
            testcheck[s2].click()
            p1 = 92
            soal = 4
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s2 = random.choice([110,111,112,113,114])
            testcheck[s2].click()
            s2 = random.choice([117,118,119])
            testcheck[s2].click()
            s2 = random.choice([122,123,124])
            testcheck[s2].click()
            s2 = random.choice([125,126,127])
            testcheck[s2].click()
            s2 = random.choice([133,134])
            testcheck[s2].click()
            s2 = random.choice([137,138,139])
            testcheck[s2].click()
            s2 = random.choice([141,142,143,144])
            testcheck[s2].click()
            s2 = random.choice([147,148,149])
            testcheck[s2].click()

        elif template == 3 :
            temp3 -= 1
            s3 = random.choice([2,3,4])
            testcheck[s3].click()
            s3 = random.choice([7,8,9])
            testcheck[s3].click()
            s3 = random.choice([10,11,12])
            testcheck[s3].click()
            s3 = random.choice([15,16,17,18,19])
            testcheck[s3].click()
            s3 = random.choice([20,21,22,23,24])
            testcheck[s3].click()
            s3 = random.choice([25,26,27])
            testcheck[s3].click()
            s3 = random.choice([30,31,32])
            testcheck[s3].click()
            s3 = random.choice([35,36])
            testcheck[s3].click()
            s3 = random.choice([40,41,42])
            testcheck[s3].click()
            s3 = random.choice([45,46])
            testcheck[s3].click()
            s3 = random.choice([50,51])
            testcheck[s3].click()
            p1 = 55
            soal = 5
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s3 = random.choice([80,81])
            testcheck[s3].click()
            s3 = random.choice([85,86])
            testcheck[s3].click()

            s3 = random.choice([90,91,92,93,94])
            testcheck[s3].click()

            s3 = random.choice([95,96,97])
            testcheck[s3].click()
            s3 = random.choice([100,101,102])
            testcheck[s3].click()
            s3 = random.choice([105,106,107,108,109])
            testcheck[s3].click()
            s3 = random.choice([112,113,114])
            testcheck[s3].click()

            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(5)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            s3 = random.choice([0,1,2])
            testcheck[s3].click()
            s3 = random.choice([5,6,7,8,9])
            testcheck[s3].click()
            s3 = random.choice([10,11,12,13,14])
            testcheck[s3].click()
            b1 = random.choice([15,16,17,18,19])
            testcheck[b1].click()
            s3 = random.choice([21,22,23,23,23,24,24,24])
            testcheck[s3].click()
            s3 = random.choice([25,25,25,26,26,26,27,28,29])
            testcheck[s3].click()
            if b1 == 15 or b1 == 16 :
                s3 = random.choice([33,34])
                testcheck[s3].click()
            elif b1 == 18 or b1 == 19 :
                s3 = random.choice([30,31])
                testcheck[s3].click()
            else : 
                s3 = random.choice([30,31,32,33,34])
                testcheck[s3].click()

            s3 = random.choice([35,36,37])
            testcheck[s3].click()
            b2 = random.choice([40,41,42,43,44])
            testcheck[b2].click()
            if b2 == 40 or b2 == 41:
                s3 = random.choice([45,46])
                testcheck[s3].click()
            elif b2 == 43 or b2 == 44:
                s3 = random.choice([48,49])
                testcheck[s3].click()
            else:
                s3 = random.choice([45,46,47,48,49])
                testcheck[s3].click()

            s3 = random.choice([50,51,52,53,54])
            testcheck[s3].click()
            p1 = 57
            soal = 1
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s3 = random.choice([60,61,62,63,64])
            testcheck[s3].click()
            p1 = 66
            soal = 2
            while soal :
                s1 = random.choice([p1,p1+1,p1+2,p1+2,p1+3])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s3 = random.choice([76,77,78,78,79])
            testcheck[s3].click()
            p1 = 80
            soal = 3
            while soal :
                s1 = random.choice([p1,p1+1,p1+2])
                testcheck[s1].click()
                p1 += 5
                soal -= 1

            s3 = random.choice([95,96,97,98])
            testcheck[s3].click()
            s3 = random.choice([102,103,104])
            testcheck[s3].click()
            s3 = random.choice([105,106,107,108,109])
            testcheck[s3].click()
            s3 = random.choice([110,111,112,113,114])
            testcheck[s3].click()
            s3 = random.choice([115,116,117])
            testcheck[s3].click()
            s3 = random.choice([120,121])
            testcheck[s3].click()
            s3 = random.choice([127,128,129])
            testcheck[s3].click()
            s3 = random.choice([130,131,132])
            testcheck[s3].click()
            s3 = random.choice([135,136])
            testcheck[s3].click()
            s3 = random.choice([140,142])
            testcheck[s3].click()
            s3 = random.choice([145,146,147])
            testcheck[s3].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/FJupEdTzgyCBY4cJ8")

        print("==================")
        print("index : " + str(index))
        print("template : " + str(template))
        print("temp1 :" + str(temp1))
        print("temp2 :" + str(temp2))
        print("temp3 :" + str(temp3))
        print("times :" + str(times))
        index+=1
        times-=1
finally:
	# driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox