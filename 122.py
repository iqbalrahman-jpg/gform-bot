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
driver.get("https://forms.gle/FzHCbSreL15gv1XD6")

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
    
    "Maya Dara Putri",
    "Rio Fajar Pratama",
    "Dewi Sari Wijaya",
    "Agung Kusuma Jaya",
    "Ratih Suci Lestari",
    "Rizki Pratama Nugraha",
    "Dwi Prasetya Utama",
    "Arif Rahman Hakim",
    "Intan Ayu Lestari",
    "Ananda Dwi Wicaksono",
    "Fira Nur Hidayah",
    "Rama Aditya Wardhana",
    "Cinta Ayu Dewanti",
    "Ade Kurniawan Saputra",
    "Mira Fitriana Wati",
    "Dian Kusuma Wardani",
    "Budi Santoso Putra",
    "Rina Nuraini Sari",
    "Ahmad Fauzi Akbar",
    "Rizky Ananda Pratama",
    "Maya Dewi Sari",
    "Dwi Kusuma Jaya",
    "Agung Santosa Nugroho",
    "Dila Yuliani Wati",
    "Andi Muhammad Rizal",
    "Budi Santoso",
    "Rina Permata Sari",
    "Dian Nugroho",
    "Rudi Setiawan",
    "Maya Putri Lestari",
    "Andi Prasetyo",
    "Sinta Utami Sari",
    "Rizky Ramadhan",
    "Eka Puspita Dewi",
    "Dika Setiawan Pratama",
    "Rani Fitriani",
    "Dito Prasetya",
    "Nisa Indah Sari",
    "Rizal Pratama",
    "Tiara Dewi Puspita",
    "Yanto Wibowo",
    "Nina Anggraini",
    "Yoga Putra Wijaya",
    "Dini Cahyani",
    "Raka Triyana",
    "Maya Dewi Utami",
    "Indra Kusuma",
    "Devi Puspitasari",
    "Bima Aditya Nugraha",
    "Rina Anggraini Sari",
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

    "Bali",
    "semarang",
    "Bandung",
    "surabaya",
    "surabaya",
    "Bandung",
    "Bandung",
    "jakarta",
    "Bekasi",
    "jawa timur",
    "gresik",
    "Bandung",
    "surabaya",
    "jawa timur",
    "jakarta",
    "gresik",
    "Bekasi",
    "jawa timur",
    "DKI Jakarta",
    "DKI Jakarta",
    "Bandung",
    "jakarta",
    "Bali",
    "Yogyakarta",
    "Bandung",
    "jawa timur",
    "surabaya",
    "DKI Jakarta",
    "Bandung",
    "jakarta",
    "surabaya",
    "Bekasi",
    "gresik",
    "Bali",
    "surabaya",
    "banyuwangi",
    "denpasar",
    "jawa timur",
    "banyuwangi",
    "Surabaya",
    "gresik",
    "medan",
    "jakarta",
    "Bekasi",
    "Surabaya",
    "Bandung",
    "surabaya",
    "surabaya",
    "Yogyakarta",
    "semarang",
]

