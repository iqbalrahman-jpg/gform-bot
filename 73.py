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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe8Hna1WXXNUV1EnpDPbm69n2_tSA1umrQeFX1vY4w46Eom6Q/viewform?usp=pp_url")

nama = [
    "Mutia Ayu Nur",
    "Riskia Ayu Febrianti",
    "Ali Hasanudin",
    "Budi Prasetyo Wibowo",
    "Nana Annisa",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yuli Ayunda Dewi",
    "Bellanda Clara Ayunda ",
    "Aryo Nugraha",
    "Yahya Nugraha",
    "Yudi Pradanawan",
    "Bayu Danang Merta",
    "Budi Suryanto",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Miranda Nella",
    "Fattahilah Sadewa",
    "Annisa Chania",
    "Diah Ayu Cindy",
    "Azzarin Ristia Nabila",
    "Nia EKa Yuliana",
    "Syifa Radifah",
    "Attaka Majid",
    "Fabian Nadeo Putra",
    "Bayu Dwiganara",
    "Siti Fauziyah",
    "Salma Arowaya",
    "Aditya Derdinand",
    "Putri Keancana",
    "Reyhan Utomowa",
    "Affifah Rahman Nabila",
    "Cynara Nafisah",
    "Angga Siregar Putra",
    "Mona Hadfinna",
    "Fryshta Eka Nabilla",
    "Raja Putra Wardanawan",
    "Sutisna Ayuni",
    "Ayu Yulistya Ningsih",
    "Nabilla Syaqila Qolbi",
    "Maya Dara Putri",
    "Shaka Kurnia Wijaya",
    "Mahendra Rhejaa Fadilah",
    "Yanuar Suryadi",
    "Dewi Sari Wijaya",
    "Ratih Suci Lestari",
    "Rayhan Adi Wicasa",
    "Intan Ayu Lestari",
    "Fira Nur Hidayah",
    "Cinta Ayu Dewanti",
    "Mira Fitriana Wati",
    "Dian Kusuma Wardani",
    "M. Putra Susanto",
    "Ardyanto Rizki Putra",
    "Putra Wirawan",
    "Agung Nugroho",
    "Dani Ramadhan",
    "Rina Nuraini Sari",
    "Dimas Purbo",
    "Maya Dewi Sari",
    "Dila Yuliani Wati",
    "Rina Permata Sari",
    "Dian Nugroho",
    "Rio Fajar Pratama",
    "Maya Putri Lestari",
    "Sinta Utami Sari",
    "Agung Kusuma Jaya",
    "Rizki Pratama Nugraha",
    "Dwi Prasetya Utama",
    "Arif Rahman Hakim",
    "Eka Puspita Dewi",
    "Rani Fitriani",
    "Nisa Indah Sari",
    "Ananda Dwi Wicaksono",
    "Tiara Dewi Puspita",
    "Rama Aditya Wardhana",
    "Nina Anggraini",
    "Dini Cahyani",
    "Maya Dewi Utami",
    "Ade Kurniawan Saputra",
    "Budi Santoso Putra",
    "Devi Puspitasari",
    "Ahmad Fauzi Akbar",
    "Rina Anggraini Sari",
    "Yuni Nafisah",
    "Rizky Ananda Pratama",
    "Prita agustina",
    "Hana Anissa Herian",
    "Dwi Kusuma Jaya",
    "Okto Devano",
    "Olivia Niken",
    "faradilla nina",
    "Sarah Husaini",
    "Agung Santosa Nugroho",
    "Josephine Anindya",
    "Andi Muhammad Rizal",
    "Budi Santoso",
    "Rudi Setiawan",
    "Erfina Pratiwi",
    "Rizky Ramadhan",
    "Hani Annissa",
    "Salma Azizah",
    "Faradilla Aulia",
    "Regina April",
    "Dika Setiawan Pratama",
    "Amanda Bella Putri",
    "Rizal Pratama",
    "Yanto Wibowo",
    "Kairaini Aliesa",
    "Lika Arletta",
    "Raka Triyana",
    "Lista Kamilla",
    "Sadiva Pratiwi",
    "Indra Kusuma",
    "Windy Cantika",
    "Stephani Amanda Safitri",
    "Caroline Putri",
    "Bima Aditya Nugraha",
    "Khansa Azzahra",
    "Riska Rahmawati",
]

