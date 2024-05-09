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
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScLFrjYm1GLcxsGeiT3B4wk42q0ehuq-8a3Mg0juviUNqOCKw/formResponse")

nama = [
    "Radja Andika Satriana",
    "Della Faradillah",
    "Fauzan Kama",
    "Agus Syahidah",
    "Henny Mufti",
    "Ridhwan Izhar",
    "Raelita Rini",
    "Rizki Rizka Rachma",
    "Sofyan Sapto",
    "Fika Niroha",
    "Ariesta Melinda",
    "Annisa Ervya",
    "Fatahillah Kresno",
    "Fitrawati Jordan",
    "Syahrul Sihombing",
    "Bunga Hardianti",
    "Gita Khairunisa",
    "Kenneth Laurensia",
    "Maureen Tesa Junaidi",
    "Tubagus Lendy Octaviana",
    "Megawati Fadhillah",
    "Praditia Triashafira",
    "Ferani Nurkhayati",
    "Sylvia Esra Syahidah",
    "Umi Avrilla Abelardo",
    "Roy Chairinnisa",
    "Anindita Munikasari",
    "Dede Mubarak",
    "Yandra Kinandatsani",
    "Amalia Zakia",
    "Roy Sjukri",
    "Luna Zain",
    "Haris Wardhani",
    "Adi Oktavianty",
    "Wildan Bisri",
    "Siska Nurfalah",
    "Adityo Ficky Kusumawardhani",
    "Cardito Verev",
    "Mario Ainina",
    "Eka Rifqi",
    "Ari Virani",
    "Rahmah Riyadie",
    "Fariz Atarita",
    "Bytta Keviati",
    "Revo Setiarini",
    "Astrid Mazaya",
    "Ogie Ardiansyah",
    "Adityo Nadya",
    "Caesariana Amalia",
    "Syavira Ryanda",
    "Evi Amanda",
    "Aggil Julius Azhar",
    "Lusiana Adzkiya Nuraini",
    "Fitra Putri",
    "Azmi Octaviana",
    "Richard Caroline",
    "Sofyan Maretta",
    "Ismi Harkart",
    "Wiena Mulyana",
    "Tiari Luna Prihatiwi",
    "Asri Fatimah",
    "Hana Harkart",
    "Marini Elleonora",
    "Mario Syabantika",
    "Christy Tanuwijaya",
    "Chaerul Anggraini",
    "Agustin Maratun Raisid",
    "Reynaldi Alvino Pambudi",
    "Zara Nugraha",
    "Alditio Hadian",
    "Saliha Naenggolan",
    "Indra Fandy Adhitama",
    "Beckley Listyani",
    "Fildzah Aurealia",
    "Aprilia Tessa Acbar",
    "Ismail Zulaeha",
    "Redian Kurniawan",
    "Aburachman Ayudhani",
    "Elvin Sugiyanto",
    "Pratiwi Siahainenia",
    "Kharisma Virani",
    "Anindyanti Hilmawan",
    "Herdaru Ayuriza",
    "Meirani Falah",
    "Gleny Maryanti",
    "Praditia Asriandari",
    "Dian Sharifa",
    "Dicky Imani",
    "Imam Persadani",
    "Rinaldy Octaza",
    "Yosafat Pradipta",
    "Ratih Hafizh",
    "Rifqy Eda",
    "Nadiya Septefani",
    "Mirza Subekti",
    "Kevin Candraditya",
    "Ekka Haikal Alghifari",
    "Wan Ciptasari",
    "Chusnur Jamilah Husein",
    "Prameswari Atsila",
    "Putrima Kresno",
    "Reksa Ariyadi Ashim",
    "Satrya Krisnanto",
    "Aldi Nisrina",
    "Andika Sali",
    "Febby Deyuri Larassati",
    "Marvel Reksa Ernando",
    "Fauzi Singgih Kartikasari",
    "Sutrisno Christine",
    "Yusuf Mirza",
    "Fauzia Himawan",
    "Dhia Joan",
    "Doni Fikri",
    "Mark Julianto",
    "Wildan S",
    "Karima Halim",
    "Widya Atarita",
    "Vina Disya Septiani",
    "Tessa Irwanto",
    "Alditio Mufti",
    "Garin Suputra",
    "Gleny Desca Ernando",
    "Laras Imelda Tiodimar",
    "Handayani Aisi",
    "Anita W",
    "Renita Kurniansyah",
    "Citra Naenggolan",
    "Karina Prawita",
    "Reza Fajria",
    "Dyah Varensia",
    "Bob Triashafira",
    "Adrian Laurensia",
    "Nadiya Raissa Kartika",
    "Fariz Larascaesara",
    "June Hadian",
    "Shabrina Hamdan",
    "Monica Virgina",
    "Farqy Pratama",
    "Azrul Farandy",
    "Arthur Hafizh",
    "Fikri Chairinnisa",
    "Sendy Syabantika",
    "Tubagus Aulia",
    "Nadia Mandarasari",
    "Retno Rachmansyah",
    "Vito Jaelani",
    "Rifanny Mirza",
    "Revi Anisa",
    "Derilandry Tanjung",
    "Magdalena Tio",
    "Zianira Kusuma",
    "Anugrah Saputri",
    "Bayu Irwanto",
    "Aliriza Abdullah Rini",
    "Septania Ervya",
    "Dwi Joan",
    "Anisha Sayoga",
    "Tyas Maulidah",
    "Ismail Fadhlir Dinantika",
    "Fadhlir Fhadriani",
    "Arfan Nurullah",
    "Yoan Sari",
    "Reynaldi Tanuwijaya",
    "Anisha Wulandari",
    "Benazir Reny Anindita",
    "Dikposa Pawarti",
    "Pandu Abrianto",
    "June Risyad",
    "Jeremiah Arieska",
    "Anton Syahrul Arieska",
    "Fajar Syafjulianti",
    "Radja Mark Admianawidiastuti",
    "Reny Haddad",
    "Novia Simorangkir",
    "Geraldi Isham",
    "Syahdian Sinuka",
    "Devito Reza Nezarani",
    "Adi Virani",
    "Choirunnisa Arsya Hermala",
    "Sianne Keviati",
    "Fitri S",
    "Yola Halim",
    "Pratiwi Ariana",
    "Dara Farizi",
    "Axel Destrya",
    "Indra Aprilicia",
    "Tesa Natasya",
    "Ovienov Zulaeha",
    "Michael Cardinata",
    "Ressy Noerani",
    "Mochammad Yandra Rais",
    "Derisa Abelardo",
    "Inneke Noor",
    "Frisca Octaza",
    "Maruto Ridhwan Umaeroh",
    "Beckley Keviati",
    "Mutiara Tobing",
    "Surya Arrivalda Siahainenia",
    "Arrivaldi Usra",
    "Julian Sulistyaningra",
    "Winda Wirawan",
    "Andika Ray Rahmasari",
    "Umi Novitasari",
    "Sujendro Satrio",
    "Nindya Chaerunnisa",
    "Abdullah Sujendro Tambunan",
    "Jhon Jeremiah Hilmawan",
    "Nurul Candraini",
    "Andika Sucipto",
    "Taufik Subiarsono",
    "Pratama Aminullah",
    "Anas Mulyana",
    "Arrum Suheryanto",
    "Tresna Adisanyoto",
    "Herdaru Prahasti",
    "Sulalah Silmi Saraswati",
    "Rendy Idayu",
    "Diandra Nurhazrati",
    "Janiar Umaeroh",
    "Inneke Ayudyah Fachrully",
    "Mestika Afini",
    "Shara Natasya",
    "Priyohadi Julianto",
    "Prieskha Saputri",
    "Permana Dyarini",
    "Sakti Labas",
    "Sari Aprisilia",
    "Humam Naradhipa",
    "Marisa Pradipta",
    "Mariana Ossi Andjani",
    "Reksa Juwita",
    "Mustafid Setiawan",
    "Dwira Ramsihs",
    "Prameswari Santi",
    "Dicky Mubarak Irwansyah",
    "Bony Ulfa",
    "Titiek Pemana",
    "Sigit Mulyanti",
    "Amar Ihsanuddin",
    "Rianita Lesihantika",
    "Safirah Maryanti",
    "Aldo Rahmawati",
    "Lendy Rooswati",
    "Ilham Adhim Mazaya",
    "Hizrian Ihatrayudha",
    "Ratu Nabila Sabrina",
    "Aldo Fhadriani",
    "Sulalah Idayu",
    "Riryparas Sugiyanto",
    "Muthia Dewanta",
]

