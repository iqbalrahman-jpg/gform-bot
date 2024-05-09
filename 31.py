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
driver.get("https://docs.google.com/forms/d/1833fjaDf1vzUOYyYvoj06S4HabuJ8JSMI3-LKbgO5nI/edit")

nama = [
    "Bu rohma",
    "Bu seh",
    "Bu siti",
    "Bu siti",
    "Bu siti",
    "Bu sriyanti",
    "Bu suliana",
    "Bu sum",
    "Bu suprat",
    "Bu ten",
    "Bu tin",
    "Bu totok",
    "Bu tupan",
    "Bu vio",
    "Bu vivi",
    "Bu wahed",
    "Bu wandi",
    "Bu ya",
    "Pak budi nabil",
    "Pak budi narto",
    "ce meme",
    "Kafe limo",
    "Ce emi",
    "Ce lala",
    "Bu dewi nasruroh",
    "Bu Diana",
    "Pak dodik",
    "Bu Emil jaya",
    "Bu Fang fang",
    "Pak Feri sumberejo",
    "Pak Gofur",
    "Pak Gus bastomi",
    "Pak Hambali",
    "Pak Hamdalah",
    "Pak Hamim",
    "Pak Hendra",
    "Bu Lina",
    "Bu Heni",
    "Bu haji farida",
    "Bu Ida",
    "Bu Ika",
    "Bu Ika",
    "Pak imam",
    "Pak imron",
    "Bu ita",
    "Bu jessica",
    "Pak joko",
    "Bu karin",
    "Ko icung",
    "Ko sunliong",
    "Pak lubis",
    "Pak lutvi",
    "Ibu lulik",
    "Mak ti",
    "Pak Marsel",
    "Mas agung",
    "Mas agus",
    "Mas agus",
    "Mas al",
]

lokasi = [
    "Tegal banteng","Sumberan","Watu ulo","Sabrang","Tegal banteng","Pontang","Karanganyar","Sumberan","Pontang",
    "Ambulu","Ambulu","Sumberan","Sumberan","Ambulu","Ambulu","Jatisari","Sumberan","Ambulu","Ambulu","Krajan",
    "Jember","Ambulu","Karanganyar","Jenggawah","Karanganyar","Pontang","Balung","Kesilir","Sumberan","Sumberejo",
    "Sumberejo","Kesilir","Seruni","Silir","Ambulu","Karanganyar","Kemuning","Karangtengah","Watu ulo","Karanganyar",
    "Sumberan","Andongsari","Sabrang","Ambulu","Sumberejo","Ambulu","Karanganyar","Jatisari","Ambulu","Tegal banteng",
    "Ambulu","Sumberan","Karanganyar","Kertonegoro","Ambulu","Karangtengah","Kemuning","Sentong","Sumberejo"
]

usia = [
    9,9,9,10,10,9,10,10,10,10,9,9,10,9,9,10,10,10,10,9,9,9,10,9,9,10,10,10,10,10,10,10,10,9,9,9,9,10,10,10,10,10,10,10,9,9,10,9,10,10,9,9,10,10,10,10,10,10,10
]

#0 laki, 1 perempuan
kelamin = [
    5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,5,4,5,5,5,5,4,5,5,4,4,4,4,4,4,4,5,5,5,5,5,5,4,4,5,5,4,5,4,4,4,4,5,5,4,4,4,4,4
]

lama = [
    14,14,14,14,14,13,14,14,14,14,14,14,14,14,14,14,14,14,13,14,14,13,14,13,12,13,13,14,14,12,14,14,14,13,13,14,14,13,14,14,14,13,14,14,14,14,14,13,14,14,14,14,13,14,13,13,14,14,14
]

s1 = [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5]
s2 = [4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5,4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5]
s3 = [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5]
s4 = [5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4]

p1 = [5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4]
p2 = [5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4]
p3 = [4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5,4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5]
p4 = [5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4,5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4]
p5 = [4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4]
p6 = [5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4]
p7 = [4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5,4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5]
p8 = [5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4]
p9 = [4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4,4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4]
p10 = [4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5]
p11 = [5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5]
p12 = [5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4]
p13 = [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5]
p14 = [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5]
p15 = [4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5,4,4,4,3,3,4,3,3,5,4,4,4,3,5,3,4,3,5,3,5,4,4,4,3,5,5,4,5,4,5]

l1 = [5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5]
l2 = [5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4]
l3 = [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5]
l4 = [5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5]
l5 = [5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5]
l6 = [4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5]

k1 = [5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4,5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4] 
k2 = [4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4]
k3 = [4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5,5,5,3,4,4,5,4,4,5,5,3,4,4,5,4,4,2,5,3,4,4,4,4,2,5,5,5,5,3,4]

times = 59
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        isian = driver.find_elements("css selector", ".Hvn9fb")#isian 

        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(4)
        radiobuttons[3].click()
        radiobuttons[kelamin[index]].click()

        if lokasi[index] == "Ambulu" :
            time.sleep(2)
            radiobuttons[6].click()
        else: 
            time.sleep(2)
            radiobuttons[7].click()
            isian[0].send_keys(lokasi[index])

        driver.implicitly_wait(4)
        radiobuttons[usia[index]].click()
        radiobuttons[lama[index]].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        testcheck[s1[index]-1].click()
        testcheck[s2[index]+4].click()
        testcheck[s3[index]+9].click()
        testcheck[s4[index]+14].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        testcheck[p1[index]-1].click()
        testcheck[p2[index]+4].click()
        testcheck[p3[index]+9].click()
        testcheck[p4[index]+14].click()
        testcheck[p5[index]+19].click()
        testcheck[p6[index]+24].click()
        testcheck[p7[index]+29].click()
        testcheck[p8[index]+34].click()
        testcheck[p9[index]+39].click()
        testcheck[p10[index]+44].click()
        testcheck[p11[index]+49].click()
        testcheck[p12[index]+54].click()
        testcheck[p13[index]+59].click()
        testcheck[p14[index]+64].click()
        testcheck[p15[index]+69].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        testcheck[l1[index]-1].click()
        testcheck[l2[index]+4].click()
        testcheck[l3[index]+9].click()
        testcheck[l4[index]+14].click()
        testcheck[l5[index]+19].click()
        testcheck[l6[index]+24].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        testcheck[k1[index]-1].click()
        testcheck[k2[index]+4].click()
        testcheck[k3[index]+9].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/1833fjaDf1vzUOYyYvoj06S4HabuJ8JSMI3-LKbgO5nI/edit")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")

        times-=1
        print("times : " + str(times))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()