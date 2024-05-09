from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Firefox()
driver.get("https://forms.gle/fBtVHnPMWtgfmsjm8")
times = 12

email = [
    "alihasn.01.10@gmail.com",
    "risfebri11@gmail.com",
    "budprasety@gmail.com",
    "aryonugh@gmail.com",
    "yahnugrah@gmail.com",
    "nandayundaa1@gmail.com",
    "yudipradan01@gmail.com",
    "byumerta1@gmail.com",
    "budsuryant01@gmail.com",
    "dwa.lingga10@gmail.com",
   
    "alffiantoro@gmail.com",
    "fataahxdewa@gmail.com",
    "attakmajid@gmail.com",
    "fabiannadeo@gmail.com",
    "bayudwiganara@gmail.com",
    "aditferdinanda@gmail.com",
    "reyhanutomowa@gmail.com",
    "anggasiregarp@gmail.com",
    "rajawardanawan@gmail.com",
    "shakapwijaya@gmail.com",
   
    "mahendrejaa@gmail.com",
    "yanrasuryad@gmail.com",
    "hafidz.mhd.92@gmail.com",
    "syahrul.ahmd@gmail.com",
    "dian.agus89@gmail.com",
    "irfan.hkm.97@gmail.com",
    "rizkymaulana96@gmail.com",
    "rian.prtma@gmail.com",
    "fajar.gnwn.94@gmail.com",
    "alvin.adtya.95@gmail.com",
    
    "putra.wrwn.98@gmail.com",
    "bima.pratm.93@gmail.com",
    "agung.ngrh.90@gmail.com",
    "fikri.fauz.91@gmail.com",
    "dani.ramdhn.89@gmail.com",
    "rendra.ksma@gmail.com",
    "yoga.prtma.97@gmail.com",
    "ilham.akbar.92@gmail.com",
    "fadhil.mlna.96@gmail.com",
    "bintang.wcksna@gmail.com",
]

nama = [
    "Ali Hasanudin",
    "Rizki Bagas Febri",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Yahya Nugraha",
    "Nanda Nurahmad",
    "Yudi Pradanawan",
    "Bayu Danang Merta",
    "Budi Suryanto",
    "Sadewa Lingga Budiantoro",

    "Alffianto Kuntoro",
    "Fattahilah Sadewa",
    "Attaka Majid",
    "Fabian Nadeo Putra",
    "Bayu Dwiganara",
    "Aditya Derdinand",
    "Reyhan Utomowa",
    "Angga Siregar Putra",
    "Raja Putra Wardanawan",
    "Shaka Kurnia Wijaya",

    "Mahendra Rhejaa Fadilah",
    "Yanuar Suryadi",
    "Muhammad Hafidz",
    "Ahmad Syahrul",
    "Dian Agus",
    "Irfan Hakim",
    "Rizky Maulana",
    "Rian Pratama",
    "Fajar Gunawan",
    "Alvin Aditya",
    
    "Putra Wirawan",
    "Bima Pratama",
    "Agung Nugroho",
    "Fikri Fauzi",
    "Dani Ramadhan",
    "Rendra Kusuma",
    "Yoga Pratama",
    "Ilham Akbar",
    "Fadhil Maulana",
    "Bintang Wicaksana",

]

