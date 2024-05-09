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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeFXPEPIAp51nJ3dA2vw5mmmJyxPHXn66lXuLxSRX2PcdelUw/viewform")

email = [
    "yulisetiawan746@gmail.com",
"ekow05047@gmail.com",
"yuninafisah9@gmail.com",
"agustinaprita304@gmail.com",
"naufalardiansyah651@gmail.com",
"hanaanissa33@gmail.com",
"heraldygunawan@gmail.com",
"ekawahy099@gmail.com",
"bagusrahmad262@gmail.com",
"budisantos0@gmail.com",

"dwipancaa65@gmail.com",
"f.ninadilaa@gmail.com",
"erfinpp34@gmail.com",
"yahhszid@gmail.com",
"bagushari931@gmail.com",
"jose.anindya@gmail.com",
"srhhusaini@gmail.com",
"shabirmaulana23@gmail.com",
"ooliviya96@gmail.com",
"permatagita588@gmail.com",


"argopraz@gmail.com",
"azizahsalma237@gmail.com",
"faradillaaulia62@gmail.com",
"dimaswahyu4769@gmail.com",
"aprilregina663@gmail.com",
"agisprasetya171@gmail.com",
"arddyriski@gmail.com",
"fadlaanm24@gmail.com",
"kurniaseptinia@gmail.com",
"damarek099@gmail.com",

"freddinan35@gmail.com",
"manndabeel99@gmail.com",
"bambang.suhatmoyo@gmail.com",
"aliesakairaini@gmail.com",
"lika.arletta@gmail.com",
"arjuna.gh9@gmail.com",
"dhafidzuann@gmail.com",
"listakamila299@gmail.com",
"sadivapratiwi0@gmail.com",
"hermantocaisar@gmail.com",

"windycantika13@gmail.com",
"stephaniamanda67@gmail.com",
"ardyantoputra43@gmail.com",
"carolineerindra@gmail.com",
"saputranabil157@gmail.com",
"azzahrakhansa006@gmail.com",
"naufalazwin85@gmail.com",
"riskarahmawati400@gmail.com",
"rohmatubaidillah3@gmail.com",
"setiawannugraha372@gmail.com",

"raishaanastasya003@gmail.com",
"bumirakha35@gmail.com",
"fikkydevano119@gmail.com",
"lesmanadewa831@gmail.com",
"ilyasafadil23@gmail.com",
"belindainggridina@gmail.com",
"putri.bella.14.06.06@gmail.com",
"meydinamargaretha@gmail.com",
"muhammadwawan727@gmail.com",
"budimanyahya71@gmail.com",

"yahyabudiman72@gmail.com",
"farhannurrahman92@gmail.com",
"siscapratiwii62@gmail.com",
"fiorenahmad4@gmail.com",
"aliframadhan5098@gmail.com",
"divanipermatasari@gmail.com",
"anggadewangga089@gmail.com",
"putrisasya55@gmail.com",
"selmanabila30@gmail.com",
"iwansetyawann4@gmail.com",

"rafifadhill36@gmail.com",
"putrajonathan397@gmail.com",
"karinatauliya@gmail.com",
"diyastramahendra@gmail.com",
"agungprastyaa@gmail.com",
"aulialitahani@gmail.com",
"sifanadakwurnia@gmail.com",
"hanisalsabola@gmail.com",
"denisptrayaa@gmail.com",
"adelinagriska0@gmail.com",

]

