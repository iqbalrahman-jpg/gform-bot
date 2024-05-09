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
driver.get("https://bit.ly/physicsedugame")

nama = [
    "LEATHAN ALEXANDER PRABASWARA WIDODO",
    "BARUNA RAMADHAN SAPUTRA",
    "NADHIFA RAYYA FAHROZI",
    "CALISTA PUTRI HARNAN",
    "KHAIRUNNISA AULIA PUTRI",
    "TEGAR AJI PRASTYO DARMO",
    "NAIRA SHINTA FAUZIA",
    "JIHAN ADILLA HAKIM",
    "MIRZA ISWANDRIAN KAUTSAR",
    "MUHAMMAD FAIZIN",
    "LUNNA AZAHRA SEPTIANTI",
    "WINATHMA BINTANG MAHARANDHI",
    "MUHAMMAD ASHLAN ALI",
    "AMANDA NUR HIKMAH",
    "BEN GHAIRAN SUDAIS",
    "ANANDA QONITHA",
    "NIKA NAILA RAMADHANI",
    "ALHILAL ZANDI BASYIR KIAT",
    "IRFAN ABDI RAJASYAH",
    "RANCY REINANTI ANDREAN",
    "LUMIERE ALEXANDER PANJISWARA WIDODO",
    "TALYAA AYUMI SUBHAN",
    "MUHAMAD FAUZI ACHSAN",
    "LARISSA APRILA NAJWA",
    "YAZID IMTIAZ TARIDALA",
    "MIKAIL ALFATH PURNAMA",
    "MUHAMMAD SEPTIANDRI PUTRAMA ANNUR",
    "KHANSA CHAERUNNESA ASYIFA",
    "MUHAMMAD HAIKAL SULAEMAN",
    "SABILA SAVINA",
]

kelas = [
    "XI IPA 1",
    "XI IPA 4",
    "XI IPA 4",
    "XI IPA 2",
    "XI IPA 2",
    "XI IPA 2",
    "XI IPA 1",
    "XI IPA 2",
    "XI IPA 2",
    "XI IPA 4",
    "XI IPA 4",
    "XI IPA 4",
    "XI IPA 4",
    "XI IPA 3",
    "XI IPA 1",
    "XI IPA 4",
    "XI IPA 4",
    "XI IPA 1",
    "XI IPA 4",
    "XI IPA 2",
    "XI IPA 2",
    "XI IPA 4",
    "XI IPA 2",
    "XI IPA 2",
    "XI IPA 3",
    "XI IPA 1",
    "XI IPA 2",
    "XI IPA 3",
    "XI IPA 3",
    "XI IPA 4",
]

games = [
    "ChemCaper",
    "Kahoot!",
    "Kahoot!",
    "Anki",
    "CodeCombat",
    "TypingClub",
    "Anki",
    "Where in the World Is Carmen Sandiego?",
    "Math Blaster",
    "Where in the World Is Carmen Sandiego?",
    "Kahoot!",
    "Minecraft",
    "Rosetta Stone",
    "DragonBox",
    "Rosetta Stone",
    "Duolingo",
    "Duolingo",
    "GeoGuessr",
    "Duolingo",
    "DragonBox",
]

indexg = 0

pernah = 20
tidak = 10

benar1 = 15
salah1 = 15

benar2 = 13
salah2 = 17

times = 30
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0
        
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(kelas[index])
        textboxes[2].send_keys("SMA Cenderawasih 1 Jakarta")

        time.sleep(2)
        temp = random.randint(1,3)
        game = random.sample(["Mobile Legend", "PUBG", "DOTA", "Valorant", "Free Fire", "COD", "COC", "Genshin Impact", "UNO"], temp)

        for i in game:
            textboxes[3].send_keys(i)
            textboxes[3].send_keys(", ")

        time.sleep(2)
        if pernah != 0 and tidak != 0:
            pil = random.choice([8,9])
        elif pernah != 0 and tidak == 0:
            pil = 8
        elif pernah == 0 and tidak != 0:
            pil = 9

        time.sleep(2)
        radiobuttons[pil].click()
        if pil == 8:
            time.sleep(2)
            textboxes[4].send_keys(games[indexg])
            pernah -= 1
            indexg += 1
        else:
            textboxes[4].send_keys("-")
            tidak -= 1

        time.sleep(2)
        temp = random.randint(1,2)
        s1 = random.sample([0,1], temp)

        for i in s1:
            checkboxes[i].click()

        time.sleep(2)
        temp = random.randint(1,4)
        s2 = random.sample([4,5,6,7], temp)

        checkboxes[3].click()

        for i in s2:
            checkboxes[i].click()

        time.sleep(2)
        radiobuttons[random.choice([0,0,0,0,1])].click()
        radiobuttons[2].click()
        radiobuttons[random.choice([4,5,5,5,5,6,7])].click()

        time.sleep(2)
        if benar1 != 0 and salah1 != 0:
            satu = random.choice([1,2])
        elif benar1 != 0 and salah1 == 0:
            satu = 1
        elif benar1 == 0 and salah1 != 0:
            satu = 2

        if satu == 1:
            radiobuttons[13].click()
            radiobuttons[18].click()
            benar1 -= 1
        else:
            radiobuttons[random.choice([10,11,12,13,14])].click()
            radiobuttons[random.choice([15,16,17,19])].click()
            salah1 -= 1

        time.sleep(2)
        if benar2 != 0 and salah2 != 0:
            dua = random.choice([1,2])
        elif benar2 != 0 and salah2 == 0:
            dua = 1
        elif benar2 == 0 and salah2 != 0:
            dua = 2

        if dua == 1:
            radiobuttons[random.choice([20,21])].click()
            radiobuttons[28].click()
            benar2 -= 1
        else:
            radiobuttons[random.choice([20,21,22,23])].click()
            radiobuttons[random.choice([24,25,26,27,29])].click()
            salah2 -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://bit.ly/physicsedugame")

        index+=1
        print("==================")
        print("indexg : " + str(indexg))
        print("")
        print("pernah : " + str(pernah))
        print("tidak : " + str(tidak))
        print("")
        print("benar1 : " + str(benar1))
        print("salah1 : " + str(salah1))
        print("")
        print("benar2 : " + str(benar2))
        print("salah2 : " + str(salah2))
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