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
driver.get("https://forms.gle/7cYtWqJcMcJxbVZh8")

email = [
	"mtianur001@gmail.com",
    "alihasn.01.10@gmail.com",
    "risfebri11@gmail.com",
    "budprasety@gmail.com",
    "aryonugh@gmail.com",
    "nanissa0110@gmail.com",
    "yahnugrah@gmail.com",
    "putriptr0110@gmail.com",
    "nandayundaa1@gmail.com",
    "yudipradan01@gmail.com",
    "yulayund1@gmail.com",
    "byumerta1@gmail.com",
    "Bellandayu01@gmail.com",
    "budsuryant01@gmail.com",
    "nela.mirra@gmail.com",
    "dwa.lingga10@gmail.com",
    "alffiantoro@gmail.com",
    "annicsaa@gmail.com",
    "fataahxdewa@gmail.com",
    "diahcindy03@gmail.com",
    "attakmajid@gmail.com",
    "azzarinrst@gmail.com",
    "fabiannadeo@gmail.com",
    "niaejuliana@gmail.com",
    "bayudwiganara@gmail.com",
    "syifaradifah@gmail.com",
    "aditferdinanda@gmail.com",
    "sitifauziyyahh@gmail.com",
    "reyhanutomowa@gmail.com",
    "salmaarowaya@gmail.com",
    "anggasiregarp@gmail.com",
    "putrikeancana@gmail.com",
    "rajawardanawan@gmail.com",
    "affifahh7@gmail.com",
    "shakapwijaya@gmail.com",
    "cynnarafisa@gmail.com",
    "monahfnna87@gmail.com",
    "mahendrejaa@gmail.com",
    "fryshta.eka823@gmail.com",
    "yanrasuryad@gmail.com",
    "rahannadi1@gmail.com",
    "sutisnayun@gmail.com",
    "ayulistyaan@gmail.com",
    "muhh.santosoo@gmail.com",
    "rudinurbaktii01@gmail.com",
    "ptrawiraw.an@gmail.com",
    "agungnugh@gmail.com",
    "dn.ramadhan@gmail.com",
    "dimas.purbo07@gmail.com",
    "nabilla.s.qolbi@gmail.com",
]

# efektif
alasanEfektif = [
    "E-tilang memungkinkan proses penindakan pelanggaran lalu lintas yang lebih cepat daripada metode manual tradisional.",
    "E-tilang mengurangi risiko manipulasi atau kecurangan dalam proses penilangan karena data tersimpan secara digital.",
    "Menggunakan teknologi digital meminimalkan kesalahan manusia dalam mencatat data pelanggaran.",
    "Penggunaan teknologi memungkinkan transparansi dan kendali yang lebih baik dalam proses penindakan.",
    "Data elektronik yang terekam dapat digunakan sebagai bukti yang lebih kuat dalam persidangan.",
    "Penindakan yang lebih cepat dan efisien dapat mengurangi pelanggaran lalu lintas dan dengan demikian meningkatkan keselamatan jalan.",
    "Mekanisme ini dapat membantu memastikan penegakan hukum yang lebih konsisten karena tidak tergantung pada interpretasi petugas.",
    "Sistem E-tilang sering dilengkapi dengan layanan pembayaran online yang memudahkan pelanggar untuk membayar denda mereka.",
    "Proses manual seringkali memerlukan lebih banyak sumber daya manusia dan biaya operasional daripada E-tilang.",
    "Masyarakat dapat melaporkan pelanggaran dengan lebih mudah melalui aplikasi atau situs web resmi.",
    "Penegak hukum dapat memantau pelanggaran secara real-time dan merespons dengan cepat.",
    "E-tilang menghindari potensi konflik verbal atau fisik antara petugas dan pelanggar.",
    "Kepatuhan terhadap aturan lalu lintas dapat meningkat karena pelanggar menyadari adanya kemungkinan tertangkap melalui teknologi.",
    "Proses digital memastikan hak pelanggar untuk mengajukan pembelaan atau pembelaan lebih mudah dijalankan.",
    "Dengan E-tilang, kebutuhan akan petugas lapangan yang banyak dapat berkurang.",
    "Sumber daya penegakan hukum dapat dialokasikan dengan lebih baik ke area yang membutuhkan penindakan lebih intensif.",
    "Semua catatan dan bukti terkait pelanggaran tersimpan dalam sistem, yang memudahkan pemantauan dan pelaporan."
]
    