nama = [
"Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Mutia Ayu Nur",

    "Bayu Danang Merta",
    "Bellanda Clara Ayunda ",
    "Budi Suryanto",
    "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Yuli Ayunda Dewi",

    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Attaka Majid",

    "Putri Keancana",
    "Raja Putra Wardanawan",
    "Affifah Rahman Nabila",
    "Shaka Kurnia Wijaya",
    "Cynara Nafisah",
    "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
    "Fryshta Eka Nabilla",
    "Yanuar Suryadi",
    "Angga Siregar Putra",

    "Sutisna Ayuni",
    "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Nayla Chelsea Anggita",
    "Putra Rudi Wirawan Nurbakti",
    "Fani Cintya A",
    "Rasya Gibran Sulistyo",
    "M. Fadil Achmad",
    "Delima Ariesta",
    "Rayhan Adi Wicasa",

    "Muhammad Iqbal Ramadhan",
    "Bagas Putra Ariel",
    "Afifah Renu Hasanah",
    "Reno Naufal Wijaya",
    "Putri Agustina Wahyuni",
    "Syifa Putri Ramadhani",
    "Muhammad Nur Faqih Mahmud",
    "Jesica Putri Ayu Deviana",
    "Immada Clarissa Putri Anjani",
    "Rayhan Cakra Lesmana",

    "Cintya Cindy Ayu Nissa",
    "Bella Nur Rahma",
    "Budi Ahmad Putra Laksa",
    "Cilla Cintya Chania",
    "M. Irsyad Gunawan Agung",
    "Fikri Budi Ramadhan",
    "Indah Budi Pratiwi",
    "Intan Putri Aprillia",
    "Rensky Maulana Ibrahim",
    "Achmad Billy Maulana",

    "Paradista Chania Aysala",
    "Tiara Andini Azzizah",
    "Yoga Syahrul Anugrah",
    "Bella Permata Sari",
    "Rifky Wahyu Saputra",
    "Fadhil Achmad Saputro",
    "Arya Perdana Kusuma Wicasa",
    "Siti Rahma Aulia Sarah",
    "Aldi Maulana Akbar",
    "Franky Kusuma Adelardo",

    "Rayhan Bagus Ghifari",
    "Marshanda Clarista Putri Bianca",
    "Muhammad Gilang Ramadhan",
    "Anggraeni Ratna Safitri",
    "Kayla Naisya Faradila",
    "Safa Fitri Aulia",
    "Famelya Anggita Novianti",
    "Revan Malik Ibrahim",
    "Adriansyah Qolbi Muhammad",
    "Nadilla Carina Fionita",
    "Yuli Setiawan",
    
"Eko Wijaya",
"Yuni Nafisah",
"Prita agustina",
"Naufal Ardiansyah",
"Hana Anissa Herian",
"Heraldy Gunawan",
"Eka Wahyu",
"Bagus Rahmad",
"Budi Santoso",

]

kelamin = [
    0,1,0,0,1,0,1,1,0,1,
    0,1,0,1,0,0,1,0,1,1,
    1,0,1,0,1,0,1,0,1,0,
    1,0,1,0,1,1,0,1,0,0,
    0,1,0,1,0,1,0,0,1,0,
    0,0,1,0,1,1,0,1,1,0,
    1,1,0,1,0,0,1,1,0,0,
    1,1,0,1,0,0,0,1,0,0,
    0,1,0,1,1,1,1,0,0,1,
    1,0,1,1,0,1,0,1,0,0,
    
]





index  = 3
times  = 28
positif = 22
negatif = 6

try:
    while times:
        time.sleep(2)
        #Hardcoded logic
        test = 0

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea


        # textboxes[0].send_keys(email[index])
        textarea[0].send_keys(nama[index])
        textboxes[0].send_keys("7")


        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()

        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        
        if positif != 0 and negatif != 0 :
            bantuan = random.choice([0,1,1,1,1,1])
            if bantuan == 1 :
                positif -= 1
            else :
                negatif -= 1
        elif positif == 0 :
            bantuan = 0
            negatif -= 1
        elif negatif == 0 :
            bantuan = 1
            positif -= 1

        if bantuan == 1 :
            p = 0
            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 3
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p,p+1,p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 3
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            x = 0
            soal = 1
            while soal :
                jawaban = random.choice([x+2,x+3])
                x += 4
                soal -= 1

            checkboxes[jawaban].click()

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 3
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([x,x+1])
                checkboxes[jawaban].click()
                x += 4
                soal -= 1
            
            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1
        else :
            p = 0
            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 3
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p,p+1,p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 3
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            x = 0
            soal = 1
            while soal :
                jawaban = random.choice([x,x+1])
                checkboxes[jawaban].click()
                x += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 3
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([x+2,x+3])
                checkboxes[jawaban].click()
                x += 4
                soal -= 1
            
            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1
            


    
        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            )

        submit_button.click()

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah


        if bantuan == 1 :
            p = 0
            
            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 4
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 3
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1,p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 7
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1
        else :
            p = 0
            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 4
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 3
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1,p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 1
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 7
            while soal :
                jawaban = random.choice([p,p+1])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

            soal = 2
            while soal :
                jawaban = random.choice([p+2,p+3])
                radiobuttons[jawaban].click()
                p += 4
                soal -= 1

        time.sleep(2)

        time.sleep(3)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeFXPEPIAp51nJ3dA2vw5mmmJyxPHXn66lXuLxSRX2PcdelUw/viewform")

        index+=1
        print("==================")
        
        times-=1
        print("index  = " + str(index))
        print("times  = " + str(times))
        print("positif  = " + str(positif))
        print("negatif  = " + str(negatif))
        time.sleep(5)





finally:
    # driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # radiobuttons = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        # textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

        # time.sleep(1)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()