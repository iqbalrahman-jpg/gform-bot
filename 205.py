from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import random
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLScUnxBCAsu3xrC-pPmodYE8go8N5jNwhZzp9cYp_Cg0w26V0A/formResponse"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

usia = [
    15, # 20/21/22
    10
]

times = 1
index = 0

email = [
    "alihasn.01.10@gmail.com",
    "risfebri11@gmail.com",
    "budprasety@gmail.com",
    "aryonugh@gmail.com",
    "nanissa0110@gmail.com",
    "yahnugrah@gmail.com",
    "putriptr0110@gmail.com",
    "nandayundaa1@gmail.com",
    "yudipradan01@gmail.com",
    "mtianur001@gmail.com",

    "byumerta1@gmail.com",
    "Bellandayu01@gmail.com",
    "budsuryant01@gmail.com",
    "nela.mirra@gmail.com",
    "dwa.lingga10@gmail.com",
    "alffiantoro@gmail.com",
    "annicsaa@gmail.com",
    "fataahxdewa@gmail.com",
    "diahcindy03@gmail.com",
    "yulayund1@gmail.com",

    "azzarinrst@gmail.com",
    "fabiannadeo@gmail.com",
    "niaejuliana@gmail.com",
    "bayudwiganara@gmail.com",
    "syifaradifah@gmail.com",
    "aditferdinanda@gmail.com",
    "sitifauziyyahh@gmail.com",
    "reyhanutomowa@gmail.com",
    "salmaarowaya@gmail.com",
    "attakmajid@gmail.com",
]

nama = [
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Mutia Ayu Nur",

    "Bayu Danang Merta",
    "Bellanda Clara Ayunda ",
    "Budi Suryanto",
    "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Yuli Ayunda Dewi",

    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Attaka Majid",
]

kelamin = [
    0,1,0,0,1,0,1,1,0,1,
    0,1,0,1,0,0,1,0,1,1,
    1,0,1,0,1,0,1,0,1,0,
]

skala3 = [
    [
        1,0,1,0,1,0,1,0,1,0
    ],
    [
        0,1,0,1,0,1,0,1,1,1
    ],
    [
        1,0,1,0,1,0,1,0,1,1
    ],
    [
        0,1,0,1,0,0,0,0,0,0
    ],
    [
        1,0,1,0,1,0,1,0,1,1
    ]
]

try:
    while times:
        time.sleep(2)
        tipeUsia = data.pilihTipe(usia)
        usia[tipeUsia] -= 1

        if tipeUsia == 0 :
            usiaJawab = random.choice([20,21,22])
        else :
            usiaJawab = random.choice([18,19,23,24,25,26,27,28])

        usiaTambahan = random.randint(0,1)

        banyakSkala = random.choice([1,2,2,2,3,3])
        skalaTipe = random.sample([0,1,2,3,4,5], banyakSkala)

        while 2 in skalaTipe and 3 in skalaTipe :
            skalaTipe = random.sample([0,1,2,3,4,5], banyakSkala)

        time.sleep(1)
        data.pindahHalaman(driver)

        time.sleep(2)
        bawah = data.tombol(2, driver)

        bawah[0].click()
        data.pindahHalaman(driver)

        time.sleep(2)
        isian = data.tombol(0, driver)
        bawah = data.tombol(2, driver)

        isian[0].send_keys(email[index])
        isian[1].send_keys(nama[index])
        isian[2].send_keys(usiaJawab)
        isian[2].send_keys(
            random.choice([" tahun", " Tahun", " thn", "thn", "tahun", "Tahun"]) if usiaTambahan == 1 else ""
        )

        time.sleep(1)
        bawah[kelamin[index]].click()

        tambahan = []
        for a in range(6) :
            tambahan.append(random.randint(0,3))

        time.sleep(2)
        for i in range(3) :
            data.pindahHalaman(driver)

            time.sleep(3)
            samping = data.tombol(3, driver)

            if i == 2 :
                skala3Tipe = random.randint(1,2)
                skala3Jawab = random.sample([0,1,2,3,4,5], skala3Tipe)

                p = 0
                for x in range(len(skala3)) :
                    if x in skala3Jawab :
                        for i in range(10) :
                            if skala3[x][i] == 1 :
                                s1 = random.choice([2,3,3,3,4,4,4])
                                samping[p+s1].click()
                            else :
                                s1 = random.choice([0,0,0,1,1,1,2])
                                samping[p+s1].click()
                            p += 5
                    else :
                        for i in range(10) :
                            s1 = random.choice([0,1,2,3,4])
                            samping[p+s1].click()

                            p += 5

            else :
                for x in range(6) :
                    time.sleep(1)
                    awal = 0

                    time.sleep(2)
                    if x == 0 :
                        awal = 0 + 2 if x in skalaTipe else 0
                    elif awal % 10 == 0:
                        awal += 2 if x in skalaTipe else 0
                    else :
                        awal = 50 * x + 2 if x in skalaTipe else 0

                    time.sleep(1)
                    awal = data.polaJawab3(2 if x in skalaTipe else 4, awal, 10, 5, samping)

                    time.sleep(1)
                    p = (50 * x)
                    for j in range(tambahan[x]) :
                        s1 = random.choice([p, p+5 ,p+10 ,p+15 ,p+20 ,p+25 ,p+30 ,p+35 ,p+40 ,p+45])
                        s2 = random.choice([s1, s1+1, s1+1, s1+1 , s1+2] if x in skalaTipe else [s1, s1+2, s1+3, s1+3, s1+3, s1+4, s1+4, s1+4])
                        samping[s2].click()






        # data.kirim(driver)
        # driver.implicitly_wait(4)
        # driver.get(link)

        index+=1
        print("==================")
        print("usia = " + str(usia))
        print("")

        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    # driver.quit()
    print("berhasil")

        # radiobuttons = data.tombol("kebawah", driver)
        # textboxes = data.tombol("isian", driver)
        # checkboxes = data.tombol("checkbox", driver)
        # testcheck = data.tombol("kesamping", driver)
        # textarea = data.tombol("textarea", driver)
        # pilihan = data.tombol("bubble", driver)
        # lainnya = data.tombol("lainnya", driver)

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")
