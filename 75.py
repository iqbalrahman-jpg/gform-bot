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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScREEc3rsoG7hHAt48x8nAWjWLSj7fw4qiEEOKb6Yqmo_7ZgQ/viewform?usp=sharing")

nama = [
    "Maya Dara Putri",
    "Rio Fajar Pratama",
    "Dewi Sari Wijaya",
    "Agung Kusuma Jaya",
    "Ratih Suci Lestari",
    "Rizki Pratama Nugraha",
    "Dwi Prasetya Utama",
    "Arif Rahman Hakim",
    "Intan Ayu Lestari",
    "Ananda Dwi Wicaksono",
    "Fira Nur Hidayah",
    "Rama Aditya Wardhana",
    "Cinta Ayu Dewanti",
    "Ade Kurniawan Saputra",
    "Mira Fitriana Wati",
    "Dian Kusuma Wardani",
    "Budi Santoso Putra",
    "Rina Nuraini Sari",
    "Ahmad Fauzi Akbar",
    "Rizky Ananda Pratama",
    "Maya Dewi Sari",
    "Dwi Kusuma Jaya",
    "Agung Santosa Nugroho",
    "Dila Yuliani Wati",
    "Andi Muhammad Rizal",
    "Budi Santoso",
    "Rina Permata Sari",
    "Dian Nugroho",
    "Rudi Setiawan",
    "Maya Putri Lestari",
    "Andi Prasetyo",
    "Sinta Utami Sari",
    "Rizky Ramadhan",
    "Eka Puspita Dewi",
    "Dika Setiawan Pratama",
    "Rani Fitriani",
    "Dito Prasetya",
    "Nisa Indah Sari",
    "Rizal Pratama",
    "Tiara Dewi Puspita",
    "Yanto Wibowo",
    "Nina Anggraini",
    "Yoga Putra Wijaya",
    "Dini Cahyani",
    "Raka Triyana",
    "Maya Dewi Utami",
    "Indra Kusuma",
    "Devi Puspitasari",
    "Bima Aditya Nugraha",
    "Rina Anggraini Sari",
]

telp = [
    "085719303458",
    "085694967112",
    "087771034388",
    "085691005874",
    "081316619265",
    "081807757031",
    "087884291109",
    "087734232521",
    "083831978961",
    "085817281922",
    "085772067944",
    "085780272919",
    "085711503322",
    "083899226851",
    "081296660892",
    "083879828932",
    "085328666691",
    "085716463668",
    "081310967642",
    "089602615268",
    "085740420953",
    "085786378946",
    "089929069068",
    "082299476447",
    "083870192449",
    "087730874992",
    "081381810073",
    "085777737195",
    "081219725497",
    "082310667325",
    "081291723604",
    "089788617285",
    "083876928695",
    "081903140419",
    "085641900173",
    "087749986541",
    "085697561906",
    "089606196660",
    "082221184819",
    "087774894040",
    "089691111149",
    "089781140247",
    "089637520605",
    "081286306638",
    "087887672122",
    "081261351555",
    "085692270650",
    "081284714591",
    "082220406216",
    "081574018719",
]

#0 cowo, 1 cewe
kelamin = [
1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,]

dampak = 0
tdampak = 1

beda = 1
tbeda = 0

transisi = 1
ttransisi = 0

belajar = 1
tbelajar = 0

lingkungan = 1
tlingkungan = 0

putus1 = 1
putus2 = 0
putus3 = 0

membayar1 = 1
membayar2 = 0
membayar3 = 0