usia = [0,0,0,1,1,1,1,1,1,1,0,0,0,2,1,0,1,1,3,2,0,0,1,0,1,0,2,3,2,1,0,1,1,0,1,0,1,1,1,3,0,0,1,0,2,1,0,3,3,1,1,3,0,3,2,0,3,1,0,1,
        0,1,0,0,1,0,1,2,0,1,1,0,1,3,0,0,2,0,2,1,0,2,0,1,1,0,1,1,0,0,0,1,2,0,2,2,1,3,1,1,0,0,1,1,1,2,0,2,1,2,1,0,1,3,1,1,1,0,1,1]

kelamin = [4,4,5,5,4,4,4,4,4,5,5,5,5,5,5,5,4,5,4,4,4,4,4,5,5,5,4,4,5,4,5,4,4,5,4,4,5,4,4,4,4,5,5,5,4,4,5,4,4,4,4,4,5,5,5,5,5,4,5,4,
        4,4,4,5,4,4,5,5,5,5,4,4,4,5,4,5,4,4,4,5,5,4,5,4,4,5,4,4,5,4,4,4,4,5,4,5,5,5,4,5,4,4,4,4,5,4,5,5,4,4,5,4,4,5,4,4,4,5,4,4]

page1 = [
    [1,3,2,2,2,3,2,3,2,3,2,2,3,3,3,2,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,4,4,3,3,3,4,3,4,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,4,3,4,3,3,3,4,3,4,4,3,3,3,3,4,4,3,3,4,4,3,4,4,4,3,3,4,3,4,3,4,4,3,3,3,4,4,3,4,4,3,4,3,3,4,4,4,4,3],
    [2,1,3,2,3,3,3,3,3,3,3,3,2,2,3,2,3,3,3,3,4,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,4,3,3,3,3,4,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,4,3,3,2,2,3,3,3,2,3,4,4,4,3,3,3,3,4,3,3,3,4,3,4,4,4,2,4,3,4,3,3,3,4,4,3,4,4,4,4,4,3,4,3,4,3],
    [1,2,3,2,3,3,2,3,3,1,3,3,2,3,3,3,4,3,3,3,2,3,3,3,2,3,3,4,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,4,3,3,3,4,4,3,3,4,3,2,3,4,3,3,3,3,3,3,3,3,3,3,2,4,3,3,3,3,2,3,3,3,3,4,3,3,3,4,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,4,4,2,3,3,3,4,3,3,3,3,4,3,4,3,3,3,3,3,4,3],
    [3,3,2,2,2,3,2,3,3,3,2,3,3,3,2,3,3,2,2,2,2,3,3,3,3,3,2,4,3,3,3,3,3,3,3,3,3,3,3,4,4,2,3,3,3,3,3,3,3,3,4,4,1,3,3,3,4,4,4,3,3,3,4,3,4,3,4,4,4,4,3,4,4,4,4,3,3,3,3,3,4,4,4,3,3,3,3,2,4,3,3,4,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,4,4,4],
    [1,3,2,3,3,2,3,2,1,2,3,2,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,4,3,3,3,4,3,3,2,4,3,3,4,3,3,4,4,3,3,4,3,3,4,3,4,4,3,3,3,4,3,4,4,4,4,4,4,4,3,3,4,3,4,3,3,3,4,3,3,4,3,3,4,3,4,3,4,4,4,4,3,4,4,4,3,4,3,4,4,4,4,3,3],
    [2,3,1,2,2,3,3,2,2,3,3,3,3,3,3,3,3,4,3,2,4,2,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,3,3,3,3,3,3,3,4,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,4,3,3,3,3,3,3,4,3,3,4,4,3,3,4,4,3,3,4,4,3,3,4,3,3,4,3,3,3,3,4,3,3,4,3,3,3,3,4,4,4,4,4,3,3,3,4,3,4,3,4,4],
    [2,1,2,2,2,1,2,2,3,3,2,3,3,2,3,2,2,2,2,3,2,3,3,3,4,3,3,1,3,3,3,3,3,3,3,3,3,3,3,2,1,3,4,3,3,3,3,3,3,3,3,2,4,4,3,4,2,4,3,3,3,3,3,3,4,4,3,3,3,3,4,2,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,3,2,4,4,4,3,4,2,4,4,3,3,4,3,3,3,3,4,3,3,3,4,3,4,3,3,3,3],
]

