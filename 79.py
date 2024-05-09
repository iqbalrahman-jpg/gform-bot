from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import random

profil = ["Profile 7", "Profile 8", "Profile 9", "Profile 10"]


inisial = [
    "AH",
    "RF",
    "BP",
    "AN",
    "NA",
    "YN",
    "PA",
    "NA",
    "YP",
    "MA",
    "BM",
    "BA",
    "BS",
    "NM",
    "SL",
    "AK",
    "AC",
    "FS",
    "DC",
    "YA",
    "RR",
    "FP",
    "NY",
    "BD",
    "SR",
    "AF",
    "SF",
    "RU",
    "SA",
    "AM",
    "PK",
    "RW",
    "AR",
    "SP",
    "CN",
    "MF",
    "RM",
    "FE",
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
]

instagram = [
    "@_alihasan_",
    "@riskiafebrianti253",
    "@budi.prasetyo",
    "@aryo_nh",
    "@nanaannisaqs",
    "@yahyanugrahaa",
    "@ptraay",
    "@nanditha_salsa",
    "@reky.wahyudi.7771",
    "@mutiaayunur_",
    "@bayu.dana.merta",
    "@bellaayunda88",
    "@budisuryanto78",
    "@nella_mirandaa",
    "@sadewaputralingga",
    "@alfianasiskuntoro",
    "@chacuik_11",
    "@kokosadewafatahilah",
    "@ayucindydiah",
    "@ayun_da2458",
    "@6302.ri",
    "@fabianputra720",
    "@ninaekayuliana",
    "@dhbayuaji",
    "@syifa.radifaa",
    "@aditferdinand_",
    "@stifauziyah",
    "@utomorayhan",
    "@arwayassershahin",
    "@attaka456",
    "@putriaulia1911",
    "@rajabwardana",
    "@rhmaff_",
    "@shaka_wp",
    "@cynaranafisah",
    "@mona_fina",
    "@rafli_m.s",
    "@frysta_putri",
]

#0 cowo 1 cewe
kelamin = [0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1]

index = 0
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get("https://forms.gle/3ojjEE9VWBjdMbkU8")

        if i == len(profil) - 1:
            times = 8
        else:
            times = 10

        idx = 1
        idxx = 1

        while times:
            time.sleep(2)

            if idx == 10:
                idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(10)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[idx].click()

            time.sleep(10)
            # ================================================================================
            
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
            checkboxes[0].click()

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
            usia = random.randint(19,23)
            domisili = random.randint(2,6)
            pekerjaan = random.choice([10,11,12,13,13,13,13,13,13,13])

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian

            textboxes[0].send_keys(inisial[index])
            textboxes[1].send_keys(usia)
            textboxes[2].send_keys(telp[index])
            textboxes[3].send_keys(instagram[index])
            driver.implicitly_wait(4)

            radiobuttons[8].click()
            radiobuttons[kelamin[index]].click()
            radiobuttons[domisili].click()
            time.sleep(2)
            radiobuttons[8].click()
            radiobuttons[pekerjaan].click()
            radiobuttons[15].click()
            radiobuttons[16].click()

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

            radiobuttons[0].click()

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
                )

            submit_button.click()

            driver.implicitly_wait(4)
            driver.get("https://forms.gle/3ojjEE9VWBjdMbkU8")

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))

        driver.quit()
        
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
            # kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            # kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            # if len(kirims1) != 0 :
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            #     )
            # else:
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            #     )

            # submit_button.click()