from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfFwC8wFE4L2iDrcENq91kbckPfTsgmKWPvdCbyna0yFCBNWw/viewform?usp=sf_link")

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
]

#1 laki, 0 perempuan
kelamin = [0,1,0,1,0,1,1,1,0,1,0,1,0,1,0]

telp = [
    "081465440213",
    "082626799993",
    "0892070442682",
    "081435537182",
    "082653326205",
    "081925969337",
    "089545039679",
    "088159431341",
    "081245784308",
    "081861512349",
    "081329475162",
    "083181803382",
    "085729213971",
    "081780590311",
    "081720592823",
]

times = 15
index = 0

baik = 10
jelek = 5

sering = 8
jarang = 7

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
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        usia = random.choice([2,3,4,5,6,7])
        domisili = random.choice([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
        medsos = random.choice([31,32,33,34,35])
        alasan = random.choice([36,37,38,39,40])

        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(4)
        radiobuttons[kelamin[index]].click()
        radiobuttons[usia].click()
        radiobuttons[domisili].click()
        radiobuttons[medsos].click()
        radiobuttons[alasan].click()
        driver.implicitly_wait(4)
        textboxes[1].send_keys(telp[index])
        driver.implicitly_wait(4)
        checkboxes[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if baik != 0 and jelek != 0:
            time.sleep(2)
            p = random.choice([1,2])
            if p == 1:
                s1 = random.choice([2,3,4])
                s2 = random.choice([0,1,2])
                s2 += 5
                s3 = random.choice([0,1,2])
                s3 += 10
                s4 = random.choice([0,1,2])
                s4 += 15
                s5 = random.choice([1,2,3,4])
                s5 += 20
                s6 = random.choice([0,1,2])
                s6 += 25
                s7 = random.choice([2,3,4])
                s7 += 30
                s8 = random.choice([0,1,2])
                s8 += 35
                s9 = random.choice([0,1,2])
                s9 += 40
                testcheck[s1].click()
                testcheck[s2].click()
                testcheck[s3].click()
                testcheck[s4].click()
                testcheck[s5].click()
                testcheck[s6].click()
                testcheck[s7].click()
                testcheck[s8].click()
                testcheck[s9].click()
                temp = 0
                baik -= 1
            else:
                time.sleep(2)
                s1 = random.choice([0,1,2])
                s2 = random.choice([2,3,4])
                s2 += 5
                s3 = random.choice([2,3,4])
                s3 += 10
                s4 = random.choice([2,3,4])
                s4 += 15
                s5 = random.choice([0,1,2,3])
                s5 += 20
                s6 = random.choice([2,3,4])
                s6 += 25
                s7 = random.choice([0,1,2])
                s7 += 30
                s8 = random.choice([2,3,4])
                s8 += 35
                s9 = random.choice([2,3,4])
                s9 += 40
                testcheck[s1].click()
                testcheck[s2].click()
                testcheck[s3].click()
                testcheck[s4].click()
                testcheck[s5].click()
                testcheck[s6].click()
                testcheck[s7].click()
                testcheck[s8].click()
                testcheck[s9].click()
                temp = 1
                jelek -= 1
        elif baik != 0 and jelek == 0:
            time.sleep(2)
            s1 = random.choice([2,3,4])
            s2 = random.choice([0,1,2])
            s2 += 5
            s3 = random.choice([0,1,2])
            s3 += 10
            s4 = random.choice([0,1,2])
            s4 += 15
            s5 = random.choice([1,2,3,4])
            s5 += 20
            s6 = random.choice([0,1,2])
            s6 += 25
            s7 = random.choice([2,3,4])
            s7 += 30
            s8 = random.choice([0,1,2])
            s8 += 35
            s9 = random.choice([0,1,2])
            s9 += 40
            testcheck[s1].click()
            testcheck[s2].click()
            testcheck[s3].click()
            testcheck[s4].click()
            testcheck[s5].click()
            testcheck[s6].click()
            testcheck[s7].click()
            testcheck[s8].click()
            testcheck[s9].click()
            temp = 0
            baik -= 1
        elif baik == 0 and jelek != 0:
            time.sleep(2)
            s1 = random.choice([0,1,2])
            s2 = random.choice([2,3,4])
            s2 += 5
            s3 = random.choice([2,3,4])
            s3 += 10
            s4 = random.choice([2,3,4])
            s4 += 15
            s5 = random.choice([0,1,2,3])
            s5 += 20
            s6 = random.choice([2,3,4])
            s6 += 25
            s7 = random.choice([0,1,2])
            s7 += 30
            s8 = random.choice([2,3,4])
            s8 += 35
            s9 = random.choice([2,3,4])
            s9 += 40
            testcheck[s1].click()
            testcheck[s2].click()
            testcheck[s3].click()
            testcheck[s4].click()
            testcheck[s5].click()
            testcheck[s6].click()
            testcheck[s7].click()
            testcheck[s8].click()
            testcheck[s9].click()
            temp = 1
            jelek -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        if temp == 0 and jarang != 0 and sering != 0:
            time.sleep(2)
            pi = random.choice([1,2])
            if pi == 1:
                n1 = random.choice([0,1,1,1,1])
                n2 = random.choice([2,3,3,3,3])
                n3 = random.choice([4,5,5,5,5])
                n4 = n1 + 6
                n5 = random.choice([8,8,8,9])
                n6 = n1 + 10
                n7 = random.choice([12,13,13,13,13])
                n8 = n7 + 2
                n9 = random.choice([16,17,17,17,17])
                n10 = random.choice([18,19,19,19,19])
                n11 = random.choice([20,21])
                n12 = random.choice([22,23,23,23,23])
                n13 = random.choice([24,25,25,25,25])
                n14 = random.choice([26,27,27,27,27])
                n15 = random.choice([28,29,29,29])
                n16 = n15 + 2
                n17 = n15 + 4
                n18 = random.choice([34,35,35,35,35])
                n19 = random.choice([36,37,37,37,37])
                n20 = n19 + 2
                n21 = n12 + 18
                n22 = random.choice([42,43,43,43,43])
                n23 = random.choice([44,45,45,45,45])
                radiobuttons[n1].click()
                radiobuttons[n2].click()
                radiobuttons[n3].click()
                radiobuttons[n4].click()
                radiobuttons[n5].click()
                radiobuttons[n6].click()
                radiobuttons[n7].click()
                radiobuttons[n8].click()
                radiobuttons[n9].click()
                radiobuttons[n10].click()
                radiobuttons[n11].click()
                radiobuttons[n12].click()
                radiobuttons[n13].click()
                radiobuttons[n14].click()
                radiobuttons[n15].click()
                radiobuttons[n16].click()
                radiobuttons[n17].click()
                radiobuttons[n18].click()
                radiobuttons[n19].click()
                radiobuttons[n20].click()
                radiobuttons[n21].click()
                radiobuttons[n22].click()
                radiobuttons[n23].click()
                jarang -= 1
            else:
                n1 = random.choice([1,0,0,0,0])
                n2 = random.choice([3,2,2,2,2])
                n3 = random.choice([5,4,4,4,4])
                n4 = n1 + 6
                n5 = random.choice([8,9])
                n6 = n1 + 10
                n7 = random.choice([12,13,13,13,13])
                n8 = n7 + 2
                n9 = random.choice([17,16,16,16,16])
                n10 = random.choice([19,18,18,18,18])
                n11 = random.choice([20,21])
                n12 = random.choice([23,22,22,22,22])
                n13 = random.choice([25,24,24,24,24])
                n14 = random.choice([27,26,26,26,26])
                n15 = random.choice([29,28,28,28])
                n16 = n15 + 2
                n17 = n15 + 4
                n18 = random.choice([35,34,34,34,34])
                n19 = random.choice([37,36,36,36,36])
                n20 = n19 + 2
                n21 = n12 + 18
                n22 = random.choice([43,42,42,42,42])
                n23 = random.choice([45,44,44,44])
                radiobuttons[n1].click()
                radiobuttons[n2].click()
                radiobuttons[n3].click()
                radiobuttons[n4].click()
                radiobuttons[n5].click()
                radiobuttons[n6].click()
                radiobuttons[n7].click()
                radiobuttons[n8].click()
                radiobuttons[n9].click()
                radiobuttons[n10].click()
                radiobuttons[n11].click()
                radiobuttons[n12].click()
                radiobuttons[n13].click()
                radiobuttons[n14].click()
                radiobuttons[n15].click()
                radiobuttons[n16].click()
                radiobuttons[n17].click()
                radiobuttons[n18].click()
                radiobuttons[n19].click()
                radiobuttons[n20].click()
                radiobuttons[n21].click()
                radiobuttons[n22].click()
                radiobuttons[n23].click()
                sering -= 1

        elif temp == 0 and jarang == 0:
            n1 = random.choice([1,0,0,0,0])
            n2 = random.choice([3,2,2,2,2])
            n3 = random.choice([5,4,4,4,4])
            n4 = n1 + 6
            n5 = random.choice([8,9])
            n6 = n1 + 10
            n7 = random.choice([12,13,13,13,13])
            n8 = n7 + 2
            n9 = random.choice([17,16,16,16,16])
            n10 = random.choice([19,18,18,18,18])
            n11 = random.choice([20,21])
            n12 = random.choice([23,22,22,22,22])
            n13 = random.choice([25,24,24,24,24])
            n14 = random.choice([27,26,26,26,26])
            n15 = random.choice([29,28,28,28])
            n16 = n15 + 2
            n17 = n15 + 4
            n18 = random.choice([35,34,34,34,34])
            n19 = random.choice([37,36,36,36,36])
            n20 = n19 + 2
            n21 = n12 + 18
            n22 = random.choice([43,42,42,42,42])
            n23 = random.choice([45,44,44,44])
            radiobuttons[n1].click()
            radiobuttons[n2].click()
            radiobuttons[n3].click()
            radiobuttons[n4].click()
            radiobuttons[n5].click()
            radiobuttons[n6].click()
            radiobuttons[n7].click()
            radiobuttons[n8].click()
            radiobuttons[n9].click()
            radiobuttons[n10].click()
            radiobuttons[n11].click()
            radiobuttons[n12].click()
            radiobuttons[n13].click()
            radiobuttons[n14].click()
            radiobuttons[n15].click()
            radiobuttons[n16].click()
            radiobuttons[n17].click()
            radiobuttons[n18].click()
            radiobuttons[n19].click()
            radiobuttons[n20].click()
            radiobuttons[n21].click()
            radiobuttons[n22].click()
            radiobuttons[n23].click()
            sering -= 1

        else:
            if sering != 0 and jarang != 0:
                time.sleep(2)
                pi = random.choice([1,2])
                if pi == 1:
                    n1 = random.choice([0,1,1,1,1])
                    n2 = random.choice([2,3,3,3,3])
                    n3 = random.choice([4,5,5,5,5])
                    n4 = n1 + 6
                    n5 = random.choice([8,8,8,9])
                    n6 = n1 + 10
                    n7 = random.choice([12,13,13,13,13])
                    n8 = n7 + 2
                    n9 = random.choice([16,17,17,17,17])
                    n10 = random.choice([18,19,19,19,19])
                    n11 = random.choice([20,21])
                    n12 = random.choice([22,23,23,23,23])
                    n13 = random.choice([24,25,25,25,25])
                    n14 = random.choice([26,27,27,27,27])
                    n15 = random.choice([28,29,29,29])
                    n16 = n15 + 2
                    n17 = n15 + 4
                    n18 = random.choice([34,35,35,35,35])
                    n19 = random.choice([36,37,37,37,37])
                    n20 = n19 + 2
                    n21 = n12 + 18
                    n22 = random.choice([42,43,43,43,43])
                    n23 = random.choice([44,45,45,45,45])
                    radiobuttons[n1].click()
                    radiobuttons[n2].click()
                    radiobuttons[n3].click()
                    radiobuttons[n4].click()
                    radiobuttons[n5].click()
                    radiobuttons[n6].click()
                    radiobuttons[n7].click()
                    radiobuttons[n8].click()
                    radiobuttons[n9].click()
                    radiobuttons[n10].click()
                    radiobuttons[n11].click()
                    radiobuttons[n12].click()
                    radiobuttons[n13].click()
                    radiobuttons[n14].click()
                    radiobuttons[n15].click()
                    radiobuttons[n16].click()
                    radiobuttons[n17].click()
                    radiobuttons[n18].click()
                    radiobuttons[n19].click()
                    radiobuttons[n20].click()
                    radiobuttons[n21].click()
                    radiobuttons[n22].click()
                    radiobuttons[n23].click()
                    jarang -= 1
                else:
                    n1 = random.choice([1,0,0,0,0])
                    n2 = random.choice([3,2,2,2,2])
                    n3 = random.choice([5,4,4,4,4])
                    n4 = n1 + 6
                    n5 = random.choice([8,9])
                    n6 = n1 + 10
                    n7 = random.choice([12,13,13,13,13])
                    n8 = n7 + 2
                    n9 = random.choice([17,16,16,16,16])
                    n10 = random.choice([19,18,18,18,18])
                    n11 = random.choice([20,21])
                    n12 = random.choice([23,22,22,22,22])
                    n13 = random.choice([25,24,24,24,24])
                    n14 = random.choice([27,26,26,26,26])
                    n15 = random.choice([29,28,28,28])
                    n16 = n15 + 2
                    n17 = n15 + 4
                    n18 = random.choice([35,34,34,34,34])
                    n19 = random.choice([37,36,36,36,36])
                    n20 = n19 + 2
                    n21 = n12 + 18
                    n22 = random.choice([43,42,42,42,42])
                    n23 = random.choice([45,44,44,44])
                    radiobuttons[n1].click()
                    radiobuttons[n2].click()
                    radiobuttons[n3].click()
                    radiobuttons[n4].click()
                    radiobuttons[n5].click()
                    radiobuttons[n6].click()
                    radiobuttons[n7].click()
                    radiobuttons[n8].click()
                    radiobuttons[n9].click()
                    radiobuttons[n10].click()
                    radiobuttons[n11].click()
                    radiobuttons[n12].click()
                    radiobuttons[n13].click()
                    radiobuttons[n14].click()
                    radiobuttons[n15].click()
                    radiobuttons[n16].click()
                    radiobuttons[n17].click()
                    radiobuttons[n18].click()
                    radiobuttons[n19].click()
                    radiobuttons[n20].click()
                    radiobuttons[n21].click()
                    radiobuttons[n22].click()
                    radiobuttons[n23].click()
                    sering -= 1
            elif sering != 0 and jarang == 0:
                n1 = random.choice([1,0,0,0,0])
                n2 = random.choice([3,2,2,2,2])
                n3 = random.choice([5,4,4,4,4])
                n4 = n1 + 6
                n5 = random.choice([8,9])
                n6 = n1 + 10
                n7 = random.choice([12,13,13,13,13])
                n8 = n7 + 2
                n9 = random.choice([17,16,16,16,16])
                n10 = random.choice([19,18,18,18,18])
                n11 = random.choice([20,21])
                n12 = random.choice([23,22,22,22,22])
                n13 = random.choice([25,24,24,24,24])
                n14 = random.choice([27,26,26,26,26])
                n15 = random.choice([29,28,28,28])
                n16 = n15 + 2
                n17 = n15 + 4
                n18 = random.choice([35,34,34,34,34])
                n19 = random.choice([37,36,36,36,36])
                n20 = n19 + 2
                n21 = n12 + 18
                n22 = random.choice([43,42,42,42,42])
                n23 = random.choice([45,44,44,44])
                radiobuttons[n1].click()
                radiobuttons[n2].click()
                radiobuttons[n3].click()
                radiobuttons[n4].click()
                radiobuttons[n5].click()
                radiobuttons[n6].click()
                radiobuttons[n7].click()
                radiobuttons[n8].click()
                radiobuttons[n9].click()
                radiobuttons[n10].click()
                radiobuttons[n11].click()
                radiobuttons[n12].click()
                radiobuttons[n13].click()
                radiobuttons[n14].click()
                radiobuttons[n15].click()
                radiobuttons[n16].click()
                radiobuttons[n17].click()
                radiobuttons[n18].click()
                radiobuttons[n19].click()
                radiobuttons[n20].click()
                radiobuttons[n21].click()
                radiobuttons[n22].click()
                radiobuttons[n23].click()
                sering -= 1
            else :
                n1 = random.choice([0,1,1,1,1])
                n2 = random.choice([2,3,3,3,3])
                n3 = random.choice([4,5,5,5,5])
                n4 = n1 + 6
                n5 = random.choice([8,8,8,9])
                n6 = n1 + 10
                n7 = random.choice([12,13,13,13,13])
                n8 = n7 + 2
                n9 = random.choice([16,17,17,17,17])
                n10 = random.choice([18,19,19,19,19])
                n11 = random.choice([20,21])
                n12 = random.choice([22,23,23,23,23])
                n13 = random.choice([24,25,25,25,25])
                n14 = random.choice([26,27,27,27,27])
                n15 = random.choice([28,29,29,29])
                n16 = n15 + 2
                n17 = n15 + 4
                n18 = random.choice([34,35,35,35,35])
                n19 = random.choice([36,37,37,37,37])
                n20 = n19 + 2
                n21 = n12 + 18
                n22 = random.choice([42,43,43,43,43])
                n23 = random.choice([44,45,45,45,45])
                radiobuttons[n1].click()
                radiobuttons[n2].click()
                radiobuttons[n3].click()
                radiobuttons[n4].click()
                radiobuttons[n5].click()
                radiobuttons[n6].click()
                radiobuttons[n7].click()
                radiobuttons[n8].click()
                radiobuttons[n9].click()
                radiobuttons[n10].click()
                radiobuttons[n11].click()
                radiobuttons[n12].click()
                radiobuttons[n13].click()
                radiobuttons[n14].click()
                radiobuttons[n15].click()
                radiobuttons[n16].click()
                radiobuttons[n17].click()
                radiobuttons[n18].click()
                radiobuttons[n19].click()
                radiobuttons[n20].click()
                radiobuttons[n21].click()
                radiobuttons[n22].click()
                radiobuttons[n23].click()
                jarang -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfFwC8wFE4L2iDrcENq91kbckPfTsgmKWPvdCbyna0yFCBNWw/viewform?usp=sf_link")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("baik  : " + str(baik))
        print("jelek : " + str(jelek))
        print("sering: " + str(sering))
        print("jarang: " + str(jarang))

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