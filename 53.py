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
driver.get("https://www.cognitoforms.com/UnversitasIndonesia/KuesionerTesisSharyneSylvani")

namaDepan = [
    "Mutia",
    "Ali",
    "Riskia",
    "Budi",
    "Aryo",
    "Nana",
    "Yahya",
    "Putri",
    "Nanda",
    "Yudi",
    "Yuli",
    "Bayu",
    "Bellanda",
    "Budi",
    "Miranda",
    "Sadewa",
    "Alffianto",
    "Annisa",
    "Fattahilah",
    "Diah",
    "Attaka",
    "Azzarin",
    "Fabian",
    "Nia",
    "Bayu",
    "Syifa",
    "Aditya",
    "Siti",
    "Reyhan",
    "Salma",
    "Angga",
    "Putri",
    "Raja",
    "Affifah",
    "Shaka",
    "Cynara",
    "Mona",
    "Mahendra",
    "Fryshta",
    "Yanuar",
    "Rayhan",
    "Sutisna",
    "Ayu",
    "Muhammad",
    "Ardyanto",
    "Putra",
    "Agung",
    "Dani",
    "Dimas",
    "Nabilla",
]

namaBelakang = [
    "Nur",
    "Hasanudin",
    "Febrianti",
    "Wibowo",
    "Nugraha",
    "Annisa",
    "Nugraha",
    "Dewi",
    "Ayunda",
    "Pradanawan",
    "Dewi",
    "Merta",
    "Ayunda",
    "Suryanto",
    "Nella",
    "Budiantoro",
    "Kuntoro",
    "Chania",
    "Sadewa",
    "Cindy",
    "Majid",
    "Nabila",
    "Putra",
    "Yuliana",
    "Dwiganara",
    "Radifah",
    "Derdinand",
    "Fauziyah",
    "Utomowa",
    "Arowaya",
    "Putra",
    "Keancana",
    "Wardanawan",
    "Nabila",
    "Wijaya",
    "Nafisah",
    "Hadfinna",
    "Fadilah",
    "Nabilla",
    "Suryadi",
    "Wicasa",
    "Ayuni",
    "Ningsih",
    "Susanto",
    "Putra",
    "Wirawan",
    "Nugroho",
    "Ramadhan",
    "Purbo",
    "Qolbi",
]

telp = [
    "084624253733",
    "088565440513",
    "083626799003",
    "088070442682",
    "083435047182",
    "089579629094",
    "080103002233",
    "086659262105",
    "087136378661",
    "080640301967",
    "083806763847",
    "088509885576",
    "084985961237",
    "086137328130",
    "089843988039",
    "086738422620",
    "089045039379",
    "087788078906",
    "088159431881",
    "089474988296",
    "088530547344",
    "085109243357",
    "080470592685",
    "083273198985",
    "081850592479",
    "081211906212",
    "081212784008",
    "081250284950",
    "081264718461",
    "081280281529",
    "081290475868",
    "081270348686",
    "082132447386",
    "087886158249",
    "081278010606",
    "087778433058",
    "085956060930",
    "087848003451",
    "0882008113306",
    "083838919000",
    "081511323691",
    "088294743163",
    "083181803358",
    "081331973192",
    "0895609625455",
    "085729979914",
    "085156051463",
    "085729213992",
    "087780590374",
    "081720592854",
]

#1 laki 0 perempuan
kelamin = [0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,0,]

