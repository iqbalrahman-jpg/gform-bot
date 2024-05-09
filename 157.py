from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import data
import data_157
import list
import random
import time

link = "https://forms.gle/J4NcqfoSVMk6tmVHA"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get(link)

times = data_157.times
index = data_157.index

try:
    while times:
        time.sleep(2)
        pil1 = data_157.pilihanPositif(0)
        pil2 = data_157.pilihanPositif(1)

        data_157.kategori[0][pil1] -= 1
        data_157.kategori[1][pil2] -= 1

        time.sleep(2)
        radiobuttons = data.tombol("kebawah", driver)
        textboxes = data.tombol("isian", driver)
        textarea = data.tombol("textarea", driver)

        textboxes[0].send_keys(list.nama[index])

        time.sleep(2)
        radiobuttons[pil1].click()
        radiobuttons[pil2 + 2].click()

        time.sleep(2)
        textarea[0].send_keys(data_157.kirimAlasan(0, pil1))
        textarea[1].send_keys(data_157.kirimAlasan(1, pil2))

        data.kirim(driver)
        driver.implicitly_wait(4)
        driver.get(link)

        index+=1
        print("==================")
        print("kategori 1 = " + str(data_157.kategori[0][0]) + ", " + str(data_157.kategori[0][1]))
        print("kategori 2 = " + str(data_157.kategori[1][0]) + ", " + str(data_157.kategori[1][1]))
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

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()


        

