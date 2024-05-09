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
driver.get("https://docs.google.com/forms/d/1MPJZqy538Btsd7r2HjgRR70w0bijZmqrTAWSOi2Te38/edit")

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
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Angga Siregar Putra",
    "Putri Keancana",
    "Raja Putra Wardanawan",
    "Affifah Rahman Nabila",
    "Shaka Kurnia Wijaya",
    "Cynara Nafisah",
    "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
    "Fryshta Eka Nabilla",
    "Yanuar Suryadi",
    "Rayhan Adi Wicasa",
    "Sutisna Ayuni",
    "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Ardyanto Rizki Putra",
    "Putra Wirawan",
    "Agung Nugroho",
    "Dani Ramadhan",
    "Dimas Purbo",
    "Nabilla Syaqila Qolbi",
]

domisili = [
    "Yogyakarta",
    "surabaya",
    "Bali",
    "Bandung",
    "Bekasi",
    "Bekasi",
    "Bandung",
    "medan",
    "banyuwangi",
    "surabaya",
    "Bandung",
    "banyuwangi",
    "Bekasi",
    "jawa timur",
    "gresik",
    "semarang",
    "jakarta",
    "surabaya",
    "surabaya",
    "semarang",
    "DKI Jakarta",
    "Bekasi",
    "jakarta",
    "DKI Jakarta",
    "Bandung",
    "jakarta",
    "jawa timur",
    "surabaya",
    "jawa timur",
    "surabaya",
    "Bandung",
    "surabaya",
    "denpasar",
    "Surabaya",
    "jawa timur",
    "Bekasi",
    "DKI Jakarta",
    "Bali",
    "banyuwangi",
    "jawa timur",
    "Bali",
    "Surabaya",
    "DKI Jakarta",
    "Bandung",
    "gresik",
    "gresik",
    "banyuwangi",
    "jakarta",
    "Yogyakarta",
    "banyuwangi",
]

alasan = [
    "Harga murah terjangkau bagi semua kalangan",
    "Rasa enak yang dihadirkan menjadi pilihan favorit",
    "Tempat nyaman dan bersih menciptakan suasana yang mengundang untuk duduk lebih lama",
    "Harga murah dan tempat nyaman menjadi alasan utama mengapa banyak orang datang",
    "Rasa enak dan tempat nyaman memberikan pengalaman makan yang menyenangkan",
    "Harga murah dan rasa enak menjadikan pilihan yang menguntungkan",
    "Tempat nyaman dan bersih memberikan kenyamanan saat menikmati hidangan",
    "Harga murah dan tempat bersih memberikan nilai lebih bagi pengunjung",
    "Rasa enak dan tempat bersih menjadi destinasi kuliner yang direkomendasikan",
    "Harga murah, rasa enak, dan tempat nyaman menjadi kombinasi yang sulit ditolak",
    "Tempat nyaman dan harga murah membuat menjadi opsi terbaik di kawasan tersebut",
    "Rasa enak dan tempat bersih menjadi kelebihan utama dari tempat ini",
    "Harga murah dan tempat nyaman memenuhi kebutuhan pelanggan yang mencari pengalaman kuliner yang terjangkau",
    "Rasa enak dan tempat nyaman menciptakan suasana yang mengundang kembali",
    "Harga murah, tempat nyaman, dan bersih menjadi alasan mengapa orang-orang terus datang",
    "Rasa enak, tempat nyaman, dan harga murah menghasilkan kombinasi yang memikat",
    "Tempat bersih dan harga murah menjadi pilihan yang menarik bagi wisatawan",
    "Rasa enak, tempat nyaman, dan bersih memberikan pengalaman makan yang menyenangkan",
    "Harga murah dan tempat bersih menjadikan pilihan yang terjangkau dan berkualitas",
    "Rasa enak, tempat nyaman, dan harga murah",
    "Harga murah membuatnya menjadi opsi yang terjangkau bagi pelanggan",
    "Rasa enak mengundang selera untuk mencoba lagi",
    "Tempat nyaman dan bersih memberikan suasana yang menyenangkan saat makan",
    "Harga murah dan rasa enak adalah kombinasi yang sulit ditolak",
    "Tempat nyaman dan harga murah memberikan nilai tambah bagi pengunjung",
    "Rasa enak dan tempat bersih menjadikannya tempat yang layak dikunjungi",
    "Harga murah dan tempat nyaman membuatnya menjadi pilihan favorit",
    "Rasa enak, tempat nyaman, dan harga murah memberikan pengalaman kuliner yang memuaskan",
    "Tempat bersih dan harga murah menjadi alasan untuk kembali datang",
    "Rasa enak, tempat nyaman, dan bersih adalah standar yang dihadirkan oleh tempat ini",
    "Harga murah, rasa enak, dan tempat bersih membuatnya berbeda dari tempat lain",
    "Tempat nyaman dan harga murah menghadirkan nilai lebih bagi para pelanggan",
    "Rasa enak dan tempat bersih memberikan kesan yang baik kepada pengunjung",
    "Harga murah dan tempat nyaman menciptakan kombinasi yang menarik perhatian",
    "Rasa enak, tempat nyaman, dan harga murah adalah alasan utama mengapa orang datang",
    "Tempat bersih dan harga murah menjadi nilai tambah dari pengalaman makan di tempat ini",
    "Rasa enak, tempat nyaman, dan bersih memberikan kepuasan yang maksimal",
    "Harga murah dan tempat bersih memberikan nilai ekonomis dan kenyamanan",
    "Rasa enak dan tempat nyaman menjadi daya tarik yang membuat selalu ramai",
    "Harga murah, rasa enak, dan tempat bersih memberikan pengalaman makan yang menyenangkan",
    "Harga murah dan tempat nyaman menjadikannya tempat yang cocok untuk keluarga",
    "Rasa enak dan harga murah menjadi pilihan tempat yang terjangkau bagi pecinta kuliner",
    "Tempat bersih dan rasa enak menciptakan pengalaman makan yang memuaskan",
    "Harga murah, rasa enak, dan tempat nyaman menjadi kombinasi yang sempurna",
    "Tempat nyaman dan bersih membuatnya menjadi tempat yang ideal untuk bersantai sambil menikmati hidangan lezat",
    "Rasa enak dan tempat nyaman membuat pengunjung betah berlama-lama di sana",
    "Harga murah dan tempat bersih memberikan nilai tambah bagi pengunjung",
    "Tempat nyaman dan harga murah memberikan nilai lebih dalam pengalaman kuliner",
    "Rasa enak dan tempat bersih membuat pengunjung merasa puas dan nyaman",
    "Harga murah, rasa enak, dan tempat nyaman menjadikan tempat tersebut menjadi favorit banyak orang",
]

