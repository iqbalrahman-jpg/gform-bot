from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("http://tinyurl.com/PrototipeCatcalling")

#nama atau inisial
nama = [
        "Mutia Ayu Nur",
    "Ali Hasanudin",
        "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
        "Nana Annisa",
        "Putri Kirana Dewi",
        "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
        "Yuli Ayunda Dewi",
    "Bayu Danang Merta",
        "Bellanda Clara Ayunda", 
    "Budi Suryanto",
        "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
        "Annisa Chania",
    "Fattahilah Sadewa",
        "Diah Ayu Cindy",
    "Attaka Majid",
        "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
        "Nia EKa Yuliana",
    "Bayu Dwiganara",
        "Syifa Radifah",
]

#satu kata saat mendengar kata catcalling
satukata = [
    "Seksisme",
    "Pelecehan",
    "Kekerasan",
    "Diskriminasi",
    "Intimidasi",
    "Patriarki",
    "Kekuasaan",
    "Merendahkan",
    "buruk",
    "pelecehan",
    "Penghinaan",
    "Meresahkan",
    "Memalukan",
    "Menyebalkan",
    "Merendahkan",
    "Menyakiti",
    "Mempermalukan",
    "Ketidaknyamanan",
    "Ketakutan",
    "Kesalahan",
    "jelek",
    "Penghinaan",
    "Kekerasan",
    "Buruk",
    "Menyebalkan",
    "Tidak pantas",
]

#perasaan saat melakukan catcalling (jumlah e podokno pernahP)
melakukanP = [
    "Terkadang merasa senang, terkadang membosankan",
    "Menyenangkan saat melihat dia terdiam",
    "Senang",
    "Menyesal setelah melakukannya",
    "terasa lega",
    "ingin melakukannya lagi, walaupun terkadang merasa kasihan",
    "Bisa membalaskan rasa dendam",
    "Terkadang kasihan tapi cukup menyenangkan",
    "Merasa seperti superior"
]

#perasaan saat mendapatkan catcalling (jumlah e padakno pernahK)
mendapatkanP = [
    "Tidak nyaman dan terintimidasi ketika mendapatkan catcalling",
    "perasaan saya campur aduk antara takut dan marah.",
    "Merasa kesal dan marah",
    "Terkadang membuat saya merasa tidak dihargai sebagai manusia yang sepadan",
    "Merasa direndahkan dan tak dihargai sebagai manusia",
    "Perasaan tidak nyaman dan terganggu selalu muncul saat saya mendapatkannya",
    "Merasa seperti objek seksual yang tidak dihargai sebagai manusia yang utuh.",
    "Saya merasa tidak aman dan terancam saat mendapatkan catcalling, terutama di tempat umum yang ramai.",
    "Perasaan tidak enak dan terintimidasi selalu muncul ketika saya mendapatkan catcalling, terutama dari seseorang yang agresif.",
    "Mendapatkan catcalling membuat saya merasa tidak nyaman dan merugikan, karena hal itu bisa mengganggu keseharian dan kenyamanan saya.",
    "tidak nyaman dan terganggu",
    "merasa sedih saat seseorang melakukannya",
    "sedih saat mendapatkan perilaku catcalling",
    "Tidak senang dan sedih",
]

