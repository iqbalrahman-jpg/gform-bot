from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import random

link = "https://docs.google.com/forms/d/e/1FAIpQLSeYEY0JhzjshuH1lH214OpO_M7ai3_wM1vomlekiM5AHRPv3Q/viewform"

profil = ["Profile 7", "Profile 8", "Profile 9", "Profile 10", "Profile 11"]

email = [
    "alihasn.01.10@gmail.com",
    "risfebri11@gmail.com",
    "budprasety@gmail.com",
    "aryonugh@gmail.com",
    "nanissa0110@gmail.com",
    "yahnugrah@gmail.com",
    "putriptr0110@gmail.com",
    "nandayundaa1@gmail.com",
    "yudipradan01@gmail.com",
    "mtianur001@gmail.com",

    "byumerta1@gmail.com",
    "Bellandayu01@gmail.com",
    "budsuryant01@gmail.com",
    "nela.mirra@gmail.com",
    "dwa.lingga10@gmail.com",
    "alffiantoro@gmail.com",
    "annicsaa@gmail.com",
    "fataahxdewa@gmail.com",
    "diahcindy03@gmail.com",
    "yulayund1@gmail.com",

    "azzarinrst@gmail.com",
    "fabiannadeo@gmail.com",
    "niaejuliana@gmail.com",
    "bayudwiganara@gmail.com",
    "syifaradifah@gmail.com",
    "aditferdinanda@gmail.com",
    "sitifauziyyahh@gmail.com",
    "reyhanutomowa@gmail.com",
    "salmaarowaya@gmail.com",
    "attakmajid@gmail.com",

    "putrikeancana@gmail.com",
    "rajawardanawan@gmail.com",
    "affifahh7@gmail.com",
    "shakapwijaya@gmail.com",
    "cynnarafisa@gmail.com",
    "monahfnna87@gmail.com",
    "mahendrejaa@gmail.com",
    "fryshta.eka823@gmail.com",
    "yanrasuryad@gmail.com",
    "anggasiregarp@gmail.com",

    "sutisnayun@gmail.com",
    "ayulistyaan@gmail.com",
    "muhh.santosoo@gmail.com",
    "nahychelsee@gmail.com",
    "rudinurbaktii01@gmail.com",
    "raafnii@gmail.com",
    "rcuulii@gmail.com",
    "fadiljaiduni@gmail.com",
    "ariestyadelima@gmail.com",
    "rahannadi1@gmail.com",
]

nama = [
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Mutia Ayu Nur",

    "Bayu Danang Merta",
    "Bellanda Clara Ayunda ",
    "Budi Suryanto",
    "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Yuli Ayunda Dewi",

    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Attaka Majid",

    "Putri Keancana",
    "Raja Putra Wardanawan",
    "Affifah Rahman Nabila",
    "Shaka Kurnia Wijaya",
    "Cynara Nafisah",
    "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
    "Fryshta Eka Nabilla",
    "Yanuar Suryadi",
    "Angga Siregar Putra",

    "Sutisna Ayuni",
    "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Nayla Chelsea Anggita",
    "Putra Rudi Wirawan Nurbakti",
    "Fani Cintya A",
    "Rasya Gibran Sulistyo",
    "M. Fadil Achmad",
    "Delima Ariesta",
    "Rayhan Adi Wicasa",
]

kelamin = [
    0,1,0,0,1,0,1,1,0,1,
    0,1,0,1,0,0,1,0,1,1,
    1,0,1,0,1,0,1,0,1,0,
    1,0,1,0,1,1,0,1,0,0,
    0,1,0,1,0,1,0,0,1,0,
]

soal = [
    6,4,7
]

pertanyaan = [
    "Bagaimana pendapat Anda ketika di dorong untuk menggunakan aplikasi telemedicine terbaru?",
    "Menurut Anda, Bagaimana media sosial dapat mendorong atau mempengaruhi Anda dalam melakukan sesuatu?",
    "Apa faktor yang membuat Anda percaya bahwa layanan telemedicine yang Anda gunakan dapat diandalkan?",
    "Dalam pengalaman Anda, bagaimana perbandingan nilai dan biaya dari layanan aplikasi telemedicine dibandingkan dengan kunjungan langsung ke dokter atau fasilitas kesehatan?",
    "Apa yang memotivasi Anda untuk lebih sering menggunakan layanan telemedicine?",
    "Bisakah Anda menceritakan tentang pengalaman terakhir menggunakan layanan telemedicine dan bagaimana ini memenuhi kebutuhan Anda?",
]