times = 1
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if kelamin[index] == 0 :
            kel = 3
        else:
            kel = 2

        time.sleep(2)
        usia = random.choice([4,5,6])

        if usia == 4:
            pendidikan = random.choice([17,18,18,18,19,19])
            if kel == 2:
                pernikahan = random.choice([8,9,9,9])
            else:
                pernikahan = 9
        else:
            pendidikan = random.choice([18,19,20,21])
            pernikahan = random.choice([8,9,9,9])

        keluarga = random.choice([10,11,12,10,11,12,10,11,12,10,11,12,13,14])

        time.sleep(2)
        if pendidikan == 17 :
            if kel == 2 and pernikahan == 8:
                pekerjaan = random.choice([24,24,26,26,27,29])
            else:
                pekerjaan = random.choice([24,24,26,26,27])
        elif pendidikan == 18:
            if kel == 2 and pernikahan == 8:
                pekerjaan = random.choice([24,24,26,25,26,29])
            else:
                pekerjaan = random.choice([24,24,26,26,30])
        elif pendidikan == 19:
            if kel == 2 and pernikahan == 8:
                pekerjaan = random.choice([23,24,24,26,25,26,29,30])
            else:
                pekerjaan = random.choice([23,24,24,26,26,30])
        else :
            if kel == 2 and pernikahan == 8:
                pekerjaan = random.choice([23,24,24,24,26,26,25,26,29,30])
            else:
                pekerjaan = random.choice([23,24,24,24,26,26,26,30])

        time.sleep(2)
        if pekerjaan == 27:
            pendapatan = 32
        elif usia <= 5:
            pendapatan = random.choice([32,33,34,35,36,32,33,34,35,32,33,34,35])
        else:
            pendapatan = random.choice([33,34,35,36,37,38,35,36,37,38,35,36,37,38])

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        time.sleep(2)
        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(telp[index])
        driver.implicitly_wait(4)

        radiobuttons[0].click()
        radiobuttons[kel].click()
        radiobuttons[usia].click()
        radiobuttons[pernikahan].click()
        radiobuttons[keluarga].click()
        radiobuttons[pendidikan].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[pendapatan].click()

        time.sleep(2)
        if dampak != 0 and tdampak != 0:
            pdam = random.choice([0,1])
            if pdam == 0:
                dampak -= 1
            else:
                tdampak -= 1
        elif dampak != 0 and tdampak == 0:
            pdam = 0 
            dampak -= 1
        elif dampak == 0 and tdampak != 0:
            pdam = 1
            tdampak -= 1

        time.sleep(2)
        if beda != 0 and tbeda != 0:
            pbeda = random.choice([0,1])
            if pbeda == 0:
                beda -= 1
            else:
                tbeda -= 1
        elif beda != 0 and tbeda == 0:
            pbeda = 0 
            beda -= 1
        elif beda == 0 and tbeda != 0:
            pbeda = 1 
            tbeda -= 1

        time.sleep(2)
        if transisi != 0 and ttransisi != 0:
            ptran = random.choice([0,1])
            if ptran == 0:
                transisi -= 1
            else:
                ttransisi -= 1
        elif transisi != 0 and ttransisi == 0:
            ptran = 0 
            transisi -= 1
        elif transisi == 0 and ttransisi != 0:
            ptran = 1 
            ttransisi -= 1

        time.sleep(2)
        if belajar != 0 and tbelajar != 0:
            pbel = random.choice([0,1])
            if pbel == 0:
                belajar -= 1
            else:
                tbelajar -= 1
        elif belajar != 0 and tbelajar == 0:
            pbel = 0 
            belajar -= 1
        elif belajar == 0 and tbelajar != 0:
            pbel = 1
            tbelajar -= 1

        time.sleep(2)
        if lingkungan != 0 and tlingkungan != 0:
            pling = random.choice([0,1])
            if pling == 0:
                lingkungan -= 1
            else:
                tlingkungan -= 1
        elif lingkungan != 0 and tlingkungan == 0:
            pling = 0 
            lingkungan -= 1
        elif lingkungan == 0 and tlingkungan != 0:
            pling = 1 
            tlingkungan -= 1

        time.sleep(2)
        if putus1 != 0 and putus2 != 0 and putus3 != 0:
            pputus = random.choice([0,1,2])
            if pputus == 0:
                putus1 -= 1
            elif pputus == 1:
                putus2 -= 1
            else:
                putus3 -= 1
        elif putus1 != 0 and putus2 != 0 and putus3 == 0:
            pputus = random.choice([0,1])
            if pputus == 0:
                putus1 -= 1
            else:
                putus2 -= 1
        elif putus1 != 0 and putus2 == 0 and putus3 != 0:
            pputus = random.choice([0,2])
            if pputus == 0:
                putus1 -= 1
            else:
                putus3 -= 1
        elif putus1 == 0 and putus2 != 0 and putus3 != 0:
            pputus = random.choice([1,2])
            if pputus == 1:
                putus2 -= 1
            else:
                putus3 -= 1
        elif putus1 != 0 and putus2 == 0 and putus3 == 0:
            pputus = 0
            putus1 -= 1
        elif putus1 == 0 and putus2 != 0 and putus3 == 0:
            pputus = 1
            putus2 -= 1
        elif putus1 == 0 and putus2 == 0 and putus3 != 0:
            pputus = 2
            putus3 -= 1

        time.sleep(2)
        if membayar1 != 0 and membayar2 != 0 and membayar3 != 0:
            pbayar = random.choice([0,1,2])
            if pbayar == 0:
                membayar1 -= 1
            elif pbayar == 1:
                membayar2 -= 1
            else:
                membayar3 -= 1
        elif membayar1 != 0 and membayar2 != 0 and membayar3 == 0:
            pbayar = random.choice([0,1])
            if pbayar == 0:
                membayar1 -= 1
            else:
                membayar2 -= 1
        elif membayar1 != 0 and membayar2 == 0 and membayar3 != 0:
            pbayar = random.choice([0,2])
            if pbayar == 0:
                membayar1 -= 1
            else:
                membayar3 -= 1
        elif membayar1 == 0 and membayar2 != 0 and membayar3 != 0:
            pbayar = random.choice([1,2])
            if pbayar == 1:
                membayar2 -= 1
            else:
                membayar3 -= 1
        elif membayar1 != 0 and membayar2 == 0 and membayar3 == 0:
            pbayar = 0
            membayar1 -= 1
        elif membayar1 == 0 and membayar2 != 0 and membayar3 == 0:
            pbayar = 1
            membayar2 -= 1
        elif membayar1 == 0 and membayar2 == 0 and membayar3 != 0:
            pbayar = 2
            membayar3 -= 1


        time.sleep(2)
        if pdam == 0:
            radiobuttons[40].click()
            radiobuttons[42].click()
            radiobuttons[44].click()
            radiobuttons[46].click()
        else:
            radiobuttons[41].click()
            radiobuttons[43].click()
            radiobuttons[45].click()
            radiobuttons[47].click()

        time.sleep(2)
        if pbeda == 0:
            radiobuttons[48].click()
        else:
            radiobuttons[49].click()

        time.sleep(2)
        if ptran == 0:
            radiobuttons[random.choice([50,51])].click()
            radiobuttons[52].click()
            radiobuttons[54].click()
        else:
            radiobuttons[50].click()
            radiobuttons[53].click()
            radiobuttons[55].click()

        time.sleep(2)
        if pbel == 0:
            radiobuttons[56].click()
        else:
            radiobuttons[57].click()

        time.sleep(2)
        if pling == 0:
            radiobuttons[58].click()
        else:
            radiobuttons[59].click()

        time.sleep(2)
        informasi = random.choice([62,64,61,61,61,61,66,66,66,66])
        radiobuttons[informasi].click()

        time.sleep(2)
        if pputus == 0:
            radiobuttons[68].click()
        elif pputus == 1:
            radiobuttons[69].click()
        else:
            radiobuttons[70].click()

        time.sleep(2)
        if pbayar == 0:
            s1 = random.choice([76,77])

            radiobuttons[72].click()
            radiobuttons[74].click()
            radiobuttons[s1].click()
            if s1 == 77:
                radiobuttons[random.choice([78,78,78,79,80])]

            radiobuttons[random.choice([82,82,83])].click()
            radiobuttons[84].click()
            radiobuttons[88].click()
            radiobuttons[91].click()
            radiobuttons[94].click()
        elif pbayar == 1:
            s1 = random.choice([76,76,76,77])

            radiobuttons[72].click()
            radiobuttons[74].click()
            radiobuttons[s1].click()
            if s1 == 77:
                radiobuttons[random.choice([78,79,80])]

            radiobuttons[82].click()
            radiobuttons[85].click()
            radiobuttons[89].click()
            radiobuttons[92].click()
            radiobuttons[95].click()
        else:
            s1 = random.choice([76,76,76,77])

            radiobuttons[72].click()
            radiobuttons[74].click()
            radiobuttons[s1].click()
            if s1 == 77:
                radiobuttons[random.choice([78,79,80])]

            radiobuttons[82].click()
            radiobuttons[86].click()
            radiobuttons[90].click()
            radiobuttons[93].click()
            radiobuttons[96].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScREEc3rsoG7hHAt48x8nAWjWLSj7fw4qiEEOKb6Yqmo_7ZgQ/viewform?usp=sharing")

        index+=1
        print("==================")
        print("dampak  : " + str(dampak))
        print("tdampak : " + str(tdampak))
        print("")
        print("beda : " + str(beda))
        print("tbeda : " + str(tbeda))
        print("")
        print("transisi  : " + str(transisi))
        print("ttransisi : " + str(ttransisi))
        print("")
        print("belajar  : " + str(belajar))
        print("tbelajar : " + str(tbelajar))
        print("")
        print("lingkungan  : " + str(lingkungan))
        print("tlingkungan : " + str(tlingkungan))
        print("")
        print("putus1 : " + str(putus1))
        print("putus2 : " + str(putus2))
        print("putus3 : " + str(putus3))
        print("")
        print("membayar1 : " + str(membayar1))
        print("membayar2 : " + str(membayar2))
        print("membayar3 : " + str(membayar3))
        print("")

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