harapan = [
    "Saya berharap terus berinovasi dalam menyajikan menu-menu baru yang kreatif",
    "Semoga selalu memiliki ide-ide segar untuk inovasi kuliner yang menarik",
    "Harapannya, terus berinovasi dalam menciptakan hidangan yang unik dan menggugah selera",
    "Saya berharap ada terus menerus inovasi pada cita rasa makanan yang disajikan di tempat ini",
    "Semoga selalu berusaha untuk lebih berinovasi dalam mengeksplorasi resep-resep baru",
    "Harapan saya, terus berinovasi dengan menghadirkan sajian yang tidak terduga dan mengejutkan",
    "Saya berharap senantiasa menciptakan pengalaman kuliner yang inovatif dan berbeda dari yang lain",
    "Semoga selalu berani melakukan inovasi dalam hal presentasi makanan yang menarik",
    "Harapannya, terus berinovasi dalam menciptakan menu vegetarian atau vegan yang lezat dan kreatif",
    "Saya berharap ada terus menerus inovasi dalam penyajian makanan yang dapat menggugah selera pengunjung",
    "Semoga selalu mengikuti tren terbaru dan berinovasi dengan konsep-konsep yang segar",
    "Harapan saya, terus berinovasi dalam menghadirkan suasana yang unik dan menarik bagi pengunjung",
    "Saya berharap senantiasa menghadirkan menu-menu spesial sebagai bentuk inovasi dalam penawaran makanan",
    "Semoga selalu berinovasi dalam menciptakan hidangan yang cocok dengan berbagai preferensi dan kebutuhan makanan",
    "Harapannya, terus berinovasi dengan memanfaatkan bahan-bahan lokal dan tradisional untuk menciptakan cita rasa yang autentik",
    "Saya berharap ada terus menerus inovasi dalam penyajian minuman yang kreatif dan menggugah selera",
    "Semoga selalu berinovasi dalam menghadirkan menu-menu sehat yang lezat dan menarik",
    "Harapan saya, terus berinovasi dalam menciptakan suasana yang ramah lingkungan dan berkelanjutan",
    "Saya berharap senantiasa menghadirkan kejutan-kejutan kuliner melalui inovasi yang terus dilakukan",
    "Semoga selalu berinovasi dalam menyediakan opsi makanan bagi mereka yang memiliki diet khusus atau alergi",
    "Harapannya, terus berinovasi dengan menyajikan menu-menu dengan konsep fusion yang menarik",
    "Saya berharap ada terus menerus inovasi dalam menghadirkan hidangan yang menggabungkan cita rasa tradisional dan modern",
    "Semoga selalu berinovasi dalam menciptakan pengalaman kuliner yang tak terlupakan",
    "Harapan saya, terus berinovasi dalam menciptakan makanan yang tidak hanya lezat, tetapi juga estetis secara visual",
    "Saya berharap senantiasa menghadirkan kejutan baru melalui inovasi yang terus mereka lakukan",
    "Semoga terus berinovasi dalam menyediakan pilihan menu yang ramah bagi mereka yang memiliki alergi makanan",
    "Harapannya, terus berinovasi dalam menghadirkan hidangan yang menggabungkan rasa lokal dan internasional",
    "Saya berharap ada terus menerus inovasi dalam penggunaan bahan-bahan organik dan segar dalam menu makanan di tempat ini",
    "Semoga selalu berinovasi dengan menghadirkan hidangan seimbang yang mengutamakan nutrisi dan kesehatan",
    "Harapan saya, terus berinovasi dalam menyediakan opsi makanan vegetarian yang lezat dan menggugah selera",
    "Saya berharap senantiasa menghadirkan menu-menu seasonal yang berubah-ubah sesuai dengan ketersediaan bahan",
    "Semoga selalu berinovasi dalam menghadirkan pengalaman makan yang interaktif dan menyenangkan",
    "Harapannya, terus berinovasi dengan menggali potensi bahan lokal dan mendukung industri lokal",
    "Saya berharap ada terus menerus inovasi dalam menyajikan hidangan dengan teknik masak yang kreatif dan unik",
    "Semoga selalu berinovasi dalam memperluas pilihan menu untuk mengakomodasi berbagai selera dan preferensi",
    "Harapan saya, terus berinovasi dengan menghadirkan hidangan tradisional dengan sentuhan modern",
    "Saya berharap senantiasa menghadirkan suasana yang cozy dan mengundang untuk dinikmati bersama keluarga dan teman",
    "Semoga selalu berinovasi dalam menyediakan menu khusus anak-anak yang sehat dan menggemaskan",
    "Harapannya, terus berinovasi dalam menyediakan makanan untuk kebutuhan diet tertentu seperti keto, vegan, atau gluten-free",
    "Saya berharap ada terus menerus inovasi dalam penyajian hidangan dengan sentuhan artistik yang menggugah selera dan indra penglihatan",
    "Semoga selalu berinovasi dalam menyediakan minuman segar dan unik yang menciptakan pengalaman yang menyegarkan",
    "Harapan saya, terus berinovasi dengan menghadirkan konsep ruang yang Instagramable untuk menciptakan momen berbagi yang berkesan",
    "Saya berharap senantiasa menghadirkan acara khusus seperti cooking class atau food tasting untuk meningkatkan interaksi dengan pengunjung",
    "Semoga selalu berinovasi dalam menyediakan pelayanan yang ramah, efisien, dan personal kepada setiap pengunjung",
    "Harapannya, terus berinovasi dengan menggali cerita di balik setiap hidangan untuk memberikan pengalaman yang lebih mendalam kepada pengunjung",
    "Saya berharap ada terus menerus inovasi dalam penggunaan teknologi dalam pemesanan dan pembayaran di sini",
    "Semoga selalu berinovasi dalam memperluas jangkauan delivery service untuk memberikan kenyamanan kepada pengunjung",
    "Harapan saya, terus berinovasi dalam menyediakan paket makanan siap saji untuk memudahkan konsumen yang sibuk",
    "Saya berharap senantiasa menghadirkan program loyalitas atau reward untuk menghargai setiap kunjungan pengunjung",
    "Semoga selalu berinovasi dalam menjaga kebersihan dan keamanan di setiap area, memberikan rasa aman bagi pengunjung",
]

times = 50
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(domisili[index])
        driver.implicitly_wait(4)

        textarea[0].send_keys(alasan[index])
        textarea[1].send_keys(harapan[index])
        driver.implicitly_wait(4)

        radiobuttons[0].click()
        radiobuttons[random.choice([1,2])].click()
        radiobuttons[random.choice([3,4])].click()
        radiobuttons[random.choice([5,6,6])].click()
        radiobuttons[7].click()

        driver.implicitly_wait(4)
        p = 0 
        soal = 5
        while soal:
            s1 = random.choice([p,p+1,p+2,p+3,p+4,p+5,p+6,p+7,p+5,p+6,p+7,p+5,p+6,p+7,p+8,p+9])
            testcheck[s1].click()
            p += 10
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/1MPJZqy538Btsd7r2HjgRR70w0bijZmqrTAWSOi2Te38/edit")

        index+=1
        print("==================")
        # print("  : " + str())
        # print("")
        
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