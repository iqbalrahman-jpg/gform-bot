from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://forms.gle/g9Zb43Fui2t96LYp7")

email = [
"mtianur001@gmail.com",
"alihasn.01.10@gmail.com",
"risfebri11@gmail.com",
"budprasety@gmail.com",
"aryonugh@gmail.com",
"nanissa0110@gmail.com",
"yahnugrah@gmail.com",
"putriptr0110@gmail.com",
"nandayundaa1@gmail.com",
"yudipradan01@gmail.com",
"yulayund1@gmail.com",
"byumerta1@gmail.com",
"Bellandayu01@gmail.com",
"budsuryant01@gmail.com",
"nela.mirra@gmail.com",
"dwa.lingga10@gmail.com",
"alffiantoro@gmail.com",
"annicsaa@gmail.com",
"fataahxdewa@gmail.com",
"diahcindy03@gmail.com",
"attakmajid@gmail.com",
"azzarinrst@gmail.com",
"fabiannadeo@gmail.com",
"niaejuliana@gmail.com",
"bayudwiganara@gmail.com",
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
"ardyantoputra43@gmail.com",
"puttr.wirawan@gmail.com",
"agungnugrh1@gmail.com",
"daniramadhan1982@gmail.com",
"dimapurb0@gmail.com",
"nabillasyaqila.q@gmail.com"
]

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
    "Nabilla Syaqila Qolbi"
]

# 6 cowok 7 cewek
kelamin = [ 7,6,7,6,6,7,6,7,7,6,7,6,7,6,7,6,6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7,6,7,7,6,7,6,6,7,7,6,6,6,6,6,6,7,]

mkn = [
"Sop Buntut",
"Mie Gacoan",
"Ayam Goreng",
"Nasi Goreng",
"Nasi Uduk",
"Nasi Padang",
"Sate Ayam",
"Martabak",
"Rendang",
"Bakso",
"Nasi Kuning",
"Nasi pecel",
"gacoan",
"MCD",
"Bubur ayam",
"Takoyaki",
"Ayam Geprek",
"Bebek purnama",
"Soto Makasasar",
"KFC",
"Bubur Ayam Jakarta",
"Tahu tek",
"Soto Daging",
"McDonald's",
"Nasi goreng 69",
"yoshinoya",
"Bakmie Goreng",
"Mie Gacoan",
"Pepper Lunch",
"Ikan bakar",
"Ayam Penyet",
"Mie Wizmie",
"Siomay",
"Sate taichan",
"Gule kambing",
"nasi bakar",
"Burger King",
"Suprek",
"Sushi",
"Soto Betawi",
"Terangbulan",
"Ayam bakar",
"Bebek songkem",
"KFC",
"richeese factory",
"Marugame",
"Soto Madura",
"Rawon",
"Gacoan",
"Yoshinoya",
]