# 50
wisata = [
    "Jarak yang terlalu jauh dari tempat tinggal",
    "Keterbatasan waktu untuk melakukan perjalanan jauh",
    "Kurangnya minat terhadap destinasi desa wisata",
    "Kurangnya informasi yang tersedia tentang desa wisata tersebut",
    "Biaya perjalanan yang tidak terjangkau",
    "Kurangnya fasilitas yang memadai di desa wisata",
    "Cuaca yang tidak mendukung untuk perjalanan ke desa wisata",
    "Ketidakmungkinan meninggalkan pekerjaan atau kewajiban lain",
    "Kondisi kesehatan yang tidak memungkinkan untuk melakukan perjalanan",
    "Keamanan dan keadaan politik yang tidak stabil di daerah tersebut",
    "Ketidaktersediaan transportasi umum yang memadai",
    "Kurangnya dukungan atau persetujuan dari keluarga atau teman",
    "Ketidakmungkinan untuk mendapatkan cuti dari pekerjaan",
    "Tidak ada minat dalam aktivitas atau atraksi yang ditawarkan di desa wisata",
    "Ketidakmampuan untuk beradaptasi dengan lingkungan yang berbeda",
    "Kurangnya aksesibilitas bagi orang dengan kebutuhan khusus",
    "Kurangnya fasilitas akomodasi yang memadai di desa wisata",
    "Keadaan lalu lintas yang buruk di sekitar desa wisata",
    "Kurangnya fasilitas kesehatan atau keamanan yang dapat diandalkan di desa wisata",
    "Terbatasnya pilihan makanan atau masalah diet khusus yang sulit dipenuhi di desa wisata",
    "Kurangnya variasi kegiatan atau atraksi yang menarik di desa wisata",
    "Kurangnya dukungan atau fasilitas bagi anak-anak atau keluarga yang bepergian bersama",
    "Keterbatasan aksesibilitas untuk orang dengan kendaraan pribadi",
    "Ketidakmampuan atau ketidakinginan untuk mengikuti aturan atau kebiasaan lokal di desa wisata",
    "Tidak tertarik dengan apa yang ditawarkan oleh desa wisata tersebut",

    "Kebutuhan biaya perjalanan yang cukup banyak",
    "Keterbatasan pilihan makanan diet / khusus yang sulit dipenuhi",
    "Kurangnya fasilitas akomodasi yang memadai",
    "Terkadang kurangnya informasi yang tersedia tentang desa wisata tersebut",
    "Tidak tertarik dengan apa yang ditawarkan oleh desa wisata disana",
    "Tidak ada minat dalam aktivitas yang ditawarkan di desa wisata",
    "Kurangnya informasi yang tersedia tentang desa wisata tersebut",
    "Kurang tertarik dengan destinasi desa wisata",
    "Kurangnya variasi kegiatan atau atraksi yang menarik di desa",
    "Ketidaktersediaan transportasi umum yang memadai di lokasi wisatanya",
    "Ksulitan untuk meninggalkan pekerjaan atau kewajiban lain",
    "Perlu biaya perjalanan yang banyak",
    "Kurangnya fasilitas di desa wisata",
    "Cuaca yang kurang mendukung saat perjalanan ke desa wisata",
    "Ketersediaan transportasi umum yang kurang memadai",
    "Kurangnya dukungan atau fasilitas bagi anak-anak",
    "Jarak tempuh terlalu jauh dari tempat tinggal",
    "Kondisi kesehatan tidak memungkinkan untuk melakukan perjalanan",
    "Ketidakpastian terkait kamanan dan keadaan politik di daerah tersebut",
    "tidak dapat beradaptasi dengan lingkungan yang berbeda",
    "Sulit untuk meninggalkan pekerjaan",
    "Kurang tertarik terhadap destinasi desa wisata",
    "Kurangnya aksesibilitas bagi orang berkebutuhan khusus",
    "Kurangnya fasilitas kesehatan atau keamanan yang dapat diandalkan",
    "Terbatasnya waktu untuk melakukan perjalanan jauh",
]

