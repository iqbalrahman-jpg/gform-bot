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
driver.get("https://forms.gle/SoQfbDzaS6LE9teA9")

lebih = [
    "jika sisa sedikit akan saya buang",
    "saya buang",
    "simpan di kulkas untuk besok",
    "jika masih bisa dimakan saya simpan di kulkas",
    "jika masih banyak dan tidak ada yang makan akan asya kasih ke orang",
    "simpan di kulkas untuk makan besok",
    "saya olah lagi menjadi makanan lain",
    "simpan di kulkas",
    "buang makanan sisanya",
    "taruh di kulkas agar bisa dimakan lagi",
    "taruh di kulkas",
    "saya berikan tetangga atau teman",
    "saya beri ke kucing jiga itu seperti ayam, ikan, dsb",
    "saya simpan di kulkas",
    "saya beri ke orang lain jika masih layak",
]

kulkas = [
    "sebagian makanan yang tidak saya inginkan lagi harus saya buang",
    "dibuang jika tidak layak diberikan ",
    "jika memang tidak bisa untuk diberikan ke orang lain, terpaksa saya harus membuangnya",
    "saya sedekahkan atau berikan ke tetangga, atau teman",
    "beberapa makanan terpaksa saya buang",
    "saya buang ke tempat sampah",
    "berikan ke orang lain jika masih layak",
    "dibuang saja ke sampah",
    "saya harus membuang sebagian makanan",
    "jika memang terpaksa akan saya buang",
    "buang",
    "saya buang ke tempat sampah",
    "terpaksa dengan sedih saya buang ke sampah",
    "seringkali saya kasih ke saudara saya yang suka",
    "saya berikan orang lain",
]

times = 4
index = 11

usia1 = 0
food = 0

mkn3 = 4
mkn2 = 0
mknb = 0

yes = 3

ya = 4
some = 0
no = 0

bnyk0 = 0
bnyk1 = 3
bnyk2 = 1

