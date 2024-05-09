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

link = "https://forms.gle/WWeEN3ZVXWrh3Zi48"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

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
]

kelamin = [
	1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,
]

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        usia = random.choice([2,3,4,5])

        if usia == 2 :
            pendidikan = random.choice([6,7])
        elif usia == 3:
            pendidikan = random.choice([6,7,7,7,8])
        else :
            pendidikan = random.choice([6,7,7,7,7,8])
        
        if usia == 2 and pendidikan == 6 :
            pekerjaan = 10
        elif usia == 2 :
            pekerjaan = random.choice([12,13,14])
        elif usia == 3 and kelamin[index] == 1 :
            pekerjaan = random.choice([11,12,13,14])
        elif usia == 3 :
            pekerjaan = random.choice([12,13,14])
        elif kelamin[index] == 1:
            pekerjaan = random.choice([11,12,13,14])
        else :
            pekerjaan = random.choice([12,13,14])
        
        if pekerjaan == 10 :
            pendapatan = 15
        elif pekerjaan == 13 or pekerjaan == 14 :
            pendapatan = random.choice([16,17,18,19])
        else :
            pendapatan = random.choice([15,16,17])

        sosmed = random.choice([20,21,22,23,24])

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        textboxes[0].send_keys(email[index])

        radiobuttons[usia].click()
        radiobuttons[kelamin[index]].click()
        radiobuttons[pendidikan].click()
        radiobuttons[pekerjaan].click()
        radiobuttons[pendapatan].click()
        radiobuttons[sosmed].click()

        time.sleep(2)
        p = 3
        for i in range(27) :
            s1 = p 
            testcheck[s1].click()
            p += 5

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        # print("  : " + str())
        # print("")
        
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