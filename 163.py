from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_163
import list
import random
import time

link = "https://forms.gle/PT9mtiVoBiSnaysE9"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_163.times
index = data_163.index

try:
    while times:
        time.sleep(2)

        isian = data.tombol(0, driver)
        area = data.tombol(1, driver)
        kebawah = data.tombol(2, driver)
        kesamping = data.tombol(3, driver)

        isian[0].send_keys(list.nama[index])
        kebawah[list.kelamin[index]].click()

        p = 0
        for i in range(10) :
            if i % 2 == 0 :
                p += 2
                data.polaJawab3(1, p, 1, 5, kesamping)
                p -= 2
            else :
                data.polaJawab3(3, p, 1, 5, kesamping)
            
            p += 5
        
        time.sleep(2)
        area[0].send_keys(data_163.isian[index])
        
        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        # print("")
        
        times-=1
        print("index = " + str(index))
        print("times = " + str(times))
finally:
    # driver.quit()
    print("berhasil")

        # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
        # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")
