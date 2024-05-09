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
driver.get("http://bit.ly/SkripsiAerox")

nama = [
        "Mutia Ayu Nur",
    "Ali Hasanudin",
        "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
        "Nana Annisa",
    "Yahya Nugraha",
    "Putra Agung Dewantoro",
    "Nanda Bagas Kurniawan",
    "Yudi Pradanawan",
    "Yuli Putra Senopati",
    "Bayu Danang Merta",
        "Bellanda Clara Ayunda", 
    "Budi Suryanto",
    "Ahmad Miranda Sutanto",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
        "Annisa Chania",
    "Fikri Fauzi",
    "Fattahilah Sadewa",
        "Diah Ayu Cindy",
    "Attaka Majid",
        "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
        "Nia EKa Yuliana",
    "Bayu Dwiganara",
        "Syifa Radifah",
    "Aditya Derdinand",
    "Fikri Fahrurozi",
    "Reyhan Utomowa",
        "Salma Arowaya",
    "Angga Siregar Putra",
    "Putra Keancana",
    "Raja Putra Wardanawan",
    "Bima Pratama",
    "M. Rahman Attala",
    "Shaka Kurnia Wijaya",
        "Cynara Nafisah",
        "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
        "Fryshta Eka Nabilla",
    "Yanuar Suryadi",
    "Rayhan Adi Wicasa",
        "Sutisna Ayuni",
        "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Ardyanto Rizki Putra",
    "Putra Wirawan",
    "Agung Nugroho",
    "Dani Ramadhan",
    "Dimas Purbo",
]

kelamin = [1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,]

telp = [
"81211906212",
"81212784008",
"81250284950",
"81264718461",
"81280281529",
"8128632193",
"81290475868",
"81270348686",
"82132447386",
"87886158249",
"81278010606",
"87778433058",
"85956060930",
"87848003451",
"882008113306",
"83838919000",
"81511323691",
"88294743163",
"83181803358",
"895609625455",
"85729979914",
"85156051463",
"85729213992",
"87780590374",
"817205928",
"084624253733",
"088565440513",
"083626799003",
"088070442682",
"083435047182",
"089579629094",
"080103002233",
"086659262105",
"087136378661",
"080640301967",
"083806763847",
"088509885576",
"084985961237",
"086137328130",
"089843988039",
"086738422620",
"089045039379",
"087788078906",
"088159431881",
"089474988296",
"088530547344",
"085109243357",
"080470592685",
"083273198985",
"081850592479",
]

times = 47
index = 3

pelajar = 32

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(nama[index])

        radiobuttons[kelamin[index]].click()

        if pelajar != 0 :
            time.sleep(2)
            usia = random.choice([2,3])
            radiobuttons[3].click()
            time.sleep(2)

            radiobuttons[usia].click()
            radiobuttons[7].click()
            penghasilan = random.choice([12,12,13])
            radiobuttons[penghasilan].click()
            pelajar -= 1
        else :
            time.sleep(2)
            usia = random.choice([4,4,5,6])
            radiobuttons[2].click()
            time.sleep(2)
            radiobuttons[usia].click()
            pekerjaan = random.choice([8,9,10,11])
            radiobuttons[pekerjaan].click()
            penghasilan = random.choice([13,14,15])
            radiobuttons[penghasilan].click()


        domisili = random.choice([16,17,18,19,20])
        radiobuttons[domisili].click()

        textboxes[1].send_keys(telp[index])
        wallet = random.choice([21,22,23])
        radiobuttons[wallet].click()

        checkboxes[0].click()

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
        soal = 7
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
        soal = 6
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
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("http://bit.ly/SkripsiAerox")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("pelajar : " + str(pelajar))

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