# 100
destinasi = [
    "Tenganan (Desa Bali Aga)",
    "Penglipuran",
    "Ubud",
    "Sidemen",
    "Jatiluwih",
    "Munduk",
    "Pemuteran",
    "Amed",
    "Tirta Gangga",
    "Trunyan",
    "Kintamani",
    "Kuta",
    "Sanur",
    "Seminyak",
    "Canggu",
    "Jimbaran",
    "Lovina",
    "Padangbai",
    "Sukawati",
    "Gianyar",
    "Mengwi",
    "Batuan",
    "Klungkung",
    "Bedugul",
    "Negara",
    "Bangli",
    "Abiansemal",
    "Petulu",
    "Tampaksiring",
    "Blahbatuh",
    "Pejeng",
    "Belimbing",
    "Karangasem",
    "Seririt",
    "Pupuan",
    "Buleleng",
    "Sukawana",
    "Sangeh",
    "Payangan",
    "Nusa Penida",
    "Tegalalang",
    "Sebatu",
    "Keliki",
    "Pejeng Kangin",
    "Medahan",
    "Taro",
    "Taro Village",
    "Selat",
    "Temukus",
    "Sudaji",

    "Medahan",
    "Pejeng",
    "Canggu",
    "Belimbing",
    "Kuta",
    "Taro Village",
    "Tampaksiring",
    "Klungkung",
    "Seminyak",
    "Kuta",
    "Keliki",
    "Padangbai",
    "Abiansemal",
    "Munduk",
    "Ubud",
    "Abiansemal",
    "Blahbatuh",
    "Seririt",
    "Pejeng Kangin",
    "Seminyak",
    "Nusa Penida",
    "Sidemen",
    "Tegalalang",
    "Amed",
    "Mengwi",
    "Sukawana",
    "Bedugul",
    "Medahan",
    "Sukawati",
    "Bangli",
    "Trunyan",
    "Payangan",
    "Karangasem",
    "Taro",
    "Sanur",
    "Amed",
    "Penglipuran",
    "Sudaji",
    "Batuan",
    "Sidemen",
    "Gianyar",
    "Selat",
    "Sukawati",
    "Klungkung",
    "Petulu",
    "Gianyar",
    "Canggu",
    "Jimbaran",
    "Pupuan",
    "Keliki",

]

