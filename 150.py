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

link = "https://docs.google.com/forms/d/e/1FAIpQLSf_PhJLXUDyHoCtlPALAzAhJF08VuDhE8QBfF16BB9CDBpHDw/viewform"
profil = ["profile 1"]

inisial = [
    "AA"
]

universitas = [
    "Universitas Indonesia",
    "Institut Teknologi Sepuluh Nopember",
    "Politeknik Pelayaran Banten",
    "Universitas Negeri Yogyakarta",
    "Politeknik Kesehatan Semarang",
    "Universitas Trunojoyo Madura",
    "Politeknik Perkapalan Negeri Surabaya",
    "Universitas Negeri Jakarta",
    "Institut Seni Indonesia Surakarta",
    "Politeknik STMI Jakarta",
    "Politeknik Kesehatan Surakarta",
    "Universitas Islam Internasional Indonesia",
    "Politeknik Manufaktur Bandung",
    "Institut Pertanian Bogor",
    "Politeknik Penerbangan Surabaya",
    "Universitas Terbuka",
    "Universitas Tidar",
    "Universitas Islam Negeri Salatiga",
    "Politeknik Kesehatan Banten",
    "Politeknik Kelautan dan Perikanan Pangandaran",
    "Universitas Veteran Jawa Timur",
    "Universitas Siliwangi",
    "Politeknik Penerbangan Indonesia Curug",
    "Politeknik Negeri Media Kreatif",
    "Universitas Islam Negeri Syarif Hidayatullah Jakarta",
    "Politeknik Negeri Malang",
    "Politeknik APP Jakarta",
    "Universitas Islam Negeri Maulana Malik Ibrahim",
    "Politeknik Negeri Semarang",
    "Universitas Diponegoro",
    "Universitas Sultan Ageng Tirtayasa",
    "Universitas Islam Negeri Sunan Kalijaga Yogyakarta",
    "Politeknik Ilmu Pelayaran Semarang",
    "Universitas Islam Negeri Raden Mas Said",
    "Universitas Veteran Yogyakarta",
    "Politeknik Kesehatan Semarang",
    "Universitas Trunojoyo Madura",
    "Politeknik Pelayaran Banten",
    "Politeknik Negeri Media Kreatif",
    "Institut Teknologi Sepuluh Nopember",
    "Politeknik Penerbangan Surabaya",
    "Politeknik Pelayaran Banten",
    "Universitas Islam Negeri Maulana Malik Ibrahim",
    "Universitas Trunojoyo Madura",
    "Universitas Indonesia",
    "Universitas Negeri Yogyakarta",
    "Universitas Diponegoro",
    "Universitas Veteran Jawa Timur",
    "Politeknik STMI Jakarta",
    "Universitas Trunojoyo Madura",
    "Institut Pertanian Bogor",
    "Politeknik Kelautan dan Perikanan Pangandaran",
    "Universitas Islam Negeri Maulana Malik Ibrahim",
    "Politeknik Ilmu Pelayaran Semarang",
    "Politeknik Manufaktur Bandung",
    "Universitas Terbuka",
    "Politeknik Kesehatan Banten",
    "Politeknik Negeri Malang",
    "Universitas Islam Internasional Indonesia",
    "Universitas Trunojoyo Madura",
]

positif = 50
negatif = 10

jawabanSesuai = [1,2,0,0,5,6,0,0,0,10,11,12,0,0,15]

index = 0
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=Users\\iqbalrahman\\Library\\Application Support\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])
        driver = webdriver.Chrome(executable_path=r'Users\\iqbalrahman\\Documents\\Kerjaan\\input\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver', options=chrome_options)
        driver.get(link)

        times = 1
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
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            radiobuttons[0].click()

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
            semester = random.choice([0,0,0,0,2])
            if semester == 0 :
                status = random.choice([0,0,0,0,1])
            else :
                status = 0

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            textboxes[0].send_keys(inisial[index])
            textboxes[1].send_keys(universitas[index])

            radiobuttons[semester].click()
            radiobuttons[status].click()

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
            lama = random.randint(3,10)
            akhir = random.choice([" Bulan", " bulan", " bln", " Bln"])

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian

            radiobuttons[0].click()
            radiobuttons[random.choice([2,3,4,5,6])]

            textboxes[0].send_keys(lama)
            textboxes[0].send_keys(akhir)

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

            if positif != 0 and negatif != 0 :
                pil = random.choice([0,0,1])
            elif positif != 0 and negatif == 0 :
                pil = 0
            elif positif == 0 and negatif != 0 :
                pil = 1
            
            if pil == 1:
                time.sleep(2)

                temp = 1
                p = 2
                s = 0
                while temp != 16 :
                    if temp == jawabanSesuai[temp-1] :
                        s1 = random.choice([p,p+1,p+1,p+1,p+1,p+1,p+1,p+2,p+2,p+2,p+2,p+2,p+2])
                        radiobuttons[s1].click()

                    else :
                        s1 = random.choice([s,s+1,s+1])
                        radiobuttons[s1].click()

                    p += 5
                    s += 5
                    temp += 1

                positif -= 1
            else :
                time.sleep(2)

                temp = 1
                p = 2
                s = 0
                while temp != 16 :
                    if temp == jawabanSesuai[temp-1] :
                        s1 = random.choice([s,s+1,s+1])
                        radiobuttons[s1].click()

                    else :
                        s1 = random.choice([p,p+1,p+1,p+1,p+1,p+1,p+1,p+2,p+2,p+2,p+2,p+2,p+2])
                        radiobuttons[s1].click()

                    p += 5
                    s += 5
                    temp += 1

                negatif -= 1

            # time.sleep(3)
            # kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
            # kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

            # if len(kirims1) != 0 :
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
            #     )
            # else:
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
            #     )

            # submit_button.click()

            # driver.implicitly_wait(4)
            # driver.get(link)

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))
            print(" " + str())
            print("positif = " + str(positif))
            print("negatif = " + str(negatif))

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