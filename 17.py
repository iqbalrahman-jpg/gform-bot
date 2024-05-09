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
driver.get("http://tinyurl.com/flowstatescaleINA")

nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Bagas Marsha",
    "Yudi Pradanawan",
    "Yulianto Nasution",
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
    "Azzarin Rizki Maulana",
    "Fabian Nadeo Putra",
    "Nis Eko Martahu",
    "Bayu Dwiganara",
    "Radan Syirahano",
]

#0 laki, 1 perempuan
kelamin = [1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,]

times = 26
index = 0

usia20 = 20
usialain = 6

atlet = 13
atletLain = 13

tahun7 = 13
tahun5 = 8
tahun10 = 2
tahun1 = 3

kota = 13
provinsi = 8
nasional = 3
internasional = 1
belump = 1

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        time.sleep(2)
        radiobuttons[kelamin[index]].click()

        if usia20 != 0 and usialain != 0 :
            time.sleep(2)
            pilih = random.choice([1,2])
            if pilih == 1:
                umur = random.randint(20,30)
                textboxes[1].send_keys(umur)
                usia20 -= 1
            else :
                umur = random.choice([15,16,17,18,19,31,32,33,34,35,36,37,38,39,40])
                textboxes[1].send_keys(umur)
                usialain -= 1
        elif usia20 != 0 and usialain == 0 :
            time.sleep(2)
            umur = random.randint(20,30)
            textboxes[1].send_keys(umur)
            usia20 -= 1
        elif usia20 == 0 and usialain != 0 :
            time.sleep(2)
            umur = random.choice([15,16,17,18,19,31,32,33,34,35,36,37,38,39,40])
            textboxes[1].send_keys(umur)
            usialain -= 1

        if atlet != 0 and atletLain != 0 :
            time.sleep(2)
            s1 = random.choice([2,3,4,5])
            radiobuttons[s1].click()
            if s1 == 2:
                atlet -= 1
            else :
                atletLain -= 1
        elif atlet != 0 and atletLain == 0 :
            radiobuttons[2].click()
            atlet -= 1
        elif atlet == 0 and atletLain != 0 :
            s1 = random.choice([3,4,5])
            radiobuttons[s1].click()
            atletLain -= 1

        tekun = random.choice([7,7,8,8,9])
        radiobuttons[tekun].click()

        if umur < 20 and tahun1 != 0 and tahun5 != 0 :
            time.sleep(2)
            lama = random.choice([10,11,12,13])
            radiobuttons[lama].click()
            if lama == 13 :
                tahun5 -= 1
            else :
                tahun1 -= 1
        elif umur < 20 and tahun1 != 0 and tahun5 == 0 :
            time.sleep(2)
            lama = random.choice([10,11,12])
            radiobuttons[lama].click()
            tahun1 -= 1
        elif umur < 20 and tahun1 == 0 and tahun5 != 0 :
            time.sleep(2)
            radiobuttons[13].click()
            tahun5 -= 1
        elif umur < 20 and tahun1 == 0 and tahun5 == 0:
            if tahun5 != 0 and tahun7 != 0 and tahun10 != 0:
                time.sleep(2)
                lama = random.choice([13,14,15])
                radiobuttons[lama].click()
                if lama == 13:
                    tahun5 -= 1
                elif lama == 14:
                    tahun7 -= 1
                else :
                    tahun10 -= 1
            elif tahun5 != 0 and tahun7 != 0 and tahun10 == 0:
                time.sleep(2)
                lama = random.choice([13,14])
                radiobuttons[lama].click()
                if lama == 13:
                    tahun5 -= 1
                else :
                    tahun7 -= 1
            elif tahun5 != 0 and tahun7 == 0 and tahun10 != 0:
                time.sleep(2)
                lama = random.choice([13,15])
                radiobuttons[lama].click()
                if lama == 13:
                    tahun5 -= 1
                else :
                    tahun10 -= 1
            elif tahun5 != 0 and tahun7 == 0 and tahun10 == 0:
                time.sleep(2)
                radiobuttons[13].click()
                tahun5 -= 1
            elif tahun5 == 0 and tahun7 != 0 and tahun10 == 0:
                time.sleep(2)
                radiobuttons[14].click()
                tahun7 -= 1
            elif tahun5 == 0 and tahun7 == 0 and tahun10 != 0:
                time.sleep(2)
                radiobuttons[15].click()
                tahun10 -= 1
            elif tahun5 == 0 and tahun7 != 0 and tahun10 != 0:
                time.sleep(2)
                lama = random.choice([14,15])
                radiobuttons[lama].click()
                if lama == 14:
                    tahun7 -= 1
                else :
                    tahun10 -= 1
        elif umur >= 20 and tahun5 != 0 and tahun7 != 0 and tahun10 != 0:
            time.sleep(2)
            lama = random.choice([13,14,15])
            radiobuttons[lama].click()
            if lama == 13:
                tahun5 -= 1
            elif lama == 14:
                tahun7 -= 1
            else :
                tahun10 -= 1
        elif umur >= 20 and tahun5 != 0 and tahun7 != 0 and tahun10 == 0:
            time.sleep(2)
            lama = random.choice([13,14])
            radiobuttons[lama].click()
            if lama == 13:
                tahun5 -= 1
            else :
                tahun7 -= 1
        elif umur >= 20 and tahun5 != 0 and tahun7 == 0 and tahun10 != 0:
            time.sleep(2)
            lama = random.choice([13,15])
            radiobuttons[lama].click()
            if lama == 13:
                tahun5 -= 1
            else :
                tahun10 -= 1
        elif umur >= 20 and tahun5 != 0 and tahun7 == 0 and tahun10 == 0:
            time.sleep(2)
            radiobuttons[13].click()
            tahun5 -= 1
        elif umur >= 20 and tahun5 == 0 and tahun7 != 0 and tahun10 == 0:
            time.sleep(2)
            radiobuttons[14].click()
            tahun7 -= 1
        elif umur >= 20 and tahun5 == 0 and tahun7 == 0 and tahun10 != 0:
            time.sleep(2)
            radiobuttons[15].click()
            tahun10 -= 1
        elif umur >= 20 and tahun5 == 0 and tahun7 != 0 and tahun10 != 0:
            time.sleep(2)
            lama = random.choice([14,15])
            radiobuttons[lama].click()
            if lama == 14:
                tahun7 -= 1
            else :
                tahun10 -= 1
        elif umur >= 20 and tahun5 == 0 and tahun7 == 0 and tahun10 == 0:
            time.sleep(2)
            lama = random.choice([10,11,12])
            radiobuttons[lama].click()
            tahun1 -= 1

        hari = random.randint(16,23)
        radiobuttons[hari].click()

        if kota != 0 and provinsi !=0 and nasional != 0 and internasional != 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([24,25,26,27,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi !=0 and nasional != 0 and internasional != 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([24,25,26,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            else :
                kota -= 1
        elif kota != 0 and provinsi !=0 and nasional != 0 and internasional == 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([25,26,27,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi !=0 and nasional == 0 and internasional != 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([24,26,27,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional != 0 and internasional != 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([24,25,27,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi !=0 and nasional != 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([25,26,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi !=0 and nasional == 0 and internasional != 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([24,26,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional != 0 and internasional != 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([24,25,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional != 0 and internasional != 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([24,25,26])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi !=0 and nasional == 0 and internasional == 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([26,27,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional != 0 and internasional == 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([25,27,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional != 0 and internasional == 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([25,26,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional == 0 and internasional != 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([24,27,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional == 0 and internasional != 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([24,26,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi ==0 and nasional != 0 and internasional != 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([24,25,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi !=0 and nasional == 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([26,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional != 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([25,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional != 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([25,26])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi !=0 and nasional == 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([26,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional != 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([25,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional != 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([25,26])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional == 0 and internasional != 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([24,27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional == 0 and internasional != 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([24,26])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi ==0 and nasional != 0 and internasional != 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([24,25])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional == 0 and internasional == 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([27,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional == 0 and internasional == 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([26,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi ==0 and nasional != 0 and internasional == 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([25,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi ==0 and nasional == 0 and internasional != 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([24,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota != 0 and provinsi ==0 and nasional == 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([27])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional == 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([26])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi ==0 and nasional != 0 and internasional == 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([25])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi ==0 and nasional == 0 and internasional != 0 and belump ==0:
            time.sleep(2)
            kompeteni = random.choice([24])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi ==0 and nasional == 0 and internasional == 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1
        elif kota == 0 and provinsi !=0 and nasional != 0 and internasional != 0 and belump !=0:
            time.sleep(2)
            kompeteni = random.choice([24,25,26,28])
            radiobuttons[kompeteni].click()
            if kompeteni == 24:
                internasional -= 1
            elif kompeteni == 25:
                nasional -= 1
            elif kompeteni == 26:
                provinsi -= 1
            elif kompeteni == 27:
                kota -= 1
            else :
                belump -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p1 = 2
        soal = 36
        while soal:
            s1 = random.choice([p1,p1+1,p1+2,p1+1,p1+2,p1+1,p1+2])
            testcheck[s1].click()
            soal -= 1
            p1 += 5


        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("http://tinyurl.com/flowstatescaleINA")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("usia20 : " + str(usia20))
        print("usialain : " + str(usialain))
        print("atlet : " + str(atlet))
        print("atletLain : " + str(atletLain))
        print("tahun7 : " + str(tahun7))
        print("tahun5 : " + str(tahun5))
        print("tahun10 : " + str(tahun10))
        print("tahun1 : " + str(tahun1))
        print("kota : " + str(kota))
        print("provinsi : " + str(provinsi))
        print("nasional : " + str(nasional))
        print("internasional : " + str(internasional))
        print("belump : " + str(belump))

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