from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeCwBSbWtjtoGoQJew_jrTL-4C4VfGskKviO4RV-HJTUwLWvw/viewform?usp=sf_link")


nama = ["Eka Wahyu",
"Yuli Setiawan",
"Eko Wijaya",
"Yuni Nafisah",
"Prita agustina",
"Naufal Ardiansyah",
"Bagus Rahmad",
"Hana Anissa Herian",
"Heraldy Gunawan",
"Budi Santoso",

"Bagus Hariawan",
"Dwi Panca",
"Okto Devano",
"Olivia Niken",
"Yazid Hasbilluh Kurniawan",
"faradilla nina",
"Shabir Maulana",
"Sarah Husaini",
"Josephine Anindya",
"Erfina Pratiwi",

"Argo Prasetyawan",
"Salma Azizah",
"Faradilla Aulia",
"Dimas Wahyu",
"Regina April",
"Agis Prasetya",
"Ardy Riski",
"Muhammad Fadlan",
"Septinia Kurniawan",
"Damar Eka",

"Fredinan Puan",
"Amanda Bella Putri",
"Bambang Suhatmoyo",
"Kairaini Aliesa",
"Lika Arletta",
"Arjuna Ghafur",
"Damar Hafidzhuan",
"Lista Kamilla",
"Sadiva Pratiwi",
"Hermanto Caisar",

"Windy Cantika",
"Stephani Amanda Safitri",
"Ardyanto Putra Wardhana",

]

# laki 0 perempuan 1
kelamin = [ 1,1,0,1,1,0,0,1,0,0,
            0,0,0,1,0,1,0,1,1,1,
            0,1,1,0,1,0,0,0,1,0,
            0,1,0,1,1,0,0,1,1,0,
            1,1,0
]
#kurang 10
times = 43
index = 0

try:
    while times:
        time.sleep(29)
        #Hardcoded logic
        test = 0
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(nama[index])
        radiobuttons[kelamin[index]].click()
        umur = random.choice([2,3,4,5,2,3,4,5,2,3,4,5,6])
        radiobuttons[umur].click()

        if umur < 3:
            pekerjaan = random.choice([8,9,11,11])
        else:
            if kelamin == 1:
                pekerjaan = random.choice([7,8,9,10])
            else :
                pekerjaan = random.choice([7,8,9])

        radiobuttons[pekerjaan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 4
        while soal:
            jawab = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5
        
        p = 20
        kesulitan = random.choice([p,p+1,p+2,p+3,p+4])
        testcheck[kesulitan].click()
        p = 25
        kompetitor = random.choice([p,p+1,p+2,p+3,p+4])
        testcheck[kompetitor].click()
        p = 30
        soal = 4
        while soal:
            jawab = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 2
        while soal:
            jawab = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 10
        if kompetitor < 27:
            bersaing = random.choice([p,p+1,p+2])
        else :
            bersaing = random.choice([p+2,p+3,p+4])

        testcheck[bersaing].click()

        p = 15
        soal = 7
        while soal:
            jawab = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        p = 0
        kebutuhan = random.choice([p,p+1,p+2,p+3,p+4])
        testcheck[kebutuhan].click()
        p = 5
        kualitas = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
        testcheck[kualitas].click()
        p = 10
        mengenal = random.choice([p,p+1,p+2,p+3,p+4])
        testcheck[mengenal].click()
        p = 15
        soal = 2
        while soal:
            jawab = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 25
        membandingkan = random.choice([p,p+1,p+2,p+3,p+4,p+3,p+4])
        testcheck[membandingkan].click()
        p = 30
        memutuskan = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
        testcheck[memutuskan].click()
        p = 35
        pengalaman = random.choice([p,p+1,p+2,p+3,p+4,p+3,p+4])
        testcheck[pengalaman].click()
        p = 40
        soal = 2
        while soal:
            jawab = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeCwBSbWtjtoGoQJew_jrTL-4C4VfGskKviO4RV-HJTUwLWvw/viewform?usp=sf_link")

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