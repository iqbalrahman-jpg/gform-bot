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
driver.get("https://forms.gle/PDeQqcKmPK1YDnLj7")

email = [
    "monahfnna87@gmail.com",
    "mahendrejaa@gmail.com",
    "fryshta.eka823@gmail.com",
    "sutisnayun@gmail.com",
    "cintaayudewanti@gmail.com",
    "ayulistyaan@gmail.com",
    "muhh.santosoo@gmail.com",
    "ptrawiraw.an@gmail.com",
    "dn.ramadhan@gmail.com",
    "mirafitrianawati@gmail.com",
    "dilayulianiwati@gmail.com",
    "dimas.purbo07@gmail.com",
    "mayadewisari@gmail.com",
    "nabilla.s.qolbi@gmail.com",
    "mayadara.putri@gmail.com",
    "riofajar.pratama@gmail.com",
    "dewisariwijaya@gmail.com",
    "agungkusumajaya@gmail.com",
    "ratihsucilestari@gmail.com",
    "arifrahmanhakim@gmail.com",    
    "diankusumawardani@gmail.com",
    "intanayulestari@gmail.com",
    "anandadwiwicaksono@gmail.com",
    "rinanurainisari@gmail.com",
    "firanurhidayah@gmail.com",
]

nama = [
    "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
    "Fryshta Eka Nabilla",
    "Sutisna Ayuni",
    "Cinta Ayu Dewanti",
    "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Rina Permata Sari",
    "Dani Ramadhan",
    "Mira Fitriana Wati",
    "Dila Yuliani Wati",
    "Dimas Purbo",
    "Maya Dewi Sari",
    "Nabilla Syaqila Qolbi",
    "Maya Dara Putri",
    "Rio Fajar Pratama",
    "Dewi Sari Wijaya",
    "Agung Kusuma Jaya",
    "Ratih Suci Lestari",
    "Arif Rahman Hakim",
    "Dian Kusuma Wardani",
    "Intan Ayu Lestari",
    "Ananda Dwi Wicaksono",
    "Rina Nuraini Sari",
    "Fira Nur Hidayah",
]

alamat = [
    "Cileunyi Wetan",
    "Bandung Selatan",
    "Soreang",
    "Bandung Timur",
    "Cimahi",
    "Cibiru Hilir",
    "Lembang",
    "Cileunyi Kidul",
    "Cibiru",
    "Cileunyi",
    "Soreang",
    "Bandung",
    "Lembang",
    "Baleendah",
    "Arcamanik",
    "Soreang",
    "Cimahi",
    "Bandung",
    "Bandung Barat",
    "Ciparay",
    "Cimahi",
    "Cibiru Hilir",
    "Lembang",
    "Cibiru Hilir",
    "Dayeuhkolot",
]

telp = [
    "081659261105",
    "082136378661",
    "081640301967",
    "083806763847",
    "089509885576",
    "082985961237",
    "081137328130",
    "084843988039",
    "083138422620",
    "089045039379",
    "082138078906",
    "088159411881",
    "089474988296",
    "088530527344",
    "085109323557",
    "080470542685",
    "083273133185",
    "081850452479",
    "081211522212",
    "081212521008",
    "081250243950",
    "08126123461",
    "0812802851529",
    "08129041231868",
    "0812703123516",
]
#0 laki 1 perempuan
kelamin = [1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,1,]

times = 25
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(email[index])

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        usia = random.choice([2,2,3,3,3,3,3,4,4,4,5,6])

        if usia == 2:
            pekerjaan = 7
            pendidikan = random.choice([13,14])
            pendapatan = 19
        elif usia == 3:
            pekerjaan = random.choice([7,7,7,7,8,9,10])
            pendidikan = random.choice([14,15,16,17])
            pendapatan = random.choice([19,20,21])
        else:
            pekerjaan = random.choice([8,9,9,10])
            pendidikan = random.choice([14,15,16,17])
            pendapatan = random.choice([19,20,21,21,21])

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        textboxes[1].send_keys(nama[index])
        textboxes[2].send_keys(telp[index])
        driver.implicitly_wait(4)
        textarea[0].send_keys(alamat[index])
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        radiobuttons[usia].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[pendidikan].click()
        radiobuttons[pendapatan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox 

        time.sleep(2)
        radiobuttons[0].click()
        mengenal = random.randint(0,6)
        sering = random.randint(9,11)

        temp = random.randint(1,5)
        random_item = random.sample([0,1,2,3,4], temp)

        time.sleep(2)
        radiobuttons[mengenal].click()
        radiobuttons[sering].click()
        driver.implicitly_wait(4)

        for i in random_item :
           checkboxes[i].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 19
        while soal :
            s1 = random.choice([p,p+1,p+2,p+3,p+3,p+4,p+4,p+2,p+3,p+3,p+4,p+4])
            testcheck[s1].click()
            p += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 19
        while soal :
            s1 = random.choice([p,p+1,p+2,p+3,p+3,p+4,p+4,p+2,p+3,p+3,p+4,p+4])
            testcheck[s1].click()
            p += 5
            soal -= 1

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

        time.sleep(40)

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/PDeQqcKmPK1YDnLj7")

        index+=1
        print("==================")
        print("index : " + str(index))
        # print("")

        times-=1
        print("times : " + str(times))
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