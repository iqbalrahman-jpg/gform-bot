from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

# driver = webdriver.Firefox()
driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfeVPSx9B8-Wn9eM_5NPLpMJrpORgjevlc6TAJwuzuKpidBwg/viewform?usp=pp_url")


nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Yuli Ayunda Dewi",
    "Bayu Danang Merta",
]

essay1 = [
    "Setuju, karena dapat mempercepat produksi tanaman melalui teknik seperti rekayasa genetik, penggunaan mikroorganisme yang menguntungkan, dan teknik pemuliaan tanaman yang lebih efisien.",
    "Iya, karena tanaman yang tahan terhadap penyakit, hama, dan kondisi lingkungan yang ekstrem, sehingga meningkatkan produktivitas dan keberlanjutan pertanian.",
    "setuju, karena dengan menggunakan bioteknologi, sifat-sifat tanaman seperti rasa, aroma, gizi, dan nilai tambah lainnya dapat ditingkatkan, sehingga memberikan manfaat bagi konsumen dan pelaku industri pertanian.",
    "setuju, karena bioteknologi memungkinkan transfer gen dari spesies lain ke tanaman, yang dapat menghasilkan tanaman transgenik dengan sifat-sifat yang diinginkan, seperti ketahanan terhadap herbisida, pestisida, atau kondisi lingkungan tertentu.",
    "setuju, dapat mempercepat waktu yang dibutuhkan untuk mengembangkan varietas tanaman baru dapat dipercepat secara signifikan.",
    "Setuju, karena membantu mengembangkan tanaman yang tahan terhadap serangan hama dan penyakit, sehingga mengurangi ketergantungan pada penggunaan pestisida kimia yang berpotensi merusak lingkungan.",
    "karena dengan bioteknologi seperti pengembangan varietas tanaman yang tahan terhadap kekeringan atau salinitas, pertanian dapat dilakukan di lahan yang tidak produktif secara alami, sehingga mengurangi tekanan terhadap lahan pertanian yang subur.",
    "Setuju, bioteknologi dapat digunakan untuk memperbaiki kualitas tanah melalui penggunaan mikroba yang bermanfaat untuk meningkatkan kesuburan tanah, mengurai bahan organik, dan meminimalkan erosi tanah.",
    "bioteknologi seperti biofortifikasi, nutrisi penting dalam tanaman dapat ditingkatkan, seperti peningkatan kandungan zat besi atau vitamin dalam tanaman pangan.",
    "setuju, bioteknologi dapat membantu mengembangkan vaksin tanaman yang dapat melindungi tanaman dari serangan patogen, seperti virus atau bakteri.",
    "Setuju, karena membantu dalam produksi biomaterial dan bioenergi melalui teknik seperti fermentasi mikroba atau produksi biofuel dari tanaman energi.",
    "Bioteknologi dapat digunakan dalam pemantauan lingkungan untuk mendeteksi kontaminan",
]

essay2 = [
    "Memberikan edukasi dan pelatihan kepada petani tentang manfaat dan prinsip-prinsip bioteknologi dalam pertanian.",
    "Memastikan ketersediaan sumber daya seperti benih tanaman bioteknologi dan peralatan yang diperlukan untuk menerapkan teknologi tersebut.",
    "adanya program subsidi atau insentif bagi petani yang menerapkan teknologi bioteknologi dalam pertanian.",
    "kolaborasi antara petani dan institusi riset dalam pengembangan dan implementasi teknologi bioteknologi.",
    "demonstrasi lapangan untuk memperlihatkan secara langsung kepada petani tentang keunggulan dan hasil yang dapat diperoleh dari menerapkan bioteknologi.",
    "Melakukan penyuluhan dan penyadaran kepada petani mengenai manfaat bioteknologi dalam meningkatkan produktivitas dan keberlanjutan pertanian.",
    "Memastikan petani memiliki akses yang mudah terhadap informasi terkini mengenai perkembangan teknologi bioteknologi dalam pertanian.",
    "Membangun kemitraan dengan industri bioteknologi untuk mendukung petani dalam menerapkan teknologi tersebut.",
    "Menyediakan pendanaan atau pembiayaan khusus bagi petani yang ingin menerapkan teknologi bioteknologi dalam pertanian.",
    "Mendorong terbentuknya komunitas petani yang tertarik dan aktif dalam menerapkan prinsip bioteknologi dalam praktik pertanian mereka.",
    "Mendorong penelitian dan pengembangan lebih lanjut dalam bidang bioteknologi pertanian untuk menghasilkan teknologi yang lebih efektif dan terjangkau bagi petani.",
    "Memberikan penghargaan dan pengakuan kepada petani yang berhasil menerapkan prinsip bioteknologi dalam pertanian sebagai bentuk apresiasi dan insentif.",
]
#gapake
kelamin = [3,3,3,3]

times = 12
index = 0
petani = 4
bukan = 8



try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes[0].send_keys(nama[index])

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        if petani != 0 and bukan != 0:
            jawab = random.choice([0,1])
            if jawab == 0:
                petani -= 1
            else:
                bukan -=1
        elif petani == 0:
            jawab = 1
            bukan -= 1
        elif bukan == 0:
            jawab = 0
            petani -= 1

        radiobuttons[jawab].click()
        jenis = random.choice([3,7])
        radiobuttons[jenis].click()
        if jenis == 3:
            tanaman = 11
        else:
            tanaman = random.choice([8,9,10])

        radiobuttons[tanaman].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        mengenal = random.choice([0,0,0,1])
        radiobuttons[mengenal].click()

        time.sleep(2)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textboxes = driver.find_elements("css selector", ".KHxj8b")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        menerapkan = random.choice([0,1])
        radiobuttons[menerapkan].click()
        gunakan = random.choice([3,4,5,6])
        radiobuttons[gunakan].click()

        temp = random.choice([1,2,3,4])
        ecom = random.sample([0,1,2,3],temp)
        for i in ecom :
           checkboxes[i].click()
        
        temp = random.choice([1,2,3])
        ecom = random.sample([5,6,8],temp)
        for i in ecom :
           checkboxes[i].click()

        textboxes[1].send_keys(essay1[index])
        textboxes[2].send_keys(essay2[index])

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfeVPSx9B8-Wn9eM_5NPLpMJrpORgjevlc6TAJwuzuKpidBwg/viewform?usp=pp_url")

        index+=1
        print("==================")
        print("index : " + str(index))

        times-=1
        print("times : " + str(times))
        print("petani : " + str(petani))
        print("bukan : " + str(bukan))
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