#40
pendapat = [
"Tampilan logo Chief Barber and Supplies Co sungguh modern dan menarik.",
"Bentuk logo tersebut memperlihatkan tema utama merek dengan sangat baik.",
"Logo ini memberikan kesan berkelas dan eksklusif.",
"Warna hitam putih pada logo menambah kesan kuat dan tangguh dari brand.",
"Huruf pada logo terkomposisi dengan keren dan berkesan.",
"Simbol dalam logo memberikan kesan kepercayaan dan keamanan.",
"Logo ini cocok dengan industri yang diwakilinya.",
"Desain logo menampilkan kesan keberanian dan keberhasilan.",
"Logo ini menunjukkan profesionalisme dan ketangguhan yang dibutuhkan untuk bisnis barber.",
"Font yang digunakan pada logo menambah kesan modern dan stylish.",
    
"Saya sangat kagum dengan desain logo Chief Barber and Supplies Co yang sangat modern dan elegan.",
"Bentuknya yang unik berhasil menggambarkan tema utama merek dengan sangat baik.",
"Tampilan hitam-putih menambah kesan kuat dan tangguh dari brand.",
"Simbol dalam logo memberikan kesan kepercayaan dan keamanan kepada para konsumen.",
"Menurut saya, logo ini sangat cocok untuk industri barber",
"Logo ini menampilkan kesan keberanian dan keberhasilan yang diperlukan dalam bisnis ini.",
"Saya juga sangat terkesan dengan font yang digunakan pada logo, yang memberikan kesan modern dan stylish."
"Logo ini menggambarkan kesan berkelas dan eksklusif.",
"Desain logo ini sangat mudah dikenali dan mengundang ketertarikan.",
"Logo Chief Barber and Supplies Co terlihat sangat memorable dan mudah diingat.",
    
"Desain logo ini cocok untuk digunakan sebagai merek dagang atau ikonik yang kuat dan berkesan.",
"Logo ini menggambarkan kesan eksklusif dan berkelas yang akan memperkuat citra merek.",
"Logo ini menciptakan perpaduan warna hitam putih yang kuat, menunjukkan kesan keberanian dan kepemimpinan.",
"Chief Barber and Supplies Co memiliki logo yang unik dan menarik perhatian dengan bentuk yang sangat istimewa.",
"Bentuk logo yang sangat unik menambahkan daya tarik pada merek tersebut dan menarik konsumen untuk memilihnya.",
"Desain logo memberikan kesan profesional dan terpercaya bagi para pelanggan.",
"Logo ini menunjukkan kesan modern dan terkini dalam industri barber sehingga akan selalu up-to-date.",
"Simbol logo memberikan kesan keamanan dan kenyamanan bagi pelanggan, membuat mereka merasa aman dan nyaman selama menggunakan layanan.",
"Logo ini sangat cocok digunakan sebagai representasi dari bisnis barber yang kuat dan terpercaya.",
"Logo ini menunjukkan bahwa merek tersebut memiliki kesan stylish dan modern yang disukai oleh para konsumen muda dan trendi."
    
"Logo ini terlihat sangat mudah dikenali dan mudah diingat.",
"Desain logo ini terlihat sangat fresh dan up-to-date.",
"Logo ini sangat cocok untuk pelanggan yang ingin tampil stylish dan trendy.",
"Logo ini terlihat sangat eksklusif dan premium.",
"Logo ini menggambarkan kesan berkelas dan eksklusif.",
"Desain logo ini menampilkan kesan modern dan terkini.",
"Teks logo memberikan kesan keamanan dan kepercayaan bagi pelanggan.",
"Logo ini terlihat sangat kuat dan profesional.",
"Bentuk pada logo menampilkan kesan khas Amerika",
"Logo ini menggambarkan kesan eksklusif.",

"Bentuk pada logo menampilkan kesan khas Amerika",
"Logo ini menggambarkan kesan eksklusif.",
]