contoh = [
    "Meniup klakson mobil dengan keras saat melihat wanita yang sedang berjalan di trotoar.",
    "Melambaikan tangan dan mengucapkan kata-kata cabul saat melihat wanita yang sedang berjalan di jalan.",
    "Memanggil atau meneriakkan nama panggilan yang tidak sopan kepada wanita yang sedang berjalan di jalan.",
    "Mengikuti atau mengintai wanita yang sedang berjalan sendirian.",
    "Membuat gerakan isyarat atau mengeluarkan suara menggoda saat melihat wanita yang sedang berjalan di dekatnya.",
    "Memandang dengan seksual atau berbicara dengan kata-kata cabul kepada wanita yang sedang berjalan di jalan.",
    "Melakukan komentar cabul atau seksual terhadap penampilan fisik wanita yang sedang berjalan di jalan.",
    "Menjadi lebih agresif dan membuat komentar atau gerakan yang lebih mengintimidasi saat ada kelompok wanita yang sedang berjalan.",
    "Menunggu di tempat-tempat yang sering dilewati wanita dan melakukan komentar atau gerakan cabul saat melihat mereka.",
    "Memperlihatkan atau menunjukkan kemaluan secara terang-terangan saat melihat wanita yang sedang berjalan di jalan.",
    "Melakukan tindakan atau gerakan yang mengarah pada pelecehan seksual terhadap wanita yang sedang berjalan di jalan.",
    "Memperlihatkan atau menunjukkan benda-benda cabul kepada wanita yang sedang berjalan di jalan.",
    "Melakukan gerakan atau suara yang mengganggu atau mengintimidasi saat berpapasan dengan wanita yang sedang berjalan di jalan.",
    "Melakukan tindakan atau gerakan cabul kepada wanita yang sedang berjalan di jalan dengan menggunakan telepon genggam.",
    "Memasang stiker atau gambar cabul di mobil atau tempat umum yang sering dilalui wanita.",
    "Membuat gerakan cabul atau seksual kepada wanita yang sedang bekerja di tempat umum seperti kasir atau pelayan toko.",
    "Mengeluarkan suara yang mengganggu atau cabul kepada wanita yang sedang menunggu transportasi umum.",
    "Membuat gerakan atau suara cabul terhadap wanita yang sedang bersepeda atau berolahraga di jalan.",
    "Menyentuh atau mencolek tubuh wanita secara tidak sopan saat berpapasan di jalan.",
    "Mengikuti atau mengintai wanita yang sedang berada di dalam kendaraan.",
    "Menyusul atau mengikuti wanita yang sedang berjalan dengan harapan bisa berkenalan atau mendapatkan nomor telepon.",
    "Mengajak atau meminta wanita yang sedang berjalan untuk menemani atau bergabung dengan mereka.",
    "Menyebarkan rumor atau mengadu domba tentang wanita yang sering lewat di jalan.",
    "Memaksa atau mengancam agar wanita memberikan nomor telepon atau berkumpul dengan mereka.",
    "Membuat tindakan atau gerakan cabul saat berada di tempat umum seperti taman atau gedung perk",
]

pandangan = [
    "Menurut saya, catcalling adalah perilaku yang tidak pantas dan tidak menghormati hak privasi seseorang.",
    "Pandangan saya tentang catcalling adalah bahwa ini adalah bentuk pelecehan verbal yang harus dihentikan.",
    "Saya percaya bahwa catcalling adalah perilaku yang merendahkan dan sangat tidak sopan.",
    "Catcalling adalah bentuk diskriminasi gender dan harus dihentikan secepatnya.",
    "Saya merasa sangat tidak nyaman saat mengalami catcalling dan saya berharap bahwa orang-orang akan lebih memahami betapa merugikannya perilaku ini.",
    "Catcalling adalah tindakan yang sangat tidak hormat dan membuat banyak perempuan merasa terancam.",
    "Saya berpikir bahwa catcalling tidak hanya tidak pantas, tetapi juga merupakan tindakan yang melanggar hak asasi manusia.",
    "Saya percaya bahwa setiap orang berhak merasa aman saat berjalan-jalan di jalan raya tanpa takut menjadi korban catcalling.",
    "Catcalling adalah bentuk pelecehan seksual yang tidak boleh diabaikan.",
    "Pandangan saya tentang catcalling adalah bahwa ini adalah tindakan yang sangat tidak sopan dan tidak menghargai privasi orang lain.",
    "Saya sangat tidak setuju dengan catcalling karena itu dapat merusak mental seseorang dan membuat mereka merasa tidak aman.",
    "Saya percaya bahwa orang-orang harus bertanggung jawab atas perilaku mereka dan menghindari melakukan catcalling.",
    "Saya merasa sangat tidak nyaman saat mengalami catcalling dan berharap agar orang lain memahami betapa mengganggunya perilaku ini.",
    "Catcalling adalah tindakan yang merendahkan dan tidak menghargai martabat seseorang.",
    "Saya berharap masyarakat bisa lebih sadar tentang bahayanya catcalling dan mengambil tindakan untuk mencegahnya.",
    "Catcalling adalah bentuk pelecehan yang harus dihentikan dan orang harus bertanggung jawab atas tindakan mereka.",
    "Saya percaya bahwa catcalling adalah tindakan yang tidak menghormati privasi seseorang dan harus dihentikan.",
    "Saya berharap masyarakat dapat lebih memahami betapa merusaknya catcalling dan mengambil langkah-langkah untuk menghindarinya.",
    "Catcalling bukanlah suatu hal yang bisa dianggap remeh karena dapat menimbulkan trauma dan merusak mental seseorang.",
    "Saya berpikir bahwa catcalling adalah perilaku yang sangat tidak pantas dan membuat banyak orang merasa tidak aman.",
    "Saya berharap orang lain bisa memahami betapa tidak sopannya perilaku catcalling dan menghindarinya.",
    "Saya merasa sangat tidak nyaman saat mengalami catcalling dan berharap agar tidak ada orang lain yang mengalami hal yang sama.",
    "Pandangan saya tentang catcalling adalah bahwa ini adalah bentuk pelecehan dan tidak boleh diabaikan.",
    "Saya percaya bahwa masyarakat harus lebih aktif dalam mencegah catcalling dan membuat lingkungan yang aman bagi semua orang.",
    "Catcalling adalah perilaku yang sangat tidak sopan dan tidak pantas di masyarakat yang sudah maju seperti saat ini.",
]

