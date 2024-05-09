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

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSefZmblApEmXmgusD3_wMK_wXEhLb1pE4jCKFV5EWvtSxrH1w/formResponse")

email = [
    "syifaradifah@gmail.com",
    "aditferdinanda@gmail.com",
    "sitifauziyyahh@gmail.com",
    "reyhanutomowa@gmail.com",
    "salmaarowaya@gmail.com",
    "anggasiregarp@gmail.com",
    "putrikeancana@gmail.com",
    "rajawardanawan@gmail.com",
    "affifahh7@gmail.com",
    "shakapwijaya@gmail.com",
    "cynnarafisa@gmail.com",
    "monahfnna87@gmail.com",
    "mahendrejaa@gmail.com",
    "fryshta.eka823@gmail.com",
    "yanrasuryad@gmail.com",
    "rahannadi1@gmail.com",
    "sutisnayun@gmail.com",
    "ayulistyaan@gmail.com",
    "muhh.santosoo@gmail.com",
    "rudinurbaktii01@gmail.com",
    "ptrawiraw.an@gmail.com",
    "agungnugh@gmail.com",
    "dn.ramadhan@gmail.com",
    "dimas.purbo07@gmail.com",
    "nabilla.s.qolbi@gmail.com",
]

nama = [
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

kelamin = [1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,]

alamat = [
    "Jalan Prof. Sudarto",
    "Jl Prof. H. Soedarto SH",
    "Jalan Prof. Soedarto",
    "Karangayu",
    "Jalan Prof. Soedarto SH",
    "Tembalang",
    "Jl. Prof. H. Soedarto",
    "Banyumanik Kidul",
    "Jalan Prof. H. Soedarto",
    "Pleburan",
    "Jl Prof. Soedarto, S.H., Tembalang",
    "Banyumanik",
    "Pleburan",
    "Mlati",
    "Muktiharjo",
    "Gajahmungkur",
    "Jl. Imam Bardjo",
    "Tlogosari",
    "Jl. Imam Bardjo",
    "Jl. Prof. H. Soedarto",
    "Pedurungan",
    "Tlogosari",
    "Jl Prof. Soedarto, S.H., Tembalang",
    "Gajahmungkur",
    "Tlogosari",
]

#fakultas-prodi
fakultas = [
    "Fakultas Ilmu Budaya - Sastra Inggris",
    "Fakultas Ilmu Sosial dan Ilmu Politik - Ilmu Komunikasi",
    "Fakultas Teknik - Teknik Arsitektur",
    "Fakultas Ilmu Budaya - Sejarah",
    "Fakultas Ilmu Kelautan dan Perikanan - Ilmu Kelautan",
    "Departemen Teknologi Industri - Rekayasa Kimia Industri",
    "Fakultas Teknik - Teknik Sipil",
    "Fakultas Teknik - Teknik Sipil",
    "Fakultas Teknik - Teknik Elektro",
    "Fakultas Ekonomika dan Bisnis - Manajemen",
    "Fakultas Teknik - Teknik Mesin",
    "Departemen Teknologi Industri - Perancangan Mekanik",
    "Fakultas Ilmu Sosial dan Ilmu Politik - Ilmu Politik",
    "Fakultas Ilmu Sosial dan Ilmu Politik - Ilmu Politik",
    "Fakultas Teknik - Teknik Sipil",
    "Departemen Informasi dan Budaya - Informasi dan Humas",
    "Fakultas Teknik - Teknik Elektro",
    "Departemen Sipil dan Perencanaan - Perencanaan Tata Ruang dan Pertanahan",
    "Fakultas Ekonomika dan Bisnis - Akuntansi",
    "Departemen Bisnis dan Keuangan - Akuntansi Perpajakan",
    "Fakultas Ekonomika dan Bisnis - Akuntansi",
    "Fakultas Ilmu Budaya - Sejarah",
    "Fakultas Teknik - Teknik Sipil",
    "Fakultas Teknik - Teknik Arsitektur",
    "Fakultas Teknik - Teknik Sipil",

    ]
# Sarjana 3 diploma 2
strata = [3,3,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,3,2,3,3,3,3,2]

pendapatan = [
    "1.300.000",
    "1.5 JT",
    "1 - 1,5 juta",
    "2.1 Juta",
    "1 juta 400 ribu",
    "3 Juta",
    "1.2 - 1.5 jt", 
    "1.500.000",
    "3 Jutaan",
    "1.500.000",
    "3000000",
    "1 Juta",
    "1 Juta",
    "1 Juta 500",
    "1.900.000",
    "2 Juta", 
    "2.100.000",
    "1,5 Jutaan",
    "1.7 juta",
    "2.200.000",
    "2.300.000",
    "1.3 JT",
    "2 Jutaan",
    "1.5 JT",
    "2 Juta"
]

telp = [
    "081211906212",
    "081212784008",
    "081250284950",
    "081264718461",
    "081280281529",
    "081290475868",
    "081270348686",
    "082132447386",
    "087886158249",
    "081278010606",
    "087778433058",
    "085956060930",
    "087848003451",
    "0882008113306",
    "083838919000",
    "081511323691",
    "088294743163",
    "083181803358",
    "081331973192",
    "0895609625455",
    "085729979914",
    "085156051463",
    "085729213992",
    "087780590374",
    "081720592854",
]

times = 21
index = 4
benarvirus = 18
salahvirus = 3

try:
    while times:
        time.sleep(1)
        #Hardcoded logic
        test = 0

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        textboxes[0].send_keys(nama[index])
        umur = random.choice([19,20,21,22,19,20,21,22,19,20,21,22,23])
        textboxes[1].send_keys(umur)
        radiobuttons[kelamin[index]].click()
        textboxes[2].send_keys(alamat[index])
        univ = random.choice(["UNDIP","Undip","Universitas Diponegoro","undip","UNIVERSITAS DIPONEGORO","universitas diponegoro"])
        textboxes[3].send_keys(univ)
        textboxes[4].send_keys(fakultas[index])
        radiobuttons[strata[index]].click()

        if umur == 18:
            semester = 2
        elif umur  == 19:
            semester = random.choice([2,4])
        elif umur  == 20:
            semester = random.choice([2,4,4,4,6,6,6])
        elif umur  == 21:
            semester = random.choice([4,6,6,6,8,8,8])
        elif umur  == 21 or umur == 22:
            semester = random.choice([6,8])
        else:
            semester = 10

        textboxes[5].send_keys(semester)
        textboxes[6].send_keys(pendapatan[index])
        textboxes[7].send_keys(telp[index])
        wallet = random.choice([7,8,9,10])
        radiobuttons[wallet].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal
        
        p = 0
        soal = 6
        while soal:
            jawab = random.choice([p,p,p+1,p+1,p+2])
            pilihan[jawab].click()
            p += 3
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal
        
        if benarvirus != 0 and salahvirus != 0:
            time.sleep(2)
            jawab = random.choice([0,1,2,2,2,3])
            if jawab == 2:
                benarvirus -= 1
            else:
                salahvirus -=1
        elif benarvirus == 0:
            time.sleep(2)
            jawab = random.choice([0,1,3])
            salahvirus -= 1
        elif salahvirus == 0:
            time.sleep(2)
            jawab = 2
            benarvirus -= 1

        time.sleep(2)
        radiobuttons[jawab].click()

        p = 4
        soal = 5
        while soal:
            jawab = random.choice([p,p,p,p,p,p,p,p,p,p,p,p,p+1])
            pilihan[jawab].click()
            p += 2
            soal -= 1
            
        p = 4    
        penyebab = random.choice([p,p+1,p+1,p+1,p+1,p+1,p+1,p+1,p+1,p+1])
        radiobuttons[penyebab].click()
        p = 6
        gejala = random.choice([p,p,p,p,p,p,p,p,p,p,p,p,p,p+1])
        radiobuttons[gejala].click()
        p = 8
        potensi = random.choice([p,p+1,p+1,p+1,p+1,p+1,p+1,p+1,p+1,p+1])
        radiobuttons[potensi].click()

        p = 30
        soal = 4
        while soal:
            pilihan[p].click()
            p += 2
            soal -= 1

        p = 38
        pilihan[p+1].click()
        p = 10
        radiobuttons[p+2].click()
        p = 14
        bekas = random.choice([p,p,p,p,p,p,p,p,p,p,p,p,p,p+1])
        radiobuttons[bekas].click()

        p = 56
        soal = 2
        while soal:
            pilihan[p].click()
            p += 2
            soal -= 1

        x = 60
        soal = 2
        while soal:
            jawab = random.choice([x,x+1,x+1])
            pilihan[jawab].click()
            x += 2
            soal -= 1

        y = 64
        y = random.choice([y,y+1,y+1])
        pilihan[y].click()

        p = 16
        radiobuttons[p+1].click()
        p = 18
        radiobuttons[p+1].click()


        

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        pilihan = driver.find_elements("css selector", ".V4d7Ke")#soal di dalam soal
        time.sleep(3)
        p = 7
        soal = 2
        while soal:
            jawab = random.choice([p+3,p+4])
            pilihan[jawab].click()
            p += 6
            soal -= 1

        p = 19
        jawab = random.choice([p,p+1])
        pilihan[jawab].click()

        p = 25
        jawab = random.choice([p+3,p+4])
        pilihan[jawab].click()

        p = 31
        jawab = random.choice([p,p+1])
        pilihan[jawab].click()

        t = 0
        jawab = random.choice([t,t+1])
        testcheck[jawab].click()

        t = 5
        jawab = random.choice([t,t+1])
        testcheck[jawab].click()

        t = 10
        hari1 = random.choice([t,t+1,t+3,t+4])
        testcheck[hari1].click()

        t = 15
        if hari1 < 12:
            rusak = random.choice([t+3,t+4])
        else:
            rusak = random.choice([t,t+1])
        
        testcheck[rusak].click()

        t = 20
        if hari1 < 12:
            uang = random.choice([t+3,t+4])
        else:
            uang = random.choice([t,t+1])
        
        testcheck[uang].click()

        t = 25
        merusak = random.choice([t+3,t+4])
        testcheck[merusak].click()

        t = 30
        merusak2 = random.choice([t+3,t+4])
        testcheck[merusak2].click()

        t = 35
        if x == 60:
            menyemprot = random.choice([t,t+1])
        else:
            menyemprot = random.choice([t+3,t+4])
        
        testcheck[menyemprot].click()

        t = 40
        soal = 3
        while soal:
            jawab = random.choice([t+3,t+4])
            testcheck[jawab].click()
            t += 5
            soal -= 1

        t = 55
        soal = 2
        while soal:
            jawab = random.choice([t,t+1])
            testcheck[jawab].click()
            t += 5
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal
        p = 0
        menggunakan =  random.choice([p,p+1])
        radiobuttons[menggunakan].click()
        p = 3
        apakah = random.choice([p,p+1])
        radiobuttons[apakah].click()
        p = 6
        sendirian = random.choice([p,p,p,p+1,p+1,p+1,p+2])
        radiobuttons[sendirian].click()
        p = 9
        tertutup = random.choice([p,p+1,p,p+1,p,p+1,p+2])
        radiobuttons[tertutup].click()

        time.sleep(3)
        p = 12
        soal = 2
        while soal:
            jawab = random.choice([p,p+1,p,p+1,p,p+1,p+2])
            pilihan[jawab].click()
            p += 3
            soal -= 1

        p = 18
        jawab = random.choice([p,p+1,p+2])
        pilihan[jawab].click()

        p = 21
        soal = 2
        while soal:
            jawab = random.choice([p,p+1,p,p+1,p,p+1,p+2])
            pilihan[jawab].click()
            p += 3
            soal -= 1

        p = 12
        masker2 = random.choice([p,p+1,p+2])
        radiobuttons[masker2].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal
        
        p = 0
        if hari1 < 12:
            sekali = p+2
        else:
            sekali = random.choice([p,p+1])

        radiobuttons[sekali].click()

        p = 3
        if sekali > 1:
            jawab = random.choice([p])
        else:
            jawab = random.choice([p+2,p+1])

        radiobuttons[jawab].click()

        p = 6
        if sekali <= 1:
            jawab = random.choice([p,p+1])
        else:
            jawab = p+2

        radiobuttons[jawab].click()
        p = 9
        soal = 2
        while soal:
            jawab = random.choice([p,p+1,p,p+1,p+2])
            radiobuttons[jawab].click()
            p += 3
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        time.sleep(3)
        p = 0
        soal = 2
        while soal:
            jawab = random.choice([p,p+1,p,p+1,p,p+1,p+2])
            pilihan[jawab].click()
            p += 3
            soal -= 1

        p = 6
        if x == 61:
            pilihan[p+2].click()
        else:
            jawab = random.choice([p,p+1])
            pilihan[jawab].click()

        p = 9
        if y == 65:
            pilihan[p+2].click()
        else:
            jawab = random.choice([p,p+1])
            pilihan[jawab].click()
        
        p = 12
        jawab = random.choice([p,p+1,p+2])
        pilihan[jawab].click()

        p = 0
        mencampurkan = random.choice([p,p+1,p+2,p+1,p+2])
        radiobuttons[mencampurkan].click()

        p = 3
        if mencampurkan > 1:
            menyediakan = random.choice([p,p,p+1])
        elif mencampurkan == 1:
            menyediakan = 4
        else:
            menyediakan = 5
        
        radiobuttons[menyediakan].click()

        p = 6
        mencuci = random.choice([p,p,p+1,p+2])
        radiobuttons[mencuci].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()
        time.sleep(2)

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSefZmblApEmXmgusD3_wMK_wXEhLb1pE4jCKFV5EWvtSxrH1w/formResponse")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")

        times-=1
        print("times : " + str(times))
        print("benarvirus : " + str(benarvirus))
        print("salahvirus : " + str(salahvirus))
finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()