jawaban = [
    [
        "Saya ingin memastikan bahwa aplikasi tersebut dapat menyediakan konsultasi medis dengan dokter yang berpengalaman dan berkualifikasi",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk memantau kemajuan atau perubahan kondisi kesehatan saya dari waktu ke waktu",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat menyediakan layanan konsultasi yang dapat diakses dengan biaya yang terjangkau",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk mengirimkan resep obat langsung ke apotek atau rumah saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki opsi untuk menyediakan layanan konsultasi dengan dokter spesialis dari berbagai bidang",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat menyediakan layanan konsultasi yang ramah pengguna bagi pengguna dengan tingkat literasi digital yang beragam",
        "Saya ingin memastikan bahwa aplikasi tersebut memiliki dukungan pelanggan yang responsif untuk membantu menjawab pertanyaan atau masalah yang mungkin timbul",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk menyediakan informasi tentang risiko penyakit atau langkah-langkah pencegahan yang dapat diambil",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat menyediakan layanan konsultasi dalam berbagai layout, seperti pesan teks, panggilan video, atau panggilan suara",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk mengatur jadwal konsultasi yang fleksibel sesuai dengan waktu luang saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki opsi untuk menyediakan informasi tentang obat-obatan generik atau alternatif yang lebih murah",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki fitur untuk mengingatkan saya tentang janji temu konsultasi atau tindakan medis yang direncanakan",
        "Saya ingin memastikan bahwa aplikasi tersebut memiliki tindakan keamanan yang kuat untuk melindungi records medis sensitif dan informasi pribadi saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk menyediakan layanan konsultasi medis yang ramah anak-anak atau keluarga",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk menyediakan konsultasi medis dalam bahasa yang berbeda sesuai dengan preferensi pengguna",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk memberikan informasi tentang efek samping atau interaksi obat yang mungkin terjadi",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki opsi untuk menyediakan layanan konsultasi dengan ahli terkait kesehatan seperti ahli gizi atau farmasis",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki fitur untuk menyediakan rekomendasi tentang layanan kesehatan atau fasilitas medis yang terletak di dekat saya",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat menyediakan layanan konsultasi yang mudah diakses bagi pengguna dengan keterbatasan mobilitas atau aksesibilitas",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk menyediakan saran atau panduan tentang perawatan kesehatan mandiri atau pencegahan penyakit",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat menyediakan konsultasi medis dengan waktu tunggu yang singkat",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat memberikan solusi yang aman dan terpercaya untuk pertanyaan atau masalah kesehatan yang saya miliki",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk menyediakan informasi tentang ketersediaan dan biaya layanan kesehatan di berbagai fasilitas medis",
        "Saya akan memeriksa apakah aplikasi tersebut memiliki fitur untuk menyediakan panduan atau rekomendasi tentang bagaimana mengelola kondisi kesehatan tertentu di rumah",
        "Saya ingin mengetahui apakah aplikasi tersebut memiliki opsi untuk menyediakan konsultasi medis dengan dokter yang berpengalaman dalam bidang tertentu, seperti penyakit kronis atau manajemen nyeri",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat memberikan solusi untuk mengatasi hambatan dalam mengakses layanan kesehatan tradisional, seperti jarak atau biaya perjalanan",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk menghubungkan saya dengan sumber informasi kesehatan yang tepercaya, seperti artikel ilmiah atau organisasi medis terkemuka",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk mengirimkan hasil tes medis atau riwayat kesehatan saya kepada dokter atau ahli medis lainnya secara aman",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk menyediakan konsultasi medis dalam situasi darurat yang memerlukan tanggapan cepat",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat menyediakan layanan konsultasi dengan dokter yang dapat berkomunikasi dengan saya dalam bahasa yang saya pahami dengan baik",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk memberikan rekomendasi tentang gaya hidup sehat atau perubahan kebiasaan yang dapat meningkatkan kesejahteraan saya",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk menyediakan konsultasi dengan dokter atau ahli medis yang memiliki pemahaman khusus tentang kebutuhan saya sebagai individu dengan kondisi kesehatan tertentu",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk menyediakan informasi tentang ketersediaan atau promosi layanan kesehatan yang tersedia di komunitas saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki opsi untuk menyediakan layanan konsultasi dengan dokter atau spesialis dalam bidang kesehatan tertentu yang telah saya pilih sebelumnya",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki fitur untuk memberikan layanan konsultasi yang ramah pengguna bagi pengguna dengan berbagai tingkat kemampuan teknologi",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat menyediakan layanan konsultasi dengan dokter atau ahli medis yang memiliki pengalaman dan reputasi yang baik dalam praktiknya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk memberikan saran tentang pengelolaan stres atau perawatan kesehatan intellectual",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk menyediakan konsultasi medis dalam berbagai format, seperti panggilan video atau pesan teks",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk menyediakan informasi tentang kebijakan asuransi kesehatan atau cara pembayaran yang dapat saya gunakan",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki opsi untuk menyediakan layanan konsultasi dengan dokter atau ahli medis yang memiliki pemahaman tentang kebutuhan kesehatan keluarga saya secara keseluruhan",
        "Saya ingin memastikan bahwa aplikasi tersebut memiliki fitur keamanan yang memadai untuk melindungi informasi medis sensitif saya dari akses yang tidak sah",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki fitur untuk menyediakan panduan atau saran tentang bagaimana menghadapi kondisi kesehatan tertentu di masa darurat",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk memberikan informasi tentang tempat-tempat pelayanan kesehatan terdekat yang dapat saya kunjungi jika diperlukan",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki opsi untuk menyediakan konsultasi dengan dokter atau ahli medis yang memiliki spesialisasi dalam bidang medis tertentu yang mungkin relevan dengan kondisi kesehatan saya",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki fitur untuk menyediakan layanan konsultasi medis dengan biaya yang terjangkau atau bahkan free of charge",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk memberikan informasi tentang efek samping atau risiko yang terkait dengan penggunaan obat-obatan tertentu",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat menyediakan layanan konsultasi medis yang ramah dan terpercaya bagi pengguna dari berbagai latar belakang atau kepercayaan agama",
        "Saya akan mengevaluasi apakah aplikasi tersebut memiliki fitur untuk memberikan rekomendasi tentang bagaimana mengelola kondisi kesehatan kronis atau jangka panjang secara efektif",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki opsi untuk menyediakan layanan konsultasi dengan dokter atau ahli medis yang dapat berkomunikasi dengan saya dalam bahasa yang saya inginkan",
        "Saya ingin memeriksa apakah aplikasi telemedicine tersebut memiliki fitur untuk menyediakan informasi tentang penyakit menular atau wabah kesehatan masyarakat yang sedang berlangsung di daerah saya",
    ],
    [
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap nilai sosial atau popularitas mereka dengan menyajikan comments atau interaksi dari pengguna lain",
        "Dengan menyajikan konten-konten yang menyoroti kegiatan olahraga atau gaya hidup aktif, media sosial dapat mempengaruhi kebiasaan olahraga atau aktivitas fisik seseorang",
        "Melalui konten-konten yang menginspirasi atau memotivasi, media sosial dapat mempengaruhi sikap atau motivasi seseorang dalam mencapai tujuan mereka",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap kesehatan gigi dan mulut dengan menyajikan informasi tentang perawatan gigi dari pengguna lain",
        "Dengan menyajikan informasi tentang tren seni atau kreativitas, media sosial dapat mempengaruhi minat atau partisipasi seseorang dalam aktivitas seni atau kerajinan",
        "Media sosial dapat mempengaruhi keputusan seseorang dalam memilih tempat tinggal atau destinasi liburan dengan menyajikan informasi tentang tempat-tempat yang populer atau menarik",
        "Melalui penyediaan platform untuk berbagi pengetahuan atau keterampilan, media sosial dapat mempengaruhi pertumbuhan atau perkembangan pribadi seseorang",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang dalam merawat tanaman atau berkebun dengan menyajikan suggestions atau saran dari pengguna lain",
        "Dengan menyajikan informasi tentang tren fotografi atau teknik pengambilan gambar, media sosial dapat mempengaruhi minat atau partisipasi seseorang dalam fotografi",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap keberhasilan atau prestasi mereka sendiri dengan menyajikan perbandingan sosial",
        "Melalui fitur-fitur yang memungkinkan berbagi cerita atau pengalaman, media sosial dapat mempengaruhi cara seseorang memproses atau mengartikan pengalaman hidup mereka sendiri",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap keamanan cyber dengan menyajikan informasi atau saran tentang praktik-praktik keamanan online",
        "Dengan menyajikan informasi tentang tren travel running a blog atau vlog, media sosial dapat mempengaruhi minat seseorang dalam menciptakan konten atau berbagi pengalaman perjalanan",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap hubungan antar pribadi dengan menyajikan contoh-contoh dari interaksi sosial yang positif",
        "Melalui penyediaan platform untuk berbagi ide atau inovasi, media sosial dapat mempengaruhi kontribusi atau partisipasi seseorang dalam pengembangan teknologi atau bisnis",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang dalam menjalani gaya hidup yang berkelanjutan atau ramah lingkungan dengan menyajikan informasi tentang praktik-praktik hijau",
        "Dengan menyajikan informasi tentang tren gaming atau esports, media sosial dapat mempengaruhi minat atau partisipasi seseorang dalam industri sport",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap keberhasilan karir atau profesionalisme mereka sendiri dengan menyajikan contoh-contoh dari kesuksesan di bidang tersebut",
        "Melalui penyediaan platform untuk berbagi pointers atau strategi pengembangan karir, media sosial dapat mempengaruhi upaya seseorang dalam mencapai tujuan karir mereka",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap keberagaman budaya atau multikulturalisme dengan menyajikan informasi tentang budaya-budaya yang berbeda",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap citra diri mereka sendiri dengan menyajikan gambaran dari kehidupan orang lain",
        "Dengan menyajikan informasi tentang tren parenting atau pendidikan anak, media sosial dapat mempengaruhi cara seseorang merawat atau mendidik anak-anak mereka",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap penyalahgunaan zat atau alkohol dengan menyajikan informasi tentang risiko dan dampak negatifnya",
        "Melalui fitur-fitur yang memungkinkan kolaborasi atau proyek bersama, media sosial dapat mempengaruhi kerjasama atau partisipasi seseorang dalam proyek-proyek komunitas",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap keadilan atau hukum dengan menyajikan cerita atau laporan tentang keadilan yang diterapkan atau dilanggar",
        "Dengan menyajikan informasi tentang tren teknologi atau system terbaru, media sosial dapat mempengaruhi minat atau kebutuhan seseorang dalam mengupgrade perangkat mereka",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap kesehatan reproduksi dengan menyajikan informasi tentang kesehatan seksual dan reproduksi",
        "Melalui penyediaan platform untuk menyuarakan aspirasi atau keinginan, media sosial dapat mempengaruhi upaya seseorang dalam meraih impian atau tujuan hidup mereka",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap peran gender dalam masyarakat dengan menyajikan contoh-contoh dari pembagian peran tradisional atau non-tradisional",
        "Dengan menyajikan informasi tentang tren kuliner atau resep masakan, media sosial dapat mempengaruhi minat atau eksplorasi seseorang dalam memasak dan mencicipi makanan baru",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap kesehatan lingkungan dengan menyajikan informasi tentang praktik-praktik ramah lingkungan dan penanganan sampah",
        "Melalui fitur-fitur yang memungkinkan kolaborasi atau pertukaran pengetahuan, media sosial dapat mempengaruhi pertumbuhan atau pengembangan keterampilan seseorang",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap citra tubuh mereka sendiri dengan menyajikan standar kecantikan yang tidak realistis",
        "Dengan menyajikan informasi tentang tren musik atau acara konser, media sosial dapat mempengaruhi minat atau partisipasi seseorang dalam industri musik dan hiburan",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap hak-hak sipil atau hak asasi manusia dengan menyajikan informasi tentang perjuangan atau pencapaian di bidang ini",
        "Melalui fitur-fitur yang memungkinkan berbagi pengalaman perjalanan, media sosial dapat mempengaruhi keinginan seseorang untuk menjelajahi tempat-tempat baru",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap kualitas hidup dengan menyajikan cerita atau testimoni tentang kebahagiaan atau kesuksesan",
        "Dengan menyajikan informasi tentang tren fashion atau gaya, media sosial dapat mempengaruhi preferensi atau gaya berpakaian seseorang",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap keamanan cyber dengan menyajikan informasi tentang ancaman dan cara-cara melindungi diri on-line",
        "Melalui penyediaan platform untuk berbagi cerita pengalaman penggunaan produk, media sosial dapat mempengaruhi kepercayaan atau minat seseorang terhadap merek atau produk tertentu",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap aktivisme atau partisipasi dalam kampanye politik dengan menyajikan informasi tentang gerakan sosial atau politik",
        "Dengan menyajikan informasi tentang tren literatur atau rekomendasi buku, media sosial dapat mempengaruhi minat seseorang dalam membaca dan menggali pengetahuan baru",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap keamanan pangan dengan menyajikan informasi tentang label makanan dan keamanan bahan makanan",
        "Melalui fitur-fitur yang memungkinkan diskusi atau discussion board on-line, media sosial dapat mempengaruhi partisipasi seseorang dalam debat dan pertukaran ide",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap keberlanjutan dengan menyajikan informasi tentang praktik-praktik ramah lingkungan dan perubahan iklim",
        "Dengan menyajikan informasi tentang tren teknologi atau aplikasi terbaru, media sosial dapat mempengaruhi minat seseorang dalam mengadopsi teknologi baru",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap kualitas pendidikan dengan menyajikan informasi tentang institusi pendidikan dan testimoni pengalaman siswa",
        "Melalui konten-konten yang menyoroti pentingnya kesehatan intellectual, media sosial dapat mempengaruhi stigma dan kesadaran tentang kesehatan jiwa",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap pengelolaan keuangan pribadi dengan menyajikan informasi tentang perencanaan keuangan dan investasi",
        "Dengan menyajikan informasi tentang tren kesehatan dan kebugaran, media sosial dapat mempengaruhi minat seseorang dalam mengadopsi gaya hidup aktif dan sehat",
    ],
    [
        "Dukungan untuk konsultasi medis bagi individu dengan kondisi kesehatan mental atau kecanduan",
        "Integrasi dengan layanan telemedicine hewan peliharaan untuk konsultasi medis hewan",
        "Layanan konsultasi medis untuk perawatan palliatif atau cease-of-life care",
        "Dukungan untuk konsultasi medis bagi individu dengan gangguan tidur atau gangguan neurologis lainnya",
        "Integrasi dengan platform telemedicine untuk konsultasi medis selama perjalanan atau di luar negeri",
        "Kemampuan untuk menyediakan konsultasi medis untuk perawatan alternatif atau holistik",
        "Dukungan untuk konsultasi medis bagi individu dengan gangguan kesehatan kronis yang kompleks",
        "Integrasi dengan sistem pemberitahuan darurat dan pemanggilan darurat untuk situasi mendesak",
        "Layanan konsultasi medis untuk pengguna yang membutuhkan bantuan dalam mengelola stres atau kecemasan",
        "Dukungan untuk konsultasi medis bagi pengguna yang tinggal di daerah terpencil atau pedesaan",
        "Integrasi dengan sistem manajemen praktik medis untuk pengelolaan jadwal dan administrasi",
        "Kemampuan untuk memberikan konsultasi medis bagi pasien yang sedang melakukan perawatan kanker",
        "Dukungan untuk konsultasi medis bagi pengguna dengan kebutuhan kesehatan khusus atau langka",
        "Integrasi dengan platform telemedicine untuk memfasilitasi konsultasi medis di tempat kerja",
        "Layanan konsultasi medis bagi pasien dengan riwayat penyakit atau kondisi medis yang kompleks",
        "Dukungan untuk konsultasi medis bagi pengguna dengan keterbatasan mobilitas atau penggunaan kendaraan",
        "Integrasi dengan sistem manajemen informasi rumah sakit untuk berbagi statistics medis",
        "Kemampuan untuk menyediakan konsultasi medis bagi pasien yang membutuhkan perawatan jangka panjang",
        "Dukungan untuk konsultasi medis bagi pengguna dengan gangguan perkembangan atau kebutuhan khusus",
        "Integrasi dengan platform telemedicine untuk memfasilitasi konsultasi medis dalam skenario darurat atau bencana alam",
        "Dukungan untuk konsultasi medis bagi individu dengan kondisi kesehatan ginekologi atau obstetri",
        "Integrasi dengan sistem manajemen resep elektronik untuk pengiriman resep yang cepat dan tepat",
        "Layanan konsultasi medis bagi pasien dengan gangguan pencernaan atau masalah gastroenterologi",
        "Dukungan untuk konsultasi medis bagi pengguna dengan alergi atau sensitivitas makanan",
        "Integrasi dengan teknologi pembayaran virtual untuk pembayaran layanan telemedicine secara mudah",
        "Kemampuan untuk menyediakan konsultasi medis bagi pengguna yang berada di fasilitas perawatan jangka panjang",
        "Dukungan untuk konsultasi medis bagi individu dengan gangguan sistem endokrin atau hormonal",
        "Integrasi dengan sistem manajemen penyakit kronis untuk pemantauan dan perawatan yang terkoordinasi",
        "Layanan konsultasi medis bagi pasien dengan masalah dermatologi atau penyakit kulit",
        "Dukungan untuk konsultasi medis bagi pengguna dengan kondisi alat pernapasan atau paru-paru",
        "Integrasi dengan sistem manajemen facts kesehatan pribadi untuk pemantauan diri yang mandiri",
        "Kemampuan untuk menyediakan konsultasi medis bagi pasien yang membutuhkan perawatan rehabilitasi atau fisioterapi",
        "Dukungan untuk konsultasi medis bagi individu dengan gangguan otot atau penyakit neuromuskuler",
        "Integrasi dengan teknologi teledentistry untuk konsultasi dan perawatan gigi jarak jauh",
        "Layanan konsultasi medis bagi pasien dengan gangguan pendengaran atau gangguan otologi",
        "Dukungan untuk konsultasi medis bagi pengguna dengan gangguan neurologis perifer atau sentral",
        "Integrasi dengan platform telemedicine untuk memfasilitasi konsultasi medis selama kehamilan atau persalinan",
        "Kemampuan untuk menyediakan konsultasi medis bagi pasien yang membutuhkan perawatan paliatif atau hospis",
        "Dukungan untuk konsultasi medis bagi individu dengan masalah kesehatan urologi atau sistem kemih",
        "Integrasi dengan sistem manajemen perawatan terintegrasi untuk pemantauan pasien secara holistik",
        "Dukungan untuk konsultasi medis bagi pengguna dengan kondisi kesehatan yang membutuhkan perawatan dalam perjalanan",
        "Integrasi dengan sistem manajemen perawatan anak untuk konsultasi medis anak-anak",
        "Layanan konsultasi medis bagi pasien dengan gangguan pertumbuhan atau perkembangan",
        "Dukungan untuk konsultasi medis bagi individu dengan gangguan sistem kardiovaskular",
        "Integrasi dengan teknologi pengingat pengobatan untuk membantu pasien mematuhi rencana perawatan",
        "Kemampuan untuk menyediakan konsultasi medis bagi pengguna dengan gangguan kejiwaan atau psikiatri",
        "Dukungan untuk konsultasi medis bagi pasien dengan kondisi kesehatan yang memerlukan perawatan intensif",
        "Integrasi dengan sistem manajemen informasi radiologi untuk interpretasi gambar medis jarak jauh",
        "Layanan konsultasi medis bagi pasien dengan gangguan kecemasan atau stres traumatis",
        "Dukungan untuk konsultasi medis bagi individu dengan masalah kesehatan yang berkaitan dengan lingkungan atau tempat kerja",
    ],
    [
        "Telemedicine memungkinkan perusahaan untuk memberikan pemantauan kesehatan kepada karyawan tanpa harus mengganggu produktivitas mereka dengan perjalanan ke dokter.",
        "Menggunakan telemedicine mengurangi biaya tambahan untuk makanan di luar yang mungkin diperlukan selama perjalanan ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan pada waktu malam tanpa harus pergi ke pusat kesehatan darurat atau menunggu hingga keesokan harinya.",
        "Telemedicine mengurangi risiko kehilangan waktu karena menunggu di ruang tunggu dokter atau antrian di apotek.",
        "Telemedicine memungkinkan pemantauan kesehatan bagi pasien dengan gangguan neurologis tanpa harus keluar dari rumah mereka.",
        "Menggunakan telemedicine mengurangi biaya perjalanan tambahan yang mungkin diperlukan untuk kegiatan sosial setelah kunjungan ke dokter.",
        "Telemedicine memungkinkan pemantauan kesehatan di masa kritis seperti pandemi, ketika pergi ke fasilitas kesehatan dapat meningkatkan risiko penularan penyakit.",
        "Telemedicine mengurangi risiko keterlambatan pemulihan karena kesulitan akses ke perawatan medis yang tepat pada waktunya.",
        "Telemedicine memfasilitasi pemantauan kesehatan di lingkungan kerja yang berbahaya tanpa harus meninggalkan lokasi kerja.",
        "Menggunakan telemedicine mengurangi biaya akomodasi tambahan yang mungkin diperlukan untuk anak selama perjalanan ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan bagi orang dengan kondisi medis kompleks tanpa harus berpindah-pindah dari satu spesialis ke spesialis lainnya.",
        "Telemedicine mengurangi risiko kecelakaan yang mungkin terjadi selama perjalanan ke dan dari fasilitas kesehatan, terutama di kondisi cuaca buruk.",
        "Telemedicine memfasilitasi pemantauan kesehatan mental pada masa krisis seperti bencana alam atau kejadian traumatis.",
        "Menggunakan telemedicine mengurangi biaya perawatan anak yang mungkin diperlukan selama perjalanan ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan di lingkungan yang kondusif, seperti rumah atau tempat kerja, tanpa harus pergi ke tempat kesehatan yang ramai.",
        "Telemedicine mengurangi risiko terluka akibat kecelakaan selama perjalanan ke fasilitas kesehatan, terutama bagi mereka yang berada di lingkungan yang tidak dikenal.",
        "Telemedicine memungkinkan pemantauan kesehatan bagi orang dengan kondisi menular tanpa meningkatkan risiko penularan kepada orang lain.",
        "Menggunakan telemedicine mengurangi biaya tambahan untuk transportasi yang mungkin diperlukan untuk pergi ke fasilitas kesehatan.",
        "Telemedicine memfasilitasi pemantauan kesehatan di tempat kerja yang terpencil tanpa harus mengganggu produktivitas atau mengeluarkan biaya untuk transportasi.",
        "Telemedicine mengurangi risiko penularan penyakit yang mungkin terjadi melalui interaksi manusia di fasilitas kesehatan.",
        "Telemedicine memfasilitasi pemantauan kesehatan di tempat kerja tanpa mengganggu produktivitas karyawan.",
        "Menggunakan telemedicine mengurangi biaya bantuan transportasi yang mungkin diperlukan untuk pergi ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan di lingkungan yang aman, seperti rumah atau tempat kerja, tanpa perlu keluar.",
        "Telemedicine mengurangi risiko terpapar penyakit di lingkungan fasilitas kesehatan yang ramai.",
        "Telemedicine memfasilitasi pemantauan kesehatan di lingkungan yang terkontrol, seperti rumah atau kantor, tanpa perlu berpindah tempat.",
        "Menggunakan telemedicine mengurangi waktu yang dihabiskan untuk perjalanan ke dan dari fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan di daerah terpencil di mana akses ke fasilitas kesehatan mungkin terbatas.",
        "Telemedicine mengurangi risiko penularan penyakit zoonotik yang mungkin terjadi selama perjalanan ke fasilitas kesehatan hewan.",
        "Telemedicine memfasilitasi pemantauan kesehatan selama pandemi seperti COVID-19 tanpa meningkatkan risiko penularan penyakit.",
        "Menggunakan telemedicine mengurangi biaya pembelian obat di apotek yang mungkin diperlukan setelah kunjungan ke dokter.",
        "Telemedicine memfasilitasi pemantauan kesehatan di masa krisis kesehatan tanpa meningkatkan risiko penularan penyakit.",
        "Telemedicine mengurangi risiko kecelakaan yang mungkin terjadi selama perjalanan ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan di tempat kerja yang jauh tanpa harus berpergian jauh.",
        "Telemedicine mengurangi risiko penularan infeksi di tempat kerja dengan memungkinkan karyawan untuk tetap bekerja dari rumah.",
        "Telemedicine memfasilitasi pemantauan kesehatan di rumah sakit yang ramai tanpa perlu berpindah-pindah dari satu ruang ke ruang lainnya.",
        "Menggunakan telemedicine mengurangi biaya pengeluaran harian yang mungkin ditanggung oleh pasien selama kunjungan ke fasilitas kesehatan.",
        "Telemedicine memfasilitasi pemantauan kesehatan pada malam hari tanpa harus menunggu hingga keesokan harinya untuk mendapatkan perawatan.",
        "Telemedicine mengurangi risiko terluka yang mungkin terjadi selama perjalanan ke fasilitas kesehatan.",
        "Telemedicine memfasilitasi pemantauan kesehatan di wilayah rawan bencana tanpa meningkatkan risiko keamanan atau kesehatan.",
        "Telemedicine memfasilitasi pemantauan kesehatan di tempat kerja yang tidak aman tanpa harus mempertaruhkan keselamatan karyawan.",
        "Telemedicine mengurangi risiko penularan penyakit yang mungkin terjadi di lingkungan fasilitas kesehatan atau transportasi umum.",
        "Telemedicine memfasilitasi pemantauan kesehatan selama aktivitas luar ruangan tanpa harus meninggalkan tempat tersebut.",
        "Menggunakan telemedicine mengurangi biaya perjalanan yang mungkin diperlukan untuk kunjungan darurat ke fasilitas kesehatan.",
        "Telemedicine memfasilitasi pemantauan kesehatan di lokasi terpencil yang tidak aman tanpa mengorbankan keselamatan pasien atau tenaga medis.",
        "Telemedicine mengurangi risiko terinfeksi penyakit lain yang mungkin terjadi selama perjalanan atau kunjungan ke rumah sakit atau fasilitas kesehatan lainnya.",
        "Telemedicine memfasilitasi pemantauan kesehatan di masa darurat medis seperti bencana alam atau situasi krisis lainnya.",
        "Menggunakan telemedicine mengurangi biaya pembatalan janji dokter karena faktor eksternal seperti cuaca buruk atau masalah transportasi.",
        "Telemedicine memfasilitasi pemantauan kesehatan selama aktivitas perjalanan tanpa harus meninggalkan kendaraan atau tempat menginap.",
        "Telemedicine mengurangi risiko terinfeksi penyakit di tempat umum seperti ruang tunggu dokter atau apotek.",
        "Telemedicine memfasilitasi pemantauan kesehatan di lingkungan yang tidak bersih tanpa meningkatkan risiko infeksi atau penyakit.",
    ],
    [
        "Mendapatkan saran tentang manajemen berat badan setelah kehamilan: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen berat badan pasca kehamilan",
        "Mengatasi gangguan pernapasan saat tidur: Telemedicine memberikan akses ke konsultasi tentang gangguan pernapasan saat tidur seperti sleep apnea atau hipopnea",
        "Mendapatkan rekomendasi tentang manajemen stres kerja: Telemedicine memungkinkan konsultasi untuk manajemen stres yang disebabkan oleh tekanan pekerjaan atau lingkungan kerja",
        "Mengatasi kecemasan prapernikahan: Telemedicine memberikan akses ke konsultasi untuk mengelola kecemasan atau stres yang terkait dengan pernikahan atau perubahan hidup besar lainnya",
        "Mendapatkan bantuan untuk manajemen trauma: Telemedicine dapat digunakan untuk mendapatkan dukungan dan bantuan dalam mengatasi trauma atau kejadian yang menyakitkan secara emosional",
        "Mendapatkan konsultasi tentang manajemen migrain: Telemedicine memberikan akses ke konsultasi untuk pengelolaan migrain dan penanganan serangan migrain",
        "Mendapatkan dukungan untuk perawatan kanker: Telemedicine dapat digunakan untuk mendapatkan dukungan, saran, dan informasi tentang perawatan kanker dan manajemen efek samping",
        "Mengatasi masalah pencernaan pada bayi: Telemedicine memberikan akses ke konsultasi untuk masalah pencernaan seperti kolik, konstipasi, atau masalah makan pada bayi",
        "Mendapatkan panduan tentang manajemen gangguan makan: Telemedicine dapat digunakan untuk mendapatkan bantuan dan saran tentang manajemen gangguan makan seperti anoreksia atau bulimia",
        "Mendapatkan konsultasi tentang manajemen kecanduan: Telemedicine memberikan akses ke konsultasi untuk manajemen kecanduan seperti alkohol, narkoba, atau perjudian",
        "Mendapatkan dukungan untuk perawatan cease-of-existence: Telemedicine dapat digunakan untuk mendapatkan dukungan, saran, dan perawatan bagi mereka yang menghadapi akhir hidup atau kondisi terminal",
        "Mengatasi masalah tidur pada anak-anak: Telemedicine memberikan akses ke konsultasi untuk masalah tidur seperti susah tidur atau mimpi buruk pada anak-anak",
        "Mendapatkan konsultasi tentang manajemen alergi makanan: Telemedicine dapat digunakan untuk mendapatkan bantuan dan saran tentang manajemen alergi makanan pada anak-anak atau orang dewasa",
        "Mendapatkan panduan tentang manajemen kehamilan: Telemedicine memberikan akses ke konsultasi dan panduan tentang manajemen kehamilan, perawatan prenatal, dan persiapan persalinan",
        "Mendapatkan dukungan untuk manajemen gangguan kepribadian: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen gangguan kepribadian seperti bipolar atau borderline personality disease",
        "Mendapatkan konsultasi tentang manajemen nyeri haid: Telemedicine memberikan akses ke konsultasi untuk manajemen nyeri haid atau gangguan menstruasi lainnya",
        "Mendapatkan saran tentang manajemen kesehatan mental selama pandemi: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang menjaga kesehatan mental selama masa pandemi",
        "Mendapatkan bantuan untuk manajemen penyakit autoimun: Telemedicine memberikan akses ke konsultasi untuk manajemen penyakit autoimun seperti lupus, rheumatoid arthritis, atau more than one sclerosis",
        "Mendapatkan konsultasi tentang manajemen masalah seksual: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen masalah seksual seperti disfungsi ereksi, disfungsi seksual wanita, atau ketidaknyamanan selama hubungan seksual",
        "Mendapatkan panduan tentang manajemen gangguan perhatian dan hiperaktivitas: Telemedicine memberikan akses ke konsultasi untuk manajemen ADHD (attention Deficit Hyperactivity disease) atau gangguan perhatian dan hiperaktivitas pada anak-anak atau orang dewasa",
        "Mendapatkan konsultasi tentang manajemen kelelahan kronis: Telemedicine memberikan akses ke konsultasi untuk manajemen kelelahan yang berkelanjutan dan kronis",
        "Mendapatkan bantuan untuk manajemen penyakit kulit: Telemedicine dapat digunakan untuk mendapatkan konsultasi dan perawatan untuk masalah kulit seperti psoriasis, dermatitis, atau eksim",
        "Mendapatkan panduan tentang manajemen nyeri punggung: Telemedicine memberikan akses ke konsultasi untuk manajemen nyeri punggung akut atau kronis",
        "Mendapatkan saran tentang manajemen perubahan hormon selama menopause: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen gejala menopause seperti warm flashes, gangguan tidur, atau perubahan suasana hati",
        "Mendapatkan bantuan untuk manajemen gangguan kognitif: Telemedicine memberikan akses ke konsultasi untuk manajemen gangguan kognitif seperti demensia atau gangguan kognitif ringan",
        "Mendapatkan panduan tentang manajemen penyakit ginjal: Telemedicine dapat digunakan untuk mendapatkan konsultasi dan perawatan untuk masalah ginjal seperti batu ginjal, infeksi ginjal, atau penyakit ginjal kronis",
        "Mendapatkan konsultasi tentang manajemen penyakit hati: Telemedicine memberikan akses ke konsultasi untuk manajemen penyakit hati seperti hepatitis, sirosis, atau masalah hati lainnya",
        "Mendapatkan dukungan untuk manajemen gangguan penglihatan: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen gangguan penglihatan seperti rabun jauh, rabun dekat, atau mata kering",
        "Mendapatkan panduan tentang manajemen penyakit autoimun: Telemedicine memberikan akses ke konsultasi untuk manajemen penyakit autoimun seperti lupus, rheumatoid arthritis, atau multiple sclerosis",
        "Mendapatkan konsultasi tentang manajemen gangguan tidur pada anak-anak: Telemedicine dapat digunakan untuk mendapatkan konsultasi dan perawatan untuk gangguan tidur seperti insomnia, sleep apnea, atau gangguan perilaku selama tidur pada anak-anak",
        "Mendapatkan bantuan untuk manajemen gangguan pendengaran: Telemedicine memberikan akses ke konsultasi dan dukungan untuk manajemen gangguan pendengaran seperti tinnitus, gangguan pendengaran sensorineural, atau gangguan pendengaran pada anak-anak",
        "Mendapatkan panduan tentang manajemen gangguan neuromuskular: Telemedicine dapat digunakan untuk mendapatkan panduan dan dukungan untuk manajemen gangguan neuromuskular seperti ALS (amyotrophic lateral sclerosis), muscular dystrophy, atau neuropati",
        "Mendapatkan konsultasi tentang manajemen gangguan sistem saraf: Telemedicine memberikan akses ke konsultasi untuk manajemen gangguan sistem saraf seperti migrain, epilepsi, atau penyakit Parkinson",
        "Mendapatkan dukungan untuk manajemen gangguan pernapasan pada bayi: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen gangguan pernapasan seperti bronkiolitis, asma, atau gangguan pernapasan obstruktif pada bayi",
        "Mendapatkan panduan tentang manajemen gangguan pendengaran pada anak-anak: Telemedicine memberikan akses ke panduan dan saran tentang manajemen gangguan pendengaran seperti otitis media, infeksi telinga, atau gangguan pendengaran sensorineural pada anak-anak",
        "Mendapatkan konsultasi tentang manajemen gangguan kanker pada anak-anak: Telemedicine dapat digunakan untuk mendapatkan konsultasi dan dukungan untuk manajemen gangguan kanker pada anak-anak seperti leukemia, tumor otak, atau limfoma",
        "Mendapatkan bantuan untuk manajemen penyakit paru-paru: Telemedicine memberikan akses ke konsultasi dan perawatan untuk penyakit paru-paru seperti asma, COPD (persistent obstructive pulmonary sickness), atau pneumonia",
        "Mendapatkan panduan tentang manajemen masalah nutrisi pada bayi: Telemedicine dapat digunakan untuk mendapatkan panduan dan saran tentang manajemen masalah nutrisi pada bayi seperti intoleransi makanan, alergi susu sapi, atau kesulitan makan",
        "Mendapatkan konsultasi tentang manajemen gangguan sistem pencernaan pada anak-anak: Telemedicine memberikan akses ke konsultasi untuk manajemen gangguan sistem pencernaan seperti gastroenteritis, konstipasi, atau sindrom iritasi usus pada anak-anak",
        "Mendapatkan dukungan untuk manajemen gangguan neurologis pada bayi: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen gangguan neurologis seperti cerebral palsy, autisme, atau gangguan perkembangan pada bayi",
        "Mendapatkan konsultasi tentang manajemen gangguan kesehatan intellectual pada remaja: Telemedicine memberikan akses ke konsultasi dan dukungan untuk manajemen gangguan kesehatan intellectual seperti depresi, kecemasan, atau gangguan makan pada remaja",
        "Mendapatkan bantuan untuk manajemen masalah pernapasan pada bayi prematur: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen masalah pernapasan pada bayi prematur seperti sindrom gangguan pernapasan atau penyakit paru-paru kronis pada bayi",
        "Mendapatkan panduan tentang manajemen penyakit ginjal pada anak-anak: Telemedicine memberikan akses ke panduan dan saran tentang manajemen penyakit ginjal pada anak-anak seperti penyakit ginjal polikistik, glomerulonefritis, atau penyakit ginjal bawaan",
        "Mendapatkan konsultasi tentang manajemen penyakit hati pada anak-anak: Telemedicine dapat digunakan untuk mendapatkan konsultasi dan dukungan untuk manajemen penyakit hati pada anak-anak seperti hepatitis, sirosis, atau penyakit hati bawaan",
        "Mendapatkan bantuan untuk manajemen gangguan pertumbuhan pada anak-anak: Telemedicine memberikan akses ke konsultasi dan dukungan untuk manajemen gangguan pertumbuhan pada anak-anak seperti keterlambatan pertumbuhan, kegemukan, atau kelainan hormon pertumbuhan",
        "Mendapatkan panduan tentang manajemen gangguan pernapasan pada anak-anak dengan kebutuhan khusus: Telemedicine dapat digunakan untuk mendapatkan panduan dan saran tentang manajemen gangguan pernapasan pada anak-anak dengan kebutuhan khusus seperti autisme, cerebral palsy, atau Down syndrome",
        "Mendapatkan konsultasi tentang manajemen gangguan pendengaran pada remaja: Telemedicine memberikan akses ke konsultasi dan dukungan untuk manajemen gangguan pendengaran pada remaja seperti otitis media, tinnitus, atau gangguan pendengaran sensorineural",
        "Mendapatkan bantuan untuk manajemen gangguan tulang dan sendi pada anak-anak: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang manajemen gangguan tulang dan sendi pada anak-anak seperti arthritis, osteogenesis imperfecta, atau kelainan pembentukan tulang",
        "Mendapatkan panduan tentang manajemen gangguan kardiovaskular pada anak-anak: Telemedicine memberikan akses ke panduan dan saran tentang manajemen gangguan kardiovaskular pada anak-anak seperti kelainan jantung bawaan, hipertensi, atau penyakit vaskular perifer",
        "Mendapatkan konsultasi tentang manajemen gangguan pencernaan pada remaja: Telemedicine dapat digunakan untuk mendapatkan konsultasi dan dukungan untuk manajemen gangguan pencernaan pada remaja seperti penyakit Crohn, sindrom iritasi usus, atau gastritis",
    ],
    [
        "Telemedicine telah membantu saya mengatasi hambatan akses ke perawatan medis yang seringkali terjadi karena lokasi geografis atau mobilitas terbatas",
        "Saya merasa lebih terpenuhi dengan layanan telemedicine karena saya dapat memilih dokter yang sesuai dengan preferensi dan kebutuhan kesehatan saya",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih bertanggung jawab dalam mengelola kesehatan saya sendiri",
        "Saya merasa lebih nyaman berbicara tentang masalah kesehatan saya melalui telemedicine karena saya bisa melakukannya dari kenyamanan rumah saya sendiri",
        "Telemedicine memungkinkan saya untuk memprioritaskan perawatan kesehatan saya tanpa harus mengorbankan banyak waktu atau uang",
        "Penggunaan telemedicine telah mengurangi kecemasan saya terkait perawatan medis karena saya bisa mengakses bantuan dengan cepat dan mudah",
        "Saya merasa lebih didukung dalam mengatasi masalah kesehatan saya melalui telemedicine karena saya dapat menghubungi dokter dengan mudah setiap saat",
        "Telemedicine memungkinkan saya untuk mengakses layanan kesehatan yang berkualitas tanpa harus meninggalkan pekerjaan atau tanggung jawab lainnya",
        "Saya merasa lebih terbantu dalam mengatasi masalah kesehatan sehari-hari melalui konsultasi telemedicine yang cepat dan mudah",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih dekat dengan dokter saya karena kami dapat berkomunikasi secara rutin",
        "Saya merasa lebih termotivasi untuk mengambil langkah-langkah proaktif dalam menjaga kesehatan saya setelah menggunakan telemedicine",
        "Telemedicine memungkinkan saya untuk tetap terhubung dengan perawatan medis berkualitas meskipun saya tinggal di daerah yang terpencil atau terpencil",
        "Penggunaan telemedicine telah memberikan saya akses yang lebih baik ke sumber daya kesehatan dan informasi kesehatan secara on line",
        "Saya merasa lebih terbantu dalam memahami kondisi kesehatan saya dan rencana perawatan yang direkomendasikan melalui telemedicine",
        "Telemedicine membantu saya merasa lebih terbantu dalam mengatasi stres dan kecemasan terkait kesehatan dengan memberikan akses cepat ke perawatan",
        "Saya merasa lebih puas dengan pengalaman konsultasi telemedicine daripada kunjungan langsung ke klinik karena kenyamanan dan fleksibilitasnya",
        "Telemedicine memungkinkan saya untuk mengatur jadwal konsultasi sesuai dengan kebutuhan dan kenyamanan saya sendiri",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih mandiri dalam mengelola kesehatan saya sendiri",
        "Saya merasa lebih terjamin dengan kualitas perawatan medis yang saya terima melalui telemedicine karena saya bisa memilih dokter yang terpercaya",
        "Telemedicine telah meningkatkan kepercayaan diri saya dalam mengambil keputusan tentang kesehatan saya sendiri karena saya bisa mengakses informasi dan saran medis dengan mudah",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih terlibat dalam proses perawatan kesehatan saya sendiri",
        "Saya merasa lebih tenang dan terjamin dengan kualitas perawatan medis yang saya terima melalui telemedicine karena dokter saya memberikan perhatian penuh pada kebutuhan kesehatan saya",
        "Telemedicine memungkinkan saya untuk memantau kondisi kesehatan saya secara teratur tanpa harus meninggalkan rumah atau kantor",
        "Saya merasa lebih puas dengan pengalaman konsultasi telemedicine daripada kunjungan langsung ke klinik karena kenyamanan dan fleksibilitasnya",
        "Penggunaan telemedicine telah meningkatkan kepatuhan saya terhadap rencana perawatan medis saya karena akses yang lebih mudah dan nyaman",
        "Telemedicine memungkinkan saya untuk mengakses layanan kesehatan yang berkualitas tanpa harus mengorbankan banyak waktu atau uang",
        "Saya merasa lebih didukung dalam mengatasi masalah kesehatan saya melalui telemedicine karena saya dapat menghubungi dokter dengan mudah setiap saat",
        "Telemedicine membantu saya merasa lebih terbantu dalam mengatasi stres dan kecemasan terkait kesehatan dengan memberikan akses cepat ke perawatan",
        "Saya merasa lebih terbantu dalam memahami kondisi kesehatan saya dan rencana perawatan yang direkomendasikan melalui telemedicine",
        "Telemedicine membantu saya merasa lebih dekat dengan dokter saya karena kami dapat berkomunikasi secara rutin",
        "Saya merasa lebih termotivasi untuk mengambil langkah-langkah proaktif dalam menjaga kesehatan saya setelah menggunakan telemedicine",
        "Telemedicine memungkinkan saya untuk tetap terhubung dengan perawatan medis berkualitas meskipun saya tinggal di daerah yang terpencil atau terpencil",
        "Penggunaan telemedicine telah memberikan saya akses yang lebih baik ke sumber daya kesehatan dan informasi kesehatan secara on line",
        "Saya merasa lebih terbantu dalam mengatasi stres dan kecemasan terkait kesehatan dengan memberikan akses cepat ke perawatan",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih mandiri dalam mengelola kesehatan saya sendiri",
        "Telemedicine membantu saya merasa lebih puas dengan perawatan medis yang saya terima karena saya dapat memilih dokter yang terpercaya",
        "Saya merasa lebih termotivasi untuk mengambil langkah-langkah proaktif dalam menjaga kesehatan saya setelah menggunakan telemedicine",
        "Telemedicine memungkinkan saya untuk mengatur jadwal konsultasi sesuai dengan kebutuhan dan kenyamanan saya sendiri",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih mandiri dalam mengelola kesehatan saya sendiri",
        "Saya merasa lebih terjamin dengan kualitas perawatan medis yang saya terima melalui telemedicine karena saya bisa memilih dokter yang terpercaya",
        "Telemedicine memberi saya kebebasan untuk mengatasi hambatan akses ke perawatan medis yang seringkali muncul karena jarak geografis atau mobilitas terbatas",
        "Saya merasa lebih terbantu dalam memahami kondisi kesehatan saya dan rencana perawatan yang direkomendasikan melalui telemedicine",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih dekat dengan dokter saya karena kami dapat berkomunikasi secara rutin",
        "Saya merasa lebih puas dengan pengalaman konsultasi telemedicine daripada kunjungan langsung ke klinik karena kenyamanan dan fleksibilitasnya",
        "Telemedicine memungkinkan saya untuk memantau kondisi kesehatan saya secara teratur tanpa harus meninggalkan rumah atau kantor",
        "Penggunaan telemedicine telah meningkatkan kepatuhan saya terhadap rencana perawatan medis saya karena akses yang lebih mudah dan nyaman",
        "Saya merasa lebih tenang dan terjamin dengan kualitas perawatan medis yang saya terima melalui telemedicine karena dokter saya memberikan perhatian penuh pada kebutuhan kesehatan saya",
        "Telemedicine membantu saya merasa lebih termotivasi untuk mengambil langkah-langkah proaktif dalam menjaga kesehatan saya",
        "Saya merasa lebih terbantu dalam mengatasi stres dan kecemasan terkait kesehatan dengan memberikan akses cepat ke perawatan melalui telemedicine",
        "Telemedicine memberi saya kesempatan untuk mengatur jadwal konsultasi sesuai dengan kebutuhan dan kenyamanan saya sendiri",
    ],
]