alsy = [
"Logo Chief Barber and Supplies Co memiliki desain ikonik yang tahan lama.",
"Desain logo sederhana dan mudah diingat, sehingga mudah diidentifikasi oleh konsumen.",
"Logo terlihat profesional dan dapat dipercaya oleh konsumen yang mencari layanan barber berkualitas.",
"Desain logo menggambarkan kesan kekuatan yang relevan untuk bisnis barber.",
"Warna hitam pada logo memberikan kesan keberanian dan keberhasilan yang cocok untuk bisnis barber.",
"Logo Chief Barber and Supplies Co mudah diingat oleh konsumen karena terlihat memorable.",
"Desain logo klasik dan elegan cocok untuk pasar yang lebih tua atau tradisional.",
"Bentuk teks pada logo menggambarkan tema Amerika yang selalu populer.",
"Logo cocok digunakan di berbagai platform pemasaran, termasuk website, media sosial, dan materi pemasaran cetak.",
"Desain logo yang sederhana dan mudah diingat membuatnya mudah diingat dan mudah diidentifikasi.",

"Desain logo ini terlihat sangat modern dan up-to-date sehingga tetap relevan di era digital saat ini.",
"Logo ini terlihat sangat unik dan menarik perhatian sehingga tetap relevan di pasar yang semakin kompetitif.",
"Logo ini terlihat sangat stylish dan cocok bagi konsumen yang mencari pelayanan barber yang trendy.",
"Desain logo ini sangat fleksibel dan dapat dengan mudah diubah atau dimodifikasi agar tetap relevan di masa depan.",
"Logo menunjukkan kepercayaan dan keamanan, yang selalu relevan bagi bisnis yang berfokus pada layanan pelanggan.",
"Logo ini menggambarkan kesan kelas dan eksklusif yang relevan bagi konsumen yang mencari pengalaman barber yang mewah.",
"Desain logo ini dapat dengan mudah diaplikasikan pada berbagai produk atau layanan yang ditawarkan oleh merek ini.",
"Warna hitam putih pada logo memberikan kesan keberanian dan kepemimpinan, yang relevan bagi bisnis barber yang ingin menonjol di pasar.",
"Logo Chief Barber and Supplies Co memperlihatkan kesan profesionalisme dan ketangguhan yang relevan bagi bisnis barber.",
"Desain logo ini sangat mudah dikenali dan mudah diingat oleh konsumen, sehingga tetap relevan di pasar yang semakin sibuk dan penuh dengan persaingan."
]

alst = [
"Logo terlihat kuno bagi konsumen yang mencari pengalaman barber yang lebih trendi.",
"Desain logo yang sederhana dan klasik mungkin tidak cukup menarik bagi konsumen yang mencari merek yang lebih berwarna dan eksentrik.",
"Logo terlalu simpel dan kurang dapat membedakan diri dari merek barber lainnya.",
"Warna hitam putih pada logo mungkin terlalu sederhana bagi konsumen yang mencari suasana yang lebih tenang dan santai saat memotong rambut.",
"Logo terlalu intimidatif atau seram bagi beberapa konsumen.",
"Logo ini terlalu terkait dengan tema Amerika yang mungkin kurang relevan bagi konsumen di negara-negara lain.",
"Desain logo yang terlalu kaku dan formal mungkin tidak dapat menarik perhatian konsumen yang mencari pengalaman yang lebih santai dan informal.",
"Logo terlalu serius dan kurang menggambarkan kesan keceriaan dan kesenangan yang diinginkan oleh beberapa konsumen.",
"Desain logo yang tidak dapat dimodifikasi dengan mudah mungkin menjadi keterbatasan bagi perusahaan di masa depan.",
"Logo kurang fleksibel dan tidak dapat dengan mudah diubah agar tetap relevan di masa depan.",

"Desain logo yang terlihat terlalu klasik mungkin tidak dapat memikat hati konsumen muda atau generasi milenial.",
"Logo ini mungkin terlalu bias gender dan tidak mencerminkan keberagaman yang diinginkan oleh beberapa konsumen.",
"Desain logo yang terlalu seragam mungkin kurang menarik bagi konsumen yang mencari merek dengan gaya yang lebih kreatif dan unik.",
"Logo ini mungkin terlalu terkait dengan industri barber tradisional dan kurang mencerminkan inovasi atau kemajuan di bidang barber.",
"Desain logo yang terlihat terlalu serius mungkin kurang menarik bagi konsumen yang mencari pengalaman barber yang lebih santai dan ramah.",
"Logo ini mungkin terlalu mudah dilupakan oleh konsumen karena desainnya yang sederhana dan klasik.",
"Desain logo yang terlalu umum dan tidak menonjol mungkin tidak dapat membedakan diri dari merek barber lainnya.",
"Logo ini mungkin terlalu terfokus pada produk dan kurang menekankan pengalaman pelanggan.",
"Desain logo yang terlihat kurang dinamis dan tidak dapat beradaptasi dengan perubahan pasar mungkin membuatnya kurang relevan di masa depan.",
"Logo ini mungkin kurang menarik bagi konsumen yang mencari pengalaman barber yang lebih modern dan teknologi-terkini."

]