alasanTEfektif = [
    "Masih ada masalah teknis seperti kesalahan pembacaan plat kendaraan atau gangguan sistem yang dapat mengganggu efektivitasnya.",
    "Di beberapa daerah, infrastruktur digital belum cukup kuat untuk mendukung E-tilang secara efisien.",
    "Beberapa aspek hukum terkait E-tilang mungkin masih ambigu, menghambat penerapan yang konsisten.",
    "Petugas penegak hukum memerlukan pelatihan tambahan untuk mengoperasikan sistem ini dengan efektif.",
    "Ada kekhawatiran tentang privasi data pemilik kendaraan yang terekam dalam sistem.",
    "Tidak semua daerah memiliki sumber daya finansial yang cukup untuk mengadopsi sistem E-tilang.",
    "Sebagian masyarakat mungkin tidak sepenuhnya sadar tentang E-tilang, sehingga penggunaannya masih terbatas.",
    "Beberapa individu atau komunitas mungkin tidak memiliki akses yang memadai ke teknologi yang diperlukan untuk sistem E-tilang.",
    "Terdapat risiko manipulasi data atau penyalahgunaan wewenang dalam penggunaan sistem ini.",
    "Meskipun E-tilang dapat meningkatkan kepatuhan, tidak semua pelanggar akan tunduk pada sistem ini.",
    "Proses hukum yang panjang atau kendala dalam penegakan hukum dapat mengurangi efektivitas E-tilang.",
    "Beberapa petugas mungkin menyalahgunakan kewenangan mereka dalam penggunaan E-tilang.",
    "Terdapat potensi kesalahan dalam mengidentifikasi pelanggar, terutama dalam situasi yang kompleks atau kontroversial."
]

# pembelaan
alasanPembelaan = [
    "Karena saya merasa tidak salah",
    "Karena saya merasa ada yang salah dengan sistemnya",
    "Itu bukan motor saya, sepertinya sistemnya salah baca plat nomor",
    "Saya memakai atribut lengkap namun tetap ditilang",
    "Saya sudah tidak melebihi garis polisi namun tetap kena tilang",
    "Biaya yang dikenakan terlalu mahal",
    "Meminta keringanan biaya"
]

alasanTPembelaan = [
    "Karena takut ribet",
    "Saya tidak tau kalau bisa pembelaan",
    "Saya baru tau kalau bisa melakukan pembelaan",
    "Karena malas ribet",
    "Karena saya tidak mau ribet",
    "Karena saya memang bersalah",
    "Karena itu memang kesalahan saya",
    "Karena saya sadar itu memang kesalahan saya",
    "Takut semakin banyak sanksinya",
    "Menurut saya pembelaan tidak mudah diraih dan percuma",
    "Karena saya merasa percuma karena saya memang salah",
    "Malas",
    "Takut ribet dan berujung panjang",
    "Bukti saya kurang lengkap untuk melakukan pembelaan",
    "Waktu saya tidak banyak untuk mengurus hal tersebut",
    "Sibuk",
    "Ribet",
    "Saya tidak tau kalau bisa pembelaan",
    "Saya tidak mengetahui kalau saya bisa mengajukan keringanan atau komplain",
    "Karena buang-buang waktu",
    "Karena memang salah dan percuma pembelaan",
    "Karena saya ga terlalu paham dengan hal seperti itu",
    "Karena ga yakin bisa pembelaan."
]