# 50
kritik = [
    "Tingkatkan promosi dan pemasaran desa wisata secara aktif melalui media sosial, situs web, brosur, dan kampanye digital lainnya",
    "Tawarkan paket wisata yang menarik dengan harga yang terjangkau untuk menarik minat pengunjung",
    "Kembangkan dan tingkatkan fasilitas akomodasi di desa wisata, termasuk hotel, homestay, dan penginapan yang nyaman dan bersih",
    "Berikan pelatihan kepada penduduk setempat tentang pelayanan pelanggan yang baik dan kemampuan bahasa asing untuk meningkatkan pengalaman wisatawan",
    "Tawarkan kegiatan wisata yang beragam, seperti jelajah alam, trekking, olahraga air, tur sejarah, kuliner lokal, dan seni dan kerajinan tangan",
    "Bentuk kerjasama dengan pihak lokal, termasuk masyarakat setempat, pengusaha lokal, dan organisasi non-profit, untuk memperkuat daya tarik desa wisata",
    "Bangun dan pertahankan kebersihan serta keindahan lingkungan di desa wisata",
    "Sediakan sarana dan prasarana yang memadai, seperti toilet umum, tempat parkir, dan aksesibilitas yang baik untuk memudahkan pengunjung",
    "Adakan acara budaya, festival, atau pertunjukan seni secara rutin untuk memberikan pengalaman kultural yang unik bagi pengunjung",
    "Kembangkan program edukasi dan workshop untuk memperkenalkan kehidupan desa dan kebudayaan lokal kepada pengunjung",
    "Dukung usaha kecil dan lokal dengan menjual produk-produk kerajinan tangan dan makanan khas desa",
    "Berikan pelatihan kepada masyarakat setempat tentang pengelolaan wisata yang berkelanjutan, termasuk pengelolaan limbah dan pengurangan dampak negatif terhadap lingkungan",
    "Tingkatkan aksesibilitas transportasi menuju desa wisata, baik melalui jalur darat, udara, atau air",
    "Buat panduan wisata yang lengkap dan informatif, termasuk peta, informasi sejarah, dan tempat-tempat menarik yang harus dikunjungi",
    "Dukung kegiatan pertanian organik dan produk lokal untuk meningkatkan kesadaran akan keberlanjutan dan kualitas produk",
    "Tawarkan pengalaman interaktif kepada pengunjung, seperti mengikuti kegiatan pertanian, memasak makanan tradisional, atau belajar seni lokal",
    "Tingkatkan keamanan dan keamanan di desa wisata dengan mengadakan patroli keamanan dan menyediakan fasilitas yang memadai",
    "Berikan pilihan wisata ramah lingkungan, seperti trekking, penjelajahan alam, atau wisata bersepeda",
    "Kembangkan program homestay di mana pengunjung dapat tinggal bersama keluarga lokal untuk mendapatkan pengalaman budaya yang otentik",
    "Bentuk kerjasama dengan lembaga pendidikan atau universitas untuk melakukan penelitian dan pengembangan di desa wisata",
    "Dukung komunitas lokal untuk mengembangkan produk-produk wisata unik, seperti kerajinan tangan, tekstil tradisional, atau makanan khas",
    "Berikan pelatihan kepada pemandu wisata lokal agar dapat memberikan informasi yang akurat dan menarik tentang desa wisata",
    "Tingkatkan kebersihan dan pemeliharaan infrastruktur, seperti jalan, jembatan, dan taman di desa wisata",
    "Gunakan teknologi dan inovasi dalam pengembangan desa wisata, seperti aplikasi mobile untuk panduan wisata atau penggunaan energi terbarukan",
    "Dukung partisipasi masyarakat dalam pengambilan keputusan dan pengelolaan desa wisata, sehingga masyarakat lokal merasa memiliki dan bertanggung jawab terhadap keberhasilan desa wisata tersebut",

    "Berikan pelatihan khusus kepada pemandu wisata lokal agar dapat memberikan informasi menarik tentang desa wisata",
    "Adakan program homestay, dimana pengunjung dapat tinggal bersama keluarga lokal untuk mendapatkan pengalaman budaya yang otentik",
    "Berikan pelatihan kepada masyarakat setempat tentang pengelolaan wisata yang berkelanjutan",
    "Tawarkan paket wisata yang menarik dengan harga yang terjangkau",
    "Tawarkan kegiatan wisata yang beragam",
    "Dukung usaha kecil dan lokal dengan menjual produk-produk khas desa",
    "Bangun dan pertahankan kebersihan serta keindahan lingkungan di daerah desa wisata",
    "Adakan acara budaya, festival, atau pertunjukan seni yang unik bagi pengunjung",
    "Tawarkan paket wisata dengan harga yang terjangkau untuk menarik minat pengunjung",
    "Sediakan sarana dan prasarana yang memadai",
    "Dukung partisipasi masyarakat dalam pengelolaan desa wisata, agar meningkatkan keberhasilan desa wisata tersebut",
    "Gunakan teknologi dan inovasi dalam pengembangan desa wisata",
    "Tingkatkan aksesibilitas transportasi menuju desa wisata",
    "Buat panduan wisata yang lengkap dan informatif, seperti peta, informasi sejarah, dan tempat-tempat menarik yang dapat dikunjungi",
    "Sediakan sarana dan prasarana yang memadai dan baik untuk memudahkan pengunjung",
    "Tingkatkan keamanan dan keamanan di desa wisata dengan mengadakan patroli keamanan",
    "Berikan pilihan wisata ramah lingkungan",
    "Berikan pelatihan kepada penduduk setempat tentang kemampuan bahasa asing untuk meningkatkan pengalaman wisatawan",
    "Kembangkan dan tingkatkan fasilitas akomodasi di desa wisata",
    "Kembangkan program homestay di mana pengunjung dapat tinggal bersama keluarga lokal untuk mendapatkan pengalaman budaya yang otentik",
    "Bangun dan pertahankan kebersihan serta keindahan lingkungan",
    "Dukung produk lokal untuk meningkatkan kesadaran akan keberlanjutan dan kualitas produk",
    "Berikan pilihan wisata ramah lingkungan, seperti trekking atau wisata bersepeda",
    "Tingkatkan aksesibilitas transportasi menuju desa wisata, baik melalui jalur darat, udara, atau air",
    "Adakan acara budaya, festival, atau pertunjukan seni secara rutin untuk memberikan pengalaman kultural yang unik bagi pengunjung",
]

