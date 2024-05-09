from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

import random
import time
import data

link = "https://www.surveymonkey.com/r/LMR5DKR"

kategori = [
    [
        22, 0
    ],
    [
        22, 0
    ],
    [
        1, 1
    ]
]

times = 15
index = 0

try:
    while times:
        driver = webdriver.Firefox()
        actions = ActionChains(driver)
        driver.get(link)

        time.sleep(5)
        #Hardcoded logic
        usia = random.choice([0,1,2,3,3,4,4,5,5])
        kelamin = random.choice([6,7])
        domisili = random.choice([8,8,8,9])

        tipe = data.pilihTipe(kategori[0])
        kategori[0][tipe] -= 1

        setuju = data.pilihTipe(kategori[1])
        kategori[1][setuju] -= 1

        time.sleep(2)
        button = driver.find_elements("css selector", ".ok-button")#kebawah
        next = driver.find_elements("css selector", ".next-button")#kebawah
        radiobuttons = driver.find_elements("css selector", ".radio-button-label")#kebawah

        radiobuttons[usia].click()
        time.sleep(1)
        radiobuttons[kelamin].click()
        time.sleep(1)
        radiobuttons[domisili].click()

        time.sleep(2)
        if tipe == 0 :
            p = 10
            temp = 4
            for i in range(24) :
                s1 = random.choice([p,p,p,p+1])
                time.sleep(1)
                radiobuttons[s1].click()
                button[temp].click()

                p += 5
                temp += 1
                 
        else :
            p = 10
            s = p + 2
            temp = 4
            for i in range(24) :
                s1 = random.choice([s,s,s+1,s+2])
                time.sleep(1)
                radiobuttons[s1].click()
                button[temp].click()

                p += 5
                s += 5
                temp += 1
        

        time.sleep(2)
        if setuju == 0 :
            for i in range(5) :
                s1 = random.choice([p,p,p+1])
                time.sleep(1)
                radiobuttons[s1].click()
                button[temp].click()

                p += 5
                temp += 1

        else:
            s = p + 2
            for i in range(5) :
                s1 = random.choice([s,s,s+1,s+1,s+2])
                time.sleep(1)
                radiobuttons[s1].click()
                button[temp].click()

                p += 5
                s += 5
                temp += 1
        
        if tipe == 0 :
            s1 = random.choice([p,p+1])
            time.sleep(1)
            radiobuttons[s1].click()
            button[temp].click()

            time.sleep(1)
            next[0].click() 

        else : 
            s1 = random.choice([p+2,p+3,p+4])
            time.sleep(1)
            radiobuttons[s1].click()
            button[temp].click()

            time.sleep(1)
            next[0].click()

            time.sleep(2)
            button = driver.find_elements("css selector", ".ok-button")#kebawah
            done = driver.find_elements("css selector", ".done-button")#kebawah
            radiobuttons = driver.find_elements("css selector", ".radio-button-label")#kebawah

            puas = data.pilihTipe(kategori[2])
            kategori[2][puas] -= 1

            time.sleep(1)
            p = 0
            temp = 0
            for i in range(8) :
                time.sleep(1)
                s1 = random.choice([p,p,p,p+1,p+1,p+2,p+2,p+3,p+4])
                radiobuttons[s1].click()
                button[temp].click()

                p += 5
                temp += 1
            
            if puas == 0 :
                s = p + 2
                for i in range(3) :
                    time.sleep(1)
                    s1 = random.choice([s,s+1,s+2])
                    radiobuttons[s1].click()
                    button[temp].click()

                    s += 5
                    p += 5
                    temp += 1

            else :
                for i in range(3) :
                    time.sleep(1)
                    s1 = random.choice([p,p,p+1,p+2])
                    radiobuttons[s1].click()
                    button[temp].click()

                    p += 5
                    temp += 1
            
            time.sleep(1)
            radiobuttons[random.choice([p,p+1,p+2,p+3,p+4])].click()
            button[temp].click()

            done[0].click()

        driver.quit()
            
        index+=1
        print("==================")
        print("kategori " + str(kategori[0]))
        print("setuju " + str(kategori[1]))
        print("puas " + str(kategori[2]))
        print("")
        
        times-=1
        print("index  : " + str(index))
        print("times  : " + str(times))
finally:
    # driver.quit()
    print("berhasil")