alasanBrand = [
"Brand hair styling memberikan hasil yang memuaskan sesuai keinginan.",
"Produk hair styling aman dan tidak merusak rambut.",
"Brand hair styling memiliki produk yang sesuai dengan jenis rambut.",
"Harga produk hair styling terjangkau.",
"Brand hair styling mudah ditemukan di toko dan online shop.",
"Produk hair styling memiliki aroma yang enak.",
"Penggunaan produk hair styling tidak menimbulkan iritasi pada kulit kepala.",
"Brand hair styling menggunakan bahan berkualitas tinggi dan ramah lingkungan.",
"Produk hair styling tahan lama.",
"Brand hair styling memberikan tips untuk perawatan rambut."
    
"Memberikan hasil yang memuaskan dan sesuai dengan keinginan.",
"Terbukti aman dan tidak merusak rambut.",
"Menyediakan berbagai macam produk yang sesuai dengan kebutuhan dan jenis rambut.",
"Harga yang terjangkau dan tidak memberatkan dompet.",
"Mudah ditemukan dan tersedia di banyak toko dan online shop.",
"Aroma yang enak dan tidak menyengat.",
"Tidak menimbulkan iritasi atau alergi pada kulit kepala.",
"Menggunakan bahan-bahan berkualitas tinggi dan ramah lingkungan.",
"Tahan lama dan tidak mudah rusak.",
"Memberikan tips dan saran yang berguna untuk perawatan rambut.",

"Ketombe atau masalah kulit kepala lainnya tidak akan muncul saat menggunakan produk hair styling ini.",
"Kesehatan rambut menjadi prioritas utama bagi brand hair styling, sehingga mereka memberikan formula khusus untuk mengatasi kerusakan rambut.",
"Tidak sulit untuk membentuk dan mengatur rambut sesuai keinginan dengan menggunakan produk hair styling ini.",
"Panduan pemakaian yang jelas dan mudah dipahami tersedia dari brand hair styling ini.",
"Rambut tidak akan menjadi terlalu kering atau rusak setelah menggunakan produk hair styling ini.",
"Brand hair styling menyediakan berbagai pilihan produk untuk menciptakan berbagai gaya rambut yang diinginkan.",
"Tidak perlu khawatir tentang noda atau bekas di pakaian atau bantal setelah menggunakan produk hair styling ini.",
"Brand hair styling menggunakan teknologi terkini dan bahan alami untuk menciptakan produk yang efektif dan aman bagi rambut.",
"Produk hair styling dapat membantu melindungi rambut dari paparan sinar UV dan polusi yang berbahaya.",
"Brand hair styling memberikan tutorial atau video untuk membantu mengaplikasikan produk secara benar dan efektif."

"Rambut tidak terasa berat atau sulit diatur dengan produk hair styling yang digunakan.",
"Kemasan yang ramah lingkungan dan mudah didaur ulang digunakan oleh brand hair styling.",
"Rambut tidak menjadi kusut atau sulit diatur ulang dengan produk hair styling yang digunakan.",
"Brand hair styling cocok untuk digunakan oleh wanita dan pria dengan menghadirkan produk-produk yang sesuai.",
"Efek yang tahan lama dari produk hair styling yang digunakan mengurangi frekuensi pengaplikasian.",
"Sumber bahan berkualitas tinggi digunakan oleh brand hair styling.",
"Rambut tidak menjadi rapuh atau mudah patah dengan produk hair styling yang digunakan.",
"Garansi kepuasan pelanggan diberikan oleh brand hair styling sehingga konsumen merasa lebih percaya diri untuk mencoba produk baru.",
"Bahan berbahaya seperti paraben atau SLS tidak terdapat pada produk hair styling yang digunakan.",
"Brand hair styling selalu berusaha untuk memberikan produk yang inovatif dan sesuai dengan kebutuhan pasar.",
"Brand tersebut tahan lama dan tidak mudah rusak.",
"Brand tersebut tahan lama dan tidak mudah rusak.",
"Brand tersebut tahan lama dan tidak mudah rusak.",
]