# pengajuan
alasanPengajuan = [
    "Terdapat potensi kesalahan dalam mengidentifikasi pelanggaran atau pemilik kendaraan.",
    "Teknologi E-tilang bisa mengalami kesalahan teknis yang perlu diperiksa.",
    "Orang memiliki hak untuk memberikan pembelaan atau klarifikasi terhadap dugaan pelanggaran.",
    "Terdapat situasi di mana ketentuan penegakan hukum tidak jelas dan perlu ditinjau.",
    "Sistem E-tilang tidak selalu kebal terhadap penyalahgunaan oleh petugas penegak hukum.",
    "Orang mungkin kehilangan bukti atau dokumen yang mendukung kasus mereka.",
    "Mungkin ada perluasan fakta atau klarifikasi yang perlu dibuat dalam kasus pelanggaran.",
    "Kadang-kadang, ada faktor konteks yang tidak diperhitungkan dalam proses E-tilang.",
    "Ada kemungkinan pelanggaran prosedur dalam penindakan yang perlu ditinjau.",
    "Terdapat kemungkinan salah identifikasi kendaraan yang tidak terlibat dalam pelanggaran.",
    "Data elektronik mungkin tidak selalu akurat dan perlu diklarifikasi.",
    "Orang mungkin merasa denda yang dijatuhkan tidak wajar dan ingin mengajukan bantahan.",
    "Meskipun jarang, kesalahan manusia dalam input data bisa terjadi.",
    "Proses banding mendukung prinsip hak asasi manusia dalam sistem peradilan.",
    "Banding adalah cara untuk memastikan bahwa setiap individu memiliki akses yang adil terhadap sistem peradilan.",
    "Dalam beberapa kasus, banding bisa membantu memastikan hukuman yang lebih sesuai dengan pelanggaran.",
    "Banding dapat meningkatkan transparansi dalam proses penegakan hukum.",
    "Informasi tentang pelanggaran bisa menjadi tidak akurat, dan banding adalah cara untuk memperbaikinya.",
    "Banding memungkinkan pemeriksaan lebih lanjut terhadap bukti dan data yang digunakan dalam E-tilang.",
    "Proses banding bisa meningkatkan kesadaran tentang aturan lalu lintas dan meningkatkan kepatuhan masyarakat."
]

alasanTPengajuan = [
"Percuma banding kalau ga menang",
"Hanya buang buang waktu saja",
"Tidak yakin menang banding",
"Karena saya nggak yakin kalau bakalan diterima bandingnya",
"Menurut saya percuma dilakukan banding kalau ujung2nya kalah",
"Sepertinya kalau ada banding saya tetap gamau banding",
"Saya rasa percuma ikut banding",
"Hanya buang waktu saja",
"Ribet dan pasti berbelit belit",
"Karena menurut saya banding akan membuat sistem e tilang semakin ribet"
]

# rugi
alasanRugi = [
    "Tidak ada kesempatan bagi pelaku untuk memberikan klarifikasi atau alasan mereka terhadap dugaan pelanggaran.",
    "Jika ada kesalahan dalam data atau pelanggaran yang salah diidentifikasi, pelaku tidak memiliki cara untuk memperbaikinya.",
    "Tanpa sistem banding, ada risiko penyalahgunaan wewenang oleh petugas penegak hukum yang tidak dapat diselidiki lebih lanjut.",
    "Pelaku mungkin tidak memiliki cara untuk menentang pelanggaran prosedur dalam penindakan.",
    "Kesalahan teknis dalam sistem E-tilang dapat merugikan pelaku tanpa kemungkinan perbaikan.",
    "Terdapat risiko kesalahan dalam mengidentifikasi pelaku atau kendaraan yang dapat merugikan orang yang tidak bersalah.",
    "Tanpa mekanisme banding, ada risiko diskriminasi dalam penindakan yang tidak dapat dipertimbangkan lebih lanjut.",
    "Pelaku tidak memiliki perlindungan hukum yang memadai tanpa akses ke proses banding.",
    "Tidak ada sistem banding dapat menghasilkan penegakan hukum yang tidak konsisten.",
    "Kasus-kasus yang memerlukan pertimbangan konteks khusus mungkin tidak diperhatikan.",
    "Pelaku mungkin memiliki kecurigaan terhadap kesalahan manusia dalam penindakan yang tidak dapat dibuktikan.",
    "Pelaku mungkin merasa bahwa data pribadi mereka terlalu terbuka tanpa mekanisme banding.",
    "Sistem tanpa banding mungkin tidak mendorong peningkatan kepatuhan terhadap peraturan lalu lintas.",
    "Pelaku mungkin merasa bahwa hukuman yang diterima tidak sesuai dengan pelanggaran yang dilakukan.",
    "Denda yang dikenakan tanpa kesempatan banding dapat mengakibatkan kerugian keuangan yang signifikan.",
    "Pelaku dapat menjadi rentan terhadap penyalahgunaan wewenang oleh petugas penegak hukum.",
    "Orang mungkin tidak memahami sepenuhnya aturan lalu lintas yang melibatkan pelanggaran mereka.",
    "Dalam beberapa kasus, penilaian pelanggaran dapat menjadi subjektif tanpa mekanisme banding.",
    "Pelaku mungkin merasa bahwa mereka tidak diberi kesempatan untuk membela diri atau membuktikan kesalahan mereka.",
    "Tanpa banding, pelaku memiliki sedikit pilihan selain membayar denda atau menghadapi konsekuensi lebih lanjut.",
    "Pelaku mungkin kehilangan kesempatan untuk memahami pelanggaran mereka dan menghindari pengulangan di masa depan."
]