essays = [
#essay 1
[
    "limbah medis ditempatkan dalam wadah terpisah yang ditandai sebagai limbah medis.",
    "Simpan limbah medis yang telah dipilah dalam wadah yang tertutup rapat dan aman sebelum diangkut ke tempat pembuangan akhir.",
    "Petugas kesehatan setempat akan memberikan informasi penting tentang jadwal pengumpulan dan jenis wadah yang digunakan untuk limbah medis.",
    "Pastikan limbah medis diangkut dengan aman menggunakan kendaraan khusus sesuai dengan pedoman pengelolaan limbah medis.",
    "Limbah medis harus dibuang di fasilitas pembuangan akhir yang sesuai dan diizinkan oleh pemerintah setempat.",
    "Pastikan limbah medis ditempatkan dalam wadah yang secara khusus ditandai sebagai limbah medis agar mudah dikenali.",
    "Simpan limbah medis dalam wadah yang tertutup rapat dan pastikan tidak ada kebocoran atau kontaminasi.",
    "Koordinasikan dengan petugas kesehatan setempat untuk mengetahui jadwal pengumpulan limbah medis dan wadah yang harus digunakan.",
    "Pastikan kendaraan yang digunakan untuk mengangkut limbah medis memenuhi standar keamanan dan sanitasi yang ditetapkan.",
    "Limbah medis harus dibuang ke fasilitas pembuangan akhir yang memenuhi persyaratan pemerintah agar tidak menimbulkan risiko bagi lingkungan dan kesehatan masyarakat.",
    "limbah ditempatkan pada tempat khusus, diangkut dengan aman menggunakan kendaraan khusus untuk dibuang ke penampungan akhir",
    "Limbah diletakkan di tempat yang ditentukan, Limbah diangkut dengan kendaraan khusus untuk dibuang ke tempat akhir dengan aman.",
    "Limbah ditempatkan di area khusus, Kendaraan khusus digunakan untuk mengangkut limbah dengan aman ke tempat pembuangan akhir.",
    "Tempatkan limbah pada tempat yang telah ditentukan, Limbah diangkut menggunakan kendaraan khusus dengan tujuan dibuang ke tempat penampungan akhir dengan aman.",
    "Tempat khusus digunakan untuk meletakkan limbah, Pengangkutan limbah dilakukan dengan kendaraan khusus untuk dibuang ke lokasi penampungan akhir dengan aman.",
    "Limbah diletakkan dengan tepat pada lokasi yang telah ditentukan, Kendaraan khusus digunakan untuk aman-aman membawa limbah menuju tempat pembuangan akhir.",
    "Letakkan limbah di wadah yang disediakan, Limbah dipindahkan dengan kendaraan khusus dengan tujuan akhir di tempat penampungan yang aman.",
    "Tempatkan limbah pada wadah yang sesuai, Transportasi limbah dilakukan dengan menggunakan kendaraan khusus untuk menuju penampungan akhir dengan keamanan terjamin.",
    "Limbah ditempatkan dengan benar pada area yang ditentukan, Pengangkutan limbah dilaksanakan dengan kendaraan yang dirancang khusus untuk membawa limbah menuju tempat pembuangan akhir dengan aman.",
    "Letakkan limbah pada kontainer yang telah ditentukan, Limbah diangkut dengan kendaraan spesifik untuk dibuang dengan aman ke tempat penampungan akhir.",
    "Limbah diarahkan ke tempat khusus penampungan, Transportasi limbah dilakukan melalui kendaraan khusus agar aman saat dibuang ke tempat akhir penampungan.",
    "Limbah disimpan dengan rapat dalam wadah yang tertutup, Pengangkutan limbah menggunakan kendaraan khusus yang aman menuju tempat pembuangan akhir.",
    "Wadah yang tertutup rapat digunakan untuk menyimpan limbah dengan aman, Limbah diangkut dengan kendaraan khusus agar dapat dibuang dengan aman di tempat penampungan akhir.",
    "Limbah ditempatkan dalam wadah yang rapat untuk menjaga keamanan dan kebersihan, Kendaraan khusus digunakan untuk mengangkut limbah dengan aman hingga mencapai tempat pembuangan akhir.",
    "Penggunaan wadah yang rapat memastikan limbah tersimpan dengan baik dan terhindar dari kontaminasi lingkungan, Limbah diangkut dengan aman menggunakan kendaraan khusus demi memastikan pembuangan akhir yang tepat dan teratur.",
    "Tempat khusus untuk meletakkan limbah, Pengangkutan limbah dilakukan dengan kendaraan khusus untuk dibuang ke lokasi penampungan akhir",
    "Limbah diletakkan di tempat yang ditentukan, Limbah diangkut dengan kendaraan khusus lalu dibuang ke tempat akhir",
    "limbah medis ditempatkan dalam wadah terpisah",
],
#essay 2
[
    "Limbah B3 medis COVID-19 di tempat tinggal saya dikemas dengan rapat dan diikat erat.",
    "Kemasan limbah B3 medis COVID-19 di rumah saya harus tertutup, tidak bocor, dan kedap udara.",
    "Saya memastikan limbah B3 medis COVID-19 di tempat tinggal saya terkemas dengan aman dan terhindar dari tumpahan.",
    "Limbah B3 medis COVID-19 di rumah saya harus dikemas dalam wadah yang tertutup rapat agar tidak menimbulkan risiko penyebaran.",
    "Kemasan limbah B3 medis COVID-19 di tempat tinggal saya harus memenuhi persyaratan keamanan dan menghindari kebocoran.",
    "Saya mengemas limbah B3 medis COVID-19 di rumah saya dengan kemasan yang sesuai, yaitu tertutup rapat, tidak bocor, dan kedap udara.",
    "Limbah B3 medis COVID-19 di tempat tinggal saya dikemas dengan hati-hati untuk mencegah kontaminasi dan penyebaran penyakit.",
    "Saya mengikat limbah B3 medis COVID-19 di rumah saya dengan erat agar tidak ada kebocoran atau penyebaran yang dapat membahayakan lingkungan.",
    "Kemasan limbah B3 medis COVID-19 di tempat tinggal saya harus memenuhi standar keamanan dan perlindungan lingkungan.",
    "Saya memilih kemasan yang tepat untuk limbah B3 medis COVID-19 di rumah saya, yaitu kemasan yang tertutup rapat, tidak bocor, dan dapat mencegah paparan yang tidak diinginkan.",
    "Limbah B3 medis COVID-19 di tempat tinggal dikemas dengan teliti dan hati-hati untuk menjaga keamanan dan kesehatan.",
    "memastikan limbah B3 medis COVID-19 di rumah tidak dapat terkontaminasi atau tumpah selama proses pengemasan.",
    "Kemasan limbah B3 medis COVID-19 di tempat tinggal harus memenuhi persyaratan keamanan yang ditetapkan.",
    "mengikuti petunjuk pengemasan yang diberikan untuk limbah B3 medis COVID-19 di rumah guna menjaga keamanan dan kebersihan lingkungan.",
    "Limbah B3 medis COVID-19 di tempat tinggal dikemas dengan mengutamakan keselamatan petugas yang menangani limbah tersebut.",
    "menggunakan wadah khusus yang dirancang untuk limbah B3 medis COVID-19 di rumah agar dapat mencegah risiko penyebaran penyakit.",
    "Kemasan limbah B3 medis COVID-19 di tempat tinggal harus kuat dan tahan terhadap kebocoran untuk menghindari kontaminasi.",
    "menjaga agar limbah B3 medis COVID-19 di rumah tetap terkendali dengan mengemasnya dengan rapi dan rapat.",
    "tidak mengabaikan tindakan pengemasan yang benar untuk limbah B3 medis COVID-19 di tempat tinggal guna menjaga keamanan dan kesehatan bersama.",
    "Kemasan limbah B3 medis COVID-19 di rumah harus diikat secara erat dan aman untuk mencegah terjadinya kebocoran selama proses pengangkutan.",
    "memperhatikan kebersihan dan keamanan saat mengemas limbah B3 medis COVID-19 di tempat tinggal untuk mencegah risiko paparan yang tidak diinginkan.",
    "Kemasan limbah B3 medis COVID-19 di rumah harus memenuhi standar keselamatan dan kebersihan yang ditetapkan.",
    "selalu menggunakan kemasan yang tahan lama dan kokoh untuk limbah B3 medis COVID-19 di tempat tinggal agar tidak terjadi kerusakan selama proses penanganan.",
    "Limbah B3 medis COVID-19 di rumah dikemas dengan cermat untuk meminimalkan risiko penyebaran penyakit dan menjaga kebersihan lingkungan sekitar.",
    "mengikuti prosedur pengemasan yang telah ditetapkan untuk limbah B3 medis COVID-19 di tempat tinggal guna menjaga keamanan dan kebersihan secara maksimal.",
    
    "memastikan limbah di rumah tidak dapat terkontaminasi atau tumpah selama proses pengemasan.",
    "Kemasan limbH di tempat tinggal harus memenuhi persyaratan keamanaN.",
    "Kemasan limbah B3 medis di tempat tinggal harus memenuhi persyaratan yang ditetapkan.",
    "mengikuti petunjuk pengemasan yang diberikan guna menjaga keamanan dan kebersihan lingkungan.",
    "menjaga limbah medis di rumah tetap terkendali dengan mengemasnya dengan rapi dan rapat.",
],
#essay 3
[
    "4 hari",
    "6 hari",
    "empat hari",
    "6 hari",
    "empat hari",
    "3 hari",
    "3 hari",
    "6 hari",
    "tujuh hari",
    "7 hari",
    "enam hari",
    "5 hari",
    "5 hari",
    "3 hari",
    "tujuh  hari",
    "lima hari",
    "3 hari",
    "6 hari",
    "lima hari",
    "3 hari",
    "empat hari",
    "5 hari",
    "6 hari",
    "empat hari",
    "3 hari",
    "6 hari",
    "6 hari",
    "tiga hari",
    "3 hari",
    "4 hari",
    "tiga hari",
    "3 hari",
    "empat hari",
    "5 hari",
    "4 hari",
    "lima hari",
    "3 hari",
    "6 hari",
    "6 hari",
],
# essay 4
[
    "Drum logam yang tertutup rapat",
    "Kotak plastik kedap udara dengan penutup kunci",
    "Botol kaca berpenutup kedap udara",
    "Kantong plastik khusus limbah medis yang dikikis",
    "Ember plastik berpenutup rapat",
    "Bak sampah medis berpenutup",
    "Karung khusus limbah medis dengan tali pengikat",
    "Kotak kardus dengan lapisan plastik dalam yang kedap air",
    "Kontainer plastik khusus limbah medis dengan sistem segel ganda",
    "Kotak logam tahan karat dengan penutup yang tersegel",
    "Tabung kaca dengan penutup yang rapat",
    "Kantong laminasi yang tahan air dengan sistem segel ganda",
    "Ember logam berpenutup dengan kunci ganda",
    "Peti kayu berlapis plastik dengan penutup rapat",
    "Drum plastik berpenutup karet yang kedap air",
    "Tas plastik tebal yang dilas di sisi-sisinya",
    "Wadah khusus limbah medis berlapis baja",
    "Tong plastik khusus limbah medis dengan tutup berengsel",
    "Tabung PVC dengan penutup ulir",
    "Kotak karton laminasi dengan penutup bersegel",
    "Botol plastik berpenutup ulir kedap udara",
    "Tas kertas berlapis plastik yang kedap air",
    "Ember karet dengan penutup rapat",
    "Wadah berbentuk silinder dari plastik tahan panas dengan penutup kunci",
    "Tabung logam berpenutup ulir yang tahan korosi",
    "Tabung PVC dengan penutup",
    "Ember karet yang ditutup rapat",
],
# essay 5
[
    "Perusahaan pengelola limbah medis terdaftar.",
    "Perusahaan jasa pengelola limbah medis.",
    "Pengangkutan limbah medis yang ditunjuk oleh instansi.",
    "Pihak ketiga yang memiliki lisensi dan izin untuk mengangkut limbah medis.",
    "Tim khusus pengangkut limbah medis dari rumah sakit atau klinik.",
    "Layanan pengangkutan limbah medis yang bekerja sama dengan lembaga pemerintah setempat.",
    "Perusahaan pengangkutan limbah medis yang ditunjuk oleh instansi terkait.",
    "Tim khusus dari lembaga riset atau universitas yang memiliki program pengelolaan limbah medis.",
    "Tim khususuniversitas yang memiliki program pengelolaan limbah medis.",
    "Perusahaan pengelola limbah medis.",
    "Komunitas atau lembaga nirlaba yang memiliki program pengelolaan limbah medis.",
    "Perusahaan pengelola limbah medis khusus.",
    "Layanan pengangkutan limbah medis yang bekerja sama dengan daerah setempat",
],
# essay 6
[
    "Di tempat penampungan umum, limbah B3 medis COVID-19 diangkut oleh petugas untuk pembuangan akhir kota.",
    "Di penampungan kota, petugas mengangkut limbah B3 medis COVID-19 untuk dibuang di tempat pembuangan akhir.",
    "Pembuangan akhir kota dilakukan dengan mengangkut limbah B3 medis COVID-19 dari tempat penampungan umum.",
    "Petugas bertanggung jawab mengangkut limbah B3 medis COVID-19 ke tempat penampungan kota untuk pembuangan akhir.",
    "Diangkut oleh petugas, limbah B3 medis COVID-19 dibuang di tempat penampungan umum di kota.",
    "Limbah B3 medis COVID-19 diangkut oleh petugas ke tempat pembuangan akhir di kota.",
    "tidakh tahu, karena diangkut oleh petugas",
    "Petugas mengirim limbah B3 medis COVID-19 dari penampungan kota ke tempat pembuangan akhir kota.",
    "Di tempat penampungan umum, limbah B3 medis COVID-19 diangkut oleh petugas menuju pembuangan akhir kota.",
    "Petugas membawa limbah B3 medis COVID-19 dari tempat penampungan kota untuk dibuang di tempat pembuangan akhir kota.",
    "di penampungan kota",
    "Pembuangan akhir kota dilakukan dengan mengangkut limbah B3 medis COVID-19 dari penampungan umum.",
    "Petugas bertugas mengangkut limbah B3 medis COVID-19 ke tempat penampungan kota untuk pembuangan akhir di kota.",
    "Diangkut oleh petugas, limbah B3 medis COVID-19 dibuang di tempat penampungan umum yang ada di kota.",
    "di tempat penampungan umum",
    "Limbah B3 medis COVID-19 diangkut oleh petugas ke tempat pembuangan akhir yang berada di kota.",
    "Petugas mengirim limbah B3 medis COVID-19 dari penampungan kota ke tempat pembuangan akhir yang ada di kota.",
    "Di tempat penampungan umum, petugas mengangkut limbah B3 medis COVID-19 untuk pembuangan akhir di kota.",
    "Petugas membawa limbah B3 medis COVID-19 dari tempat penampungan kota ke tempat pembuangan akhir di kota.",
    "Pembuangan akhir kota dilakukan dengan mengangkut limbah B3 medis COVID-19 dari penampungan umum di kota.",
    "Petugas bertugas mengangkut limbah B3 medis COVID-19 ke tempat penampungan kota untuk pembuangan akhir kota.",
    "pembuangan akhir kota",
    "Diangkut oleh petugas, limbah B3 medis COVID-19 dibuang di tempat penampungan umum yang terletak di kota.",
    "Limbah B3 medis COVID-19 diangkut oleh petugas ke tempat pembuangan akhir yang terletak di kota.",
    "Petugas mengirim limbah B3 medis COVID-19 dari penampungan kota ke tempat pembuangan akhir yang terletak di kota.",
],
# essay 7
[
    "Pemerintah memberikan informasi melalui sosial media tentang pengelolaan limbah medis COVID-19.",
    "Masyarakat diberikan brosur dan pamflet tentang cara aman mengelola limbah medis.",
    "Acara dan seminar diadakan untuk mengajarkan cara yang benar mengelola limbah medis.",
    "Petugas kesehatan dilatih dalam pengelolaan limbah medis COVID-19.",
    "Pemerintah bekerja sama dengan lembaga lain untuk menyampaikan informasi tentang pengelolaan limbah medis.",
    "Peraturan ditegakkan untuk memastikan pengelolaan limbah medis yang benar.",
    "Masyarakat dapat mengajukan pertanyaan dan mendapatkan informasi melalui konsultasi dan layanan informasi pemerintah.",
    "Informasi pengelolaan limbah medis disebarkan melalui iklan dan spanduk di tempat umum.",
    "Pusat layanan informasi didirikan untuk memberikan panduan tentang pengelolaan limbah medis.",
    "Tim edukasi diterjunkan untuk memberikan sosialisasi langsung tentang pengelolaan limbah medis.",
    "Pemerintah mengadakan webinar tentang pengelolaan limbah medis COVID-19.",
    "Video edukatif diproduksi dan diunggah online untuk memperluas pemahaman tentang pengelolaan limbah medis.",
    "Materi pengelolaan limbah medis diberikan dalam program pelatihan komunitas.",
    "Pameran kesehatan diselenggarakan untuk menyampaikan informasi tentang pengelolaan limbah medis kepada masyarakat.",
    "Media cetak menerbitkan artikel tentang pentingnya pengelolaan limbah medis yang baik.",
    "Sistem pemberitahuan SMS dikirimkan kepada masyarakat untuk memberikan pengingat tentang pengelolaan limbah medis.",
    "Dinas kesehatan setempat memberikan brosur panduan pengelolaan limbah medis kepada fasilitas kesehatan.",
    "Kampanye nasional diluncurkan untuk meningkatkan kesadaran tentang pengelolaan limbah medis yang aman.",
    "Informasi pengelolaan limbah medis disajikan dalam bentuk infografis yang mudah dipahami.",
    "Program radio dan televisi mengadakan siaran khusus tentang pengelolaan limbah medis COVID-19.",
    "Pusat pengelolaan limbah medis didirikan sebagai sumber informasi dan bantuan bagi masyarakat.",
    "Sekolah dan perguruan tinggi melibatkan siswa dalam proyek pengelolaan limbah medis sebagai bagian dari kurikulum.",
    "Tim penyuluhan berkunjung ke desa-desa untuk memberikan pengetahuan tentang pengelolaan limbah medis kepada masyarakat.",
    "Petugas kesehatan memberikan penyuluhan langsung tentang pengelolaan limbah medis kepada pasien dan keluarganya.",
    "Masyarakat dapat mengakses panduan pengelolaan limbah medis melalui aplikasi ponsel yang disediakan oleh pemerintah.",
    "Pemerintah memberikan informasi melalui diskusi tentang pengelolaan limbah medis COVID-19.",
],
# essay 8
[
    "internet, tentang tata cara pengolahan limbah medis yang benar",
    "Internet menyediakan akses mudah ke informasi tentang tata cara pengolahan limbah medis yang benar.",
    "Banyak sumber online yang menyediakan panduan mengenai pengolahan limbah medis yang benar.",
    "Melalui internet, dapat ditemukan berbagai artikel dan blog yang membahas tata cara pengolahan limbah medis dengan benar.",
    "Website pemerintah menyediakan informasi lengkap tentang tata cara pengolahan limbah medis melalui internet.",
    "Video tutorial yang berisi tata cara pengolahan limbah medis yang benar dapat diakses melalui internet.",
    "Banyak forum online yang memungkinkan diskusi dan tanya jawab seputar pengolahan limbah medis yang benar.",
    "Melalui internet, ada platform e-learning yang menyediakan kursus dan pelatihan tentang pengolahan limbah medis yang benar.",
    "Banyak organisasi non-pemerintah menyediakan panduan online tentang pengolahan limbah medis yang benar.",
    "Dengan menggunakan internet, informasi terkini seputar tata cara pengolahan limbah medis dapat diperoleh dengan cepat.",
    "Melalui internet, ada akses ke publikasi ilmiah dan jurnal yang membahas tentang pengolahan limbah medis yang benar.",
    "Media sosial dapat menjadi platform untuk berbagi informasi tentang tata cara pengolahan limbah medis yang benar.",
    "Dalam grup diskusi online, anggota dapat saling berbagi pengalaman dan pengetahuan tentang pengolahan limbah medis yang benar.",
    "Internet memberikan kemudahan akses ke dokumen panduan resmi pemerintah tentang pengolahan limbah medis yang benar.",
    "Melalui internet, dapat ditemukan infografis yang jelas dan mudah dipahami mengenai tata cara pengolahan limbah medis yang benar.",
    "Dalam webinar online, ahli memberikan penjelasan tentang tata cara pengolahan limbah medis yang benar melalui internet.",
    "Aplikasi mobile tentang pengolahan limbah medis dapat diunduh melalui internet.",
    "Internet memungkinkan akses ke database informasi kesehatan yang mencakup tata cara pengolahan limbah medis yang benar.",
    "Melalui internet, ada forum diskusi khusus yang fokus membahas pengolahan limbah medis dengan benar.",
    "Dalam website khusus, pengguna dapat mengikuti langkah-langkah praktis dalam pengolahan limbah medis yang benar.",
    "Ada berbagai platform webinar yang menyediakan sesi pelatihan mengenai tata cara pengolahan limbah medis yang benar melalui internet.",
    "Melalui internet, dapat ditemukan video animasi yang menjelaskan secara visual tata cara pengolahan limbah medis yang benar.",
    "Ada newsletter online yang mengirimkan informasi terkini seputar pengolahan limbah medis yang benar.",
    "Dalam website resmi institusi kesehatan, terdapat bagian yang menjelaskan tata cara pengolahan limbah medis yang benar.",
    "Dalam grup komunitas online, anggota saling berbagi sumber informasi tentang tata cara pengolahan limbah",

],
]