#20
saran = [
    "Terus melakukan riset dan pengembangan produk agar selalu menghadirkan produk yang inovatif dan sesuai dengan kebutuhan konsumen.",
    "Lebih fokus pada penggunaan bahan-bahan alami dan ramah lingkungan untuk mendukung sustainability.",
    "Menawarkan produk hair styling untuk berbagai jenis rambut, seperti rambut keriting, halus, atau tebal.",
    "Memperluas jangkauan produk agar tersedia di toko-toko online maupun offline yang lebih luas.",
    "Mengadakan promo atau diskon secara berkala untuk menarik konsumen baru dan mempertahankan pelanggan lama.",
    "Memperhatikan kemasan produk agar lebih praktis dan mudah digunakan.",
    "Menyediakan panduan pemakaian yang lebih detail untuk membantu konsumen memaksimalkan penggunaan produk.",
    "Mengembangkan produk hair styling yang lebih natural, tanpa kandungan bahan kimia berbahaya seperti sulfat atau paraben.",
    "Meningkatkan kualitas dan ketahanan produk agar lebih awet dan tahan lama pada rambut.",
    "Menambahkan produk perawatan rambut, seperti shampoo dan conditioner, untuk memperkuat brand dan menawarkan paket perawatan yang lengkap.",
    "Mengadakan acara pelatihan atau workshop gratis tentang cara mengaplikasikan produk yang tepat dan tren gaya rambut terbaru.",
    "Menjalin kerja sama dengan influencer atau hairstylist terkenal untuk mengenalkan produk brand ke konsumen yang lebih luas.",
    "Memperkenalkan produk hair styling yang lebih mudah diaplikasikan, seperti spray atau cream.",
    "Menyediakan kemasan travel size yang lebih kecil agar mudah dibawa-bawa dalam perjalanan atau saat bepergian.",
    "Menyediakan kemasan refill agar lebih ramah lingkungan dan bisa mengurangi jumlah sampah.",
    "Menjaga kualitas produk dan menjamin keaslian produk untuk mempertahankan kepercayaan konsumen.",
    "Memperluas jangkauan target pasar, seperti untuk anak-anak atau orang dengan rambut tertentu, misalnya rambut berminyak atau rontok.",
    "Menyediakan opsi custom hair styling untuk konsumen yang ingin menciptakan gaya rambut yang unik dan personal.",
    "Memberikan informasi tentang sumber bahan-bahan yang digunakan dan cara pembuatan produk yang transparan dan mudah dipahami oleh konsumen.",
    "Terus berkomunikasi dengan konsumen dan memperhatikan umpan balik agar bisa meningkatkan kualitas produk dan layanan.",

]

namaBarber = [
"Batavia Barber Lotte Shopping Avenue",
"Jakarta Barber Shop (JBS) Tebet",
"Djoeragan Barbershop",
"Barberbros Kemang",
"Clean Cuts Barbershop",
"Ramo Barbershop Setiabudi",
"Vessel Barber Cilandak",
"Barberbox",
"Pax Wijaya",
"Paxi Barbeshop",

"Manhattan Coffe & Cuts",
"Chief Barbeshop",
"Hairnerds Studio",
"Di Bawah Pohon Barbershop",
"Frank’s Barber",
"Ko Tang Barbershop",
"Alexander Barbershop",
"Djoeragan Barbershop",
"Barberbox",
"Pax Wijaya",

"Manhattan Coffe & Cuts",
"Ramo Barbershop Setiabudi",
"Chief Barbeshop",
"Alexander Barbershop",
"Barberbros Kemang",
"Paxi Barbeshop",
"Batavia Barber Lotte Shopping Avenue",
"Clean Cuts Barbershop",
"Vessel Barber Cilandak",
"Ko Tang Barbershop",

"Jakarta Barber Shop (JBS) Tebet",
"Hairnerds Studio",
"Di Bawah Pohon Barbershop",
"Frank’s Barber",
"Barberbox",
"Pax Wijaya",
"Manhattan Coffe & Cuts",
"Chief Barbeshop",
"Alexander Barbershop",
"Ramo Barbershop Setiabudi",
]