# 50
identitas = [
    "Desa adat dengan warisan budaya yang kaya",
    "Keunikan sebagai desa Bali Aga",
    "Pendet Dance sebagai tarian tradisional khas",
    "Geringsing Double Ikat, kain tradisional dengan teknik ikat ganda",
    "Arsitektur tradisional dengan rumah-rumah adat",
    "Seni tenun ikat yang rumit dan indah",
    "Keahlian masyarakat dalam kerajinan anyaman bambu",
    "Warisan sejarah dengan adanya Benteng Tenganan",
    "Kehidupan agraris dengan kegiatan pertanian, terutama penanaman padi",
    "Keindahan alam dengan pegunungan, sawah, dan sungai",
    "Tradisi upacara adat yang masih dijaga dan dilakukan secara rutin",
    "Kekayaan seni dan budaya dalam seni lukis dan ukir",
    "Kerajinan perak tradisional yang diproduksi oleh masyarakat desa",
    "Keberagaman kuliner dengan hidangan khas Tenganan",
    "Keberadaan desa wisata yang ramah pengunjung",
    "Tempat-tempat suci seperti pura dan tempat ibadah lainnya",
    "Kebersihan dan keindahan lingkungan yang dijaga dengan baik",
    "Kebersamaan dan gotong royong dalam kehidupan masyarakat",
    "Konservasi dan pengelolaan alam yang berkelanjutan",
    "Keberlanjutan tradisi dan budaya melalui program pendidikan adat",
    "Keunikan dalam upacara Ngusaba sebagai ungkapan rasa syukur kepada Sang Hyang Widhi",
    "Perkampungan dengan suasana yang tenang dan damai",
    "Keahlian dalam pembuatan topeng-topeng tradisional",
    "Kerajinan anyaman khas, seperti tikar dan tas anyaman",
    "Kepedulian terhadap pelestarian lingkungan dan satwa liar",

    "Keberadaan Desa Wisata Ramah Pengunjung",
    "Pelestarian tradisi dan budaya melalui program pendidikan adat",
    "Keindahan alam dengan pegunungan, persawahan dan sungai",
    "Tradisi upacara adat yang masih dilestarikan dan dilakukan secara rutin",
    "Tradisi upacara adat yang masih dilestarikan dan dilakukan secara rutin",
    "Kemasyarakatan dan Gotong Royong dalam Kehidupan Masyarakat",
    "Kehidupan pertanian dan kegiatan pertanian, khususnya penanaman padi",
    "Kompetensi dalam produksi topeng tradisional",
    "Kekayaan seni dan budaya dalam lukisan dan patung",
    "Kerajinan khas anyaman seperti karpet dan tas anyaman",
    "Kebersihan dan keindahan lingkungan sekitar dalam kondisi baik",
    "Kehidupan pertanian dan kegiatan pertanian, khususnya penanaman padi",
    "Kompetensi dalam produksi topeng tradisional",
    "Tempat-tempat suci seperti pura dan tempat ibadah lainnya",
    "Memastikan perlindungan lingkungan dan satwa liar",
    "Kerajinan khas anyaman seperti karpet dan tas anyaman",
    "Variasi Kuliner dengan Hidangan Khas Tenganan",
    "Peninggalan Sejarah dengan Benteng Tenganan",
    "Kekayaan seni dan budaya dalam lukisan dan patung",
    "Keunikan Upacara Ngusaba Sebagai Ungkapan Syukur Kepada Sang Hyang Widhi",
    "Kerajinan perak tradisional penduduk desa",
    "Keunikan dari Desa Bali Aga",
    "Desa dengan suasana tenang dan damai",
    "Variasi Kuliner dengan Hidangan Khas Tenganan",
    "Tari pendet sebagai tarian tradisional yang khas",
]