jumlahEssay = [25,25,25,25,25,25,25,25]


idx1 = 0
idx2 = 0
idx3 = 0
idx4 = 0
idx5 = 0
idx6 = 0
idx7 = 0
idx8 = 0

times = 1
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0
        sample = []
        essaytemp = [0,0,0,0,0,0,0,0]

        for i in range(len(jumlahEssay)):
            if jumlahEssay[i] != 0 :
                sample.append(i+1)

        essay = random.sample(sample, 4)
        essay.sort()

        p = 0
        # soal = 8
        while p < 4:
            for i in range(8):
                if essay[p] == i+1:
                    essaytemp[i] = 1
            p += 1

        # dropdown = driver.find_elements("css selector", ".cog-branding")#isian
        # driver.execute_script("dropdown[0].style.display = 'none';")
        driver.execute_script("document.getElementsByClassName('cog-branding')[0].style.display = 'none';")

        textboxes = driver.find_elements("css selector", ".el-input__inner")#isian
        radiobuttons = driver.find_elements("css selector", ".el-radio__inner")#isian
        pilihan = driver.find_elements("css selector", ".el-select-dropdown__item")#isian
        textarea = driver.find_elements("css selector", ".el-textarea__inner")#isian
        checkboxes = driver.find_elements("css selector", ".el-checkbox__inner")#isian
        
        usia = random.choice([1,2,3,4,5])

        if usia == 1:
            pernikahan = 11
            pendidikan = random.choice([14,15,16])
        else:
            pernikahan = random.choice([10,11])
            pendidikan = random.choice([15,16,16,17,18,19,19])

        if pendidikan == 14 or pendidikan == 15:
            pekerjaan = 21
            rumah = 31
        elif pendidikan >= 16 and usia == 5 :
            pekerjaan = random.choice([22,24,25,27])
            rumah = random.choice([29,30,31,32])
        elif pendidikan >= 16 and usia < 5:
            pekerjaan = random.choice([22,23,24,27])
            rumah = random.choice([29,30,31,32])
        elif pendidikan >= 16 and kelamin[index] == 0:
            pekerjaan = random.choice([22,23,24,26,27])
            rumah = random.choice([29,30,31,32])

        individu = random.choice([34,35,35,35,36,37,38])

        time.sleep(2)
        
        textboxes[0].send_keys(namaDepan[index])
        textboxes[1].send_keys(namaBelakang[index])
        textboxes[2].send_keys(telp[index])

        #usia
        textboxes[3].click()
        time.sleep(2)
        pilihan[usia].click()

        #kelamin
        textboxes[4].click()
        time.sleep(2)
        pilihan[kelamin[index]+7].click()

        #pernikahan
        textboxes[5].click()
        time.sleep(2)
        pilihan[pernikahan].click()

        textboxes[6].click()
        time.sleep(2)
        pilihan[pendidikan].click()

        textboxes[7].click()
        time.sleep(2)
        pilihan[pekerjaan].click()

        textboxes[8].click()
        time.sleep(2)
        pilihan[rumah].click()

        textboxes[9].click()
        time.sleep(2)
        pilihan[individu].click()

        time.sleep(2)

        if essaytemp[0] == 1:
            time.sleep(2)
            s1 = random.choice([6,7])
            radiobuttons[s1].click()
            radiobuttons[8].click()
            textarea[0].send_keys(essays[0][idx1])
            idx1 += 1
            jumlahEssay[0] -= 1
            s1 = random.choice([10,11])
            radiobuttons[s1].click()
            if s1 == 10 :
                banyak = random.randint(2,10)
                textboxes[10].send_keys(banyak)
        else:
            time.sleep(2)
            s1 = random.choice([6,7])
            radiobuttons[s1].click()
            radiobuttons[9].click()
            # textarea[0].send_keys("-")
            s1 = random.choice([10,11])
            radiobuttons[s1].click()
            if s1 == 10 :
                banyak = random.randint(2,10)
                textboxes[10].send_keys(banyak)

        jumlah = random.choice([40,41,42])
        textboxes[11].click()
        time.sleep(2)
        pilihan[jumlah].click()

        p1 = random.choice([12,13])
        p2 = random.choice([14,15])
        p3 = random.choice([16,17,17,17])

        radiobuttons[p1].click()
        radiobuttons[p2].click()
        radiobuttons[p3].click()

        if p3 == 16:
            textboxes[12].click()
            pilihan[random.choice([44,45,46,47])].click()

        time.sleep(2)
        if essaytemp[1] == 1:
            time.sleep(2)
            radiobuttons[19].click()
            textarea[1].send_keys(essays[1][idx2])
            idx2 += 1
            jumlahEssay[1] -= 1
        else:
            time.sleep(2)
            radiobuttons[18].click()

        time.sleep(2)
        if essaytemp[2] == 1:
            time.sleep(2)
            radiobuttons[21].click()
            textarea[2].send_keys(essays[2][idx3])
            idx3 += 1
            jumlahEssay[2] -= 1
        else:
            time.sleep(2)
            radiobuttons[20].click()

        time.sleep(2)
        if essaytemp[3] == 1:
            time.sleep(2)
            radiobuttons[23].click()
            textboxes[13].send_keys(essays[3][idx4])
            idx4 += 1
            jumlahEssay[3] -= 1
        else:
            time.sleep(2)
            radiobuttons[22].click()

        time.sleep(2)
        if essaytemp[4] == 1:
            time.sleep(2)
            radiobuttons[25].click()
            textarea[3].send_keys(essays[4][idx5])
            idx5 += 1
            jumlahEssay[4] -= 1
        else:
            time.sleep(2)
            radiobuttons[24].click()

        radiobuttons[random.choice([26,27])].click()

        time.sleep(2)
        if essaytemp[5] == 1:
            time.sleep(2)
            radiobuttons[random.choice([28,29])].click()
            radiobuttons[31].click()
            textboxes[14].send_keys(essays[5][idx6])
            idx6 += 1
            jumlahEssay[5] -= 1
        else:
            time.sleep(2)
            radiobuttons[28].click()
            radiobuttons[30].click()

        temp = random.randint(1,3)
        organisir = random.sample([0,1,2], temp)

        for i in organisir:
            checkboxes[i].click()

        time.sleep(2)
        if essaytemp[6] == 1:
            time.sleep(2)
            radiobuttons[32].click()
            textarea[4].send_keys(essays[6][idx7])
            idx7 += 1
            jumlahEssay[6] -= 1
        else:
            time.sleep(2)
            radiobuttons[33].click()

        time.sleep(2)
        if essaytemp[7] == 1:
            time.sleep(2)
            radiobuttons[34].click()
            textarea[5].send_keys(essays[7][idx8])
            idx8 += 1
            jumlahEssay[7] -= 1
        else:
            time.sleep(2)
            radiobuttons[35].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        time.sleep(20)
        driver.get("https://www.cognitoforms.com/UnversitasIndonesia/KuesionerTesisSharyneSylvani")

        index+=1
        print("==================")
        print("jumlahEssay  : " + str(jumlahEssay))
        print("")
        print("idx1  : " + str(idx1))
        print("idx2  : " + str(idx2))
        print("idx3  : " + str(idx3))
        print("idx4  : " + str(idx4))
        print("idx5  : " + str(idx5))
        print("idx6  : " + str(idx6))
        print("idx7  : " + str(idx7))
        print("idx8  : " + str(idx8))

        times-=1
        print("")
        print("index  : " + str(index))
        print("")
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