page2 = [
    [2,3,2,3,2,3,3,3,3,2,2,3,2,3,3,2,3,3,2,3,2,3,3,3,3,1,3,3,3,3,3,3,3,4,3,3,3,3,3,3,2,3,4,4,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,4,3,4,2,3,3,3,3,2,3,3,3,3,3,3,4,4,3,3,4,3,4,3,3,3,3,3,3,3,3,4,4,3,3,3,3,3,3,3,4,4,3,3,3,4,3,3,3,4,4,3,3,4,4,4,3,4],
    [1,3,3,2,3,1,2,3,3,2,3,2,3,1,3,2,2,3,3,3,3,3,3,3,2,3,2,3,3,3,3,3,2,3,3,3,3,3,3,2,4,3,3,3,3,3,3,3,3,4,3,3,3,2,3,3,3,3,3,3,4,3,3,3,3,4,3,3,3,3,3,3,4,3,3,4,3,4,3,3,3,3,4,3,4,3,3,4,4,4,3,3,3,4,3,3,4,3,3,3,3,3,3,3,4,3,3,4,3,3,3,4,3,4,3,3,4,4,3,3],
    [2,3,1,2,3,1,3,3,1,3,1,3,2,3,3,3,2,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,4,3,3,3,3,3,3,4,3,3,3,4,4,3,4,3,3,3,3,4,2,3,3,3,4,3,3,3,4,4,3,3,4,4,2,4,4,3,3,3,4,4,4,3,4,3,3,3,4,3,4,4,2,3,3,3,3,4,3,3,3,3,3,4,3,3,3,4,4,2,3,4,3,4,3,3,2,3,3,3,3,3,3,3,3,4,3,3],
    [2,3,2,2,3,3,2,2,3,2,3,3,3,2,2,3,2,4,2,3,2,3,3,2,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,3,1,3,3,4,3,3,3,3,2,3,3,3,2,3,3,2,3,3,3,3,4,3,3,3,3,3,3,3,3,3,3,2,2,4,3,4,4,3,3,3,3,4,4,3,3,3,3,3,3,3,3,3,3,4,4,3,3,2,3,2,4,2,3,4,3,4,4,4,3,3,3,3,3,3,3,3,3,4,4,3],
]

page3 = [
    [2,1,2,3,3,3,3,3,3,3,2,3,2,3,2,4,2,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,1,3,3,3,3,3,3,2,3,3,3,3,3,3,4,3,4,4,3,3,3,4,3,4,3,3,3,3,3,3,3,3,3,3,3,2,3,3,4,3,3,3,4,4,3,3,3,4,4,3,3,3,3,4,3,3,3,3,3,3,4,3,4,3,3,4,3,3,3,3,4],
    [1,2,2,2,2,1,2,2,3,3,2,2,3,2,3,3,3,2,2,3,3,3,3,3,3,3,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,4,3,4,2,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,4,3,3,2,3,3,3,3,3,3,4,3,3,3,3,3,2,3,3,3,3,3,3,3,3,4,3,3,3,4,3,4,3,3,3,4,2,3,3,3,3,4,4,3,3,4,3,2,3,3,4,3,4,4,3,3,3],
    [3,2,3,3,3,1,3,2,3,3,3,2,3,2,3,3,2,3,3,3,3,3,4,3,3,3,3,1,3,3,3,3,3,3,3,3,3,3,3,1,4,3,3,2,3,3,3,3,2,4,3,3,4,3,3,3,3,3,3,3,3,3,3,4,3,3,4,3,3,3,4,3,3,3,3,4,3,3,3,3,3,4,3,3,4,3,3,3,3,3,3,3,4,4,3,4,3,4,4,3,4,2,4,4,3,4,3,3,3,3,3,4,3,3,3,3,3,4,3,4],
    [2,1,3,2,2,2,2,2,2,3,3,3,3,3,3,3,2,2,3,2,3,3,3,3,3,3,4,2,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,2,3,2,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,4,3,3,3,2,2,3,3,3,3,3,3,3,3,3,4,3,3,3,4,4,3,2,4,4,4,4,4,3,3,3,4,3,3,4,3,4,4,3,3,3,3,3],
    [2,1,2,2,3,3,2,2,3,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,4,4,4,3,3,3,4,4,4,4,3,4,3,4,3,3,3,4,3,4,3,2,4,4,4,3,3,3,4,4,3,4,4,4,2,2,3,3,3,4,4,3,4,3,4,3,3,3,3,4,3,3,3,3,3,4,3,4,3,3,3,3,4,3,3,3,4,3,3,3,4,3,4,3,4],
    [1,2,3,3,2,3,3,3,3,3,3,2,2,3,2,2,2,2,2,3,2,3,2,2,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,3,3,3,3,2,3,3,2,3,3,3,2,3,3,3,4,3,3,3,2,3,3,3,3,3,3,4,2,3,2,3,3,4,3,4,3,2,3,3,4,3,4,3,4,3,3,4,3,3,3,3,4,3,2,3,3,3,3,3,3,4,3,4,3,4,4,2,3,3,3,4,4,3,2,2,4],
]