kelamin = [ 
    0,1,0,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,1,0,
    0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,
    1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,
    1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,
    1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,
    0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,1,0,
    0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,
    0,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,1,1,1
]

notelp = [
    "0852555775",
    "0899555947",
    "0878555545",
    "0856555207",
    "0859555013",
    "0853555851",
    "0811555635",
    "0899555975",
    "0811555299",
    "0878555156",
    "0878555822",
    "0856555879",
    "0853555337",
    "0838555990",
    "0896555136",
    "0852555534",
    "0878555604",
    "0838555573",
    "0878555428",
    "0854555699",
    "0854555073",
    "0838555036",
    "0858555237",
    "0838555910",
    "0838555769",
    "0816555176",
    "0819555777",
    "0878555525",
    "0853555394",
    "0838555865",
    "0878555825",
    "0852555190",
    "0878555683",
    "0838555504",
    "0853555270",
    "0897555935",
    "0838555007",
    "0858555029",
    "0878555525",
    "0838555114",
    "0838555169",
    "0855555626",
    "0811555935",
    "0896555411",
    "0878555842",
    "0878555484",
    "0857555339",
    "0878555582",
    "0858555705",
    "0817555080",
    "0878555694",
    "0817555597",
    "0878555417",
    "0854555619",
    "0878555656",
    "0855555740",
    "0878555482",
    "0818555081",
    "0897555999",
    "0852555799",
    "0838555860",
    "0897555946",
    "0898555253",
    "0819555551",
    "0856555398",
    "0878555551",
    "0898555519",
    "0838555521",
    "0815555836",
    "0899555403",
    "0878555598",
    "0838555254",
    "0878555986",
    "0838555302",
    "0878555396",
    "0897555368",
    "0878555230",
    "0878555984",
    "0838555381",
    "0856555691",
    "0838555629",
    "0815555476",
    "0878555471",
    "0838555526",
    "0878555536",
    "0818555175",
    "0898555682",
    "0838555431",
    "0854555721",
    "0838555661",
    "0838555103",
    "0816555672",
    "0811555117",
    "0852555794",
    "0857555512",
    "0899555195",
    "0838555703",
    "0878555700",
    "0814555760",
    "0811555767",
    "0838555587",
    "0853555857",
    "0878555098",
    "0856555401",
    "0838555242",
    "0838555322",
    "0816555157",
    "0896555445",
    "0855555802",
    "0838555521",
    "0878555909",
    "0856555486",
    "0813555336",
    "0898555173",
    "0896555898",
    "0838555914",
    "0817555787",
    "0838555149",
    "0838555804",
    "0854555962",
    "0816555246",
    "0815555217",
    "0878555225",
    "0855555900",
    "0878555683",
    "0855555306",
    "0838555422",
    "0838555925",
    "0899555231",
    "0854555934",
    "0899555461",
    "0899555341",
    "0852555346",
    "0878555187",
    "0817555317",
    "0838555688",
    "0855555075",
    "0838555686",
    "0838555521",
    "0859555316",
    "0812555477",
    "0853555676",
    "0819555784",
    "0878555732",
    "0878555271",
    "0817555400",
    "0838555211",
    "0878555361",
    "0878555126",
    "0811555924",
    "0896555202",
    "0898555401",
    "0857555212",
    "0838555250",
    "0838555098",
    "0859555320",
    "0853555212",
    "0838555869",
    "0814555358",
    "0838555491",
    "0838555551",
    "0878555675",
    "0812555218",
    "0812555853",
    "0878555162",
    "0878555152",
    "0878555600",
    "0838555412",
    "0838555778",
    "0898555437",
    "0838555268",
    "0838555426",
    "0896555499",
    "0878555449",
    "0853555600",
    "0819555882",
    "0813555060",
    "0858555214",
    "0838555096",
    "0838555917",
    "0878555623",
    "0898555634",
    "0838555908",
    "0818555461",
    "0899555758",
    "0853555835",
    "0878555467",
    "0878555085",
    "0878555860",
    "0838555691",
    "0898555894",
    "0897555668",
    "0838555719",
    "0817555742",
    "0899555094",
    "0896555123",
    "0878555516",
    "0898555205",
    "0818555684",
    "0819555585",
    "0897555205",
    "0897555759",
    "0856555220",
    "0855555740",
    "0878555879",
    "0858555158",
    "0878555059",
    "0816555432",
    "0878555175",
    "0859555419",
    "0857555984",
    "0838555394",
    "0818555105",
    "0819555682",
    "0838555214",
    "0878555100",
    "0899555030",
    "0852555338",
    "0812555915",
    "0819555033",
    "0838555121",
    "0838555607",
    "0818555892",
    "0811555681",
    "0817555711",
    "0838555221",
    "0853555215",
    "0816555043",
    "0855555623",
    "0838555729",
    "0838555671",
    "0818555544",
    "0838555533",
    "0838555910",
    "0878555507",
    "0899555518",
    "0815555316",
    "0838555522",
    "0854555922",
    "0858555417",
    "0852555751",
    "0853555755",
    "0817555551",
    "0819555068",
    "0896555554",
    "0838555709",
    "0858555222",
    "0878555133",
    "0858555865",
    "0878555958",
]

