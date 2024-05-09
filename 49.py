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
driver.get("https://forms.gle/WcMttu948f2jfUyM6")

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
]

#0 laki 1 perempuan
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,]

baik = 68
jelek = 7

times = 75
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        angkatan = random.choice([0,1,2,3])

        if angkatan == 0:
        	usia = random.randint(22,24)
        elif angkatan == 1:
        	usia = random.randint(21,23)
        elif angkatan == 2:
        	usia = random.randint(20,21)
        else:
        	usia = random.randint(18,19)

        ipk = random.choice([2,3,3,3])

        belakang = random.randint(1,99)

        if belakang == 10 : 
            belakang = 1
        elif belakang == 20 :
            belakang = 2
        elif belakang == 30 :
            belakang = 3
        elif belakang == 40 :
            belakang = 4
        elif belakang == 50 :
            belakang = 5
        elif belakang == 60 :
            belakang = 6
        elif belakang == 70 :
            belakang = 7
        elif belakang == 80 :
            belakang = 8
        elif belakang == 90 :
            belakang = 9
        else :
            belakang = belakang

        driver.implicitly_wait(4)
        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(usia)
        textboxes[2].send_keys(ipk)
        textboxes[2].send_keys(random.choice([",","."]))
        textboxes[2].send_keys(belakang)
        driver.implicitly_wait(4)

        radiobuttons[angkatan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if baik != 0 and jelek != 0:
        	pil = random.choice([1,2])
        	if pil == 1:
        		baik -= 1
        	else: 
        		jelek -= 1
        elif baik != 0 and jelek == 0:
        	pil = 1
        	baik -= 1
        elif baik == 0 and jelek != 0:
        	pil = 2
        	jelek -= 1

        if pil == 1:
        	soal1 = [8,15,16]
        	soal3 = [3,4,7,17]

        	idx1 = 0
        	idx2 = 0 

        	p = 0
        	soal = 16
        	nosoal = 1
        	while soal:
        		if nosoal == soal1[idx1]:
        			s1 = random.choice([p+3,p+4])
        			testcheck[s1].click()
        			idx1 += 1
        		elif nosoal == soal3[idx2]:
        			s1 = random.choice([p,p+1,p+3,p+4])
        			testcheck[s1].click()
        			idx2 += 1
        		else:
        			s1 = random.choice([p,p+1])
        			testcheck[s1].click()
        		
        		p += 5
        		soal -= 1
        		nosoal += 1

        	time.sleep(3)
	        submit_button = WebDriverWait(driver, 10).until(
	            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
	        )

	        submit_button.click()

        	testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        	soals1 = [2,5,10,12,13]
        	soals3 = [6,7,13]

        	idx1 = 0
        	idx2 = 0 

        	p = 0
        	soal = 12
        	nosoal = 1
        	while soal:
        		if nosoal == soals1[idx1]:
        			s1 = random.choice([p,p+1])
        			testcheck[s1].click()
        			idx1 += 1
        		elif nosoal == soals3[idx2]:
        			s1 = random.choice([p,p+1,p+3,p+4])
        			testcheck[s1].click()
        			idx2 += 1
        		else:
        			s1 = random.choice([p+3,p+4])
        			testcheck[s1].click()
        		
        		p += 5
        		soal -= 1
        		nosoal += 1
 
        else:
        	soal1 = [8,15,16]
        	soal3 = [3,4,7,17]

        	idx1 = 0
        	idx2 = 0 

        	p = 0
        	soal = 16
        	nosoal = 1
        	while soal:
        		if nosoal == soal1[idx1]:
        			s1 = random.choice([p,p+1])
        			testcheck[s1].click()
        			idx1 += 1
        		elif nosoal == soal3[idx2]:
        			s1 = random.choice([p,p+1,p+3,p+4])
        			testcheck[s1].click()
        			idx2 += 1
        		else:
        			s1 = random.choice([p+3,p+4])
        			testcheck[s1].click()
        		
        		p += 5
        		soal -= 1
        		nosoal += 1

        	time.sleep(3)
	        submit_button = WebDriverWait(driver, 10).until(
	            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
	        )

	        submit_button.click()

        	testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        	soals1 = [2,5,10,12,13]
        	soals3 = [6,7,13]

        	idx1 = 0
        	idx2 = 0 

        	p = 0
        	soal = 12
        	nosoal = 1
        	while soal:
        		if nosoal == soals1[idx1]:
        			s1 = random.choice([p+3,p+4])
        			testcheck[s1].click()
        			idx1 += 1
        		elif nosoal == soals3[idx2]:
        			s1 = random.choice([p,p+1,p+3,p+4])
        			testcheck[s1].click()
        			idx2 += 1
        		else:
        			s1 = random.choice([p,p+1])
        			testcheck[s1].click()
        		
        		p += 5
        		soal -= 1
        		nosoal += 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/WcMttu948f2jfUyM6")

        index+=1
        print("==================")
        print("index  : " + str(index))
        print("")
        print("baik  : " + str(baik))
        print("jelek : " + str(jelek))

        times-=1
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