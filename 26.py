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
driver.get("https://forms.gle/MnmtA3sN3x5r5ptw6")

email = [
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

#0 laki, 1 perempuan
kelamin = [1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,]

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        pekerjaan = random.choice([2,2,2,3,3,3,4,5,6,7])
        pernah = random.choice([16,16,17])

        if pernah == 16:
            akan = random.choice([18,18,18,19])
        else :
            akan = 18

        textboxes[0].send_keys(email[index])
        driver.implicitly_wait(4)
        radiobuttons[kelamin[index]].click()
        radiobuttons[pekerjaan].click()
        
        if pekerjaan == 2 or pekerjaan == 3:
            time.sleep(2)
            radiobuttons[8].click()
            s2 = 12
            radiobuttons[12].click()
        else :
            time.sleep(2)
            s1 = random.choice([9,10,11])
            radiobuttons[s1].click()
            if pekerjaan == 7:
                time.sleep(2)
                s2 = random.choice([12,13])
                radiobuttons[s2].click()
            else:
                if s1 != 11:
                    time.sleep(2)
                    s2 = random.choice([13,14])
                    radiobuttons[s2].click()
                else:
                    time.sleep(2)
                    s2 = random.choice([13,14,15])
                    radiobuttons[s2].click()

        radiobuttons[pernah].click()
        radiobuttons[akan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)
        rad = driver.find_elements("css selector", ".AB7Lab")

        if pekerjaan == 7:
            time.sleep(2)
            p1 = random.choice([3,4,5,6])
            rad[p1].click()
            p1 = 8
            soal = 3
            while soal:
                s1 = random.choice([p1,p1+1,p1+2,p1+3,p1+4,p1+5])
                rad[s1].click()
                soal -= 1
                p1 += 7

            p2 = random.choice([56,57,57,57,58,58,58,59,60,61])
            rad[p2].click()

            if p2 < 59 :
                p1 = 63
                soal = 3
                while soal:
                    s1 = random.choice([p1,p1+1,p1+2,p1+2,p1+3,p1+4])
                    rad[s1].click()
                    soal -= 1
                    p1 += 7
            else:
                p1 = 63
                soal = 3
                while soal:
                    s1 = random.choice([p1+2,p1+3,p1+4,p1+5])
                    rad[s1].click()
                    soal -= 1
                    p1 += 7

            time.sleep(2)
            p3 = random.choice([112,113,114,115,116,117,118])
            rad[p3].click()

            if p3 < 115:
                p1 = 119
                soal = 2
                while soal:
                    s1 = random.choice([p1,p1+1,p1+2,p1+3])
                    rad[s1].click()
                    soal -= 1
                    p1 += 7
            else:
                p1 = 119
                soal = 2
                while soal:
                    s1 = random.choice([p1+2,p1+3,p1+4,p1+5,p1+6])
                    rad[s1].click()
                    soal -= 1
                    p1 += 7

            time.sleep(2)
            if akan == 18:
                p1 = 154
                soal = 4
                while soal:
                    s1 = random.choice([p1+2,p1+3,p1+4,p1+5,p1+6])
                    rad[s1].click()
                    soal -= 1
                    p1 += 7
            else :
                p1 = 154
                soal = 4
                while soal:
                    s1 = random.choice([p1,p1+1,p1+2,p1+3])
                    rad[s1].click()
                    soal -= 1
                    p1 += 7
        else:
            time.sleep(2)
            if s2 == 12 or s2 == 13:
                p1 = random.choice([3,4,5,6])
                rad[p1].click()
                p1 = 8
                soal = 3
                while soal:
                    s1 = random.choice([p1,p1+1,p1+2,p1+3,p1+4,p1+5])
                    rad[s1].click()
                    soal -= 1
                    p1 += 7

                p2 = random.choice([56,57,57,57,58,58,58,59,60,61])
                rad[p2].click()

                if p2 < 59 :
                    p1 = 63
                    soal = 3
                    while soal:
                        s1 = random.choice([p1,p1+1,p1+2,p1+2,p1+3,p1+4])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7
                else:
                    p1 = 63
                    soal = 3
                    while soal:
                        s1 = random.choice([p1+2,p1+3,p1+4,p1+5])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7

                time.sleep(2)
                p3 = random.choice([112,113,114,115,116,117,118])
                rad[p3].click()

                if p3 < 115:
                    p1 = 119
                    soal = 2
                    while soal:
                        s1 = random.choice([p1,p1+1,p1+2,p1+3])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7
                else:
                    p1 = 119
                    soal = 2
                    while soal:
                        s1 = random.choice([p1+2,p1+3,p1+4,p1+5,p1+6])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7

                time.sleep(2)
                if akan == 18:
                    p1 = 154
                    soal = 4
                    while soal:
                        s1 = random.choice([p1+2,p1+3,p1+4,p1+5,p1+6])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7
                else :
                    p1 = 154
                    soal = 4
                    while soal:
                        s1 = random.choice([p1,p1+1,p1+2,p1+3])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7
            else:
                p1 = random.choice([3,4,5,6])
                rad[p1].click()
                p1 = 8
                soal = 3
                while soal:
                    s1 = random.choice([p1,p1+1,p1+2,p1+3,p1+4,p1+5])
                    rad[s1].click()
                    soal -= 1
                    p1 += 7

                p2 = random.choice([58,59,60,61,62])
                rad[p2].click()

                if p2 < 59 :
                    p1 = 63
                    soal = 3
                    while soal:
                        s1 = random.choice([p1,p1+1,p1+2,p1+2,p1+3,p1+4])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7
                else:
                    p1 = 63
                    soal = 3
                    while soal:
                        s1 = random.choice([p1+3,p1+4,p1+5,p1+6])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7

                time.sleep(2)
                p3 = random.choice([114,115,116,117,118])
                rad[p3].click()

                if p3 < 115:
                    p1 = 119
                    soal = 2
                    while soal:
                        s1 = random.choice([p1+1,p1+2,p1+3])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7
                else:
                    p1 = 119
                    soal = 2
                    while soal:
                        s1 = random.choice([p1+2,p1+3,p1+4,p1+5,p1+6])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7

                time.sleep(2)
                if akan == 18:
                    p1 = 154
                    soal = 4
                    while soal:
                        s1 = random.choice([p1+3,p1+4,p1+5,p1+6])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7
                else :
                    p1 = 154
                    soal = 4
                    while soal:
                        s1 = random.choice([p1,p1+1,p1+2,p1+3])
                        rad[s1].click()
                        soal -= 1
                        p1 += 7

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/MnmtA3sN3x5r5ptw6")

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
        # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()