#20
alasanPuas = [
    "Kualitas potongan rambut tidak baik",
    "Barber tidak berpengalaman dan profesional",
    "Interior barbershop tidak menarik dan nyaman",
    "Atmosfer yang tidak santai dan ramah",
    "Pelayanan yang tidak cepat dan efisien",
    "Harga tidak terjangkau",
    "Tidak tersedia berbagai macam layanan perawatan rambut",
    "Produk perawatan rambut yang kurang berkualitas",
    "Tidak tersedia layanan booking online yang mudah dan cepat",
    "Lokasi tidak strategis dan mudah dijangkau",
    "Tidak tersedia fasilitas parkir yang memadai",
    "Ketersediaan alat dan produk yang kurang lengkap",
    "Barber yang tidak memberikan saran terbaik terkait perawatan rambut",
    "Tidak membuat pelanggan merasa dihargai dan diperhatikan",
    "Tidak membuat pelanggan merasa puas dan percaya diri setelah potongan rambut",
    "Tidak tersedia minuman dan cemilan gratis",
    "Kebersihan dan sanitasi yang tidak terjaga",
    "Tidak tersedia fasilitas entertainment seperti TV atau musik yang menyenangkan",
    "Tidak tersedia paket perawatan rambut untuk acara khusus seperti pernikahan atau ulang tahun",
    "Tidak memiliki program loyalitas atau diskon untuk pelanggan tetap.",
    "Tidak memiliki program loyalitas atau diskon untuk pelanggan tetap.",
    "Tidak memiliki program loyalitas atau diskon untuk pelanggan tetap.",
]

negatif = 0
indpuas = 0

ya = 3
tidak = 3