alasanTRugi = [
    "Sistem E-tilang dapat mendorong pelaku untuk lebih patuh terhadap aturan lalu lintas, mengurangi pelanggaran.",
    "E-tilang memungkinkan penindakan cepat dan efisien, menghindari proses panjang yang terkait dengan banding.",
    "Tidak ada biaya atau waktu yang harus dikeluarkan oleh pelaku untuk mengajukan banding.",
    "Data digital memberikan transparansi tinggi, sehingga pelaku dapat melihat bukti pelanggaran dengan mudah.",
    "Tanpa banding, risiko penyalahgunaan proses banding oleh pelaku juga dihindari.",
    "Sistem E-tilang dapat membantu memfokuskan upaya pada peningkatan keselamatan jalan daripada proses hukum.",
    "Dengan data elektronik yang akurat, kemungkinan kesalahan dalam pelanggaran dapat diminimalisir.",
    "Pelaku tahu dengan pasti berapa denda yang harus mereka bayar, tanpa perlu menunggu keputusan banding.",
    "Tanpa proses banding, sumber daya penegakan hukum dapat dialokasikan dengan lebih baik untuk penindakan lebih lanjut."
]

# ketidakadaan
alasanKetidakadaan = [
    "Bukti digital dalam E-tilang dianggap kuat dan sulit untuk dibantah, yang mungkin tidak memberikan ruang yang cukup untuk pembelaan.",
    "Meskipun jarang terjadi, terdapat kemungkinan kecurangan atau kesalahan dalam proses E-tilang yang tidak dapat ditangani tanpa sistem banding.",
    "Sistem E-tilang sering kali menghasilkan keputusan otomatis tanpa pertimbangan manusia, mengurangi ruang bagi pembelaan individual.",
    "Terdapat risiko kesalahan identifikasi pelanggaran atau pemilik kendaraan yang tidak dapat diselidiki tanpa sistem banding.",
    "Hak asasi manusia termasuk hak untuk membela diri dan memiliki proses hukum yang adil, yang bisa terganggu oleh ketidakadaan sistem banding.",
    "Kesalahan teknis dalam teknologi E-tilang bisa merugikan pelaku yang ingin membela diri.",
    "Kadang-kadang, ketentuan hukum yang tidak jelas atau penerapannya yang subjektif memerlukan sistem banding untuk klarifikasi.",
    "Sistem banding adalah bagian dari sistem peradilan yang menjamin keamanan hukum bagi individu.",
    "Meskipun jarang, kesalahan manusia dalam input data atau penindakan bisa terjadi, dan sistem banding membantu mengatasi hal ini.",
    "Sistem banding dapat mencegah penyalahgunaan wewenang oleh petugas penegak hukum.",
    "Terkadang, konteks yang tidak diperhitungkan dalam proses E-tilang perlu dijelaskan dalam proses banding.",
    "Orang mungkin kehilangan bukti atau dokumen yang mendukung kasus mereka, dan sistem banding dapat memberi mereka kesempatan untuk memperbaikinya.",
    "Tanpa sistem banding, penafsiran yang salah terhadap kasus pelanggaran mungkin tidak dapat diperbaiki.",
    "Sistem banding juga berfungsi sebagai peluang untuk individu memahami dan mempelajari hak dan kewajiban mereka dalam hukum lalu lintas.",
    "Sistem banding adalah cara untuk memastikan bahwa setiap individu memiliki kesempatan yang sama untuk membela diri.",
    "Sistem banding membantu memastikan bahwa denda yang dijatuhkan adalah wajar dan sesuai dengan pelanggaran yang dilakukan.",
    "Proses banding dapat meningkatkan kesadaran masyarakat tentang aturan lalu lintas.",
    "Mekanisme banding meningkatkan transparansi dalam penegakan hukum, yang penting untuk menjaga kepercayaan masyarakat.",
    "Sistem banding memberikan kesempatan kepada pelaku untuk menjelaskan situasi mereka dan mengajukan bukti yang relevan.",
    "Tanpa banding, pelaku dapat menjadi korban dari keputusan yang mungkin berlebihan atau tidak adil.",
    "Banding dapat digunakan untuk menguji apakah prosedur penegakan hukum telah diikuti dengan benar dan adil dalam kasus tertentu.",
    "Pelaku tidak memiliki kesempatan untuk memberikan klarifikasi atau alasan mereka terhadap dugaan pelanggaran",
"Jika ada kesalahan dalam data atau pelanggaran yang salah diidentifikasi, pelaku tidak memiliki cara untuk memperbaikinya",
"Tanpa sistem banding, pelaku mungkin tidak memiliki cara untuk menentang pelanggaran prosedur dalam penindakan",
"Kesalahan teknis dalam sistem E-tilang dapat merugikan pelaku tanpa kemungkinan perbaikan",
"Terdapat risiko kesalahan dalam mengidentifikasi pelaku atau kendaraan yang dapat merugikan orang yang tidak bersalah",
"Pelaku tidak memiliki perlindungan hukum yang memadai tanpa akses ke proses banding",
"Tidak ada sistem banding dapat menghasilkan penegakan hukum yang tidak konsisten",
"Kasus-kasus yang memerlukan pertimbangan konteks khusus mungkin tidak diperhatikan",
"Pelaku mungkin memiliki kecurigaan terhadap kesalahan manusia dalam penindakan yang tidak dapat dibuktikan atau diklarifikasi"
]