kategori = [
    6,0,44
]

index = 0

def pilihanCheck(awal, akhir, banyak) :
    listData = []
    i = awal
    while i <= akhir :
        listData.append(i)
        i += 1

    return random.sample(listData, banyak)

def pilihTipe(data) -> int :
    datar = []
    for i in range(len(data)) :
        if data[i] != 0 :
            datar.append(i)

    return random.sample(datar, 1)[0]

def berikutnya() :
    time.sleep(3)
    kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
    kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

    if len(kirims1) != 0 :
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )
    else:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
        )

    submit_button.click()

def polaJawab3(pola: int, awal: int, banyakSoal: int, kelipatan: int, jawab: list[WebElement]) :
    p = awal
    for i in range(banyakSoal) :
        if pola == 0 :
            s1 = random.choice([p,p,p,p+1,p+1,p+1,p+2])
        elif pola == 2 :
            s1 = random.choice([p,p+1,p+1,p+1,p+2,p+2,p+2])
        else :
            s1 = random.choice([p,p+1,p+2])

        jawab[s1].click()
        p += kelipatan

try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        service = Service(r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(link)

        if i == 0 :
            times = 10
            idx = 1
        else :
            times = 10
            idx = 1

        idxx = 1

        while times:
            time.sleep(2)

            if idx == 10:
                idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(5)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[idx].click()

            time.sleep(5)
            # ================================================================================
            tipeJawab = pilihTipe(kategori)
            kategori[tipeJawab] -= 1

            time.sleep(2)
            textboxes = driver.find_elements("css selector", ".whsOnd")#isian

            textboxes[0].send_keys(email[index])

            berikutnya()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            radiobuttons[kelamin[index]].click()

            usia = random.choice([2,3,3,4,5,6,7])
            radiobuttons[usia].click()
            if usia == 2 :
                pekerjaan = 14
            elif usia == 3:
                pekerjaan = random.choice([9,14,14,15,17])
            else :
                pekerjaan = random.choice([9,10,11,12,13,15,17])
            radiobuttons[pekerjaan].click()

            if pekerjaan == 14 :
                pendapatan = 19
            else :
                pendapatan = random.choice([19,20,21,22,23,24])

            radiobuttons[pendapatan].click()


            if pendapatan <= 20 :
                pengeluaran = random.choice([25,26])
            else :
                pengeluaran = random.choice([25,26,27,27,28,29,30,31])

            radiobuttons[pengeluaran].click()


            perangkat = random.choice([33,34])
            radiobuttons[perangkat].click()


            aplikasi = random.randint(35,42)
            radiobuttons[aplikasi].click()


            darimana = random.randint(44,49)
            radiobuttons[darimana].click()


            temp = random.choice([1,2,3,2,3,3,4,4,3,3])
            pilihanJawaban = random.sample(([0,1,2,3,4,5]), temp)

            for i in pilihanJawaban :
                checkboxes[i].click()

            seberapa = random.choice([51,52,53,54,55])
            radiobuttons[seberapa].click()


            nominal = random.randint(57,64)
            radiobuttons[nominal].click()





            for i in range(6) :
                berikutnya()

                time.sleep(3)
                textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
                testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

                polaJawab3(tipeJawab, tipeJawab, 3, 5, testcheck)

                time.sleep(1)
                textarea[0].send_keys(jawaban[i][index])

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
                )

            submit_button.click()

            driver.implicitly_wait(4)
            driver.get(link)

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("kategori = " + str(kategori))
            print("")
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))

        driver.quit()

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
            # kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            # kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            # if len(kirims1) != 0 :
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            #     )
            # else:
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            #     )

            # submit_button.click()