indsaran = 5
Saranidx = 16
Puasidx = 2
index = 39
iy = 3
it = 7
try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(email[index])
        
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(5)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        textboxes[1].send_keys(nama[index])
        
        usia = random.choice([2,3,3,3])
        radiobuttons[usia].click()

        domisili = random.choice([7,8])
        radiobuttons[domisili].click()

        textboxes[2].send_keys("-")
        pekerjaan = random.choice([20,21,22])
        radiobuttons[pekerjaan].click()

        if usia == 2:
            gaji = random.choice([24,25,26,27])
            radiobuttons[gaji].click()
        else :
            gaji = random.choice([24,25,26,27,28,28,29,29,30,31])
            radiobuttons[gaji].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes1 = driver.find_elements("css selector", ".Hvn9fb")#isian
        textboxes = driver.find_elements("css selector", ".KHxj8b")#isian

        radiobuttons[2].click()

        if negatif != 0:
            s1 = random.choice([0,1])
            radiobuttons[s1].click()
            time.sleep(2)

            if s1 == 1:
                negatif -= 1
                radiobuttons[6].click()
                textboxes1[0].send_keys("-")
                driver.implicitly_wait(4)

                radiobuttons[8].click()
                radiobuttons[10].click()
                radiobuttons[12].click()
                driver.implicitly_wait(4)

                textboxes[0].send_keys(pendapat[index])
                time.sleep(2)

                if ya != 0 and tidak != 0:
                    rel = random.choice([13,14])
                    if rel == 13:
                        radiobuttons[rel].click()
                        textboxes[1].send_keys(alsy[iy])
                        textboxes[2].send_keys("-")
                        ya -= 1
                        iy += 1
                    else :
                        radiobuttons[rel].click()
                        textboxes[1].send_keys("-")
                        textboxes[2].send_keys(alst[it])
                        tidak -= 1
                        it += 1
                elif ya == 0:
                    radiobuttons[14].click()
                    textboxes[1].send_keys("-")
                    textboxes[2].send_keys(alst[it])
                    it += 1
                    tidak -= 1
                else :
                    radiobuttons[13].click()
                    textboxes[1].send_keys(alsy[iy])
                    textboxes[2].send_keys("-")
                    iy += 1
                    tidak -= 1
            else:
                tau = random.choice([2,3,4,5])
                radiobuttons[tau].click()
                prod = random.choice([7,7,8])
                radiobuttons[prod].click()
                pot = random.choice([9,9,10])
                radiobuttons[pot].click()
                radiobuttons[11].click()
                driver.implicitly_wait(4)

                textboxes[0].send_keys(pendapat[index])
                time.sleep(2)

                if ya != 0 and tidak != 0:
                    rel = random.choice([13,14])
                    time.sleep(2)

                    if rel == 13:
                        radiobuttons[rel].click()
                        textboxes[1].send_keys(alsy[iy])
                        textboxes[2].send_keys("-")
                        ya -= 1
                        iy += 1
                    else :
                        radiobuttons[rel].click()
                        textboxes[1].send_keys("-")
                        textboxes[2].send_keys(alsy[it])
                        it += 1
                        tidak -= 1
                elif ya == 0:
                    radiobuttons[14].click()
                    textboxes[1].send_keys("-")
                    textboxes[2].send_keys(alst[it])
                    it += 1
                    tidak -= 1
                else :
                    radiobuttons[13].click()
                    textboxes[1].send_keys(alsy[iy])
                    textboxes[2].send_keys("-")
                    iy += 1
                    ya -= 1
        else:
            time.sleep(2)
            radiobuttons[0].click()
            time.sleep(3)
            tau = random.choice([2,3,4,5])
            radiobuttons[tau].click()
            prod = random.choice([7,7,8])
            radiobuttons[prod].click()
            pot = random.choice([9,9,10])
            radiobuttons[pot].click()
            radiobuttons[11].click()
            driver.implicitly_wait(4)

            textboxes[0].send_keys(pendapat[index])
            time.sleep(2)

            if ya != 0 and tidak != 0:
                rel = random.choice([13,14])
                time.sleep(2)

                if rel == 13:
                    radiobuttons[rel].click()
                    textboxes[1].send_keys(alsy[iy])
                    textboxes[2].send_keys("-")
                    ya -= 1
                    iy += 1
                else :
                    radiobuttons[rel].click()
                    textboxes[1].send_keys("-")
                    textboxes[2].send_keys(alsy[it])
                    it += 1
                    tidak -= 1
            elif ya == 0:
                radiobuttons[14].click()
                textboxes[1].send_keys("-")
                textboxes[2].send_keys(alst[it])
                it += 1
                tidak -= 1
            else :
                radiobuttons[13].click()
                textboxes[1].send_keys(alsy[iy])
                textboxes[2].send_keys("-")
                iy += 1
                ya -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes1 = driver.find_elements("css selector", ".Hvn9fb")#isian
        textboxes = driver.find_elements("css selector", ".KHxj8b")#isian

        pernah = random.choice([0,0,0,0,0,1])
        radiobuttons[pernah].click()
        radiobuttons[2].click()
        time.sleep(3)

        if pernah == 0:
            time.sleep(3)
            produk = random.choice([2,3,4])
            radiobuttons[produk].click()
            time.sleep(1)
            sering = random.choice([6,7,8,9,10])
            radiobuttons[sering].click()
            time.sleep(1)
            suka = random.choice([11,12,13,14,15,16])
            radiobuttons[suka].click()
            time.sleep(1)
            gunakan = random.choice([18,19,20,21,22,23,24,25])
            radiobuttons[gunakan].click()
            driver.implicitly_wait(4)
            textboxes[0].send_keys(alasanBrand[index])        
            driver.implicitly_wait(4)

            radiobuttons[27].click()
            radiobuttons[29].click()
        else:
            time.sleep(3)
            radiobuttons[5].click()
            time.sleep(2)
            driver.implicitly_wait(4)
            textboxes1[0].send_keys("-")
            driver.implicitly_wait(4)
            radiobuttons[10].click()
            radiobuttons[17].click()
            driver.implicitly_wait(4)
            textboxes1[1].send_keys("-")
            driver.implicitly_wait(4)
            radiobuttons[26].click()
            driver.implicitly_wait(4)
            textboxes1[2].send_keys("-")
            driver.implicitly_wait(4)
            textboxes[0].send_keys("-")
            driver.implicitly_wait(4)
            radiobuttons[28].click()
            radiobuttons[30].click()

        if indsaran != 0 :
            s1 = random.choice([31,32])
            if s1 == 31:
                radiobuttons[31].click()
                textboxes[1].send_keys(saran[Saranidx])
                driver.implicitly_wait(4)
                Saranidx += 1
                indsaran -= 1
            else:
                radiobuttons[32].click()
                textboxes[1].send_keys("-")
                driver.implicitly_wait(4)
        else :
            radiobuttons[32].click()
            textboxes[1].send_keys("-")
            driver.implicitly_wait(4)

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        time.sleep(3)

        gambar = random.choice([0,1,2,3,4])
        radiobuttons[gambar].click()
        time.sleep(5)
        harga1 = random.choice([5,5,6,6,7,7,8,8,9,10])
        radiobuttons[harga1].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
        time.sleep(1)

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".Od2TWd")#kesamping

        toko = random.choice([0,1,2])
        radiobuttons[toko].click()

        if toko == 0:
            toko1 = random.choice([3,4,5])
            radiobuttons[toko1].click()
            radiobuttons[10].click()
        elif toko == 1:
            radiobuttons[6].click()
            toko2 = random.choice([7,8,9])
            radiobuttons[toko2].click()
        else :
            toko1 = random.choice([3,4,5])
            radiobuttons[toko1].click()
            toko2 = random.choice([7,8,9])
            radiobuttons[toko2].click()

        toko3 = random.choice([11,12,13,14,15])
        radiobuttons[toko3].click()

        soal = 8
        p1 = 16
        p2 = 17
        p3 = 18
        p4 = 19
        p5 = 20
        p6 = 21
        p7 = 22
        p8 = 23
        while soal:
            jawab1 = random.choice([p1,p1,p1,p2,p2,p2,p2,p3,p3,p4,p5,p6,p7,p8])
            testcheck[jawab1].click()
            p1 += 8
            p2 += 8
            p3 += 8
            p4 += 8
            p5 += 8
            p6 += 8
            p7 += 8
            p8 += 8
            soal -= 1

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".KHxj8b")#isian
        textboxes1 = driver.find_elements("css selector", ".whsOnd")#isian
        testcheck = driver.find_elements("css selector", ".Od2TWd")#kesamping

        brp = random.choice([0,1,2,3])
        radiobuttons[brp].click()
        hrg = random.choice([4,5,6,7,8,9,10])
        radiobuttons[hrg].click()

        textboxes1[1].send_keys(namaBarber[index])

        if indpuas != 0:
            pss = random.choice([11,12])
            radiobuttons[pss].click()
            if pss == 11 :
                driver.implicitly_wait(4)
                textboxes[0].send_keys("-")
                indpuas -= 1
            else :
                textboxes[0].send_keys([alasanPuas[Puasidx]])
                Puasidx += 1
        else :
            radiobuttons[12].click()
            textboxes[0].send_keys([alasanPuas[Puasidx]])
            Puasidx += 1

        radiobuttons[11].click()
        driver.implicitly_wait(4)
        textboxes[0].send_keys("-")

        soal = 8
        p1 = 13
        p2 = 14
        p3 = 15
        p4 = 16
        p5 = 17
        p6 = 18
        p7 = 19
        p8 = 20
        while soal:
            jawab = random.choice([p1,p1,p1,p2,p2,p2,p2,p3,p3,p4,p5,p6,p7,p8])
            testcheck[jawab].click()
            p1 += 8
            p2 += 8
            p3 += 8
            p4 += 8
            p5 += 8
            p6 += 8
            p7 += 8
            p8 += 8
            soal -= 1

        jasa = random.choice([13,14,15,16])
        radiobuttons[jasa].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        radiobuttons[1].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        time.sleep(100)
        driver.implicitly_wait(4)
        driver.get("https://forms.gle/fBtVHnPMWtgfmsjm8")

        index+=1
        print("negatif :" + str(negatif))
        print("Saranidx :" + str(Saranidx))
        print("Puasidx :" + str(Puasidx))
        print("indpuas :" + str(indpuas))
        print("indsaran :" + str(indsaran))
        print("index :" + str(index))
        print("iy :" + str(iy))
        print("ya :" + str(ya))
        print("it :" + str(it))
        print("tidak :" + str(tidak))

        times-=1
        print(times)
finally:
	# driver.quit()
    print("berhasil")


        # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox