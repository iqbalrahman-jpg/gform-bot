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

profil = ["Profile 106", "Profile 107", "Profile 6"]

email = [
    "email@gmail.com",
]

nama = [
    "Yuli Setiawan",
    "Eko Wijaya",
    "Yuni Nafisah",
    "Prita agustina",
    "Naufal Ardiansyah",
    "Hana Anissa Herian",
    "Heraldy Gunawan",
    "Eka Wahyu",
    "Bagus Rahmad",
    "Budi Santoso",

    "Dwi Panca",
    "faradilla nina",
    "Erfina Pratiwi",
    "Yazid Hasbilluh Kurniawan",
    "Bagus Hariawan",
    "Josephine Anindya",
    "Sarah Husaini",
    "Shabir Maulana",
    "Olivia Niken",
    "Gita Permata",

    "Argo Prasetyawan",
    "Salma Azizah",
    "Faradilla Aulia",
    "Dimas Wahyu",
    "Regina April",
    "Agis Prasetya",
    "Ardy Riski",
    "Muhammad Fadlan",
    "Septinia Kurniawan",
    "Damar Eka",

    "Fredinan Puan",
    "Amanda Bella Putri",
    "Bambang Suhatmoyo",
    "Kairaini Aliesa",
    "Lika Arletta",
    "Arjuna Ghafur",
    "Damar Hafidzhuan",
    "Lista Kamilla",
    "Sadiva Pratiwi",
    "Hermanto Caisar",

    "Windy Cantika",
    "Stephani Amanda Safitri",
    "Ardyanto Putra Wardhana",
    "Caroline Putri",
    "Nabil Saputra",
    "Khansa Azzahra",
    "Naufal Azwin",
    "Riska Rahmawati",
    "Rohmat Ubaidillah",
    "Setiawan Nugraha",

    "Anastasya Raisha",
    "Rakha Bumi",
    "Fikky Devano Purwanto",
    "Lesmana Dewa",
    "Ilyasa Fadil",
    "Belinda Inggridina Amelia",
    "Putri Bella Kartika",
    "Meydina Margaretha",
    "Muhammad Wawan",
    "Budiman Yahya Pradana",

    "Yahya Budiman",
    "Farhan Nurrahman",
    "Sisca Pratiwi",
    "Ahmad Fioren",
    "Alif Ramadhan",
    "Divani Permatasari",
    "Angga Dewangga",
    "Sasya Putri",
    "Selma Nabila Hayati",
    "Iwan Setiawan",

    "Rafi Fadhil Athalla",
    "Jonathan Putra",
    "Karina Aulia",
    "Diyastra Mahendra",
    "Agung Prasetya",
    "Aulia Lita Hani",
    "Sifa Nada",
    "Hani Salsabila",
    "Denis Prasetya kurniawan",
    "Griska Adelina Septinia",

    "Niara Rahmadhani",
    "Fajar Wijaya",
    "Anissha Fitrianni",
    "Galih Wibowo",
    "Rahma Aulia",
    "Maya Dewi",
    "Dhesy Lestari",
    "Rizky Firdaus",
    "Ditho Prasetyo",
    "Amanda Putri",

    "Karina Tiyas",
    "Abhista Deana",
    "Juana Noelle",
    "Jasmine Hanura",
    "Santiawati Agustina",
    "Pawitri Sari",
    "Yusti Fanggraeni",
    "Pamela Audine",
    "Anisha Pranaya",
    "Keita Pramudya",

    "Haris Cristopher",
    "Sinta Cintia",
    "Toni Sucipto",
    "Hani Baharani",
    "Ruli Abdhi",
    "Vidi Pratama",
    "Azzahra Fitriana",
    "Ilham Maulana",
    "Mayya Fitri",
    "Romadhon Ramzy",
]

kelamin = [
    1,0,1,1,0,1,0,1,0,0,
    0,1,1,0,0,1,1,0,1,1,
    0,1,1,0,1,0,0,0,1,0,
    0,1,0,1,1,0,0,1,1,0,
    1,1,0,1,0,1,0,1,0,0,

    # 50
    1,0,0,0,0,1,1,1,0,0,
    0,0,1,0,0,1,0,1,1,0,
    0,0,1,0,0,1,1,1,0,1,
    1,0,1,0,1,1,1,0,0,1,
    1,1,1,1,1,1,1,1,1,1,


    # 100
    0,1,0,1,0,0,1,0,1,0,
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
        "Saya merasa tertarik dengan kemungkinan kenyamanan yang ditawarkan oleh aplikasi tersebut",
        "Saya ingin memastikan bahwa aplikasi tersebut aman dan dapat diandalkan sebelum saya menggunakannya",
        "Saya ingin mengetahui lebih lanjut tentang fitur-fitur yang disediakan oleh aplikasi tersebut sebelum saya memutuskan apakah akan menggunakannya",
        "Saya akan mengambil waktu untuk melakukan riset lebih lanjut untuk memastikan bahwa aplikasi tersebut sesuai dengan kebutuhan medis saya",
        "Saya bersedia mencoba aplikasi tersebut asalkan ada bukti yang menunjukkan keefektifannya",
        "Saya ingin mendengar pengalaman orang lain yang telah menggunakan aplikasi telemedicine tersebut sebelumnya",
        "Saya merasa skeptis terhadap teknologi baru dalam bidang kesehatan, tetapi saya tetap terbuka untuk menjelajahi opsi tersebut",
        "Saya ingin memastikan bahwa aplikasi tersebut memenuhi standar etika medis yang tinggi",
        "Saya akan berbicara dengan profesional medis saya sebelum mengadopsi aplikasi tersebut untuk memastikan kecocokan dengan kondisi saya",
        "Saya melihat potensi aplikasi telemedicine untuk meningkatkan aksesibilitas layanan kesehatan, tetapi saya juga ingin memastikan bahwa itu tidak menggantikan hubungan individual dengan dokter saya",
        "Saya ingin mengetahui apakah aplikasi tersebut terintegrasi dengan catatan medis elektronik saya",
        "Saya akan mengevaluasi apakah aplikasi tersebut mudah digunakan dan memiliki antarmuka yang ramah pengguna",
        "Saya ingin memastikan bahwa privasi dan keamanan information saya terjamin ketika menggunakan aplikasi tersebut",
        "Saya akan memeriksa apakah aplikasi tersebut dilengkapi dengan dukungan pelanggan yang baik",
        "Saya ingin memeriksa apakah biaya penggunaan aplikasi tersebut masuk akal bagi saya",
        "Saya akan mencari tahu apakah aplikasi tersebut telah mendapatkan sertifikasi atau persetujuan dari lembaga kesehatan yang relevan",
        "Saya akan menilai apakah aplikasi tersebut dapat memberikan layanan yang memadai untuk kondisi kesehatan saya",
        "Saya ingin memeriksa apakah aplikasi tersebut memungkinkan saya untuk terhubung dengan dokter yang berkualitas",
        "Saya ingin mengetahui apakah aplikasi tersebut memberikan opsi untuk konsultasi langsung dengan dokter atau hanya melalui pesan teks atau panggilan telepon",
        "Saya akan mengevaluasi apakah aplikasi tersebut memiliki fitur-fitur tambahan yang dapat membantu saya dalam mengelola kesehatan saya secara holistik",
        "Saya terbuka untuk mencoba aplikasi telemedicine terbaru jika itu dapat memudahkan proses konsultasi medis saya",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat menyediakan layanan yang sesuai dengan kebutuhan medis saya",
        "Saya merasa antusias dengan kemungkinan menghemat waktu dan biaya dengan menggunakan aplikasi telemedicine",
        "Saya ingin mengetahui apakah aplikasi tersebut memiliki fitur-fitur khusus yang dapat membantu saya dalam mengelola kondisi kesehatan saya",
        "Saya akan mencari tahu apakah aplikasi telemedicine tersebut dapat terintegrasi dengan sistem kesehatan yang ada",
        "Saya ingin mengetahui apakah aplikasi tersebut dapat menyediakan konsultasi dengan spesialis dalam bidang kesehatan tertentu",
        "Saya tertarik untuk mengetahui apakah aplikasi telemedicine tersebut dapat memfasilitasi pengiriman resep obat secara online",
        "Saya akan mempertimbangkan faktor-faktor seperti keamanan dan privasi information sebelum memutuskan untuk menggunakan aplikasi tersebut",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat diakses dengan mudah dan memiliki dukungan teknis yang baik",
        "Saya akan bertanya-tanya apakah aplikasi tersebut memungkinkan saya untuk memantau perkembangan kondisi kesehatan saya dari waktu ke waktu",
        "Saya ingin mengetahui apakah aplikasi tersebut menawarkan pilihan konsultasi dalam bahasa yang saya pahami",
        "Saya akan mempertimbangkan apakah aplikasi tersebut memungkinkan saya untuk melakukan konsultasi secara anonim jika diperlukan",
        "Saya akan mencari tahu apakah aplikasi telemedicine tersebut dapat memberikan solusi yang ramah biaya untuk layanan kesehatan",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat memberikan informasi yang akurat dan terpercaya kepada saya",
        "Saya akan mengevaluasi apakah aplikasi tersebut dapat menyediakan layanan darurat jika diperlukan",
        "Saya tertarikuntuk mengetahui apakah aplikasi tersebut dapat memberikan saran kesehatan yang sesuai dengan pola hidup saya",
        "Saya ingin mengetahui apakah aplikasi telemedicine tersebut telah diuji dan direkomendasikan oleh lembaga kesehatan yang terkemuka",
        "Saya akan mempertimbangkan apakah aplikasi tersebut dapat memberikan layanan yang sesuai dengan kondisi medis saya yang mungkin kompleks",
        "Saya akan mengevaluasi apakah aplikasi tersebut memungkinkan saya untuk berbagi catatan medis saya dengan dokter secara aman",
        "Saya ingin mengetahui apakah aplikasi telemedicine tersebut dapat memfasilitasi konsultasi kelompok atau dukungan komunitas untuk kondisi kesehatan tertentu",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat menyediakan layanan darurat 24/7",
        "Saya ingin mengetahui apakah aplikasi tersebut memiliki fitur untuk mengingatkan saya tentang jadwal konsultasi atau pengambilan obat",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut dapat memfasilitasi konsultasi dengan tim medis yang beragam, seperti dokter umum, spesialis, atau ahli gizi",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat membantu saya mengakses hasil tes laboratorium atau pemindaian medis lainnya",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat berfungsi dengan baik di berbagai perangkat, seperti ponsel pintar, tablet, atau komputer",
        "Saya akan mempertimbangkan apakah aplikasi telemedicine tersebut dapat menyediakan dukungan untuk pemantauan kondisi kesehatan jangka panjang",
        "Saya ingin mengetahui apakah aplikasi tersebut dapat membantu saya mengelola jadwal konsultasi untuk anggota keluarga saya",
        "Saya akan mengevaluasi apakah aplikasi tersebut dapat memfasilitasi konsultasi medis yang bersifat interaktif, misalnya melalui video atau chat langsung",
        "Saya ingin mengetahui apakah aplikasi tersebut memiliki fitur untuk merekam riwayat medis saya secara rinci",
        "Saya akan mempertimbangkan apakah aplikasi telemedicine tersebut dapat membantu saya mencari dokter atau spesialis yang sesuai dengan preferensi saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk memantau efek samping obat atau perubahan kondisi kesehatan",
        "Saya ingin mengetahui apakah aplikasi telemedicine tersebut dapat menyediakan layanan konsultasi gizi atau manajemen berat badan",
        "Saya akan mengevaluasi apakah aplikasi tersebut dapat menyediakan saran kesehatan yang sesuai dengan faktor-faktor lingkungan tempat tinggal saya",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat memberikan layanan yang inklusif bagi pengguna dengan berbagai kebutuhan aksesibilitas",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat membantu saya mengatur resep obat secara mudah dan efisien",
        "Saya ingin mengetahui apakah aplikasi tersebut memiliki fitur untuk menghubungkan saya dengan ahli psikologi atau konselor untuk konsultasi kesehatan mental",
        "Saya akan mempertimbangkan apakah aplikasi tersebut dapat memberikan solusi untuk mengelola kondisi kesehatan kronis secara efektif",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut dapat memberikan edukasi kesehatan yang bermanfaat, misalnya tentang pencegahan penyakit atau gaya hidup sehat",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat menyediakan layanan yang sesuai dengan kebijakan asuransi kesehatan saya, jika berlaku",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat memfasilitasi konsultasi untuk situasi kesehatan mendesak yang tidak memerlukan kunjungan langsung ke rumah sakit",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk menyimpan riwayat kesehatan saya secara terperinci, termasuk alergi dan riwayat penyakit",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat memberikan solusi untuk mengatasi kendala geografis dalam mengakses layanan kesehatan",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki dukungan multibahasa untuk memfasilitasi pengguna dari berbagai latar belakang",
        "Saya ingin mengetahui apakah aplikasi tersebut memiliki fitur untuk menghubungkan saya dengan layanan darurat medis lokal jika diperlukan",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat menyediakan opsi untuk konsultasi medis yang terjadwal atau segera",
        "Saya ingin memastikan bahwa aplikasi tersebut dapat memberikan solusi yang aman dan efektif untuk konsultasi medis yang berkualitas",
        "Saya akan mempertimbangkan apakah aplikasi tersebut menyediakan opsi untuk mengakses rekam medis saya secara online",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk mengirimkan pengingat tentang perawatan kesehatan rutin, seperti pemeriksaan tahunan",
        "Saya ingin mengetahui apakah aplikasi tersebut dapat memfasilitasi konsultasi dengan ahli gizi atau pelatih kebugaran untuk tujuan manajemen berat badan",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki fitur untuk menyediakan konsultasi dengan spesialis dalam bidang kesehatan tertentu, seperti kardiolog atau onkolog",
        "Saya ingin memastikan bahwa aplikasi tersebut memiliki keamanan yang ketat dalam hal privasi data dan informasi medis saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut dapat memberikan saran tentang kebiasaan hidup sehat, seperti nutrisi dan olahraga",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki fitur untuk menyediakan informasi tentang penyakit atau kondisi kesehatan tertentu",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk memantau tanda-tanda vital saya, seperti tekanan darah atau denyut jantung",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki layanan pengingat untuk mengambil obat secara teratur",
        "Saya akan mempertimbangkan apakah aplikasi telemedicine tersebut dapat memfasilitasi konsultasi dengan psikolog atau terapis untuk kesehatan mental",
        "Saya ingin mengetahui apakah aplikasi tersebut memiliki fitur untuk menghubungkan saya dengan fasilitas medis terdekat jika diperlukan kunjungan langsung",
        "Saya akan mengevaluasi apakah aplikasi tersebut memiliki fitur untuk menyediakan informasi tentang pola penyebaran penyakit atau wabah di area saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut dapat memberikan solusi untuk mengatasi masalah aksesibilitas fisik bagi pengguna dengan disabilitas",
        "Saya ingin memeriksa apakah aplikasi telemedicine tersebut memiliki opsi untuk memberikan umpan balik tentang pengalaman konsultasi medis saya untuk terus meningkatkan layanannya",
        "Saya ingin memeriksa apakah aplikasi tersebut menyediakan layanan konsultasi medis untuk kondisi-kondisi yang umum di antara keluarga saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk menghubungkan saya dengan spesialis anak jika diperlukan",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut dapat memberikan panduan tentang bagaimana mengelola kondisi kesehatan tertentu di rumah",
        "Saya ingin memeriksa apakah aplikasi tersebut memiliki fitur untuk menyediakan rekomendasi obat atau perawatan alternatif",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut dapat memberikan informasi tentang vaksinasi yang diperlukan atau direkomendasikan",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk menghubungkan saya dengan klinik atau rumah sakit yang sesuai dengan kebutuhan spesifik saya",
        "Saya ingin memastikan bahwa aplikasi tersebut memiliki dukungan teknis yang andal untuk membantu saya dalam mengatasi masalah atau pertanyaan yang mungkin timbul",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk mengatur janji temu konsultasi dengan beberapa dokter atau spesialis sekaligus",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk menyediakan konsultasi dalam situasi darurat yang memerlukan penanganan segera",
        "Saya ingin memeriksa apakah aplikasi tersebut dapat membantu saya mengelola informasi tentang obat-obatan yang saya konsumsi secara teratur",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk menyediakan informasi tentang perawatan kesehatan yang berhubungan dengan tahapan kehidupan tertentu, seperti kehamilan",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk menyediakan konsultasi dengan ahli terapi fisik atau rehabilitasi",
        "Saya ingin memeriksa apakah aplikasi tersebut dapat menyediakan informasi tentang penyakit menular atau peringatan kesehatan masyarakat yang relevan",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk menyediakan sumber informasi tentang gaya hidup sehat dan kebiasaan yang dapat meningkatkan kesejahteraan saya",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk memberikan saran tentang bagaimana mengelola stres atau masalah kesehatan mental",
        "Saya ingin memastikan bahwa aplikasi tersebut menyediakan tindakan keamanan yang memadai untuk melindungi data pribadi dan informasi medis saya",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk memberikan informasi tentang layanan kesehatan yang tersedia di area tempat tinggal saya",
        "Saya akan mengevaluasi apakah aplikasi telemedicine tersebut memiliki opsi untuk menyediakan konsultasi dengan terapis berlisensi atau konselor kesehatan mental",
        "Saya ingin memeriksa apakah aplikasi tersebut dapat memberikan rekomendasi tentang bagaimana mengelola makanan atau diet yang sesuai dengan kondisi kesehatan tertentu",
        "Saya tertarik untuk mengetahui apakah aplikasi tersebut memiliki fitur untuk memberikan informasi tentang program-program kesehatan dan kebugaran yang tersedia di komunitas saya",
    ],
    [
        "Media sosial dapat memberikan inspirasi dari konten-konten yang ditampilkan oleh pengguna lain, mendorong seseorang untuk mencoba hal-hal baru",
        "Melalui iklan yang disesuaikan, media sosial dapat mempengaruhi preferensi belanja seseorang, mendorong mereka untuk membeli produk atau layanan tertentu",
        "Media sosial bisa menjadi platform untuk memperluas jaringan sosial, yang dapat membantu seseorang dalam mencari peluang karir atau kemitraan bisnis",
        "Berinteraksi dengan komunitas atau kelompok yang memiliki minat atau tujuan serupa di media sosial bisa mendorong seseorang untuk terlibat dalam aktivitas atau gerakan tertentu",
        "Melalui tren atau challenge yang viral, media sosial dapat mempengaruhi seseorang untuk mencoba hal baru atau mengikuti tren yang sedang populer",
        "Media sosial dapat mempercepat penyebaran informasi dan opini, yang dapat mempengaruhi sikap atau tindakan seseorang terhadap suatu isu atau peristiwa",
        "Dengan menyajikan gaya hidup atau citra tertentu, media sosial dapat mempengaruhi persepsi diri seseorang dan mendorong mereka untuk meniru gaya hidup tersebut",
        "Keterlibatan dalam kompetisi atau penghargaan di media sosial dapat mendorong seseorang untuk meningkatkan keterampilan atau prestasi mereka dalam bidang tertentu",
        "Melalui endorsment dari tokoh terkenal atau influencer, media sosial dapat mempengaruhi keputusan pembelian seseorang terhadap produk atau merek tertentu",
        "Media sosial dapat memberikan platform untuk menyuarakan pendapat atau aspirasi, yang dapat mempengaruhi pihak-pihak tertentu untuk bertindak atau merespons",
        "Melalui konten edukatif atau informatif, media sosial dapat mempengaruhi persepsi atau pengetahuan seseorang tentang suatu topik atau isu",
        "Berbagi pengalaman atau testimonial positif di media sosial dapat mendorong seseorang untuk mencoba produk atau layanan yang sama",
        "Media sosial dapat mempengaruhi prioritas waktu dan perhatian seseorang dengan menariknya konten-konten yang ditampilkan, yang dapat mengubah pola perilaku sehari-hari",
        "Dengan memberikan dukungan atau pujian dari pengguna lain, media sosial dapat mempengaruhi rasa percaya diri atau motivasi seseorang",
        "Media sosial dapat memperluas wawasan seseorang tentang budaya atau perspektif yang berbeda, yang dapat mempengaruhi sikap atau pandangan mereka terhadap dunia",
        "Melalui fitur-fitur seperti geotagging atau rekomendasi lokasi, media sosial dapat mempengaruhi pilihan tempat atau destinasi seseorang untuk dikunjungi",
        "Media sosial dapat memperkenalkan seseorang kepada peluang atau ide-ide baru, yang dapat mempengaruhi langkah-langkah yang mereka ambil dalam hidup",
        "Dengan menyajikan penawaran atau diskon khusus, media sosial dapat mempengaruhi keputusan pembelian seseorang terhadap suatu produk atau layanan",
        "Melalui diskusi atau debat yang terjadi di media sosial, seseorang dapat terpapar pada argumen atau sudut pandang yang berbeda, yang dapat mempengaruhi keyakinan atau opini mereka",
        "Media sosial dapat memicu perasaan FOMO (Fear of Missing Out), yang dapat mendorong seseorang untuk terlibat dalam aktivitas atau acara tertentu",
        "Media sosial dapat mengarahkan perhatian seseorang pada tren kesehatan atau kebugaran tertentu, mendorong mereka untuk mengadopsi gaya hidup yang lebih sehat",
        "Melalui konten-konten kreatif atau hiburan, media sosial dapat memberikan hiburan yang mengalihkan perhatian seseorang dari stres atau kekhawatiran sehari-hari",
        "Media sosial dapat menciptakan tekanan sosial untuk mencapai standar tertentu dalam penampilan atau prestasi, yang dapat mempengaruhi kepercayaan diri seseorang",
        "Dengan memfasilitasi keterlibatan dalam kampanye amal atau aksi sosial, media sosial dapat mendorong seseorang untuk berkontribusi pada kebaikan sosial atau lingkungan",
        "Media sosial dapat memberikan akses kepada seseorang untuk mempelajari keterampilan baru atau mengakses sumber daya pendidikan secara gratis atau terjangkau",
        "Melalui algoritma yang disesuaikan, media sosial dapat menciptakan filter bubble yang membatasi paparan seseorang terhadap sudut pandang atau informasi yang beragam",
        "Dengan menyajikan kesuksesan atau pencapaian orang lain, media sosial dapat memicu perasaan kompetitif dan motivasi untuk mencapai kesuksesan serupa",
        "Media sosial dapat memberikan akses kepada seseorang untuk menyampaikan pesan atau cerita mereka sendiri, yang dapat mempengaruhi orang lain untuk berempati atau bertindak",
        "Melalui pembentukan komunitas online, media sosial dapat memberikan dukungan emosional atau informasi kepada individu yang mengalami tantangan atau kesulitan tertentu",
        "Media sosial dapat menciptakan ekspektasi yang tidak realistis tentang kehidupan atau hubungan, yang dapat mempengaruhi persepsi seseorang tentang kebahagiaan atau keberhasilan",
        "Dengan menyajikan konten-konten yang menggoda, media sosial dapat mempengaruhi kebiasaan makan atau pola tidur seseorang",
        "Melalui eksposur terus-menerus terhadap konten tertentu, media sosial dapat mempengaruhi persepsi seseorang tentang keindahan atau nilai-nilai estetika",
        "Media sosial dapat memberikan platform untuk mengekspresikan opini politik atau ideologi, yang dapat mempengaruhi sikap atau partisipasi seseorang dalam politik",
        "Dengan menyajikan kisah sukses dari pengusaha atau influencer, media sosial dapat mempengaruhi motivasi seseorang untuk mengejar karir atau bisnis yang sama",
        "Media sosial dapat menyebabkan gangguan atau kecemasan dengan memperkuat perbandingan sosial yang tidak sehat atau pameran kehidupan yang sempurna",
        "Melalui penggunaan teknik pemasaran yang cerdas, media sosial dapat mempengaruhi persepsi nilai atau status suatu produk atau merek",
        "Media sosial dapat memberikan platform untuk advokasi atau aktivisme, yang dapat mempengaruhi perubahan sosial atau politik",
        "Dengan menyajikan tren gaya hidup yang berkelanjutan atau ramah lingkungan, media sosial dapat mempengaruhi keputusan konsumsi seseorang terhadap produk atau layanan",
        "Melalui filter dan efek yang disediakan, media sosial dapat mempengaruhi persepsi seseorang tentang citra tubuh atau penampilan mereka sendiri",
        "Media sosial dapat menciptakan tekanan untuk terus memperbarui atau memperbaiki profil online seseorang, yang dapat mempengaruhi perilaku mereka dalam menggunakan platform tersebut",
        "Media sosial dapat memberikan platform bagi seseorang untuk belajar tentang tren investasi atau peluang keuangan, yang dapat mempengaruhi keputusan investasi mereka",
        "Melalui kolaborasi dengan merek atau produk tertentu, media sosial dapat mempengaruhi persepsi atau preferensi seseorang terhadap merek tersebut",
        "Media sosial dapat mempengaruhi keputusan perjalanan seseorang dengan menyajikan informasi atau ulasan destinasi wisata dari pengguna lain",
        "Dengan menyajikan konten yang mempromosikan kebahagiaan atau kepuasan hidup, media sosial dapat mempengaruhi persepsi seseorang tentang kualitas hidup mereka sendiri",
        "Media sosial dapat mempengaruhi sikap atau pandangan seseorang terhadap isu-isu sosial atau politik dengan menyajikan berita atau opini dari sumber-sumber tertentu",
        "Melalui penggunaan filter atau edit foto, media sosial dapat mempengaruhi persepsi seseorang tentang standar kecantikan atau penampilan",
        "Media sosial dapat memperkuat stereotip gender atau budaya tertentu melalui representasi yang disajikan dalam konten-kontennya",
        "Dengan menyajikan penawaran atau promosi eksklusif, media sosial dapat mempengaruhi keputusan pembelian seseorang terhadap produk atau layanan",
        "Media sosial dapat memfasilitasi pertukaran informasi atau saran tentang kesehatan mental atau kesejahteraan psikologis, yang dapat mempengaruhi cara seseorang merawat diri mereka sendiri",
        "Melalui penggunaan bahasa atau istilah tertentu, media sosial dapat mempengaruhi pemahaman atau persepsi seseorang terhadap suatu topik atau isu",
        "Media sosial dapat mempengaruhi pilihan pendidikan atau karier seseorang dengan menyajikan informasi tentang program-program atau peluang kerja",
        "Dengan menyajikan konten yang menyoroti masalah sosial atau lingkungan, media sosial dapat mempengaruhi kesadaran atau partisipasi seseorang dalam gerakan sosial",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang dalam hubungan dengan menyajikan model-model atau contoh-contoh dari hubungan yang sehat atau tidak sehat",
        "Melalui kemitraan dengan organisasi atau badan amal, media sosial dapat mempengaruhi partisipasi seseorang dalam kegiatan-kegiatan sukarela atau donasi",
        "Media sosial dapat mempengaruhi pilihan hiburan seseorang dengan menyajikan rekomendasi film, musik, atau acara televisi dari pengguna lain",
        "Dengan menyajikan informasi tentang tren parenting atau tips pengasuhan anak, media sosial dapat mempengaruhi cara seseorang merawat anak-anak mereka",
        "Media sosial dapat mempengaruhi persepsi atau pandangan seseorang terhadap agama atau spiritualitas dengan menyajikan konten-konten yang relevan",
        "Melalui pemunculan influencer-influencer yang mempromosikan gaya hidup yang berkelanjutan, media sosial dapat mempengaruhi keputusan konsumsi seseorang terhadap produk atau layanan",
        "Media sosial dapat mempengaruhi tingkat stres atau kecemasan seseorang dengan menyajikan konten-konten yang mendukung kesehatan mental atau teknik-teknik relaksasi",
        "Dengan menyajikan testimoni atau ulasan produk dari pengguna lain, media sosial dapat mempengaruhi kepercayaan seseorang terhadap kualitas atau kegunaan produk tersebut",
        "Media sosial dapat mempengaruhi keputusan seseorang dalam merencanakan liburan atau perjalanan dengan menyajikan foto-foto atau ulasan destinasi wisata",
        "Dengan menyajikan konten-konten yang mendukung gaya hidup minimalis atau sederhana, media sosial dapat mempengaruhi kebiasaan konsumsi seseorang",
        "Media sosial dapat mempengaruhi persepsi atau pandangan seseorang terhadap topik politik dengan memperkuat polarisasi dan konflik",
        "Melalui konten-konten yang menyoroti keberagaman atau inklusi, media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap kelompok minoritas",
        "Media sosial dapat mempengaruhi keputusan pendidikan atau karier seseorang dengan menyajikan informasi tentang peluang beasiswa atau program pelatihan",
        "Dengan menyajikan penawaran khusus atau diskon untuk pengikut media sosial, perusahaan dapat mempengaruhi keputusan pembelian seseorang",
        "Media sosial dapat mempengaruhi persepsi seseorang tentang keadilan atau kesetaraan dengan menyajikan cerita-cerita atau berita yang berkaitan dengan isu-isu sosial",
        "Melalui komunitas atau grup dukungan online, media sosial dapat mempengaruhi cara seseorang mengatasi tantangan atau krisis pribadi",
        "Media sosial dapat mempengaruhi pola konsumsi seseorang dengan menyajikan informasi tentang makanan sehat atau resep masakan",
        "Dengan menyajikan informasi tentang tren teknologi atau inovasi terbaru, media sosial dapat mempengaruhi minat atau penggunaan teknologi seseorang",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap diri mereka sendiri dengan menyajikan komparasi sosial dengan orang lain",
        "Melalui penyampaian berita palsu atau hoaks, media sosial dapat mempengaruhi keyakinan atau pandangan seseorang terhadap suatu topik atau isu",
        "Media sosial dapat mempengaruhi pola tidur atau kualitas tidur seseorang dengan menyajikan konten yang mengganggu atau menghibur",
        "Dengan menyajikan informasi tentang tren fashion atau gaya hidup, media sosial dapat mempengaruhi keputusan berbelanja seseorang",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang dalam hubungan interpersonal dengan menyajikan contoh-contoh dari interaksi sosial yang baik atau buruk",
        "Melalui promosi yang ditargetkan, media sosial dapat mempengaruhi keputusan pembelian seseorang berdasarkan preferensi dan minat individu",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap suatu acara atau peristiwa dengan menyajikan berita atau liputan yang tendensius",
        "Dengan menyajikan testimoni atau cerita inspiratif, media sosial dapat mempengaruhi motivasi atau semangat seseorang untuk mengatasi rintangan atau hambatan",
        "Media sosial dapat mempengaruhi kebiasaan membaca atau menonton dengan menyajikan rekomendasi buku atau film dari pengguna lain",
        "Dengan menyajikan informasi tentang tren investasi atau peluang pasar, media sosial dapat mempengaruhi keputusan finansial seseorang",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap kesehatan mental dengan menyajikan konten-konten yang mendukung pemahaman dan kesadaran akan masalah ini",
        "Dengan menyajikan informasi tentang tren pengembangan diri atau self-improvement, media sosial dapat mempengaruhi motivasi seseorang untuk mencapai potensi pribadi mereka",
        "Melalui konten-konten yang menekankan pentingnya kesetaraan gender, media sosial dapat mempengaruhi sikap atau perilaku seseorang terhadap isu-isu gender",
        "Media sosial dapat mempengaruhi persepsi seseorang tentang pentingnya waktu luang dan rekreasi dengan menyajikan rekomendasi kegiatan atau hobi dari pengguna lain",
        "Dengan menyajikan informasi tentang tren pendidikan atau teknologi pembelajaran, media sosial dapat mempengaruhi minat seseorang terhadap pembelajaran baru",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang dalam pengelolaan keuangan dengan menyajikan tips atau strategi keuangan dari pengguna lain",
        "Melalui fitur-fitur seperti live streaming, media sosial dapat mempengaruhi partisipasi seseorang dalam acara-acara atau pertunjukan online",
        "Media sosial dapat mempengaruhi cara seseorang berinteraksi dengan lingkungan fisik mereka dengan menyajikan rekomendasi tempat-tempat atau aktivitas di sekitar mereka",
        "Dengan menyajikan informasi tentang tren mode atau gaya, media sosial dapat mempengaruhi keputusan berpakaian atau penampilan seseorang",
        "Media sosial dapat mempengaruhi sikap atau pandangan seseorang terhadap lingkungan alam dengan menyajikan konten-konten yang menyoroti isu-isu lingkungan",
        "Melalui konten-konten yang menekankan pentingnya self-care atau perawatan diri, media sosial dapat mempengaruhi sikap seseorang terhadap kesehatan fisik dan mental mereka",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap kredibilitas atau kepercayaan diri mereka sendiri dengan menyajikan umpan balik atau dukungan dari pengguna lain",
        "Dengan menyajikan informasi tentang tren makanan atau diet, media sosial dapat mempengaruhi kebiasaan makan atau pola diet seseorang",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang dalam merawat hewan peliharaan dengan menyajikan tips atau saran dari pengguna lain",
        "Melalui diskusi atau debat tentang isu-isu kontroversial, media sosial dapat mempengaruhi pembentukan opini atau sikap seseorang terhadap isu-isu ini",
        "Media sosial dapat mempengaruhi keputusan seseorang dalam memilih produk-produk ramah lingkungan atau berkelanjutan dengan menyajikan informasi tentang merek-merek yang peduli lingkungan",
        "Dengan menyajikan testimoni atau cerita inspiratif tentang pengalaman-pengalaman kesuksesan, media sosial dapat mempengaruhi motivasi atau ambisi seseorang untuk mencapai tujuan mereka",
        "Media sosial dapat mempengaruhi persepsi atau penilaian seseorang terhadap kualitas hidup mereka dengan membandingkan diri mereka dengan orang lain di platform tersebut",
        "Melalui komunitas-komunitas online yang berfokus pada topik-topik tertentu, media sosial dapat mempengaruhi keterlibatan atau minat seseorang dalam topik-topik tersebut",
        "Media sosial dapat mempengaruhi sikap atau perilaku seseorang dalam pengelolaan stres atau kecemasan dengan menyajikan teknik-teknik atau strategi coping dari pengguna lain",
    ],
    [
        "Kualifikasi dan lisensi dokter yang menyediakan layanan telemedicine",
        "Reputasi dan ulasan positif dari pengguna sebelumnya",
        "Ketersediaan layanan 24/7 untuk konsultasi medis",
        "Kemampuan untuk mengakses riwayat medis dan catatan kesehatan secara online",
        "Integrasi dengan sistem rumah sakit dan penyedia layanan kesehatan lainnya",
        "Keamanan dan privasi information yang terjamin",
        "Teknologi canggih yang mendukung determination jarak jauh secara akurat",
        "Ketersediaan layanan resep dan pengiriman obat jika diperlukan",
        "Layanan dukungan pelanggan yang responsif dan informatif",
        "Kemampuan untuk berkonsultasi dengan spesialis dalam berbagai bidang medis",
        "Penggunaan stage yang mudah digunakan dan ramah pengguna",
        "Kecepatan respon dan waktu tunggu yang minimal",
        "Ketersediaan layanan konseling mental dan psikologis",
        "Integrasi dengan teknologi wearable untuk pemantauan kesehatan secara real-time",
        "Layanan follow-up dan perawatan jangka panjang yang terintegrasi",
        "Pengalaman yang nyaman dan aman untuk pengguna dari berbagai latar belakang",
        "Adopsi standar etika dan praktik medis yang tinggi",
        "Penggunaan teknologi enkripsi untuk melindungi informasi medis sensitif",
        "Kerjasama dengan asuransi kesehatan untuk pembayaran dan klaim yang mudah",
        "Keandalan sistem dan jaringan untuk menjaga koneksi selama konsultasi",
        "Transparansi dalam biaya dan kebijakan pembayaran",
        "Kemampuan untuk mengakses konsultasi dari mana saja, asalkan terhubung dengan internet",
        "Kecepatan dalam mendapatkan jadwal konsultasi yang sesuai dengan kebutuhan Anda",
        "Dukungan multibahasa untuk pengguna yang berbicara dalam bahasa yang berbeda",
        "Kemampuan untuk berbagi hasil tes dan gambar medis secara mudah",
        "Sistem peringatan dan pengingat untuk menjaga konsistensi perawatan",
        "Kemampuan untuk menghubungi dokter atau spesialis yang sama secara konsisten",
        "Pengalaman yang disesuaikan dengan kebutuhan medis individu",
        "Aksesibilitas untuk individu dengan kebutuhan khusus atau disabilitas",
        "Keberadaan mekanisme umpan balik untuk terus meningkatkan layanan",
        "Penggunaan teknologi telediagnosis yang maju untuk menunjang diagnosis",
        "Kemampuan untuk menyediakan konsultasi keluarga atau grup jika diperlukan",
        "Integritas dan kehandalan informasi yang disediakan oleh platform",
        "Kemampuan untuk mengakses catatan konsultasi dan rekomendasi kesehatan secara online",
        "Kolaborasi dengan lembaga riset medis untuk pembaruan dan inovasi terkini",
        "Dukungan untuk penggunaan teknologi video, sound, dan pesan teks",
        "Kesesuaian dengan regulasi kesehatan dan kepatuhan terhadap standar hukum",
        "Pelatihan dan sertifikasi khusus bagi dokter yang menyediakan layanan telemedicine",
        "Kolaborasi dengan apotek dan layanan kesehatan lokal untuk dukungan tambahan",
        "Kemampuan untuk menyediakan layanan darurat dan pertolongan pertama secara online dalam situasi mendesak",
        "Kemampuan untuk melakukan konsultasi dengan berbagai spesialis dalam satu platform",
        "Dukungan untuk konsultasi praperjanjian dan jadwal yang terstruktur",
        "Fleksibilitas dalam memilih metode komunikasi yang diinginkan (misalnya, video, telepon, pesan teks)",
        "Adopsi teknologi kecerdasan buatan untuk mendukung conclusion dan perawatan",
        "Kemampuan untuk mengirimkan hasil konsultasi dan resep langsung ke apotek lokal",
        "Keandalan sistem dan infrastruktur teknologi untuk mencegah gangguan layanan",
        "Dukungan untuk konsultasi dengan dokter yang memahami budaya atau kepercayaan agama tertentu",
        "Program edukasi kesehatan yang terintegrasi untuk meningkatkan pemahaman pengguna tentang kondisi mereka",
        "Kemampuan untuk mengakses konsultasi medis yang sesuai dengan zona waktu pengguna",
        "Ketersediaan layanan konsultasi medis dalam bahasa isyarat untuk pengguna tunarungu",
        "Kolaborasi dengan lembaga kesehatan masyarakat untuk menyediakan layanan telemedicine kepada komunitas yang kurang mampu",
        "Integrasi dengan sistem pemantauan kesehatan rumah untuk pasien dengan kondisi kronis",
        "Dukungan untuk aksesibilitas teknologi bagi individu dengan keterbatasan fisik",
        "Kemampuan untuk memperoleh konsultasi kedua dari dokter yang berbeda untuk verifikasi determination atau rencana perawatan",
        "Penyediaan sumber daya informasi medis yang terpercaya kepada pengguna",
        "Kolaborasi dengan organisasi nirlaba untuk menyediakan layanan telemedicine di daerah terpencil atau sulit dijangkau",
        "Kemampuan untuk mengakses catatan kesehatan elektronik secara real-time selama konsultasi",
        "Integrasi dengan aplikasi kesehatan pihak ketiga untuk pemantauan kesehatan mandiri",
        "Layanan konsultasi dengan dukun atau praktisi alternatif yang terverifikasi untuk pengguna yang memerlukan pendekatan non-konvensional",
        "Kemampuan untuk menyediakan konsultasi medis yang dikustomisasi sesuai dengan preferensi pengguna, termasuk pemilihan dokter atau spesialis tertentu",
        "Kesesuaian dengan standar keamanan dan regulasi HIPAA (Wellbeing Protections Movability and Responsibility Act) atau standar privasi information serupa",
        "Kolaborasi dengan lembaga pendidikan kedokteran untuk pengembangan konten edukasi dan pelatihan",
        "Dukungan untuk konsultasi medis darurat yang membutuhkan intervensi segera",
        "Ketersediaan layanan konsultasi medis bagi populasi lanjut usia dengan kebutuhan kesehatan yang unik",
        "Integrasi dengan aplikasi kesehatan dan kebugaran untuk memperkuat pendekatan holistik terhadap kesehatan",
        "Kemampuan untuk menghubungkan pengguna dengan program klinis atau penelitian kesehatan yang relevan",
        "Kualitas gambar dan suara yang tinggi selama konsultasi video untuk mendukung komunikasi efektif antara dokter dan pasien",
        "Dukungan untuk layanan telemedicine di tempat kerja atau sekolah untuk meningkatkan aksesibilitas perawatan kesehatan",
        "Kemampuan untuk mengelola janji temu dan jadwal konsultasi dengan mudah melalui stage telemedicine",
        "Kolaborasi dengan industri farmasi untuk memastikan ketersediaan obat dan perawatan yang tepat waktu",
        "Penggunaan teknologi blockchain untuk mengamankan information medis dan memastikan integritas informasi",
        "Program manajemen penyakit yang terintegrasi untuk pengguna dengan kondisi kronis",
        "Kemampuan untuk menyediakan saran kesehatan pencegahan dan promosi kesehatan kepada pengguna",
        "Dukungan untuk konsultasi medis dengan dokter atau spesialis dari berbagai negara atau wilayah",
        "Kemitraan dengan penyedia layanan transportasi untuk memastikan aksesibilitas bagi mereka yang kesulitan transportasi",
        "Penyediaan panduan dan sumber daya untuk membantu pasien mempersiapkan diri sebelum konsultasi telemedicine",
        "Dukungan untuk konsultasi medis keluarga yang melibatkan anggota keluarga yang terpisah secara geografis",
        "Kemampuan untuk memfasilitasi konsultasi medis multidisiplin untuk mengatasi masalah kesehatan kompleks",
        "Dukungan untuk konsultasi medis dalam situasi darurat atau bencana alam",
        "Integrasi dengan stage telemedicine lainnya untuk memfasilitasi konsultasi lintas-platform",
        "Pelatihan khusus bagi dokter untuk memastikan mereka terampil dalam memberikan layanan telemedicine",
        "Ketersediaan terapi fisik atau rehabilitasi melalui telemedicine untuk pasien dengan cedera atau kondisi fisik",
        "Dukungan untuk penggunaan teknologi Realitas Virtual atau Increased dalam konsultasi medis",
        "Layanan konsultasi gizi atau dietetika untuk membantu pengguna dalam menjaga pola makan sehat",
        "Kemampuan untuk memberikan surat rujukan atau rujukan ke spesialis atau fasilitas medis lainnya",
        "Program manajemen stres atau meditasi yang tersedia sebagai bagian dari layanan telemedicine",
        "Dukungan untuk konsultasi medis untuk kondisi kesehatan reproduksi atau kesehatan seksual",
        "Integrasi dengan teknologi IoT (Web of Things) untuk pemantauan kesehatan yang terhubung",
        "Dukungan untuk konsultasi medis bagi individu dengan kondisi kesehatan yang jarang terjadi",
        "Layanan konsultasi medis bagi populasi migran atau pengungsi yang membutuhkan akses ke layanan kesehatan",
        "Integrasi dengan sistem pemberitahuan atau pengingat untuk mengingatkan pengguna tentang jadwal perawatan",
        "Layanan konsultasi medis untuk pemeriksaan kesehatan rutin atau pemantauan kondisi kronis",
        "Dukungan untuk konsultasi medis berbasis teks untuk pengguna dengan keterbatasan pendengaran",
        "Kemampuan untuk mengakses catatan konsultasi dan hasil tes medis secara aman dan mudah",
        "Layanan konsultasi medisbagi individu dengan gangguan neurologis atau kebutuhan medis khusus lainnya",
        "Dukungan untuk konsultasi medis dengan terjemahan bahasa langsung untuk pengguna dengan bahasa ibu yang berbeda",
        "Integrasi dengan layanan telehealth mental untuk memberikan dukungan psikologis tambahan",
        "Layanan konsultasi medis dalam skala besar untuk keperluan perusahaan atau lembaga pendidikan",
        "Penggunaan algoritma dan analisis information untuk mendukung conclusion dan perawatan yang tepat",
        "Kemampuan untuk menyediakan konsultasi medis dengan biaya yang terjangkau atau dijamin oleh asuransi kesehatan",
    ],
    [
        "Telemedicine memungkinkan akses yang lebih mudah, terutama bagi mereka yang tinggal di daerah terpencil atau memiliki mobilitas terbatas.",
        "Menggunakan aplikasi telemedicine bisa jauh lebih mudah dan nyaman daripada membuat janji dan pergi ke kantor dokter.",
        "Dengan telemedicine, waktu tunggu sering kali lebih pendek, baik untuk janji maupun antara konsultasi.",
        "Menggunakan aplikasi telemedicine mengurangi biaya perjalanan yang mungkin timbul jika harus pergi ke dokter.",
        "Bisa berkonsultasi dari rumah bisa jauh lebih nyaman bagi sebagian orang daripada pergi ke fasilitas kesehatan.",
        "Kualitas layanan telemedicine bervariasi, tetapi bisa sebanding dengan kunjungan langsung, terutama untuk konsultasi rutin atau masalah umum.",
        "Dalam beberapa kasus, penggunaan telemedicine bisa dianggap lebih aman daripada pergi ke fasilitas kesehatan yang mungkin memiliki paparan terhadap penyakit menular.",
        "Telemedicine memungkinkan jadwal yang lebih fleksibel, terutama bagi mereka yang sibuk atau memiliki pekerjaan yang tidak memungkinkan untuk pergi ke dokter pada stick kerja.",
        "Beberapa orang merasa lebih nyaman berbicara tentang masalah kesehatan secara virtual daripada di hadapan dokter.",
        "Dengan telemedicine, risiko penularan penyakit antar pasien dapat diminimalkan.",
        "Pengoperasian aplikasi telemedicine dapat jauh lebih murah daripada memelihara fasilitas kesehatan fisik.",
        "Telemedicine memudahkan akses ke ahli spesialis yang mungkin sulit dijangkau di daerah tertentu.",
        "Telemedicine memfasilitasi konsultasi kedua atau opini kedua dari dokter tanpa perlu melakukan perjalanan tambahan.",
        "Mengurangi ketidaknyamanan perjalanan bagi mereka yang mungkin kesulitan melakukan perjalanan.",
        "Dengan telemedicine, ada potensi untuk menghemat biaya secara keseluruhan, terutama jika tidak perlu melakukan perjalanan jauh.",
        "Telemedicine memungkinkan kontinuitas perawatan bahkan ketika seseorang tidak dapat berkunjung ke dokter secara langsung.",
        "Beberapa aplikasi telemedicine menawarkan beragam layanan tambahan seperti pengiriman obat atau tes di rumah.",
        "Telemedicine bisa lebih mengakomodasi pasien yang lebih nyaman berbicara dalam bahasa tertentu, dengan dukungan layanan penerjemah jika diperlukan.",
        "Telemedicine mengurangi risiko infeksi yang mungkin timbul dari kontak dengan pasien lain yang sakit di fasilitas kesehatan.",
        "Dengan telemedicine, penghematan waktu bisa signifikan, terutama bagi mereka yang harus bekerja atau memiliki keterbatasan waktu lainnya.",
        "Telemedicine memungkinkan checking jangka panjang kondisi kesehatan tertentu secara teratur tanpa perlu kunjungan langsung yang sering.",
        "Beberapa stage telemedicine memberikan pilihan dokter yang lebih luas, termasuk dokter spesialis dari seluruh dunia.",
        "Bagi pasien dengan keterbatasan mobilitas atau yang terbatas secara fisik, telemedicine bisa menjadi satu-satunya pilihan yang memungkinkan.",
        "Dengan telemedicine, biaya administratif seperti pendaftaran, administrasi kertas, dan lainnya dapat berkurang.",
        "Menggunakan telemedicine mengurangi waktu yang dihabiskan untuk pergi ke dan dari fasilitas kesehatan.",
        "Untuk orang tua dengan anak kecil, atau anak-anak dengan orang tua yang membutuhkan perhatian, telemedicine bisa lebih nyaman daripada kunjungan langsung.",
        "Telemedicine memungkinkan konsultasi kesehatan tanpa mengganggu jadwal kerja atau aktivitas lainnya.",
        "Beberapa orang mengalami stres atau kecemasan saat berkunjung ke fasilitas kesehatan, yang dapat dikurangi melalui konsultasi telemedicine dari kenyamanan rumah.",
        "Dengan telemedicine, pasien dapat mempertahankan kendali atas lingkungan mereka sendiri, yang dapat penting untuk kesehatan mental dan kenyamanan.",
        "Telemedicine memungkinkan pemantauan penyakit kronis secara teratur tanpa harus selalu pergi ke dokter.",
        "Telemedicine menyediakan akses ke perawatan kesehatan bagi mereka yang mungkin terisolasi secara sosial atau geografis.",
        "Dalam situasi mendesak, telemedicine dapat memberikan akses cepat ke bantuan medis tanpa harus menunggu janji atau pergi ke unit gawat darurat.",
        "Beberapa aplikasi telemedicine menawarkan pilihan pembayaran yang lebih fleksibel, termasuk biaya rendah atau tanpa biaya untuk beberapa layanan.",
        "Telemedicine memungkinkan konsultasi dengan beberapa spesialis atau profesional kesehatan dalam satu sesi.",
        "Bagi pasienkronis yang membutuhkan konsultasi rutin, telemedicine bisa lebih nyaman daripada harus pergi ke dokter secara teratur.",
        "Menggunakan telemedicine dapat mengurangi pengeluaran tidak langsung, seperti biaya parkir atau waktu cuti kerja yang hilang.",
        "Pascaoperasi, telemedicine bisa digunakan untuk pemantauan jarak jauh tanpa perlu pergi ke rumah sakit.",
        "Telemedicine membuka pintu untuk penggunaan teknologi lanjutan seperti telediagnosis atau penggunaan AI dalam diagnosis.",
        "Bagi mereka dengan gangguan mental atau kecemasan sosial, telemedicine bisa lebih nyaman daripada interaksi langsung.",
        "Menggunakan telemedicine mengurangi penggunaan energi untuk perjalanan, mengurangi dampak lingkungan.",
        "Telemedicine memungkinkan konsultasi dengan dokter atau spesialis dari negara lain tanpa perlu melakukan perjalanan ke luar negeri.",
        "Menggunakan telemedicine menghilangkan biaya parkir yang mungkin dikeluarkan saat berkunjung ke fasilitas kesehatan.",
        "Bagi pasien dengan penyakit menular, konsultasi melalui telemedicine dapat mengurangi risiko penularan kepada orang lain.",
        "Telemedicine memungkinkan pasien untuk dengan mudah mengakses riwayat medis mereka dan informasi lainnya melalui stage digital.",
        "Jika kunjungan ke dokter melibatkan perjalanan jauh, menggunakan telemedicine dapat menghemat biaya penginapan yang mungkin diperlukan.",
        "Bagi pasien dengan penyakit menular, telemedicine memungkinkan mereka untuk tetap mengisolasi diri dan menghindari berinteraksi dengan orang lain secara langsung.",
        "Dengan telemedicine, pasien tidak perlu mengeluarkan biaya tambahan untuk peralatan medis yang mungkin diperlukan di kantor dokter.",
        "Telemedicine memberikan akses cepat ke informasi kesehatan dan edukasi tentang kondisi medis tertentu tanpa harus menunggu janji dokter.",
        "Bagi anak-anak yang mungkin takut atau cemas saat berkunjung ke dokter, telemedicine bisa menjadi pilihan yang lebih nyaman.",
        "Telemedicine mengurangi risiko kecelakaan lalu lintas atau kecelakaan lainnya yang mungkin terjadi selama perjalanan ke dokter.",
        "Untuk wanita hamil, telemedicine dapat memfasilitasi pemantauan kehamilan secara rutin tanpa harus sering-sering ke kantor dokter.",
        "Telemedicine memungkinkan pasien untuk berkonsultasi dengan dokter tentang efek samping obat tanpa harus pergi ke kantor dokter.",
        "Bagi pasien dengan kebutuhan khusus, seperti gangguan autisme atau kesulitan mobilitas, telemedicine bisa lebih mudah diakses.",
        "Menggunakan telemedicine dapat mengurangi biaya harian yang mungkin dikeluarkan oleh pasien dan keluarganya selama kunjungan ke fasilitas kesehatan.",
        "Bagi pasien dengan kecemasan sosial, telemedicine dapat memberikan alternatif yang lebih nyaman daripada berinteraksi langsung dengan orang asing.",
        "Telemedicine mengurangi risiko keterlambatan atau pembatalan janji karena faktor eksternal seperti lalu lintas atau cuaca buruk.",
        "Telemedicine memungkinkan pasien untuk berkonsultasi dengan ahli gizi atau dietisien tanpa perlu pergi ke kantor dokter.",
        "Bagi pasien yang mungkin memiliki masalah kepercayaan dengan dokter atau fasilitas kesehatan tertentu, telemedicine bisa memberikan alternatif yang lebih baik.",
        "Menggunakan telemedicine mengurangi potensi penularan infection atau penyakit lain yang mungkin terjadi di lingkungan fasilitas kesehatan.",
        "Bagi pasien lanjut usia yang mungkin sulit untuk melakukan perjalanan, telemedicine bisa memberikan opsi yang lebih nyaman dan mudah diakses.",
        "Telemedicine memungkinkan pemantauan penyakit menular secara langsung tanpa memerlukan interaksi langsung dengan pasien.",
        "Telemedicine memfasilitasi konsultasi dengan profesional kesehatan mental tanpa harus meninggalkan rumah, yang bisa sangat bermanfaat bagi mereka dengan gangguan kecemasan atau depresi.",
        "Bagi pasien yang baru saja menjalani operasi, telemedicine dapat memberikan konsultasi pascaoperasi tanpa harus keluar dari rumah.",
        "Telemedicine mengurangi biaya perjalanan jarak jauh bagi mereka yang tinggal di daerah terpencil atau tidak memiliki akses mudah ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pasien untuk mendapatkan dukungan dan pemantauan dari ahli gizi atau pelatih pribadi tanpa meninggalkan rumah.",
        "Bagi pasien dengan mobilitas terbatas, telemedicine bisa menjadi solusi yang sangat nyaman untuk mendapatkan perawatan kesehatan.",
        "Telemedicine mengurangi biaya transportasi bagi pasien yang memerlukan bantuan transportasi khusus atau mobil ambulans.",
        "Setelah cedera atau operasi, telemedicine memungkinkan pemantauan pemulihan jarak jauh tanpa harus berkunjung ke fasilitas kesehatan.",
        "Bagi pasien dengan penyakit kronis, telemedicine dapat memberikan akses cepat ke perawatan tanpa harus secara teratur mengunjungi dokter.",
        "Telemedicine memfasilitasi pemantauan kesehatan ibu hamil dan janin secara rutin dari kenyamanan rumah mereka sendiri.",
        "Menggunakan telemedicine dapat mengurangi biaya tidak langsung yang mungkin ditanggung oleh keluarga, seperti biaya perawatan anak atau pekerjaan rumah tangga yang tidak dilakukan selama perjalanan ke dokter.",
        "Telemedicine memungkinkan pemantauan yang lebih sering dan terjadwal dari kondisi kesehatan pasien tanpa perlu meninggalkan rumah.",
        "Telemedicine mengurangi risiko cedera yang mungkin terjadi selama perjalanan ke fasilitas kesehatan, terutama bagi mereka yang mengalami kesulitan mobilitas.",
        "Setelah operasi, telemedicine memungkinkan pasien untuk memantau gejala paskaoperasi dan mendapatkan nasihat medis tanpa harus keluar dari rumah.",
        "Menggunakan telemedicine dapat mengurangi biaya bantuan harian yang mungkin dibutuhkan oleh pasien selama perjalanan ke dokter.",
        "Telemedicine memungkinkan pemantauan efek samping pengobatan secara teratur tanpa harus berkunjung ke dokter.",
        "Telemedicine mengurangi stres dan kecemasan yang mungkin dirasakan oleh pasien saat berkunjung ke dokter atau fasilitas kesehatan.",
        "Untuk anak-anak yang mungkin tidak tahan lama di ruang tunggu dokter, telemedicine dapat menjadi alternatif yang lebih nyaman.",
        "Menggunakan telemedicine dapat mengurangi biaya pengurangan gangguan bagi pasien dan keluarganya yang mungkin harus mengambil cuti atau mengorganisir perawatan tambahan selama perjalanan ke dokter.",
        "Telemedicine memfasilitasi pemantauan kesehatan lansia secara rutin tanpa harus meninggalkan rumah.",
        "Telemedicine memungkinkan pemantauan kesehatan anak balita tanpa harus membawamereka ke fasilitas kesehatan yang mungkin menimbulkan risiko infeksi.",
        "Menggunakan telemedicine mengurangi biaya pembelian makanan di luar karena kebutuhan pergi ke fasilitas kesehatan.",
        "Telemedicine memfasilitasi pemantauan kesehatan di daerah terpencil di mana akses ke fasilitas kesehatan fisik mungkin terbatas.",
        "Telemedicine mengurangi stres yang terkait dengan transportasi, seperti kemacetan lalu lintas atau kesulitan mencari tempat parkir.",
        "Telemedicine memungkinkan pemantauan kesehatan selama perjalanan jauh tanpa harus meninggalkan kenyamanan kendaraan atau tempat menginap.",
        "Menggunakan telemedicine mengurangi biaya tambahan untuk akomodasi selama perjalanan ke fasilitas kesehatan di luar kota atau negara.",
        "Telemedicine memungkinkan pemantauan kesehatan mental remaja tanpa harus mengambil mereka dari lingkungan sehari-hari mereka.",
        "Telemedicine mengurangi risiko cedera akibat kecelakaan transportasi yang mungkin terjadi selama perjalanan ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan gigi dan konsultasi dengan dokter gigi tanpa harus datang ke klinik gigi.",
        "Menggunakan telemedicine mengurangi biaya perlengkapan dan peralatan medis yang mungkin dibutuhkan selama kunjungan ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan hewan peliharaan dan konsultasi dengan dokter hewan tanpa harus membawa hewan ke klinik.",
        "Menggunakan telemedicine mengurangi biaya akomodasi tambahan untuk pendamping yang mungkin diperlukan selama perjalanan ke fasilitas kesehatan.",
        "Telemedicine memfasilitasi pemantauan gizi anak dan konsultasi dengan ahli gizi tanpa harus membawa anak ke kantor dokter.",
        "Telemedicine mengurangi risiko penularan penyakit zoonotik yang mungkin terjadi saat membawa hewan peliharaan ke fasilitas kesehatan hewan.",
        "Telemedicine memungkinkan pemantauan kesehatan diri sendiri saat bepergian jauh tanpa harus mencari fasilitas kesehatan yang mungkin tidak dikenal di lokasi tersebut.",
        "Menggunakan telemedicine mengurangi biaya transportasi umum yang mungkin diperlukan untuk pergi ke fasilitas kesehatan.",
        "Telemedicine memungkinkan pemantauan kesehatan selama kebakaran hutan atau keadaan darurat lainnya di mana akses ke fasilitas kesehatan terbatas.",
        "Telemedicine mengurangi risiko penularan infeksi yang mungkin terjadi selama kunjungan ke rumah sakit atau fasilitas kesehatan lainnya.",
        "Telemedicine memungkinkan pemantauan kesehatan pasien kritis di unit perawatan intensif tanpa harus secara fisik berada di sana.",
        "Telemedicine mengurangi risiko terkena infeksi lingkungan yang mungkin terjadi di fasilitas kesehatan atau transportasi umum.",
    ],
    [
        "Kemudahan aksesibilitas: Layanan telemedicine memungkinkan saya untuk mendapatkan perawatan medis tanpa harus meninggalkan rumah atau kantor",
        "Waktu yang lebih efisien: Dengan telemedicine, saya dapat menghemat waktu yang sebelumnya saya habiskan untuk perjalanan menuju dan dari klinik atau rumah sakit",
        "Kenyamanan: Dapat berkomunikasi dengan dokter dari kenyamanan rumah saya membuat pengalaman perawatan lebih nyaman",
        "Mengurangi biaya: Sering menggunakan layanan telemedicine dapat mengurangi biaya transportasi dan biaya yang terkait dengan kunjungan langsung ke dokter",
        "Mendapatkan akses ke spesialis: Telemedicine memungkinkan saya untuk berkonsultasi dengan spesialis yang mungkin tidak tersedia secara lokal",
        "Pencegahan penularan penyakit: Dengan telemedicine, saya dapat menghindari potensi penularan penyakit yang mungkin terjadi di lingkungan klinik atau rumah sakit",
        "Mendapatkan konsultasi yang cepat: Telemedicine memungkinkan saya untuk mendapatkan konsultasi medis dengan cepat tanpa harus menunggu lama di klinik atau rumah sakit",
        "Memudahkan tindak lanjut: Dengan telemedicine, saya dapat dengan mudah melakukan tindak lanjut atau follow-up dengan dokter setelah konsultasi awal",
        "Pengelolaan penyakit kronis: Telemedicine memungkinkan saya untuk memantau kondisi kesehatan saya secara teratur tanpa harus selalu mengunjungi dokter secara fisik",
        "Ketersediaan di daerah terpencil: Telemedicine memberikan akses ke perawatan medis bagi mereka yang tinggal di daerah terpencil atau sulit dijangkau oleh fasilitas kesehatan",
        "Fleksibilitas jadwal: Dengan telemedicine, saya dapat mengatur jadwal konsultasi yang sesuai dengan jadwal harian saya tanpa harus mengganggu pekerjaan atau aktivitas lainnya",
        "Meningkatkan kualitas hidup: Dengan mendapatkan perawatan medis yang lebih mudah diakses, saya merasa lebih bisa mengelola kesehatan saya dengan lebih baik, yang pada gilirannya meningkatkan kualitas hidup saya",
        "Penghematan waktu keluarga: Dengan telemedicine, saya tidak perlu menghabiskan waktu yang berharga bersama keluarga untuk perjalanan ke dokter",
        "Mendapatkan pendapat kedua: Saya dapat dengan mudah mencari pendapat kedua dari dokter lain melalui telemedicine tanpa harus melakukan kunjungan fisik tambahan",
        "Memperkuat hubungan dengan dokter: Telemedicine memungkinkan saya untuk berkomunikasi dengan dokter secara lebih teratur, yang dapat memperkuat hubungan saya dengan mereka",
        "Mengurangi stres: Dengan telemedicine, saya tidak perlu khawatir tentang stres yang terkait dengan perjalanan atau waktu menunggu di klinik atau rumah sakit",
        "Pilihan pengobatan alternatif: Telemedicine memungkinkan saya untuk mengakses pengobatan alternatif atau integratif yang mungkin tidak tersedia secara lokal",
        "Privasi yang lebih besar: Saya merasa lebih nyaman berbicara tentang masalah kesehatan saya secara on line daripada secara langsung dengan dokter",
        "Edukasi kesehatan: Melalui telemedicine, saya dapat memperoleh informasi dan edukasi kesehatan yang lebih baik dari dokter saya",
        "Mengurangi absensi kerja: Dengan telemedicine, saya dapat menerima perawatan medis tanpa harus absen dari pekerjaan untuk kunjungan langsung ke dokter",
        "Ketersediaan obat resep: Melalui telemedicine, saya dapat memperoleh resep obat yang diperlukan tanpa harus mengunjungi dokter secara langsung",
        "monitoring kondisi kesehatan: Layanan telemedicine memungkinkan saya untuk memantau kondisi kesehatan saya secara teratur, seperti tekanan darah atau gula darah, dengan bantuan perangkat medis yang sesuai",
        "Layanan darurat: Dalam situasi darurat, telemedicine dapat memberikan akses cepat ke perawatan medis darurat tanpa harus menunggu di unit gawat darurat",
        "Mengatasi hambatan fisik: Bagi mereka dengan keterbatasan mobilitas atau disabilitas, telemedicine memberikan akses mudah ke perawatan medis tanpa harus meninggalkan rumah",
        "Penghematan biaya perjalanan: Telemedicine membantu saya menghemat biaya perjalanan jarak jauh yang mungkin diperlukan untuk kunjungan ke dokter",
        "Pengurangan waktu tunggu: Dengan telemedicine, saya dapat menghindari waktu tunggu yang sering kali panjang di klinik atau rumah sakit",
        "Konsultasi di luar jam kerja: Telemedicine memungkinkan saya untuk mendapatkan konsultasi medis di luar jam kerja yang biasanya tidak tersedia di klinik atau rumah sakit",
        "Pengurangan risiko infeksi silang: Dengan meminimalkan kontak dengan pasien lain di fasilitas kesehatan, telemedicine membantu mengurangi risiko infeksi silang",
        "Mendapatkan dukungan psikologis: Layanan telemedicine menyediakan akses mudah ke konseling atau dukungan psikologis tanpa harus meninggalkan rumah",
        "Pelayanan pascaperawatan: Telemedicine memfasilitasi pelayanan pascaperawatan yang efisien dan nyaman setelah operasi atau perawatan medis lainnya",
        "Akses ke informasi medis: Melalui telemedicine, saya dapat mengakses informasi medis dan riset terbaru untuk mendukung pengambilan keputusan terkait kesehatan saya",
        "Mendapatkan perawatan untuk keluarga: Telemedicine memungkinkan saya untuk mendapatkan perawatan medis untuk anggota keluarga yang membutuhkan tanpa harus membawa mereka ke klinik atau rumah sakit",
        "Pemeriksaan kesehatan berkala: Dengan telemedicine, saya dapat melakukan pemeriksaan kesehatan berkala secara teratur tanpa harus membuat janji temu fisik",
        "Akses ke jaringan worldwide: Telemedicine memberikan akses ke jaringan dokter dan spesialis worldwide, memperluas pilihan perawatan yang tersedia untuk saya",
        "monitoring kesehatan intellectual: Layanan telemedicine membantu saya memantau dan mengelola kesehatan intellectual saya dengan lebih baik melalui konseling on line atau terapi",
        "Mengatasi batasan geografis: Bagi mereka yang tinggal di daerah terpencil atau di luar negeri, telemedicine memberikan akses ke perawatan medis yang mungkin tidak tersedia secara lokal",
        "Pemeriksaan medis rutin: Telemedicine memungkinkan saya untuk melakukan pemeriksaan medis rutin seperti pemeriksaan fisik atau tes laboratorium dengan lebih mudah",
        "Akses ke spesialis langka: Telemedicine memungkinkan saya untuk berkonsultasi dengan spesialis langka atau jarang ditemui yang mungkin tidak tersedia di daerah saya",
        "Mendapatkan nasihat nutrisi: Melalui telemedicine, saya dapat berkonsultasi dengan ahli gizi untuk mendapatkan nasihat tentang pola makan yang sehat tanpa harus pergi ke klinik",
        "monitoring kehamilan: Layanan telemedicine menyediakan cara yang nyaman untuk memantau kehamilan dan mendapatkan konsultasi medis dari dokter kandungan",
        "Mengurangi kecemasan: Dengan telemedicine, saya merasa lebih mudah mengatasi kecemasan terkait dengan kunjungan ke fasilitas kesehatan",
        "Pemantauan jarak jauh: Telemedicine memungkinkan saya untuk memantau orang tua atau anggota keluarga lain yang tinggal jauh secara medis tanpa harus berkunjung secara langsung",
        "Penghematan energi: Bagi mereka dengan kondisi yang menguras energi, telemedicine membantu menghemat energi yang biasanya dibutuhkan untuk perjalanan dan menunggu di klinik",
        "Mengurangi keengganan untuk mencari bantuan medis: Dengan akses mudah melalui telemedicine, saya lebih mungkin untuk mencari bantuan medis pada tahap awal masalah kesehatan",
        "Perawatan lanjutan untuk kondisi kronis: Telemedicine memberikan akses mudah untuk perawatan lanjutan dan manajemen kondisi kronis seperti diabetes atau hipertensi",
        "Mendapatkan panduan tentang perawatan mandiri: Dokter telemedicine dapat memberikan panduan tentang perawatan mandiri untuk mengelola gejala atau kondisi kesehatan tertentu di rumah",
        "Menyediakan layanan kesehatan di tempat kerja: Telemedicine dapat diperluas sebagai bagian dari software kesehatan di tempat kerja, memberikan akses mudah bagi karyawan untuk konsultasi medis",
        "Mempertahankan isolasi saat sakit: Dengan telemedicine, saya dapat tetap menjaga isolasi saat sakit tanpa harus meninggalkan rumah untuk mendapatkan perawatan medis",
        "Meningkatkan kepatuhan terhadap perawatan: Akses mudah melalui telemedicine dapat meningkatkan kepatuhan saya terhadap perawatan yang direkomendasikan oleh dokter",
        "Memberikan dukungan untuk ibu menyusui: Telemedicine dapat memberikan konsultasi dan dukungan untuk ibu menyusui yang mungkin kesulitan dalam perjalanan ke dokter",
        "Konsultasi sebelum perjalanan: Telemedicine memungkinkan saya untuk berkonsultasi dengan dokter sebelum melakukan perjalanan, terutama jika saya memiliki kondisi kesehatan yang perlu diperhatikan",
        "Mengurangi kekhawatiran tentang privasi: Beberapa orang mungkin lebih nyaman berbicara tentang masalah kesehatan secara on line daripada di lingkungan klinik atau rumah sakit",
        "Mengatasi hambatan bahasa: Telemedicine dapat menyediakan layanan penerjemah untuk membantu mereka yang memiliki hambatan bahasa dalam berkomunikasi dengan dokter",
        "Memfasilitasi perawatan di malam hari: Dengan telemedicine, saya dapat mendapatkan perawatan medis di malam hari tanpa harus pergi ke unit gawat darurat",
        "Memfasilitasi perawatan anak-anak: Telemedicine memungkinkan saya untuk berkonsultasi dengan dokter untuk anak-anak saya tanpa harus membawa mereka ke klinik dan terpapar dengan risiko infeksi",
        "Mendapatkan saran tentang gaya hidup sehat: Melalui telemedicine, saya dapat mendapatkan saran dan panduan tentang gaya hidup sehat dari dokter tanpa harus pergi ke klinik",
        "Akses ke informasi medis untuk perjalanan: Telemedicine dapat menyediakan informasi medis yang diperlukan sebelum melakukan perjalanan ke daerah dengan risiko kesehatan tertentu",
        "Meningkatkan aksesibilitas bagi kaum disabilitas: Telemedicine dapat membantu memperluas akses ke perawatan medis bagi mereka dengan disabilitas fisik atau mobilitas yang terbatasi",
        "Pemantauan penyakit menular: Telemedicine memungkinkan pemantauan dan konsultasi yang lebih mudah bagi mereka yang memiliki penyakit menular seperti HIV atau hepatitis",
        "Mengatasi kekhawatiran tentang risiko penularan COVID-19: Dalam masa pandemi, telemedicine memberikan solusi yang aman untuk mendapatkan perawatan medis tanpa harus meninggalkan rumah dan terpapar risiko penularan COVID-19 di fasilitas kesehatan",
        "Mendapatkan diagnosa dini: Telemedicine memungkinkan saya untuk mendapatkan diagnosa dini atas gejala atau masalah kesehatan yang mungkin saya alami",
        "Pemantauan kehamilan: Bagi ibu hamil, telemedicine menyediakan cara yang nyaman untuk memantau perkembangan kehamilan dan mendapatkan nasihat medis",
        "Menyediakan bantuan untuk pengobatan alternatif: Telemedicine dapat memberikan akses ke dokter yang memahami dan mendukung pengobatan alternatif atau holistik",
        "Meningkatkan kesehatan mental: Telemedicine memungkinkan saya untuk mendapatkan bantuan intellectual dan emosional tanpa harus meninggalkan rumah",
        "Mendapatkan rekomendasi terkait vaksinasi: Melalui telemedicine, saya dapat berkonsultasi dengan dokter untuk mendapatkan rekomendasi vaksinasi yang sesuai untuk saya atau keluarga saya",
        "Pengobatan untuk kondisi kulit: Telemedicine dapat memberikan konsultasi dan perawatan untuk masalah kulit seperti jerawat atau eksim",
        "Membantu pencegahan penyakit: Dengan telemedicine, saya dapat berkonsultasi dengan dokter tentang langkah-langkah pencegahan untuk menjaga kesehatan saya",
        "Mendapatkan bantuan untuk masalah tidur: Telemedicine dapat memberikan konsultasi untuk masalah tidur seperti insomnia atau gangguan tidur lainnya",
        "Mengatasi kecemasan terkait kesehatan: Telemedicine membantu saya mengatasi kecemasan terkait kesehatan dengan memberikan akses cepat ke dokter",
        "Memfasilitasi perawatan di rumah sakit: Telemedicine dapat digunakan di rumah sakit untuk konsultasi antardokter atau pemeriksaan pasien jarak jauh",
        "Mendapatkan saran gizi: Melalui telemedicine, saya dapat berkonsultasi dengan ahli gizi untuk mendapatkan rekomendasi tentang pola makan yang sehat",
        "Akses ke perawatan gigi: Telemedicine dapat digunakan untuk konsultasi dan perawatan gigi, seperti saran perawatan rutin atau konsultasi darurat",
        "Mendapatkan perawatan bagi anak-anak: Telemedicine memungkinkan saya untuk mendapatkan perawatan medis untuk anak-anak saya tanpa harus membawa mereka ke dokter",
        "Meningkatkan kualitas hidup bagi orang tua: Telemedicine membantu orang tua untuk mendapatkan perawatan medis dengan lebih mudah, meningkatkan kualitas hidup mereka",
        "Mendapatkan saran untuk manajemen stres: Telemedicine dapat memberikan saran untuk manajemen stres dan kesehatan intellectual yang lebih baik",
        "Mendapatkan konsultasi tentang kesehatan reproduksi: Telemedicine menyediakan konsultasi untuk masalah kesehatan reproduksi seperti infertilitas atau kontrasepsi",
        "Mendapatkan dukungan untuk kondisi kronis: Telemedicine membantu saya mendapatkan dukungan dan manajemen yang tepat untuk kondisi kronis seperti asma atau arthritis",
        "Mengatasi hambatan mobilitas: Bagi mereka dengan hambatan mobilitas, telemedicine memberikan akses mudah ke perawatan medis dari kenyamanan rumah",
        "Mendapatkan saran tentang perawatan mata: Telemedicine dapat digunakan untuk konsultasi dan perawatan masalah mata seperti rabun jauh atau iritasi mata",
        "Membantu manajemen berat badan: Melalui telemedicine, saya dapat mendapatkan bantuan dalam manajemen berat badan dan perencanaan application kebugaran",
        "Mendapatkan perawatan untuk masalah saluran pernapasan: Telemedicine memungkinkan konsultasi untuk masalah seperti batuk, pilek, atau infeksi saluran pernapasan",
        "Mengakses terapi fisik dan rehabilitasi: Telemedicine dapat digunakan untuk mendapatkan panduan dan latihan fisioterapi dari jarak jauh",
        "Mendapatkan rekomendasi untuk manajemen nyeri: Telemedicine memberikan akses ke dokter untuk mendapatkan rekomendasi tentang pengelolaan nyeri kronis atau akut",
        "Mendapatkan bantuan untuk perawatan luka: Telemedicine dapat digunakan untuk konsultasi dan perawatan luka ringan atau bekas operasi",
        "Menyediakan bantuan untuk perawatan ortopedi: Telemedicine memungkinkan konsultasi tentang cedera atau kondisi ortopedi seperti nyeri punggung atau sakit lutut",
        "Mendapatkan resep obat untuk kondisi umum: Telemedicine memberikan kemudahan untuk mendapatkan resep obat untuk kondisi umum seperti infeksi, alergi, atau pilek",
        "Mendapatkan konsultasi tentang alergi: Telemedicine dapat digunakan untuk mendapatkan saran tentang pengelolaan alergi makanan, alergi obat, atau alergi lainnya",
        "Mengatasi gangguan pencernaan: Telemedicine memberikan akses ke konsultasi untuk gangguan pencernaan seperti GERD, sindrom iritasi usus, atau sembelit",
        "Mendapatkan saran tentang manajemen kesehatan jantung: Telemedicine dapat digunakan untuk konsultasi tentang pengelolaan risiko kesehatan jantung atau penyakit jantung yang sudah ada",
        "Mendapatkan bantuan untuk manajemen diabetes: Telemedicine memberikan akses ke konsultasi untuk pengelolaan diabetes, termasuk pemantauan glukosa darah dan manajemen gula darah",
        "Mendapatkan rekomendasi tentang penghentian merokok: Telemedicine dapat digunakan untuk mendapatkan dukungan dan rekomendasi tentang berhenti merokok",
        "Mendapatkan konsultasi tentang gangguan tidur: Telemedicine memungkinkan konsultasi untuk gangguan tidur seperti sleep apnea atau insomnia",
        "Mendapatkan saran tentang manajemen stres: Telemedicine memberikan akses ke konsultasi untuk manajemen stres dan kesehatan intellectual yang lebih baik",
        "Mendapatkan panduan tentang kebiasaan makan sehat: Telemedicine dapat digunakan untuk mendapatkan saran dan panduan tentang kebiasaan makan yang sehat dan nutrisi",
        "Mendapatkan konsultasi tentang kesehatan seksual: Telemedicine memberikan akses ke konsultasi untuk masalah kesehatan seksual seperti disfungsi ereksi atau infeksi menular seksual",
        "Mengakses sumber daya untuk pengelolaan asma: Telemedicine dapat digunakan untuk mendapatkan bantuan dan saran tentang pengelolaan asma",
        "Mendapatkan konsultasi tentang manajemen kelelahan: Telemedicine memungkinkan konsultasi untuk manajemen kelelahan kronis atau kelelahan yang berhubungan dengan kondisi kesehatan tertentu",
        "Mengatasi gangguan hormonal: Telemedicine memberikan akses ke konsultasi untuk gangguan hormonal seperti hipotiroidisme, PCOS, atau gangguan hormonal lainnya",
        "Mendapatkan dukungan untuk manajemen kesehatan mental anak-anak: Telemedicine dapat digunakan untuk mendapatkan dukungan dan saran tentang kesehatan mental anak-anak",
        "Mendapatkan konsultasi tentang manajemen kesehatan penuaan: Telemedicine memberikan akses ke konsultasi untuk manajemen kesehatan penuaan, termasuk pencegahan penyakit kronis dan perawatan geriatri",
    ],
    [
        "Pengalaman terakhir saya dengan layanan telemedicine sangat memuaskan",
        "Telemedicine membuat saya lebih nyaman karena saya bisa berkonsultasi dengan dokter dari kenyamanan rumah saya sendiri",
        "Layanan telemedicine sangat membantu saya saat saya sedang sibuk dan sulit untuk mengatur jadwal kunjungan ke dokter",
        "Pengalaman saya dengan telemedicine sangat efisien",
        "Telemedicine memungkinkan saya untuk mengakses perawatan medis berkualitas meskipun saya tinggal di daerah yang terpencil",
        "Saya merasa lebih aman menggunakan telemedicine karena saya bisa menghindari paparan terhadap penyakit lain di lingkungan klinik",
        "Layanan telemedicine memungkinkan saya untuk tetap mengikuti perkembangan kondisi kesehatan saya tanpa harus meninggalkan rumah",
        "Saya menemukan bahwa telemedicine sangat membantu dalam memantau kondisi kronis saya secara teratur",
        "Penggunaan telemedicine telah mengurangi biaya perjalanan dan waktu yang saya habiskan untuk pergi ke klinik",
        "Saya sangat menghargai kemudahan membuat janji dan mengakses layanan dengan telemedicine",
        "Telemedicine memberi saya akses ke spesialis yang mungkin sulit saya temui di daerah saya",
        "Saya merasa lebih terhubung dengan dokter saya melalui telemedicine karena saya dapat berbicara dengan mereka melalui video name",
        "Saya menemukan bahwa telemedicine memberi saya lebih banyak waktu untuk berbicara dengan dokter saya daripada kunjungan langsung",
        "Telemedicine memungkinkan saya untuk meminta resep obat secara langsung setelah konsultasi dengan dokter",
        "Saya merasa lebih diurus dengan baik oleh layanan telemedicine daripada dengan kunjungan langsung ke klinik",
        "Pengalaman saya dengan telemedicine membuat saya merasa lebih terlibat dalam pengelolaan kesehatan saya sendiri",
        "Layanan telemedicine membantu saya untuk mengatasi rasa cemas atau kekhawatiran tentang kesehatan saya dengan cepat",
        "Telemedicine memungkinkan saya untuk mendapatkan saran medis yang cepat dan tepat saat saya membutuhkannya",
        "Saya merasa lebih bebas mengungkapkan masalah kesehatan saya secara terbuka dengan dokter melalui telemedicine",
        "Pengalaman saya dengan telemedicine telah mengubah cara saya melihat perawatan kesehatan, dan saya lebih cenderung memilih opsi ini di masa depan",
        "Telemedicine membantu saya mengatasi hambatan geografis dalam mendapatkan akses ke perawatan medis yang saya butuhkan",
        "Saya menemukan bahwa telemedicine sangat cocok untuk konsultasi sederhana dan comply with-up rutin dengan dokter",
        "Layanan telemedicine memberi saya fleksibilitas untuk membuat janji konsultasi sesuai dengan jadwal saya yang padat",
        "Penggunaan telemedicine memungkinkan saya untuk tetap berada di dekat keluarga dan menjaga keseimbangan kehidupan pribadi dan profesional",
        "Saya merasa lebih puas dengan layanan telemedicine karena saya bisa lebih fokus pada percakapan dengan dokter tanpa gangguan dari lingkungan klinik",
        "Telemedicine telah memperluas jangkauan perawatan kesehatan, terutama bagi mereka yang memiliki mobilitas terbatas",
        "Saya merasa lebih terjamin dengan privasi dan kerahasiaan informasi kesehatan saya saat menggunakan layanan telemedicine",
        "Telemedicine membantu saya menghindari risiko infeksi yang mungkin terjadi di lingkungan klinik atau rumah sakit",
        "Saya menemukan bahwa dokter yang saya konsultasikan melalui telemedicine sangat ramah dan peduli terhadap kebutuhan saya",
        "Pengalaman saya dengan telemedicine memberi saya kesempatan untuk belajar lebih banyak tentang kondisi kesehatan saya dan cara mengelolanya",
        "Saya merasa lebih terdengar dan dipahami oleh dokter saya ketika menggunakan layanan telemedicine",
        "Telemedicine memberi saya akses yang lebih baik ke informasi medis dan sumber daya kesehatan secara online",
        "Saya merasa lebih santai dan tenang saat berbicara dengan dokter melalui telemedicine daripada saat bertemu langsung di klinik",
        "Penggunaan telemedicine telah mengurangi stres dan kecemasan saya terkait pergi ke dokter atau klinik",
        "Saya menemukan bahwa dokter yang saya konsultasikan melalui telemedicine sangat responsif terhadap pertanyaan dan kekhawatiran saya",
        "Telemedicine memungkinkan saya untuk tetap mendapatkan perawatan medis berkualitas bahkan saat saya sedang bepergian atau berada di luar kota",
        "Saya merasa lebih terorganisir dalam memantau kondisi kesehatan saya dengan bantuan layanan telemedicine",
        "Layanan telemedicine membantu saya merasa lebih mandiri dalam mengelola kesehatan saya sendiri",
        "Saya merasa lebih puas dengan kualitas perawatan yang saya terima melalui telemedicine daripada kunjungan langsung ke dokter",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih terhubung dengan sumber daya kesehatan yang tersedia di komunitas saya",
        "Telemedicine telah meningkatkan aksesibilitas perawatan kesehatan bagi saya, terutama dalam situasi darurat atau mendesak",
        "Saya menemukan bahwa telemedicine sangat cocok untuk konsultasi rutin dengan dokter spesialis tanpa harus menghadiri janji temu langsung",
        "Layanan telemedicine memungkinkan saya untuk mendapatkan pendapat kedua dari dokter yang berbeda dengan mudah dan cepat",
        "Saya merasa lebih diurus dengan baik dan didukung secara pribadi oleh dokter saya melalui telemedicine",
        "Pengalaman saya dengan telemedicine telah memberikan solusi yang lebih efisien bagi masalah kesehatan saya daripada metode tradisional",
        "Telemedicine telah mengurangi waktu yang saya habiskan dalam antrean dan menunggu di klinik atau rumah sakit",
        "Saya merasa lebih puas dengan pengalaman konsultasi online daripada kunjungan ke dokter yang seringkali terasa terburu-buru",
        "Layanan telemedicine memungkinkan saya untuk mengakses rekam medis dan riwayat kesehatan saya dengan mudah dari mana saja",
        "Saya menemukan bahwa dokter yang saya konsultasikan melalui telemedicine lebih memahami situasi saya secara menyeluruh dan memberikan rekomendasi yang lebih non-public",
        "Telemedicine memberi saya kesempatan untuk lebih aktif terlibat dalam perawatan kesehatan saya sendiri dan mengambil keputusan yang lebih baik",
        "Saya merasa lebih tenang dan terjamin dengan pemantauan kesehatan rutin saya melalui telemedicine",
        "Pengalaman saya dengan telemedicine telah membantu saya mengatasi hambatan bahasa dalam mendapatkan perawatan medis",
        "Saya merasa lebih efisien dalam mengelola waktu dan jadwal saya dengan bantuan layanan telemedicine",
        "Telemedicine telah memberikan akses yang lebih baik bagi saya untuk mempelajari tentang kondisi kesehatan saya dan cara-cara untuk menjaga kesehatan secara umum",
        "Saya merasa lebih terbantu dan didukung dalam mengatasi perubahan gaya hidup dan perubahan kesehatan yang dibutuhkan melalui telemedicine",
        "Penggunaan telemedicine telah membantu saya menghindari absen kerja yang tidak perlu untuk kunjungan medis",
        "Saya menemukan bahwa layanan telemedicine sangat mudah digunakan, bahkan bagi orang yang kurang berpengalaman dalam teknologi",
        "Telemedicine memberi saya kebebasan untuk memilih dokter yang sesuai dengan kebutuhan dan preferensi saya",
        "Saya merasa lebih aman dan terlindungi dari risiko infeksi saluran pernapasan dengan menggunakan telemedicine",
        "Pengalaman saya dengan telemedicine telah meningkatkan kualitas hidup saya secara keseluruhan dengan memberikan akses yang lebih mudah dan efisien ke perawatan kesehatan yang saya butuhkan",
        "Telemedicine telah mengurangi beban finansial bagi saya dengan mengurangi biaya transportasi dan waktu yang dikeluarkan untuk kunjungan medis",
        "Saya merasa lebih terlibat dalam proses perawatan saya sendiri melalui telemedicine, karena saya lebih aktif dalam mendiskusikan pilihan perawatan dengan dokter",
        "Layanan telemedicine memungkinkan saya untuk mengajukan pertanyaan atau kekhawatiran kesehatan saya secara real-time dan mendapatkan tanggapan cepat dari dokter",
        "Saya merasa lebih diperhatikan dan didengarkan oleh dokter saya melalui telemedicine, karena mereka cenderung memberikan perhatian penuh pada saya selama konsultasi",
        "Telemedicine membantu saya merasa lebih terhubung dengan dunia medis dan mendapatkan akses ke informasi kesehatan terbaru",
        "Pengalaman saya dengan telemedicine telah membantu saya mengembangkan hubungan yang lebih baik dengan dokter saya, karena kami bisa berkomunikasi secara lebih teratur",
        "Saya merasa lebih puas dengan pengalaman konsultasi telemedicine daripada kunjungan ke dokter tradisional karena kenyamanan dan efisiensinya",
        "Telemedicine memungkinkan saya untuk mengatur jadwal konsultasi sesuai dengan kebutuhan dan kenyamanan saya sendiri",
        "Saya merasa lebih terbantu dalam mengatasi masalah kesehatan sehari-hari melalui konsultasi telemedicine yang cepat dan mudah",
        "Penggunaan telemedicine telah memberikan saya kepercayaan diri yang lebih besar dalam mengelola kondisi kesehatan saya sendiri",
        "Saya merasa lebih dipertimbangkan oleh dokter saya melalui telemedicine karena mereka dapat melihat riwayat kesehatan saya secara lengkap dan mendalam",
        "Telemedicine memungkinkan saya untuk mendapatkan rekomendasi pengobatan yang tepat sesuai dengan kondisi kesehatan saya, tanpa harus menunggu lama di klinik",
        "Saya merasa lebih dihargai sebagai pasien melalui telemedicine karena dokter saya memberikan perhatian penuh pada kebutuhan dan kekhawatiran saya",
        "Layanan telemedicine memungkinkan saya untuk mendapatkan akses ke perawatan kesehatan yang sama dengan kunjungan langsung ke klinik, tanpa harus meninggalkan rumah",
        "Saya merasa lebih nyaman dan tenang saat berbicara dengan dokter melalui telemedicine karena suasana yang lebih santai dan terkontrol",
        "Telemedicine membantu saya merasa lebih termotivasi untuk memantau dan menjaga kesehatan saya secara rutin",
        "Saya merasa lebih diperhatikan dan dirawat secara individual melalui telemedicine karena dokter saya memperhatikan kebutuhan kesehatan saya secara khusus",
        "Pengalaman saya dengan telemedicine telah membantu saya menghemat waktu dan tenaga yang sebelumnya saya habiskan untuk pergi ke klinik",
        "Saya merasa lebih terbantu dalam mengelola penyakit kronis saya melalui telemedicine karena saya dapat dengan mudah berkomunikasi dengan dokter saya secara teratur",
        "Telemedicine memberikan saya kebebasan untuk memilih dokter yang sesuai dengan kebutuhan dan preferensi saya, tanpa terbatas oleh lokasi geografis",
        "Penggunaan telemedicine telah mengurangi kecemasan saya terkait perawatan medis, karena saya bisa mendapatkan bantuan dengan cepat dan mudah melalui konsultasi on line",
        "Saya merasa lebih terbantu dalam menghadapi situasi darurat kesehatan melalui telemedicine karena saya dapat menghubungi dokter dengan cepat tanpa harus pergi ke rumah sakit",
        "Telemedicine memungkinkan saya untuk mengakses saran medis yang berkualitas dari dokter ahli di bidangnya, bahkan jika mereka berada di tempat yang jauh",
        "Saya merasa lebih terorganisir dalam mengelola kondisi kesehatan saya dengan bantuan telemedicine karena saya bisa memantau perkembangan saya secara sistematis",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih percaya diri dalam mengelola gejala penyakit atau kondisi kesehatan yang mungkin saya alami",
        "Saya merasa lebih dihargai sebagai individu melalui telemedicine karena dokter saya memberikan perhatian penuh pada kebutuhan dan preferensi saya",
        "Telemedicine memungkinkan saya untuk mengakses perawatan kesehatan yang berkualitas tanpa harus mengorbankan banyak waktu atau uang",
        "Saya merasa lebih terbantu dalam mengelola stres dan kekhawatiran terkait kesehatan saya melalui telemedicine karena saya dapat berbicara dengan dokter secara langsung",
        "Penggunaan telemedicine telah meningkatkan kepatuhan saya terhadap rencana perawatan medis saya karena akses yang lebih mudah dan nyaman",
        "Saya merasa lebih terkoneksi dengan dunia medis dan perkembangan terbaru dalam bidang kesehatan melalui telemedicine",
        "Telemedicine memberi saya kesempatan untuk berkolaborasi dengan dokter saya dalam merencanakan perawatan yang terbaik untuk kebutuhan kesehatan saya",
        "Saya merasa lebih terbantu dalam mengatasi perubahan gaya hidup yang diperlukan untuk meningkatkan kesehatan saya melalui telemedicine",
        "Pengalaman saya dengan telemedicine telah membantu saya merasa lebih terkontrol atas kesehatan saya sendiri",
        "Saya merasa lebih tenang dan terjamin dengan kualitas perawatan medis yang saya terima melalui telemedicine",
        "Telemedicine memungkinkan saya untuk memantau kondisi kesehatan saya secara teratur tanpa harus meninggalkan rumah atau kantor",
        "Saya merasa lebih dipahami dan didukung dalam mengatasi tantangan kesehatan saya melalui telemedicine",
        "Penggunaan telemedicine telah membantu saya merencanakan perawatan jangka panjang yang lebih efektif untuk kondisi kesehatan saya",
        "Saya merasa lebih terbantu dalam memahami hasil tes dan diagnosa medis saya melalui telemedicine karena dokter saya dapat menjelaskannya secara rinci",
        "Telemedicine memungkinkan saya untuk mengakses layanan kesehatan yang sama dengan kunjungan langsung ke klinik tanpa harus meninggalkan rumah",
        "Pengalaman saya dengan telemedicine telah meningkatkan kualitas hidup saya secara keseluruhan dengan memberikan akses yang lebih mudah dan nyaman ke perawatan kesehatan yang saya butuhkan",
    ],
]

kategori = [
    11,0,89
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
        chrome_options.add_argument("user-data-dir=C:\\Users\\ACER\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\1.KERJOAN\\bot\\chromedriver\\chromedriver.exe', options=chrome_options)
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