page4 = [
    [3,2,3,2,2,3,3,2,3,3,3,3,2,3,3,3,3,3,3,3,4,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,3,1,3,3,3,3,3,3,4,3,3,3,3,2,3,4,3,4,3,4,3,3,4,3,3,3,3,3,3,3,3,3,3,4,3,4,3,3,3,3,4,3,3,3,3,3,3,4,3,4,3,3,3,3,3,3,3,3,4,3,4,4,3,4,3,3,4,3,4,3,3,3,3,3,3,3,3,3,3,3,3],
    [2,2,2,2,2,3,2,3,2,1,3,2,3,2,3,3,2,2,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,2,3,3,3,3,3,3,2,3,3,3,3,3,4,3,3,3,3,4,3,3,3,4,3,4,3,3,3,3,4,3,3,3,4,3,4,4,3,3,3,4,4,4,3,3,3,3,3,3,4,3,3,4,3,4,3,3,4,3,4,3,3,3,4,4,4,4,4,3,3,4,4,4],
    [3,1,2,3,3,3,3,3,3,3,3,3,2,3,3,3,4,3,3,4,3,3,2,3,3,3,3,3,3,3,3,3,3,3,4,4,4,3,3,3,4,3,3,4,3,3,3,3,3,3,4,3,3,4,3,3,3,3,3,3,4,4,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,4,4,4,4,3,4,3,4,3,3,3,4,3,3,3,3,4,4,4,3,4,3,3,4,3,3,3,3,4,3,3,3,3,4,4,4,4,3,3,4,3,3,3],
    [2,1,2,3,3,3,4,3,2,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,4,3,3,2,3,3,3,3,3,3,4,3,4,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3,4,4,4,4,3,3,4,4,4,4,3,3,4,4,4,3,3,3,4,4,4,3,4,4,4,3,4,3,3,4,3,3,3,4,4,4,4,3,4,3,4,4,4],
]

times = 120
index = 0

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

        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(5)

        radiobuttons[usia[index]].click()
        radiobuttons[kelamin[index]].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = -1
        for i in range(7):
            s1 = page1[i][index] + p
            radiobuttons[s1].click()
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = -1
        for i in range(4):
            s1 = page2[i][index] + p
            radiobuttons[s1].click()
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = -1
        for i in range(6):
            s1 = page3[i][index] + p
            radiobuttons[s1].click()
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = -1
        for i in range(4):
            s1 = page4[i][index] + p
            radiobuttons[s1].click()
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        time.sleep(2)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe8Hna1WXXNUV1EnpDPbm69n2_tSA1umrQeFX1vY4w46Eom6Q/viewform?usp=pp_url")

        index+=1
        print("==================")
        # print("  : " + str())
        # print("")
        
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