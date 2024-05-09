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
driver.get("https://forms.gle/4i6sZWD6ptcy5xNL8")

nama = [
    "dimas zainul fathoni",
    "evelyn filma fidora",
    "ambar isna azizah",
    "bagas oktavia rahmanto",
    "dewi kumala sari",
    "asri kinanty ramandha",
    "evan yoga saputra ",
    "fahmi hidayat",
    "anggun budi cahyaningrum",
    "david tri wahyudi",
    "arifa salma chalid",
    "ainur maulana mashuda",
    "alwi maulana malik",
    "ana nuriyah",
    "fiqma dwi amuba",
    "muhammad hafidh raihan",
    "mohamad gaffa rizky fauzi",
    "mohamad naufal irmansyah",
    "himawan bagus prasetya",
    "himli mualim",
    "mochamad zulkifli",
    "ilham pambudi",
    "kurniawan nurhuda",
    "maya sofiana",
    "lutfi alfiansyah",
]

nim = [
    "190511630838",
    "190511630836",
    "190511630849",
    "190511630872",
    "190511630887",
    "190511630807",
    "190511630852",
    "190511630892",
    "190511630823",
    "190511630806",
    "190511630844",
    "190511630813",
    "190511630826",
    "190511630876",
    "190511630862",
    "190511630812",
    "190511630867",
    "190511630856",
    "190511630881",
    "190511630869",
    "190511630843",
    "190511630829",
    "190511630824",
    "190511630802",
    "190511630828",
]

offering = [
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A1",
    "A2",
    "A2",
    "A2",
    "A2",
    "A2",
    "A2",
    "A2",
    "A2",
    "A2",
    "A2",
    "A2",
]

nilai = [
    "B+",
    "A",
    "B+",
    "A",
    "A",
    "A-",
    "A-",
    "A",
    "A-",
    "A",
    "B+",
    "A-",
    "A",
    "A",
    "A",
    "A",
    "B+",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A-",
]

ip = [
    "3,83",
    "3,96",
    "3,77",
    "3,96",
    "3,91",
    "4",
    "3,77",
    "3,87",
    "3,91",
    "4",
    "3,91",
    "3,87",
    "3,91",
    "3,91",
    "3,91",
    "3,59",
    "3,83",
    "3,87",
    "3,57",
    "3,87",
    "3,59",
    "3,7",
    "3,79",
    "3,91",
    "3,83",
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
]

times = 25
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(nim[index])
        textboxes[2].send_keys(nilai[index])
        textboxes[3].send_keys(ip[index])
        textboxes[4].send_keys(telp[index])
        driver.implicitly_wait(4)

        dropdown[0].click()
        time.sleep(2)
        option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+offering[index]+"')]")

        option[1].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        t1 = [2,3,5,8,10,17,20]
        t2 = [3,5,6,9,10,11,16,17,20]
        t3 = [3,4,5,8,11,14,16]

        p = 0
        soal = 20
        nosoal = 1
        idx = 0
        while soal:
            if nosoal == t1[idx]:
                s1 = random.choice([p,p+1])
                radiobuttons[s1].click()
                idx += 1
            else:
                s1 = random.choice([p+2,p+3])
                radiobuttons[s1].click()

            soal -= 1
            nosoal += 1
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 19
        nosoal = 1
        idx = 0
        while soal:
            if nosoal == t2[idx]:
                s1 = random.choice([p,p+1])
                radiobuttons[s1].click()
                idx += 1
            else:
                s1 = random.choice([p+2,p+3])
                radiobuttons[s1].click()

            soal -= 1
            nosoal += 1
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        p = 0
        soal = 16
        nosoal = 1
        idx = 0
        while soal:
            if nosoal == t3[idx]:
                s1 = random.choice([p,p+1])
                radiobuttons[s1].click()
                idx += 1
            else:
                s1 = random.choice([p+2,p+3])
                radiobuttons[s1].click()

            soal -= 1
            nosoal += 1
            p += 4

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/4i6sZWD6ptcy5xNL8")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")

        times-=1
        print("times : " + str(times))
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