alasanTKetidakadaan = [
    ""
]

# diterapkan
alasanDiterapkan = [
    "Membantu melindungi hak individu untuk membela diri dan mendapatkan perlakuan yang adil",
    "Menjamin bahwa proses hukum berjalan secara adil dan transparan",
    "Memungkinkan perbaikan ketika terjadi kesalahan identifikasi dalam pelanggaran",
    "Memungkinkan koreksi jika ada kesalahan teknis dalam sistem E-tilang",
    "Memberikan akses kepada pelaku untuk melihat bukti pelanggaran dan data yang digunakan",
    "Memberi peluang kepada pelaku untuk menjelaskan atau membela diri atas pelanggaran yang dituduhkan",
    "Meningkatkan kepatuhan masyarakat terhadap aturan lalu lintas karena mereka tahu mereka dapat membela diri jika diperlukan",
    "Meningkatkan transparansi dalam penegakan hukum dan meningkatkan kepercayaan masyarakat",
    "Membantu memastikan bahwa hukuman yang diberikan sesuai dengan pelanggaran yang dilakukan",
    "Mendukung prinsip-prinsip hak asasi manusia yang melindungi individu dari penyalahgunaan kekuasaan",
    "Memungkinkan pelaku untuk mengklarifikasi atau mengoreksi data elektronik yang mungkin tidak akurat",
    "Menjaga kepentingan publik dalam penegakan hukum dan keselamatan jalan",
    "Menjamin bahwa setiap individu memiliki kesempatan yang sama untuk membela diri dalam persidangan",
    "Mencegah potensi penyalahgunaan kekuasaan oleh pihak berwenang dalam proses penindakan",
    "Memungkinkan pelaku untuk mengajukan bukti atau argumen yang relevan dalam pembelaan mereka",
    "Membantu memeriksa apakah prosedur penindakan hukum telah diikuti dengan benar",
    "Memberikan hak kepada pelaku untuk mendapatkan klarifikasi atau penjelasan atas pelanggaran yang dituduhkan",
    "Memungkinkan pelaku untuk menjelaskan situasi khusus yang mungkin tidak terlihat dalam data pelanggaran",
    "Mencegah pelaku menjadi korban kesalahan atau ketidakadilan dalam proses penegakan hukum",
    "Proses banding dapat membantu meningkatkan kesadaran masyarakat terhadap aturan lalu lintas dan meningkatkan kepatuhan."
]

