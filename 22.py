from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe4Egonc8MY8VTIesvCr0UfP34XfY-ZFBbLEEJT45S_oRCjkg/viewform?entry.328553192=6379")

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
]

password = [
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "jajanan127",
    "jajanan127",
    "jajanan127",
    "jajanan127",
    "jajanan127",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "kuismu123",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    "081331973192",
    
]
times = 1
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        option = driver.find_elements(By.XPATH, "//span[contains(text(), 'login')]")

        option[1].click()

        time.sleep(2)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(email[index])

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
        )

        submit_button.click()

        time.sleep(2)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(password[index])





        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        # )

        # submit_button.click()

        # driver.implicitly_wait(4)
        # driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe4Egonc8MY8VTIesvCr0UfP34XfY-ZFBbLEEJT45S_oRCjkg/viewform?entry.328553192=6379")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        print("times : " + str(times))

finally:
	# driver.quit()
    print("berhasil")

    # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
    # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
    # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

    # time.sleep(3)
    # submit_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
    # )

    # submit_button.click()