#0 laki, 1 perempuan
kelamin = [1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1]

times = 25
index = 0

#melakukan catcalling (pelaku)
pernahP = 9
tidakP = 16
indexPP = 0

#mendapatkan catvalling (korban)
pernahK = 14
tidakK = 11
indexPK = 0


try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah 
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textboxes1 = driver.find_elements("css selector", ".KHxj8b")#isian
        
        pelecehan = random.choice([2,2,2,2,2,3,4,4,4])
        usia = random.randint(18,30)

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(usia)
        driver.implicitly_wait(4)
        radiobuttons[kelamin[index]].click()

        driver.implicitly_wait(4)
        textboxes[2].send_keys(satukata[index])

        radiobuttons[pelecehan].click()

        if pernahP != 0 and tidakP != 0:
            time.sleep(2)
            random_item = random.choice([1,2])
            if random_item == 1:
                radiobuttons[5].click()
                textboxes1[0].send_keys(melakukanP[indexPP])
                indexPP += 1
                pernahP -= 1
            else:
                radiobuttons[6].click()
                textboxes1[0].send_keys("-")
                tidakP -= 1
        elif pernahP != 0 and tidakP == 0:
            time.sleep(2)
            radiobuttons[5].click()
            textboxes1[0].send_keys(melakukanP[indexPP])
            indexPP += 1
            pernahP -= 1
        elif pernahP == 0 and tidakP != 0:
            time.sleep(2)
            radiobuttons[6].click()
            textboxes1[0].send_keys("-")
            tidakP -= 1

        if pernahK != 0 and tidakK != 0:
            time.sleep(2)
            random_item = random.choice([1,2])
            if random_item == 1:
                radiobuttons[7].click()
                textboxes1[1].send_keys(mendapatkanP[indexPK])
                indexPK += 1
                pernahK -= 1
            else:
                radiobuttons[8].click()
                textboxes1[1].send_keys("-")
                tidakK -= 1
        elif pernahK != 0 and tidakK == 0:
            time.sleep(2)
            radiobuttons[7].click()
            textboxes1[1].send_keys(mendapatkanP[indexPK])
            indexPK += 1
            pernahK -= 1
        elif pernahK == 0 and tidakK != 0:
            time.sleep(2)
            radiobuttons[8].click()
            textboxes1[1].send_keys("-")
            tidakK -= 1

        driver.implicitly_wait(4)
        textboxes1[2].send_keys(contoh[index])
        textboxes1[3].send_keys(pandangan[index])

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("http://tinyurl.com/PrototipeCatcalling")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")
        print("pernahP : " + str(pernahP))
        print("tidakP  : " + str(tidakP))
        print("indexPP : " + str(indexPP))
        print("")
        print("pernahK : " + str(pernahK))
        print("tidakK : " + str(tidakK))
        print("indexPK : " + str(indexPK))
        print("")

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