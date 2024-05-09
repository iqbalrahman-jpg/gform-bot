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
driver.get("https://docs.google.com/forms/d/1zgC19ewFH9XPljmfbUsTDVZNCRapoxrTQouV8brUsSg/edit")

semester = ["Semester II", "Semester IV", "Semester VI", "Semester VIII", "Semester X dan Keatas"]
semester = [5,6,7,8,9]

kelamin = [0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,]

email = [
    "anggasiregarp@gmail.com",
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
]

page = [
    [
        [4,3,2,4,3,3,1,4,4,2,4,3,3,3,2,4,3,3,1,4,3,2,3,3,4,3,2,3,3,3],
        [4,3,4,4,4,3,2,4,4,4,4,4,3,3,4,4,4,4,4,4,4,3,3,3,4,4,4,4,4,4],
        [3,4,4,4,4,3,4,3,4,4,4,4,4,3,4,4,4,4,4,4,4,4,3,3,4,4,4,4,2,4],
        [4,3,4,3,4,3,1,4,4,4,4,4,3,4,3,4,4,4,4,3,4,4,3,3,4,4,4,4,3,4],
        [3,2,4,3,3,4,4,4,2,3,3,3,3,3,3,4,3,3,3,2,2,3,4,1,4,3,3,3,2,4],
        [4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4],
        [4,4,4,4,3,4,4,4,4,4,4,3,3,3,4,3,3,3,2,3,3,2,4,2,4,3,3,4,3,3],
        [4,3,4,4,3,4,4,3,4,4,4,3,3,4,3,4,3,3,3,4,3,3,4,2,4,3,4,4,3,4],
        [4,3,3,4,4,2,4,4,4,4,4,4,3,3,4,4,4,4,4,4,4,3,3,2,4,4,4,4,4,4],
        [3,3,4,4,3,3,4,4,4,4,4,4,4,2,3,4,3,4,4,4,4,3,3,2,4,3,2,4,3,3],
        [4,4,4,4,3,4,4,4,4,3,4,3,3,3,3,4,2,3,4,4,4,4,3,2,4,4,4,3,4,3],
        [3,3,3,3,3,3,3,3,4,3,3,2,3,3,1,2,2,3,2,2,2,4,2,2,3,3,1,3,2,3],
        [2,2,3,2,3,4,2,2,1,1,4,3,1,3,2,4,2,2,4,2,1,2,3,2,4,3,2,2,2,2],
        [3,3,2,4,3,4,1,2,3,1,3,3,3,3,2,3,2,3,4,2,3,3,3,2,4,4,2,4,3,4],
        [4,4,4,4,3,4,4,4,3,3,2,4,3,2,2,1,2,3,3,1,3,4,3,4,4,2,2,4,2,2],
        [3,4,2,4,3,4,2,3,2,2,4,3,3,3,2,4,3,2,4,4,3,3,4,2,4,4,3,3,3,3],
        [4,4,4,2,2,3,2,3,4,2,4,4,3,3,3,3,4,3,4,3,2,3,3,2,4,4,3,4,3,4],
        [3,2,4,3,3,2,4,4,4,4,3,3,3,1,3,2,3,3,1,4,4,2,2,2,4,3,4,3,3,3],
    ], [
        [3,4,4,3,4,4,4,4,4,3,4,3,3,3,3,4,2,3,2,3,4,3,3,2,4,4,3,4,3,4],
        [2,4,2,1,4,4,2,3,4,2,4,4,4,3,4,3,4,3,2,4,4,2,2,3,4,3,2,4,3,4],
        [3,4,4,4,2,3,4,4,3,4,4,3,3,4,2,4,3,3,4,2,4,4,4,2,4,4,4,4,3,4],
        [2,3,2,1,4,3,3,4,2,2,3,3,2,3,4,4,3,2,2,1,1,3,2,3,4,3,4,3,4,3],
        [2,3,4,3,4,4,2,4,2,3,4,3,4,4,4,3,4,2,3,4,3,2,3,3,4,3,1,3,4,2],
        [2,3,4,1,3,2,4,4,2,2,3,3,4,3,3,4,3,2,1,3,2,2,2,4,3,2,3,3,2,4],
        [3,3,4,1,3,3,3,4,2,3,3,3,3,3,4,4,3,2,2,2,3,3,2,4,4,3,3,3,3,4],
        [4,2,2,2,4,3,1,3,2,2,4,3,2,4,2,3,3,2,2,3,2,2,1,3,4,3,3,3,3,3],
        [3,3,3,2,3,3,1,4,2,4,3,4,3,4,3,2,3,4,2,2,2,2,2,4,4,3,2,3,4,4],
        [2,3,3,4,4,4,4,4,3,3,3,3,3,3,3,4,3,4,2,4,3,4,3,4,4,3,4,3,3,3],
        [2,3,4,4,4,3,4,4,2,3,3,3,3,3,2,3,2,4,3,4,2,3,3,4,4,3,1,3,3,3],
        [3,3,3,1,2,2,4,4,2,2,2,3,3,3,2,4,2,2,3,2,1,2,2,2,4,4,3,2,2,2],
        [2,1,3,2,3,3,1,4,3,2,3,4,2,3,2,4,3,3,2,2,1,2,2,3,4,4,4,3,2,3],
        [3,2,4,1,3,3,4,4,2,2,3,3,1,3,1,4,3,2,2,3,2,2,2,3,4,3,4,3,3,3],
        [2,2,1,1,4,2,4,3,1,2,2,2,2,2,1,2,1,2,2,2,1,2,1,2,4,2,4,1,3,3],
        [3,4,4,4,3,4,4,4,4,2,3,3,4,3,4,4,4,4,2,3,3,4,4,4,3,4,3,3,4,4],
        [3,4,4,4,3,2,1,4,2,2,4,4,3,3,3,4,3,2,3,4,3,3,3,2,4,3,2,3,4,3],
        [2,3,4,1,3,3,3,4,2,2,3,3,1,3,3,3,2,2,2,3,2,2,2,3,4,3,4,3,3,2],
    ]
]

times = 1
index = 29

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        for i in range(2) :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            )

            submit_button.click()

            time.sleep(2)
            testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

            p = -1
            for x in range(18) :
                s1 = page[i][x][index] + p
                testcheck[s1].click()
                p += 4

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        time.sleep(2)
        kelas = random.choice([0,1,1,1,2,2,2,2,3,4])

        if kelas == 0:
            usia = random.choice([18,19,19,19,20])
        elif kelas == 1:
            usia = random.choice([20,21,21,22])
        elif kelas == 2:
            usia = random.choice([21,22,23])
        elif kelas == 3:
            usia = random.choice([21,22,23,24])
        else:
            usia = random.choice([24,25,26])

        time.sleep(2)
        dropdown[0].click()
        time.sleep(2)
        print(semester[kelas])

        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+semester[kelas]+"')]")
        option = driver.find_elements(By.XPATH, "//span[contains(text(), 'Semester')]")
        time.sleep(2)
        option[semester[kelas]].click()

        dropdown[1].click()
        time.sleep(2)
        options = driver.find_elements(By.XPATH, "//span[contains(text(), '"+str(usia)+" tahun')]")
        time.sleep(2)
        options[1].click()

        time.sleep(2)
        radiobuttons[kelamin[index]].click()

        time.sleep(2)
        textboxes[0].send_keys(email[index])

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/1zgC19ewFH9XPljmfbUsTDVZNCRapoxrTQouV8brUsSg/edit")

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