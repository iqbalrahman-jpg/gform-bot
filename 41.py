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

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("profile-directory=Profile 13")

driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe4Egonc8MY8VTIesvCr0UfP34XfY-ZFBbLEEJT45S_oRCjkg/viewform")

email = [
    "muhh.iqbalnazh@gmail.com",
    "rezaachm.fauz@gmail.com",
    "iqbal2.rah01@gmail.com",
    "budiman.yhs@gmail.com",
    "intan.aprilia@gmail.com",
    "renu.wulamb@gmail.com",
    "trouble.renuwu@gmail.com",
    "nurhasanaren1@gmail.com",
    "bagasa.ariel07@gmail.com",
    "rhanlesmna@gmail.com",
]

times = 10
index = 0
idx = 1
idxx = 1

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if idx == 10:
            idx = 0

        option = driver.find_elements("css selector", ".jZZ5Nd")#kebawah

        # print(len(option))
        option[0].click()

        time.sleep(20)
        driver.switch_to.window(driver.window_handles[idxx])
        time.sleep(2)

        # radiobuttons = driver.find_elements(By.XPATH, "//span[contains(text(), 'Azzarin')]")
        radiobuttons = driver.find_elements("css selector", ".JDAKTe")#kebawah
        radiobuttons[idx].click()

        time.sleep(20)

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        textboxes[0].send_keys(email[index])
        textboxes[1].send_keys("6379")
        textboxes[2].send_keys("-")
        driver.implicitly_wait(4)

        p = 4
        soal = 9
        while soal:
            testcheck[p].click()
            p += 5
            soal -= 1

        testcheck[54].click()

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
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe4Egonc8MY8VTIesvCr0UfP34XfY-ZFBbLEEJT45S_oRCjkg/viewform")

        index+=1
        idx += 1
        idxx += 1
        print("==================")
        print("index : " + str(index))
        print("idx   : " + str(idx))
        print("idxx  : " + str(idxx))
        # print("")

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