alasanTDiterapkan = [
    "Tanpa banding, proses E-tilang bisa lebih efisien dan cepat.",
    "Tidak ada biaya tambahan yang harus dikeluarkan untuk mengajukan banding.",
    "E-tilang dapat meningkatkan kepatuhan terhadap aturan lalu lintas tanpa proses banding yang memperlambat penindakan.",
    "E-tilang menggunakan teknologi canggih yang dianggap lebih akurat daripada penilaian manusia.",
    "Pelaku tahu dengan pasti berapa denda yang harus mereka bayar tanpa perlu menunggu keputusan banding.",
    "Tanpa banding, sistem hukum dapat mengurangi beban administratif dan penumpukan kasus.",
    "Data pelanggaran tersedia secara transparan untuk dilihat oleh pelaku.",
    "Tidak ada interpretasi subjektif oleh petugas penegak hukum dalam proses E-tilang.",
    "Sumber daya penegakan hukum dapat dialokasikan dengan lebih baik ke area yang membutuhkan penindakan lebih intensif.",
    "Pelaku tidak perlu menunggu keputusan banding yang dapat memakan waktu lama."
]

# efektif = len(alasanEfektif)
# tefektif = len(alasanTEfektif)

# idxEfek = 0
# idxTEfek = 0

# pembelaan = len(alasanPembelaan)
# tpembelaan = len(alasanTPembelaan)

# idxPem = 0
# idxTPem = 0

# pengajuan = len(alasanPengajuan)
# tpengajuan = len(alasanTPengajuan)

# idxPeng = 0
# idxTPeng = 0

# rugi = len(alasanRugi)
# trugi = len(alasanTRugi)

# idxRugi = 0
# idxTRugi = 0

# ketidakadaan = len(alasanKetidakadaan)
# tketidakadaan = len(alasanTKetidakadaan)

# idxAda = 0
# idxTAda = 0

# diterapkan = len(alasanDiterapkan)
# tditerapkan = len(alasanTDiterapkan)

# idxTerap = 0
# idxTTerap = 0

# 

efektif = 8
tefektif = 0

idxEfek = 9
idxTEfek = 13

pembelaan = 0
tpembelaan = 8

idxPem = 7
idxTPem = 15

pengajuan = 8
tpengajuan = 0

idxPeng = 12
idxTPeng = 10

rugi = 8
trugi = 0

idxRugi = 13
idxTRugi = 9

ketidakadaan = 8
tketidakadaan = 0

idxAda = 21
idxTAda = 1

diterapkan = 8
tditerapkan = 0

idxTerap = 12
idxTTerap = 10


