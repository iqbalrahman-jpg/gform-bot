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

link = "https://docs.google.com/forms/d/e/1FAIpQLScnbRExsdguhcUF14EVpzQV2oY12aSuDnqoK02_EhzFUqVsXQ/viewform?usp=pp_url"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

inisial = [
	"MTA",
    "AH",
    "RA",
    "BPW",
    "AN",
    "NA",
    "YN",
    "PKW",
    "Nma",
    "YP",
    "YAD",
    "BDM",
    "BCA", 
    "BS",
    "Mn",
    "SLB",
    "AK",
    "AC",
    "Fs",
    "DAC",
    "AM",
    "ARN",
    "FNP",
    "NEY",
    "BD",
    "SR",
    "AD",
    "SF",
    "RU",
    "SA",
    "ASP",
    "PK",
    "RPW",
    "ARN",
    "SKW",
    "CN",
    "MH",
    "MRF",
    "FEN",
    "YS",
    "RAw",
    "SA",
    "AN",
    "PS",
    "AR",
    "PW",
    "AN",
    "DR",
    "DP",
    "NSQ",

    "MDP",
    "RFP",
    "DSW",
    "AKJ",
    "RL",
    "RN",
    "DP",
    "AR",
    "IA",
    "ADW",
    "FN",
    "RA",
    "CAD",
    "AKS",
    "MFW",
    "DKW",
    "BSP",
    "RNS",
    "AF",
    "RA",
    "MD",
    "DK",
    "AS",
    "DY",
    "AM",
    "BS",
    "RPS",
    "DN",
    "RS",
    "MPL",
    "Ap",
    "Sus",
    "RR",
    "EP",
    "DS",
    "RF",
    "DP",
    "NIS",
    "RP",
    "TD",
    "YW",
    "NA",
    "YPW",
    "DC",
    "Rt",
    "MDu",
    "IK",
    "Dp",
    "BAN",
    "RAS",
]

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
    "rudinurbaktii01@gmail.com",
    "ptrawiraw.an@gmail.com",
    "agungnugh@gmail.com",
    "dn.ramadhan@gmail.com",
    "dimas.purbo07@gmail.com",
    "nabilla.s.qolbi@gmail.com",
    
    "mayadara.putri@gmail.com",
    "riofajar.pratama@gmail.com",
    "dewisariwijaya@gmail.com",
    "agungkusumajaya@gmail.com",
    "ratihsucilestari@gmail.com",
    "rizkipratamanugraha@gmail.com",
    "dwiprasetyautama@gmail.com",
    "arifrahmanhakim@gmail.com",
    "intanayulestari@gmail.com",
    "anandadwiwicaksono@gmail.com",
    "firanurhidayah@gmail.com",
    "ramaadityawardhana@gmail.com",
    "cintaayudewanti@gmail.com",
    "adekurniawansaputra@gmail.com",
    "mirafitrianawati@gmail.com",
    "diankusumawardani@gmail.com",
    "budisantosoputra@gmail.com",
    "rinanurainisari@gmail.com",
    "ahmadfauziakbar@gmail.com",
    "rizkyanandapratama@gmail.com",
    "mayadewisari@gmail.com",
    "dwikusumajaya@gmail.com",
    "agungsantosanugroho@gmail.com",
    "dilayulianiwati@gmail.com",
    "andimuhmmad.rizal@gmail.com",
    "budisantoso@gmail.com",
    "rinapermatasari@gmail.com",
    "diannugroho@gmail.com",
    "rudisetiawan@gmail.com",
    "mayaputrilestari@gmail.com",
    "andiprasetyo@gmail.com",
    "sintautamisari@gmail.com",
    "rizkyramadhan@gmail.com",
    "ekapuspitadewi@gmail.com",
    "dikasetiawanpratama@gmail.com",
    "ranifitriani@gmail.com",
    "ditoprasetya@gmail.com",
    "nisaindahsari@gmail.com",
    "rizalpratama@gmail.com",
    "tiaradewipuspita@gmail.com",
    "yantowibowo@gmail.com",
    "ninaanggraini@gmail.com",
    "yogaputrawijaya@gmail.com",
    "dinicahyani@gmail.com",
    "rakatriyana@gmail.com",
    "mayadewiutami@gmail.com",
    "indrakusuma@gmail.com",
    "devipuspitasari@gmail.com",
    "bimaadityanugraha@gmail.com",
    "rinaanggrainisari@gmail.com",
]

kelamin = [
    1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,
    1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1
]

positif = 4
negatif = 0

times = 4
index = 96

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = random.choice([0,1,1])

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(inisial[index])
        textboxes[1].send_keys(random.choice(["Jakarta", "jakarta", "DKI Jakarta", "dki jakarta", "DKI jakarta", "Jakarta Pusat", "Jakrata Timur", "Jakarta Barat", "Jakarta Selatan"]))
        if test == 1 : textboxes[2].send_keys(email[index])

        for i in range(4) :
            checkboxes[i].click()

        radiobuttons[kelamin[index]].click()
        radiobuttons[random.choice([2,3,4,4,5])].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if positif != 0 and negatif != 0 :
            pil = random.choice([0,1])
        elif positif != 0 and negatif == 0 :
            pil = 0
        elif positif == 0 and negatif != 0 :
            pil = 1

        if pil == 0 :
            time.sleep(2)
            p = 3
            for i in range(10) :
                if i == 5 :
                    s1 = random.choice([p-3, p-2, p-1, p, p+1, p+2, p+3])
                else :
                    s1 = random.choice([p, p+1, p+2, p+3, p+1, p+2, p+3, p+1, p+2, p+3])

                testcheck[s1].click()
                p += 7
            
            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p = 0
            for i in range(25) :
                s1 = random.choice([p, p+1, p+1, p+2, p+2, p+2])
                testcheck[s1].click()
                p += 3

            positif -= 1
        else :
            time.sleep(2)
            p = 0
            for i in range(10) :
                if i == 5 :
                    s1 = random.choice([p-3, p-2, p-1, p, p+1, p+2, p+3])
                else :
                    s1 = random.choice([p, p+1, p+2, p, p+1, p+2, p, p+1, p+2, p+3])
                    
                testcheck[s1].click()
                p += 7
            
            time.sleep(3)
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p = 0
            for i in range(25) :
                s1 = random.choice([p, p, p, p+1, p+1, p+2])
                testcheck[s1].click()
                p += 3

            negatif -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
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