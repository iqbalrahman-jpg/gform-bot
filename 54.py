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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdrslNTS2mCxCBX6TAtDMepo8qbOJa4GBuw6DTRwNHSIhS8Aw/viewform")


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
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Attaka Majid",
    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Angga Siregar Putra",
    "Putri Keancana",
    "Raja Putra Wardanawan",
    "Affifah Rahman Nabila",
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
    "Nabilla Syaqila Qolbi",
]

domisili = [
    "Yogyakarta",
    "surabaya",
    "Bali",
    "Bandung",
    "Bekasi",
    "Bekasi",
    "Bandung",
    "medan",
    "banyuwangi",
    "surabaya",
    "Bandung",
    "banyuwangi",
    "Bekasi",
    "jawa timur",
    "gresik",
    "semarang",
    "jakarta",
    "surabaya",
    "surabaya",
    "semarang",
    "DKI Jakarta",
    "Bekasi",
    "jakarta",
    "DKI Jakarta",
    "Bandung",
    "jakarta",
    "jawa timur",
    "surabaya",
    "jawa timur",
    "surabaya",
    "Bandung",
    "surabaya",
    "denpasar",
    "Surabaya",
    "jawa timur",
    "Bekasi",
    "DKI Jakarta",
    "Bali",
    "banyuwangi",
    "jawa timur",
    "Bali",
    "Surabaya",
    "DKI Jakarta",
    "Bandung",
    "gresik",
    "gresik",
    "banyuwangi",
    "jakarta",
    "Yogyakarta",
    "banyuwangi",
]

#gapake
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,]

times = 50
index = 0



try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(domisili[index])
        radiobuttons[kelamin[index]].click()
        pekerjaan =  random.choice([2,3,4])
        radiobuttons[pekerjaan].click()
        platform = random.choice([5,5,5,6,7])
        radiobuttons[platform].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        radiobuttons[0].click()
        time.sleep(2)
        radiobuttons[2].click()

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
            jawab = random.choice([p+3,p+4,p+5])
            testcheck[jawab].click()
            soal -= 1
            p += 6

        p = 24
        jawab = random.choice([p+1,p+2,p+3,p+4,p+5])
        testcheck[jawab].click()
        p = 30
        if jawab < 3:
            jawab = random.choice([p+1,p+2])
            testcheck[jawab].click()
        else:
            jawab = random.choice([p+3,p+4,p+5])
            testcheck[jawab].click()


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
        lucu = random.choice([p+1,p+2,p+3,p+4,p+5])
        testcheck[lucu].click()
        if lucu > 3:
            p = 6
            soal = 2
            while soal:
                jawab = random.choice([p+3,p+4,p+5])
                testcheck[jawab].click()
                soal -= 1
                p += 6
        else:
            p = 6
            soal = 2
            while soal:
                jawab = random.choice([p+1,p+2])
                testcheck[jawab].click()
                soal -= 1
                p += 6
        


        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        
        seksi = random.choice([0,1,2,3,4,5])
        testcheck[seksi].click()
        cantik = random.choice([6,7,8,9,10,11])
        testcheck[cantik].click()
        if seksi < 3:
            sugesti = random.choice([12,13,14])
        else:
            sugesti = random.choice([15,16,17])
        
        testcheck[sugesti].click()
        
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
        stream = random.choice([p+1,p+2,p+3,p+4,p+5,p+3,p+4,p+5])
        testcheck[stream].click()
        if stream > 3:
            p = 6
            soal = 2
            while soal:
                jawab = random.choice([p+3,p+4,p+5])
                testcheck[jawab].click()
                soal -= 1
                p += 6
        else:
            p = 6
            soal = 2
            while soal:
                jawab = random.choice([p+1,p+2])
                testcheck[jawab].click()
                soal -= 1
                p += 6

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
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdrslNTS2mCxCBX6TAtDMepo8qbOJa4GBuw6DTRwNHSIhS8Aw/viewform")

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