yaa = 5

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        if usia1 != 0:
            time.sleep(2)
            usia = random.choice([1,2])
            radiobuttons[usia].click()
            if usia == 1:
                time.sleep(2)
                usia1 -= 1
                pekerjaan = random.choice([3,5])
                radiobuttons[pekerjaan].click()
            else:
                if food != 0:
                    time.sleep(2)
                    pekerjaan = random.choice([3,3,4,5,5])
                    radiobuttons[pekerjaan].click()
                    if pekerjaan == 4:
                        food -= 1
                else:
                    time.sleep(3)
                    radiobuttons[5].click()
                    pekerjaan = random.choice([3,5,5])
                    radiobuttons[pekerjaan].click()
        else:
            time.sleep(2)
            radiobuttons[2].click()
            if food != 0:
                time.sleep(2)
                pekerjaan = random.choice([3,3,4,5,5])
                radiobuttons[pekerjaan].click()
                if pekerjaan == 4:
                    food -= 1
            else:
                time.sleep(2)
                radiobuttons[5].click()
                pekerjaan = random.choice([3,5,5])
                radiobuttons[pekerjaan].click()

        if mkn2 != 0 and mkn3 != 0 and mknb != 0:
            mkn = random.choice([1,2,3,4,5])
            testcheck[mkn-1].click()
            if mkn == 2:
                mkn2 -= 1
            elif mkn == 3:
                mkn3 -= 1
            else:
                mknb -= 1;
        elif mkn2 != 0 and mkn3 != 0 and mknb == 0:
            mkn = random.choice([2,3])
            testcheck[mkn-1].click()
            if mkn == 2:
                mkn2 -= 1
            else :
                mkn3 -= 1 
        elif mkn2 != 0 and mkn3 == 0 and mknb != 0:
            mkn = random.choice([1,2,4,5])
            testcheck[mkn-1].click()
            if mkn == 2 :
                mkn2 -= 1
            else :
                mknb -= 1
        elif mkn2 != 0 and mkn3 == 0 and mknb == 0:
            testcheck[1].click()
            mkn2 -= 1
        elif mkn2 == 0 and mkn3 != 0 and mknb != 0:
            mkn = random.choice([1,3,4,5])
            testcheck[mkn-1].click()
            if mkn == 3 :
                mkn3 -= 1
            else :
                mknb -= 1
        elif mkn2 == 0 and mkn3 != 0 and mknb == 0:
            testcheck[2].click()
            mkn3 -= 1
        elif mkn2 == 0 and mkn3 == 0 and mknb != 0:
            mkn = random.choice([1,4,5])
            testcheck[mkn-1].click()
            mknb -= 1

        penuh = random.choice([6,6,6,7])
        radiobuttons[penuh].click()

        if yes != 0:
            time.sleep(2)
            sisa = random.choice([8,9])
            radiobuttons[sisa].click()
            if sisa == 8:
                yes -= 1
        else:
            time.sleep(2)
            radiobuttons[9].click()

        online = random.choice([6,7,8,8,9,10])
        testcheck[online].click()

        if ya != 0 and some != 0 and no != 0:
            diskon = random.choice([10,11,12])
            radiobuttons[diskon].click()
            if diskon == 10:
                ya -= 1
            elif diskon == 11:
                no -= 1
            else :
                some -= 1
        elif ya != 0 and some != 0 and no == 0:
            diskon = random.choice([10,12])
            radiobuttons[diskon].click()
            if diskon == 10:
                ya -= 1
            else :
                some -= 1
        elif ya != 0 and some == 0 and no != 0:
            diskon = random.choice([10,11])
            radiobuttons[diskon].click()
            if diskon == 10:
                ya -= 1
            else :
                no -= 1
        elif ya != 0 and some == 0 and no == 0:
            radiobuttons[10].click()
            ya -= 1
        elif ya == 0 and some != 0 and no != 0:
            diskon = random.choice([11,12])
            radiobuttons[diskon].click()
            if diskon == 11:
                no -= 1
            else :
                some -= 1
        elif ya == 0 and some != 0 and no == 0:
            radiobuttons[12].click()
            some -= 1
        elif ya == 0 and some == 0 and no != 0:
            radiobuttons[11].click()
            no -= 1

        if bnyk0 != 0 and bnyk1 != 0 and bnyk2 != 0:
            diskon = random.choice([11,12,13])
            testcheck[diskon].click()
            if diskon == 11:
                bnyk0 -= 1
            elif diskon == 12:
                bnyk1 -= 1
            else :
                bnyk2 -= 1
        elif bnyk0 != 0 and bnyk1 != 0 and bnyk2 == 0:
            diskon = random.choice([11,13])
            testcheck[diskon].click()
            if diskon == 11:
                bnyk0 -= 1
            else :
                bnyk2 -= 1
        elif bnyk0 != 0 and bnyk1 == 0 and bnyk2 != 0:
            diskon = random.choice([11,12])
            testcheck[diskon].click()
            if diskon == 11:
                bnyk0 -= 1
            else :
                bnyk1 -= 1
        elif bnyk0 != 0 and bnyk1 == 0 and bnyk2 == 0:
            testcheck[11].click()
            bnyk0 -= 1
        elif bnyk0 == 0 and bnyk1 != 0 and bnyk2 != 0:
            diskon = random.choice([12,13])
            testcheck[diskon].click()
            if diskon == 12:
                bnyk1 -= 1
            else :
                bnyk2 -= 1
        elif bnyk0 == 0 and bnyk1 != 0 and bnyk2 == 0:
            testcheck[13].click()
            bnyk2 -= 1
        elif bnyk0 == 0 and bnyk1 == 0 and bnyk2 != 0:
            testcheck[12].click()
            bnyk1 -= 1

        textboxes[0].send_keys(lebih[index])
        textboxes[1].send_keys(kulkas[index])

        if yaa != 0:
            time.sleep(2)
            s1 = random.choice([13,14])
            radiobuttons[s1].click()
            if s1 == 13:
                yaa -= 1
        else :
            radiobuttons[14].click()

        s2 = random.choice([15,16,17,18,19,20])
        radiobuttons[s2].click()

        s3 = random.randint(15,25)
        testcheck[s3].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/SoQfbDzaS6LE9teA9")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("usia1 : " + str(usia1))
        print("food : " + str(food))
        print(" ")
        print("mkn3 : " + str(mkn3))
        print("mkn2 : " + str(mkn2))
        print("mknb : " + str(mknb))
        print(" ")
        print("yes : " + str(yes))
        print(" ")
        print("ya : " + str(ya))
        print("some : " + str(some))
        print("no : " + str(no))
        print(" ")
        print("bnyk0 : " + str(bnyk0))
        print("bnyk1 : " + str(bnyk1))
        print("bnyk2 : " + str(bnyk2))
        print(" ")
        print("yaa : " + str(yaa))

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