notelp = [
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

times = 50
index = 0




try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        textboxes[0].send_keys(email[index])
        radiobuttons[0].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    
        radiobuttons[0].click()

        time.sleep(2)

        radiobuttons[2].click()

        time.sleep(2)

        radiobuttons[4].click()

        time.sleep(2)

        radiobuttons[6].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        

        p = 0
        soal = 2
        while soal:
            jawab = random.choice([p,p+1,p+2])
            radiobuttons[jawab].click()
            soal -= 1
            p += 3

        textboxes[1].send_keys(mkn[index])

        apk = random.choice([6,7,8])
        radiobuttons[apk].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        radiobuttons[apk-6].click()
        
        p = 0
        soal = 3
        while soal:
            jawab = random.choice([p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 15
        soal = 3
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 30
        soal = 3
        while soal:
            jawab = random.choice([p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 45
        kp1 = random.choice([p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
        testcheck[kp1].click()
        p = 50
        kp2 = random.choice([p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
        testcheck[kp2].click()
        p = 55
        if kp1 == 46:
            kp3 = p+1
        else:
            kp3 = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])

        testcheck[kp3].click()
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        radiobuttons[apk-6].click()

        p = 0
        rf1 = random.choice([p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
        testcheck[rf1].click()
        p = 5
        rf2 = random.choice([p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
        testcheck[rf2].click()
        p = 10
        rf3 = random.choice([p,p+1,p+1,p+2,p+3,p+3])
        testcheck[rf3].click()
        p = 15
        rf4 = random.choice([p,p,p,p+1,p+1,p+1,p+2])
        testcheck[rf4].click()
        # rp1-3
        p = 20
        soal = 3
        while soal:
            jawab = random.choice([p,p,p,p+1,p+1,p+1,p+2,p+3])
            testcheck[jawab].click()
            soal -= 1
            p += 5
        # rp 4-5
        p = 35
        soal = 2
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 45
        rk1 = random.choice([p,p,p,p+1,p+1,p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
        testcheck[rk1].click()
        p = 50
        if rk1 == p or rk1 == p+1:
            rk2 = random.choice([p,p+1])
        else :
            rk2 = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])

        testcheck[rk2].click()
        p = 55
        if rk1 == p or rk1 == p+1:
            rk3 = random.choice([p,p+1])
        else :
            rk3 = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])

        testcheck[rk3].click()
        p = 60
        if rk1 == p or rk1 == p+1:
            rk4 = random.choice([p,p+1])
        else :
            rk4 = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])

        testcheck[rk4].click()

        p = 65
        rk5 = random.choice([p,p,p+1,p+1,p+2,p+3])
        testcheck[rk5].click()

        p = 70
        soal = 4
        while soal:
            jawab = random.choice([p,p,p+1,p+1,p+2,p+3])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 90
        rs1 = random.choice([p,p+1,p+2])
        testcheck[rs1].click()

        p = 95
        soal = 2
        while soal:
            jawab = random.choice([p,p+1,p+2,p+3,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 105
        rs4 = random.choice([p,p,p,p+1,p+1,p+1,p+2])
        testcheck[rs4].click()

        p = 110
        soal = 2
        while soal:
            jawab = random.choice([p,p,p,p+1,p+1,p+1,p+2])
            testcheck[jawab].click()
            soal -= 1
            p += 5
        
        p = 120
        rps3 = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
        testcheck[rps3].click()
        p = 125
        rps4 = random.choice([p,p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
        testcheck[rps4].click()
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        radiobuttons[apk-6].click()

        p = 0
        soal = 4
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 20
        if kp1 == 46:
            dt1 = random.choice([p,p+1])
        else:
            dt1 = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
        
        testcheck[dt1].click()

        p = 25
        soal = 5
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 50
        soal = 3
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 65
        soal = 3
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        p = 80
        soal = 5
        while soal:
            jawab = random.choice([p+1,p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        radiobuttons[apk-6].click()

        p = 0
        soal = 3
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        radiobuttons[apk-6].click()

        p = 0
        soal = 3
        while soal:
            jawab = random.choice([p+2,p+3,p+3,p+3,p+4,p+4,p+4])
            testcheck[jawab].click()
            soal -= 1
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[1].send_keys(nama[index])
        p = 0
        usia = random.choice([p,p+1,p+1,p+1,p+2,p+2,p+3])
        radiobuttons[usia].click()
        radiobuttons[kelamin[index]].click()
        if usia == p or usia == p+1:
            sekolah = random.choice([9,10,10,11,11,11])
        else:
            sekolah = random.choice([10,11,11,11,12])

        radiobuttons[sekolah].click()

        if usia ==  p:
            pekerjaan = random.choice([15,15,18,19,19,20])
        else:
            if sekolah == 10:
               pekerjaan = random.choice([17,18,19]) 
            else:
                pekerjaan = random.choice([16,17,18,19])

        radiobuttons[pekerjaan].click()
        textboxes[2].send_keys(notelp[index])


        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/g9Zb43Fui2t96LYp7")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        print("times : " + str(times))

finally:
	# driver.quit()
    print("berhasil")