index  = 128
times  = 122
try:
    while times:
        time.sleep(2)
        #Hardcoded logic
        test = 0

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(notelp[index])

        radiobuttons[kelamin[index]].click()
        usia = random.choice([2,3,4,2,3,4,2,3,4,5,6])
        radiobuttons[usia].click()

        if usia == 2 :
            pendidikan = 7
            profesi = 11
        elif usia == 6 :
            pendidikan = random.choice([9,10])
            profesi = random.choice([13,14,13,14,16])
        elif usia == 3 :
            pendidikan = random.choice([7,8])
            if kelamin[index] == 1 :
                profesi = random.choice([12,12,12,12,13,13,14,15,16])
            else :
                profesi = random.choice([12,12,12,12,13,13,14,16])
        else :
            pendidikan = random.choice([7,8,9])
            if kelamin[index] == 1 :
                profesi = random.choice([13,14,15,16])
            else :
                profesi = random.choice([13,14,16])

        radiobuttons[pendidikan].click()
        radiobuttons[profesi].click()

        if profesi <= 12 :
            pendapatan = random.choice([17,18])
        elif profesi == 15 :
            pendapatan = random.choice([17,18,19])
        elif profesi == 14 :
            pendapatan = random.choice([19,20,21])
        else :
            pendapatan = random.choice([18,19,20,19,20])

        radiobuttons[pendapatan].click()
        

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
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping



        p = 0
        soal = 14
        while soal :
            jawaban = random.choice([p+2,p+3,p+4,p+3,p+4])
            testcheck[jawaban].click()
            p += 5
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

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping



        p = 0
        soal = 5
        while soal :
            jawaban = random.choice([p+2,p+3,p+4,p+3,p+4])
            testcheck[jawaban].click()
            p += 5
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

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping



        p = 0
        soal = 3
        while soal :
            jawaban = random.choice([p+2,p+3,p+4,p+3,p+4])
            testcheck[jawaban].click()
            p += 5
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

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping



        p = 0
        soal = 2
        while soal :
            jawaban = random.choice([p+2,p+3,p+4,p+3,p+4])
            testcheck[jawaban].click()
            p += 5
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

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping



        p = 0
        soal = 3
        while soal :
            jawaban = random.choice([p+2,p+3,p+4,p+3,p+4])
            testcheck[jawaban].click()
            p += 5
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

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = 0
        soal = 7
        while soal :
            jawaban = random.choice([p+2,p+3,p+4,p+3,p+4])
            testcheck[jawaban].click()
            p += 5
            soal -= 1

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScLFrjYm1GLcxsGeiT3B4wk42q0ehuq-8a3Mg0juviUNqOCKw/formResponse")

        index+=1
        print("==================")
        
        times-=1
        print("index  = " + str(index))
        print("times  = " + str(times))
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