idxwisata = 25
idxsaran = 25
idxidentitas = 25

desa = 25
tdesa = 25

saran = 25
tsaran = 25

iden = 25
tiden = 25

times = 50
index = 50

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        usia = random.choice([0,1,2])

        if usia == 0:
            pekerjaan = random.choice([3,4])
        else:
            pekerjaan = 4

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(nama[index])
        textboxes[1].send_keys(domisili[index])

        time.sleep(2)
        radiobuttons[usia].click()
        radiobuttons[pekerjaan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        time.sleep(2)
        if desa != 0 and tdesa != 0 :
            pil1 = random.choice([0,1])
        elif desa != 0 and tdesa == 0 :
            pil1 = 0
        elif desa == 0 and tdesa != 0 :
            pil1 = 1

        if pil1 == 0:
            alasan1 = ""
            desa -= 1
        else:
            alasan1 = wisata[idxwisata]
            idxwisata += 1
            tdesa -= 1

        time.sleep(2)
        tertarik = random.choice([2,3])

        if tertarik == 2 :
            tujuan = random.choice([4,4,5])
            temp = random.randint(2,7)
        else:
            tujuan = random.choice([4,5,5,5,5,5])
            temp = random.randint(1,4)

        time.sleep(2)
        temps = random.choice([1,5])

        check1 = random.sample([0,1,2,3,4,5,6], temp)
        check2 = random.sample([7,8,9,10,11], temps)

        time.sleep(2)
        if saran != 0 and tsaran != 0:
            pil2 = random.choice([0,1])
        elif saran != 0 and tsaran == 0:
            pil2 = 0
        elif saran == 0 and tsaran != 0:
            pil2 = 1

        if pil2 == 0:
            alasan2 = kritik[idxsaran]
            idxsaran += 1
            saran -= 1
        else:
            alasan2 = ""
            tsaran -= 1

        time.sleep(2)
        radiobuttons[pil1].click()
        radiobuttons[tertarik].click()
        radiobuttons[tujuan].click()

        time.sleep(2)
        textboxes[0].send_keys(alasan1)
        textboxes[1].send_keys(destinasi[index])

        time.sleep(2)
        for i in check1:
            checkboxes[i].click()

        for i in check2:
            checkboxes[i].click()

        time.sleep(2)
        textarea[0].send_keys(alasan2)

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        if iden != 0 and tiden != 0:
            pil3 = random.choice([0,1])
        elif iden != 0 and tiden == 0:
            pil3 = 0
        elif iden == 0 and tiden != 0:
            pil3 = 1

        if pil3 == 0:
            alasan3 = identitas[idxidentitas]
            idxidentitas += 1
            iden -= 1
        else :
            alasan3 = ""
            tiden -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        time.sleep(2)
        radiobuttons[random.choice([0,1])].click()
        radiobuttons[random.choice([2,3,4,5,6])].click()
        radiobuttons[random.choice([7,8,9])].click()
        radiobuttons[random.choice([10,11,12,13,14,15])].click()

        time.sleep(2)
        testcheck[random.choice([0,1,2,3])].click()
        testcheck[random.choice([4,5,6,7])].click()
        testcheck[random.choice([8,9,10,11])].click()

        time.sleep(2)
        textarea[0].send_keys(alasan3)

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/FzHCbSreL15gv1XD6")

        index+=1
        print("==================")
        print("idxwisata : " + str(idxwisata))
        print("idxsaran  : " + str(idxsaran))
        print("idxidentitas  : " + str(idxidentitas))
        print("")
        print("desa  : " + str(desa))
        print("tdesa : " + str(tdesa))
        print("")
        print("saran : " + str(saran))
        print("tsaran : " + str(tsaran))
        print("")
        print("iden : " + str(iden))
        print("tiden : " + str(tiden))
        print("")

        times-=1
        print("times  : " + str(times))
        print("index  : " + str(index))
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