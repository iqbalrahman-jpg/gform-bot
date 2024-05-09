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
driver.get("http://bit.ly/KuesionerKelompok9Statdas")

nama = [
        "Nana Annisa",
        "Yuli Ayunda Dewi",
        "Annisa Chania",
        "Fattahilah Sadewa",
        "Diah Ayu Cindy",
        "Nia EKa Yuliana",
        "Putri Keancana",
        "Mona Hadfinna",
        "Agung Nugroho",
        "Dewi Sari Wijaya",
]

prestasi_non = [
    "Meraih penghargaan atau sertifikat dalam bidang kepemimpinan atau kepemudaan",
    "Menjadi juara dalam kompetisi kecantikan dan modeling",
]

olahraga = [
    "Bulu tangkis",
    "Renang",
]

#0 laki 1 perempuan
kelamin = [1,1,1,0,1,1,1,1,0,1,]

dptm1 = 5
dptm2 = 3
dptm3 = 1
dptm4 = 1

essay = 0
tidak = 8
idxe = 0

times = 10
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        driver.implicitly_wait(4)

        if dptm1 != 0 and dptm2 != 0 and dptm3 != 0 and dptm4 != 0 :
            pil = random.choice([0,1,2,3])
            if pil == 0:
                dptm1 -= 1
            elif pil == 1:
                dptm2 -= 1
            elif pil == 2:
                dptm3 -= 1
            else:
                dptm4 -= 1
        elif dptm1 != 0 and dptm2 != 0 and dptm3 != 0 and dptm4 == 0 :
            pil = random.choice([0,1,2])
            if pil == 0:
                dptm1 -= 1
            elif pil == 1:
                dptm2 -= 1
            else:
                dptm3 -= 1
        elif dptm1 != 0 and dptm2 != 0 and dptm3 == 0 and dptm4 != 0 :
            pil = random.choice([0,1,3])
            if pil == 0:
                dptm1 -= 1
            elif pil == 1:
                dptm2 -= 1
            else:
                dptm4 -= 1
        elif dptm1 != 0 and dptm2 == 0 and dptm3 != 0 and dptm4 != 0 :
            pil = random.choice([0,2,3])
            if pil == 0:
                dptm1 -= 1
            elif pil == 2:
                dptm3 -= 1
            else:
                dptm4 -= 1
        elif dptm1 == 0 and dptm2 != 0 and dptm3 != 0 and dptm4 != 0 :
            pil = random.choice([1,2,3])
            if pil == 1:
                dptm2 -= 1
            elif pil == 2:
                dptm3 -= 1
            else:
                dptm4 -= 1
        elif dptm1 != 0 and dptm2 != 0 and dptm3 == 0 and dptm4 == 0 :
            pil = random.choice([0,1])
            if pil == 0:
                dptm1 -= 1
            elif pil == 1:
                dptm2 -= 1
        elif dptm1 != 0 and dptm2 == 0 and dptm3 != 0 and dptm4 == 0 :
            pil = random.choice([0,2])
            if pil == 0:
                dptm1 -= 1
            elif pil == 2:
                dptm3 -= 1
        elif dptm1 == 0 and dptm2 != 0 and dptm3 != 0 and dptm4 == 0 :
            pil = random.choice([1,2])
            if pil == 1:
                dptm2 -= 1
            elif pil == 2:
                dptm3 -= 1
        elif dptm1 != 0 and dptm2 == 0 and dptm3 == 0 and dptm4 != 0 :
            pil = random.choice([0,3])
            if pil == 0:
                dptm1 -= 1
            else:
                dptm4 -= 1
        elif dptm1 == 0 and dptm2 != 0 and dptm3 == 0 and dptm4 != 0 :
            pil = random.choice([1,3])
            if pil == 1:
                dptm2 -= 1
            else:
                dptm4 -= 1
        elif dptm1 == 0 and dptm2 == 0 and dptm3 != 0 and dptm4 != 0 :
            pil = random.choice([2,3])
            if pil == 2:
                dptm3 -= 1
            else:
                dptm4 -= 1
        elif dptm1 != 0 and dptm2 == 0 and dptm3 == 0 and dptm4 == 0 :
            pil = random.choice([0])
            dptm1 -= 1
        elif dptm1 == 0 and dptm2 != 0 and dptm3 == 0 and dptm4 == 0 :
            pil = random.choice([1])
            dptm2 -= 1
        elif dptm1 == 0 and dptm2 == 0 and dptm3 != 0 and dptm4 == 0 :
            pil = random.choice([2])
            dptm3 -= 1
        elif dptm1 == 0 and dptm2 == 0 and dptm3 == 0 and dptm4 != 0 :
            pil = random.choice([3])
            dptm4 -= 1

        time.sleep(2)
        radiobuttons[pil].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        umur = random.randint(18,24)
        agama = random.randint(2,7)
        anak = random.randint(9,13)
        suku = random.randint(15,22)
        biaya = random.choice([24,24,24,25,26,27,27])
        profesi = random.randint(29,32)
        asal = random.randint(34,37)
        jurusan = random.choice([39,39,39,39,40,40,40,40,41])
        jalur = random.choice([42,42,43,44,44,44,44,45,46,46])
        ipk = random.choice([48,49,50,50,50,50,51,51,51,51])
        tinggal = random.choice([52,52,52,53,53,53,54,55])
        waktu = random.choice([56,57,58,58,58,59,59,59,60,61,62])

        provinsi = random.choice([
                "Jawa Timur",
                "Jawa Barat",
                "Jawa Tengah",
                "DKI Jakarta",
                "Yogyakarta",
            ])

        if ipk == 48:
            depan = 2
        elif ipk == 49:
            depan = 2
        else:
            depan = 3

        belakang = random.randint(1,99)
        if belakang == 10 : 
            belakang = 1
        elif belakang == 20 :
            belakang = 2
        elif belakang == 30 :
            belakang = 3
        elif belakang == 40 :
            belakang = 4
        elif belakang == 50 :
            belakang = 5
        elif belakang == 60 :
            belakang = 6
        elif belakang == 70 :
            belakang = 7
        elif belakang == 80 :
            belakang = 8
        elif belakang == 90 :
            belakang = 9
        else :
            belakang = belakang

        temp = random.randint(1,3)
        temps = random.randint(1,3)
        tempss = random.randint(1,5)
        tempsss = random.randint(1,3)
        tempssss = random.randint(1,3)

        if waktu == 56:
            tempuh = random.choice([63,64])
            transportasi = random.sample([0,1,2,4], temp)
        elif waktu == 57:
            tempuh = random.choice([64,65])
            transportasi = random.sample([0,1,2,4], temp)
        elif waktu == 58:
            tempuh = random.choice([64,65,66])
            transportasi = random.sample([1,2,4,5], temp)
        elif waktu == 59:
            tempuh = random.choice([65,66,67])
            transportasi = random.sample([1,2,4,5], temp)
        elif waktu == 60:
            tempuh = random.choice([66,67])
            transportasi = random.sample([1,2,3,4,5], temp)
        else:
            tempuh = random.choice([66,67,68])
            transportasi = random.sample([1,2,3,4,5], temp)

        prestasi = random.sample([7,8,9,10], temps)
        organisasi = random.sample([12,13,14,15,16,17,18], tempss)
        bahasa = random.sample([21,22,23,24,25,26], tempsss)
        program = random.sample([28,29,30,31], tempssss)

        if essay != 0 and tidak != 0:
            pil = random.choice([1,2])
            if pil == 1:
                essay1 = prestasi_non[idxe]
                essay2 = olahraga[idxe]
                essay -= 1
                idxe += 1
            else :
                essay1 = "-"
                essay2 = "-"
                tidak -= 1
        elif essay != 0 and tidak == 0:
            essay1 = prestasi_non[idxe]
            essay2 = olahraga[idxe]
            essay -= 1
            idxe += 1
        elif essay == 0 and tidak != 0:
            essay1 = "-"
            essay2 = "-"
            tidak -= 1

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(umur)
        textboxes[1].send_keys(provinsi)
        textboxes[2].send_keys(depan)
        textboxes[2].send_keys(random.choice([",","."]))
        textboxes[2].send_keys(belakang)
        textboxes[3].send_keys(essay1)
        textboxes[4].send_keys(essay2)
        driver.implicitly_wait(4)

        radiobuttons[kelamin[index]].click()
        radiobuttons[agama].click()
        radiobuttons[anak].click()
        radiobuttons[suku].click()
        radiobuttons[biaya].click()
        radiobuttons[profesi].click()
        radiobuttons[asal].click()
        radiobuttons[jurusan].click()
        radiobuttons[jalur].click()
        radiobuttons[ipk].click()
        radiobuttons[tinggal].click()
        radiobuttons[waktu].click()
        radiobuttons[tempuh].click()
        driver.implicitly_wait(4)

        for i in transportasi :
           checkboxes[i].click()

        time.sleep(1)
        for i in prestasi :
           checkboxes[i].click()

        time.sleep(1)
        for i in organisasi :
           checkboxes[i].click()

        time.sleep(1)
        for i in bahasa :
           checkboxes[i].click()

        time.sleep(1)
        for i in program :
           checkboxes[i].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("http://bit.ly/KuesionerKelompok9Statdas")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")
        print("dptm1 : " + str(dptm1))
        print("dptm2 : " + str(dptm2))
        print("dptm3 : " + str(dptm3))
        print("dptm4 : " + str(dptm4))
        print("")
        print("idxe  : " + str(idxe))
        print("")
        print("essay : " + str(essay))
        print("tidak : " + str(tidak))

        times-=1
        print("times : " + str(times))
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