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
driver.get("https://forms.gle/HELcHtNYsoRSUhsZ7")

essay1k = [
    "karena influencer korea lebih menarik perhatian saya dan lebih glowing daripada influencer indo",
    "Nama dari influencer korea lebih sering terdengar dan familiar daripada influencer indonesia",
    "Influencer Korea memiliki pemahaman yang mendalam tentang tren kecantikan terbaru dan mampu menarik minat pengguna di seluruh dunia",
    "Karena influencer Korea membawa reputasi yang sangat baik, sehingga orang-orang lebih percaya pada merek dan produk yang mereka rekomendasikan",
    "karena influencer korea dapat memberikan saran yang lebih relevan dan sesuai dengan beragam tipe kulit pengguna",
    "Influencer Korea seringkali memiliki pengetahuan mendalam tentang perawatan kulit dan mampu memberikan informasi yang terperinci tentang penggunaan produk perawatan kulit Indonesia",
    "Karena influencer Korea seringkali memiliki penampilan yang menarik dan kulit yang sehat, yang dapat menjadi daya tarik tersendiri bagi pengguna produk perawatan kulit",
    "Karena saya sebagai penggemar K-pop dan drama Korea cenderung lebih percaya kepada influencer Korea untuk mempromosikan produk perawatan kulit Indonesia",
    "karena mereka dapat memberikan testimonial yang kuat dan membagikan cerita sukses mereka dengan produk Indonesia kepada pengikut mereka",
    "Mereka memiliki pengikut dari berbagai negara, sehingga dapat membantu memperluas pasar dan meningkatkan kesadaran tentang produk perawatan kulit Indonesia di seluruh dunia",
    "Karena influencer korea sering berinteraksi dengan penggemar mereka dan mampu menciptakan efek viral yang dapat membantu promosi produk perawatan kulit Indonesia",
    "Karena mereka lebih enak dipandang dan memilikiwajah yang meyakinkan dalam mempromosikan produk skincare",
    "karena rekomendasi mereka cenderung dianggap lebih dapat diandalkan dan dapat memengaruhi keputusan pembelian pengguna",
    "Karena mereka lebih memiliki citra yang positif daripada influencer indonesia",
    "Karena influencer korea bening-bening jadi saya lebih percaya kepada mereka",
    "Karena banyak idola saya",
    "karena mereka lebih dapat menarik minat dari orang-orang yang memiliki kesukaan terhadap budaya korea",
]

essay1i = [
    "Karena influencer Indonesia melambangkan tipe kulit dan wajahnya sesuai dengan saya",
    "menurut saya influencer Indonesia lebih menarik masyarakat Indonesia secara umum dibandingkan dengan korea",
    "Karena influencer Indonesia sudah cukup untuk mempromosikan skicare yang di promosikan",
]

essay2k = [
    "iya, menurut saya sebenernya cocok cuma saya lebih preffer ke influencer korea saja",
    "ya, karena menurut saya mereka lebih kompeten daripada influencer indonesia",
    "Menurut saya lebih cocok menggunakan influencer korea karena mereka lebih enak dipandang",
    "Saya lebih cocok dengan influencer korea karena mereka lebih dapat dipercaya daripada influencer indonesia",
    "Iya. Karena mereka lebih kompten daripada influencer indonesia, menurut saya influencer indonesia kurang cocok",
    "Iya, karena mereka lebih mendapatkan banyak perhatian daripada influencer indonesia jadi lebih cocok influencer korea",
    "saya merasa lebih cocok dengan influencer korea daripada influencer indonesia karena mereka lebih bisa dipercaya",
    "Melihat dari penggemarnya yang banyak menurut saya saya lebih cocok dengan BA dari orang korea daripada indonesia",
    "Menurut saya influencer Indonesia masih cocok hanya saja dilihat dari views dan like BA orang korea lebih banyak jadi saya lebih suka dengan influencer korea",
    "Influencer indonesia sebenarnya masih cocok. Namun jika dibandingkan dengan influencer korea mereka jelas kalah",
    "Ya, saya merasa lebih cocok untuk melihat BA korea daripada Indonesia",
    "Saya lebih merasa cocokan orang korea yang menjadi Brand Ambassador daripada orang Indonesia",
    "Ya, karena menurut saya influencer Korea lebih keren dan memikat lebih banyak orang dibanding Indonesia",
    "iya, karena mereka lebih terlihat berkompeten dan lebih mahir dalam mempromosikan produk kecantikan",
    "Saya lebih cocok dengan brand ambassador korea karena lebih membangun keinginan saya dalam membeli produk yg di promosikan mereka",
    "saya suka dengan look dari wajah BA orang korea, jadi menurut saya kedepammya lebih baik tetap orang korea yang mempromosikan nya",
    "ya, saya suka dengan penampilan dan gaya bicara dari brand ambassador korea dibandingkan Indonesia",
]

essay2i = [
    "Tidak, mungkin ada baiknya juga tetap menggunakan brand ambassador indonesia agar tidak terlalu monoton",
    "Brand Ambassador Indonesia juga harus ikut andil peran dalam mempromosikan produk kecantikan di Indonesia karena agar lebih terasa jiwa lokalnya",
    "Saya lebih cocok dengan BA dari Indonesia karena agar tidak berketergantungan dengan brand ambassador dari luar terus menerus",
]

idxessayk = 0
idxessayi = 0

essaykorea = 17
essayindo = 3

usia2 = 9
usia3 = 6
usia4 = 5

