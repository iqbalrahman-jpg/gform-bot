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
driver.get("http://bit.ly/42ThqCm")

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
    "Budi Santoso",
    "Rina Permata Sari",
    "Dian Nugroho",
    "Rudi Setiawan",
    "Maya Putri Lestari",
    "Andi Prasetyo",
    "Sinta Utami Sari",
    "Rizky Ramadhan",
    "Eka Puspita Dewi",
    "Dika Setiawan Pratama",
    "Rani Fitriani",
    "Dito Prasetya",
    "Nisa Indah Sari",
    "Rizal Pratama",
    "Tiara Dewi Puspita",
    "Yanto Wibowo",
    "Nina Anggraini",
    "Yoga Putra Wijaya",
    "Dini Cahyani",
    "Raka Triyana",
    "Maya Dewi Utami",
    "Indra Kusuma",
    "Devi Puspitasari",
    "Bima Aditya Nugraha",
    "Rina Anggraini Sari",
]

telp = [
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

    "085719303458",
    "085694967112",
    "087771034388",
    "085691005874",
    "081316619265",
    "081807757031",
    "087884291109",
    "087734232521",
    "083831978961",
    "085817281922",

    "085772067944",
    "085780272919",
    "085711503322",
    "083899226851",
    "081296660892",
    "083879828932",
    "085328666691",
    "085716463668",
    "081310967642",
    "089602615268",

    "085740420953",
    "085786378946",
    "089929069068",
    "082299476447",
    "083870192449",
    "087730874992",
    "081381810073",
    "085777737195",
    "081219725497",
    "082310667325",

    "081291723604",
    "089788617285",
    "083876928695",
    "081903140419",
    "085641900173",
    "087749986541",
    "085697561906",
    "089606196660",
    "082221184819",
    "087774894040",

    "089691111149",
    "089781140247",
    "089637520605",
    "081286306638",
    "087887672122",
    "081261351555",
    "085692270650",
    "081284714591",
    "082220406216",
    "081574018719",
]

prodi = [
4,7,7,5,9,5,9,5,6,4,6,6,8,4,4,7,10,9,9,4,6,9,3,8,5,7,4,4,6,5,6,5,4,3,10,5,7,8,9,6,7,7,4,8,5,4,6,4,10,3,3,10,7,7,8,9,3,3,8,9,8,10,9,9,7,3,7,4,10,10,6,5,10,5,10,6,7,6,6,10,3,10,8,4,6,3,3,8,7,4,9,9,6,10,8,9,3,5,3,3
]

# laki 0 perempuan 1
kelamin = [
    1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,
    1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1
    ]

angkatan20 = 33
angkatanlain = 17

kost = 39
laink = 11

prestasi = 0
nonprestasi = 50

positif = 50
negatif = 0

times = 50
index = 50

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if angkatan20 != 0 and angkatanlain != 0:
            pil1 = random.choice([0,1])
        elif angkatan20 != 0 and angkatanlain == 0:
            pil1 = 0
        elif angkatan20 == 0 and angkatanlain != 0:
            pil1 = 1

        if pil1 == 1:
            tahun = random.choice([12,13,15,16])
            angkatanlain -= 1
        else:
            tahun = 14
            angkatan20 -= 1

        time.sleep(2)
        if kost != 0 and laink != 0:
            pil2 = random.choice([0,1])
        elif kost != 0 and laink == 0:
            pil2 = 0
        elif kost == 0 and laink != 0:
            pil2 = 1

        if pil2 == 0:
            tinggal = 17
            kost -= 1
        else:
            tinggal = random.choice([18,19,20])
            laink -= 1

        time.sleep(2)
        if prestasi != 0 and nonprestasi != 0:
            pil3 = random.choice([0,1])
        elif prestasi != 0 and nonprestasi == 0:
            pil3 = 0
        elif prestasi == 0 and nonprestasi != 0:
            pil3 = 1

        if pil3 == 0:
            jalur = 30
            prestasi -= 1
        else:
            jalur = random.choice([27,28,29])
            nonprestasi -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(telp[index])

        time.sleep(2)
        radiobuttons[prodi[index]].click()
        radiobuttons[kelamin[index]].click()
        radiobuttons[tahun].click()
        radiobuttons[tinggal].click()
        radiobuttons[22].click()
        radiobuttons[random.choice([24,25])].click()
        radiobuttons[jalur].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        if positif != 0 and negatif != 0 :
            pil4 = random.choice([0,2])
        elif positif != 0 and negatif == 0 :
            pil4 = 0
        elif positif == 0 and negatif != 0 :
            pil4 = 2

        if pil4 == 0:
            positif -= 1
        else:
            negatif -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = pil4
        for i in range(29) :
            s1 = random.choice([p,p+1])
            radiobuttons[s1].click()
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("http://bit.ly/42ThqCm")

        index+=1
        print("==================")
        print("angkatan20 = " + str(angkatan20))
        print("angkatanlain = " + str(angkatanlain))
        print("")
        print("kost = " + str(kost))
        print("laink = " + str(laink))
        print("")
        print("prestasi = " + str(prestasi))
        print("nonprestasi = " + str(nonprestasi))
        print("")
        print("positif = " + str(positif))
        print("negatif = " + str(negatif))
        print("")
        
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