times = 8
index = 22

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if efektif != 0 and tefektif != 0 :
            pil = random.choice([4,5])
        elif efektif != 0 and tefektif == 0 :
            pil = 4
        elif efektif == 0 and tefektif != 0 :
            pil = 5
        
        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        textboxes[0].send_keys(email[index])

        time.sleep(2)
        radiobuttons[2].click()
        radiobuttons[0].click()

        radiobuttons[pil].click()

        time.sleep(2)
        if pil == 4 :
            textarea[0].send_keys(alasanEfektif[idxEfek])
            idxEfek += 1
            efektif -= 1
        else :
            textarea[1].send_keys(alasanTEfektif[idxTEfek])
            idxTEfek += 1
            tefektif -= 1
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        if pembelaan != 0 and tpembelaan != 0 :
            pil1 = random.choice([0,1])
        elif pembelaan != 0 and tpembelaan == 0 :
            pil1 = 0
        elif pembelaan == 0 and tpembelaan != 0 :
            pil1 = 1
        
        time.sleep(2)
        radiobuttons[pil1].click()

        if pil1 == 0 :
            textarea[0].send_keys(alasanPembelaan[idxPem])
            textarea[1].send_keys("-")
            idxPem += 1
            pembelaan -= 1
        else :
            textarea[0].send_keys("-")
            textarea[1].send_keys(alasanTPembelaan[idxTPem])
            idxTPem += 1
            tpembelaan -= 1
        
        time.sleep(2)
        if pengajuan != 0 and tpengajuan != 0 :
            pil2 = random.choice([2,3])
        elif pengajuan != 0 and tpengajuan == 0 :
            pil2 = 2
        elif pengajuan == 0 and tpengajuan != 0 :
            pil2 = 3
        
        time.sleep(2)
        radiobuttons[pil2].click()

        if pil2 == 2 :
            textarea[2].send_keys(alasanPengajuan[idxPeng])
            textarea[3].send_keys("-")
            idxPeng += 1
            pengajuan -= 1
        else :
            textarea[2].send_keys("-")
            textarea[3].send_keys(alasanTPengajuan[idxTPeng])
            idxTPeng += 1
            tpengajuan -= 1
        
        time.sleep(2)
        if rugi != 0 and trugi != 0 :
            pil3 = random.choice([4,5])
        elif rugi != 0 and trugi == 0 :
            pil3 = 4
        elif rugi == 0 and trugi != 0 :
            pil3 = 5
        
        time.sleep(2)
        radiobuttons[pil3].click()

        if pil3 == 4 :
            textarea[4].send_keys(alasanRugi[idxRugi])
            textarea[5].send_keys("-")
            idxRugi += 1
            rugi -= 1
        else :
            textarea[4].send_keys("-")
            textarea[5].send_keys(alasanTRugi[idxTRugi])
            idxTRugi += 1
            trugi -= 1
        
        time.sleep(2)
        if ketidakadaan != 0 and tketidakadaan != 0 :
            pil4 = random.choice([6,7])
        elif ketidakadaan != 0 and tketidakadaan == 0 :
            pil4 = 6
        elif ketidakadaan == 0 and tketidakadaan != 0 :
            pil4 = 7
        
        time.sleep(2)
        radiobuttons[pil4].click()

        if pil4 == 6 :
            textarea[6].send_keys(alasanKetidakadaan[idxAda])
            textarea[7].send_keys("-")
            idxAda += 1
            ketidakadaan -= 1
        else :
            textarea[6].send_keys("-")
            textarea[7].send_keys(alasanTKetidakadaan[idxTAda])
            idxTAda += 1
            tketidakadaan -= 1

        time.sleep(2)
        if diterapkan != 0 and tditerapkan != 0 :
            pil5 = random.choice([8,9])
        elif diterapkan != 0 and tditerapkan == 0 :
            pil5 = 8
        elif diterapkan == 0 and tditerapkan != 0 :
            pil5 = 9
        
        time.sleep(2)
        radiobuttons[pil5].click()

        if pil5 == 8 :
            textarea[8].send_keys(alasanDiterapkan[idxTerap])
            textarea[9].send_keys("-")
            idxTerap += 1
            diterapkan -= 1
        else :
            textarea[8].send_keys("-")
            textarea[9].send_keys(alasanTDiterapkan[idxTTerap])
            idxTTerap += 1
            tditerapkan -= 1
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/7cYtWqJcMcJxbVZh8")

        index+=1
        print("==================")
        print("efektif = " + str(efektif))
        print("tefektif = " + str(tefektif))
        print("")
        print("idxEfek = " + str(idxEfek))
        print("idxTEfek = " + str(idxTEfek))
        print("")
        print("pembelaan = " + str(pembelaan))
        print("tpembelaan = " + str(tpembelaan))
        print("")
        print("idxPem = " + str(idxPem))
        print("idxTPem = " + str(idxTPem))
        print("")
        print("pengajuan = " + str(pengajuan))
        print("tpengajuan = " + str(tpengajuan))
        print("")
        print("idxPeng = " + str(idxPeng))
        print("idxTPeng = " + str(idxTPeng))
        print("")
        print("rugi = " + str(rugi))
        print("trugi = " + str(trugi))
        print("")
        print("idxRugi = " + str(idxRugi))
        print("idxTRugi = " + str(idxTRugi))
        print("")
        print("ketidakadaan = " + str(ketidakadaan))
        print("tketidakadaan = " + str(tketidakadaan))
        print("")
        print("idxAda = " + str(idxAda))
        print("idxTAda = " + str(idxTAda))
        print("")
        print("diterapkan = " + str(diterapkan))
        print("tditerapkan = " + str(tditerapkan))
        print("")
        print("idxTerap = " + str(idxTerap))
        print("idxTTerap = " + str(idxTTerap))
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