times = 20
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if usia2 != 0 and usia3 != 0 and usia4 != 0:
            pil = random.choice([2,3,4])
            if pil == 2:
                usia2 -= 1
            elif pil == 3:
                usia3 -= 1
            else:
                usia4 -= 1
        elif usia2 != 0 and usia3 != 0 and usia4 == 0:
            pil = random.choice([2,3])
            if pil == 2:
                usia2 -= 1
            else:
                usia3 -= 1
        elif usia2 != 0 and usia3 == 0 and usia4 != 0:
            pil = random.choice([2,4])
            if pil == 2:
                usia2 -= 1
            else:
                usia4 -= 1
        elif usia2 == 0 and usia3 != 0 and usia4 != 0:
            pil = random.choice([3,4])
            if pil == 3:
                usia3 -= 1
            else:
                usia4 -= 1
        elif usia2 != 0 and usia3 == 0 and usia4 == 0:
            pil = 2
            usia2 -= 1
        elif usia2 == 0 and usia3 != 0 and usia4 == 0:
            pil = 3
            usia3 -= 1
        elif usia2 == 0 and usia3 == 0 and usia4 != 0:
            pil = 4
            usia4 -= 1

        time.sleep(2)
        if pil == 2:
            penghasilan = random.choice([6,7])
            pendidikan = random.choice([6,7])
            tiktok = random.choice([10,11,12,12,12])
        elif pil == 3:
            penghasilan = random.choice([6,7,8,9,10])
            pendidikan = random.choice([6,7,7,7])
            tiktok = random.choice([10,11,12])
        else:
            penghasilan = random.choice([6,7,8,9,10])
            pendidikan = random.choice([6,7,7,8])
            tiktok = random.choice([10,10,11,12])

        time.sleep(2)
        if penghasilan <= 7:
            buy = random.choice([13,14])
        elif penghasilan == 8:
            buy = random.choice([13,14,15])
        elif penghasilan == 9:
            buy = random.choice([14,15,16])
        else:
            buy = random.choice([13,14,15,16])

        time.sleep(2)
        if essaykorea != 0 and essayindo != 0:
            essai = random.choice([1,2])
            if essai == 1:
                essaykorea -= 1
            else:
                essayindo -= 1
        elif essaykorea != 0 and essayindo == 0:
            essai = 1 
            essaykorea -= 1
        elif essaykorea == 0 and essayindo != 0:
            essai = 2
            essayindo -= 1

        time.sleep(1)
        temp = random.randint(1,4)
        sama = random.sample([0,1,2,3,4], temp)

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[0].click()
        radiobuttons[2].click()
        radiobuttons[4].click()
        radiobuttons[penghasilan].click()
        radiobuttons[11].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        
        radiobuttons[0].click()
        radiobuttons[pil].click()
        radiobuttons[pendidikan].click()
        radiobuttons[tiktok].click()
        radiobuttons[buy].click()

        for i in sama:
            checkboxes[i].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if essai == 1:
            p = 0
            soal = 4
            while soal:
                s1 = random.choice([p+1,p+2,p+3,p+4,p+2,p+3,p+4,p+2,p+3,p+4,p+2,p+3,p+4])
                testcheck[s1].click()
                p += 5
                soal -= 1
        else:
            p = 0
            soal = 4
            while soal:
                s1 = random.choice([p,p+1,p+2])
                testcheck[s1].click()
                p += 5
                soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if essai == 1:
            p = 0
            soal = 4
            while soal:
                s1 = random.choice([p+1,p+2,p+3,p+4,p+2,p+3,p+4,p+2,p+3,p+4,p+2,p+3,p+4])
                testcheck[s1].click()
                p += 5
                soal -= 1
        else:
            p = 0
            soal = 4
            while soal:
                s1 = random.choice([p,p+1,p+2])
                testcheck[s1].click()
                p += 5
                soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if essai == 1:
            p = 0
            soal = 3
            while soal:
                s1 = random.choice([p+1,p+2,p+3,p+4,p+2,p+3,p+4,p+2,p+3,p+4,p+2,p+3,p+4])
                testcheck[s1].click()
                p += 5
                soal -= 1
        else:
            p = 0
            soal = 3
            while soal:
                s1 = random.choice([p,p+1,p+2])
                testcheck[s1].click()
                p += 5
                soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        if essai == 1:
            p = 0
            soal = 2
            while soal:
                s1 = random.choice([p+1,p+2,p+3,p+4,p+2,p+3,p+4,p+2,p+3,p+4,p+2,p+3,p+4])
                testcheck[s1].click()
                p += 5
                soal -= 1

            textboxes[0].send_keys(essay1k[idxessayk])
            textboxes[1].send_keys(essay2k[idxessayk])
            idxessayk += 1
        else:
            p = 0
            soal = 2
            while soal:
                s1 = random.choice([p,p+1,p+2])
                testcheck[s1].click()
                p += 5
                soal -= 1

            textboxes[0].send_keys(essay1i[idxessayi])
            textboxes[1].send_keys(essay2i[idxessayi])
            idxessayi += 1

        textboxes[2].send_keys(random.choice(["Tidak ada", "tidak ada", "Tidak Ada", "tdk ada"]))

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/HELcHtNYsoRSUhsZ7")

        index+=1
        print("==================")
        print("idxessayk : " + str(idxessayk))
        print("idxessayi : " + str(idxessayi))
        print("")
        print("essaykorea : " + str(essaykorea))
        print("essayindo : " + str(essayindo))
        print("")
        print("usia2 : " + str(usia2))
        print("usia3 : " + str(usia3))
        print("usia4 : " + str(usia4))
        print("")

        times-=1
        print("index  : " + str(index))
        print("times  : " + str(times))
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