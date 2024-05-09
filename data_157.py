import random
import time
import data

# ===================================================================================================

index = 0
times = 30

kategori = [
    [
        22, 8
    ],
    [
        24, 6
    ]
]

alasan = [
    [
        [
            "Keterlibatan dalam proyek-proyek riset kampus menjadi bukti nyata bahwa saya memiliki komitmen untuk menggali lebih dalam dalam bidang studi ini",
            "Selain itu, saya aktif dalam kegiatan ekstrakurikuler yang berkaitan dengan teknologi, seperti mengikuti kompetisi pemrograman dan menjadi anggota tim pengembangan aplikasi",
            "Dengan latar belakang pendidikan di bidang matematika dan ilmu komputer, saya memiliki dasar pengetahuan yang kuat, suatu hal yang penting untuk mengejar studi di jurusan teknik informatika yang sering kali melibatkan konsep-konsep matematis dan pemrograman",
            "Saya telah menunjukkan minat dan keahlian dalam pemrograman dan pengembangan perangkat lunak sejak sekolah menengah, yang mencerminkan ketertarikan saya yang mendalam terhadap bidang teknik informatika",
            "Mengetahui perkembangan terkini dan tren industri melalui literatur dan media khusus menjadikan saya semakin yakin bahwa jurusan ini adalah pilihan yang tepat",
            "Partisipasi aktif dalam kegiatan ekstrakurikuler seperti olimpiade sains dan seminar ilmiah telah memperdalam pengetahuan saya tentang bidang ini",
            "Memiliki proyek-proyek sampingan atau hobi yang berkaitan dengan jurusan ini menggambarkan keselarasan minat dan kegiatan di luar akademis",
            "Keikutsertaan dalam proyek-proyek penelitian selama masa sekolah telah memupuk minat dan keterampilan dalam jurusan yang saya pilih",
            "Keterlibatan dalam proyek-proyek kemanusiaan yang melibatkan ilmu yang saya pelajari memotivasi saya untuk terus berkontribusi pada kesejahteraan masyarakat",
            "Ketertarikan dalam mengikuti seminar dan konferensi di luar kampus menunjukkan hasrat saya untuk terus belajar dan mengikuti perkembangan ilmu di jurusan ini",
            "Keterampilan komunikasi dan pemecahan masalah yang saya kembangkan selama kursus-kursus terkait menjadi nilai tambah untuk berhasil berkarier dalam bidang ini",
            "Keinginan untuk terus berkembang dan memberikan dampak positif pada dunia menjadi daya dorong utama saya dalam memilih jurusan ini",
            "Proyek-proyek kolaboratif dengan teman sekelas menunjukkan kemampuan saya dalam bekerja sama dan bersinergi dalam lingkungan akademis",
            "Meniti jalur pendidikan ini adalah bagian dari mimpi saya sejak kecil, dan saya telah menetapkan tujuan karier yang jelas dalam jurusan ini",
            "Minat yang mendalam dalam bidang ini telah termanifestasikan sejak masa sekolah menengah, di mana saya aktif mengikuti kegiatan ekstrakurikuler terkait",
            "Kepedulian terhadap isu-isu global yang berkaitan dengan bidang studi ini mendorong saya untuk memberikan kontribusi positif melalui pemahaman yang lebih dalam",
            "Keberhasilan dalam mata pelajaran terkait dengan jurusan ini, seperti matematika dan fisika, menjadi indikator kuat minat saya dalam memahami konsep-konsep tersebut",
            "Pemilihan mata kuliah kejuruan sejak awal perkuliahan menunjukkan keseriusan dan ketertarikan mendalam terhadap jurusan ini",
            "Keinginan untuk memecahkan tantangan-tantangan kompleks dalam bidang ini menjadi motivasi utama saya memilih jurusan ini",
            "Keterampilan analitis dan pemecahan masalah yang saya miliki sangat sesuai dengan tuntutan jurusan teknik informatika",
            "Keterlibatan dalam kegiatan organisasi mahasiswa terkait jurusan membuktikan bahwa saya memiliki semangat kepemimpinan dan tanggung jawab yang tinggi",
            "Partisipasi dalam kompetisi-kompetisi ilmiah telah memperkaya pengetahuan saya dan mengasah kemampuan kritis dalam bidang ini",
        ],
        [
            "Saya merasa kesulitan memahami konsep-konsep dasar matematika, yang merupakan komponen penting dalam jurusan teknik informatika",
            "Minat saya lebih tertuju pada bidang humaniora dan seni, sehingga saya merasa kurang termotivasi untuk menghadapi materi-materi teknis dalam studi teknik informatika",
            "Saya tidak memiliki pengalaman atau ketertarikan khusus dalam pemrograman sebelumnya, sehingga sulit bagi saya untuk membayangkan diri saya mengejar karir di bidang teknologi informasi",
            "Keterampilan analitis dan pemecahan masalah tidak termasuk kekuatan utama saya, dan saya lebih nyaman berada dalam lingkungan di mana aspek kreatif dan kolaboratif lebih dominan",
            "Saya merasa bahwa lingkungan kerja di bidang teknik informatika terlalu kompetitif dan kurang mendukung, yang tidak sesuai dengan preferensi dan gaya belajar saya",
            "Bahasa pemrograman dan teknologi baru sering kali sulit bagi saya untuk dipahami, dan saya merasa sulit untuk menyesuaikan diri dengan perubahan yang cepat di dunia teknologi",
            "Saya lebih tertarik pada bidang-bidang studi yang menekankan aspek interpersonal dan komunikasi, sementara jurusan teknik informatika lebih menekankan pada keterampilan teknis individu",
            "Meskipun saya menyadari pentingnya teknologi informasi dalam dunia modern, saya tidak merasa antusias atau termotivasi untuk mendalami aspek-aspek teknis yang mendalam di dalamnya",
        ]
    ],
    [
        [
            "Saya percaya bahwa perbedaan biologis antara pria dan wanita dapat memengaruhi minat intrinsik terhadap bidang tertentu, seperti ketertarikan pria pada bidang teknik dan wanita pada bidang kesehatan",
            "Seiring dengan peran tradisional yang sering ditemukan dalam masyarakat, terdapat kecenderungan bahwa pria lebih cenderung tertarik pada bidang-bidang yang menekankan keahlian teknis, sementara wanita lebih tertarik pada bidang-bidang yang membutuhkan kepekaan sosial dan emosional",
            "Penting untuk diakui bahwa preferensi dan minat terkait jurusan kuliah dapat dipengaruhi oleh pengalaman sosial dan budaya, di mana stereotip gender dapat memainkan peran dalam membentuk persepsi terhadap pilihan karir",
            "Meskipun tidak mutlak, ada kecenderungan bahwa pria dan wanita cenderung memilih jurusan yang secara historis dianggap sesuai dengan peran gender tradisional, seperti pria lebih tertarik pada ilmu komputer dan wanita pada bidang seni atau keperawatan",
            "Faktor-faktor psikologis dan biologis yang berbeda antara pria dan wanita dapat memberikan kontribusi pada minat yang berbeda terhadap jenis-jenis pekerjaan dan, oleh karena itu, jurusan kuliah yang sesuai",
            "Persepsi masyarakat terhadap kualitas tertentu yang dianggap lebih sesuai dengan jenis kelamin tertentu juga dapat memengaruhi minat seseorang terhadap pilihan jurusan kuliahnya",
            "Tidak dapat diabaikan bahwa norma-norma sosial dan ekspektasi masyarakat mengenai peran gender dapat membatasi pilihan jurusan seseorang, meskipun individu tersebut mungkin memiliki minat yang berbeda",
            "Seiring dengan pergeseran nilai dan norma sosial, semakin banyak bukti yang menunjukkan bahwa minat dan pilihan jurusan dapat sangat bervariasi, namun pengaruh jenis kelamin masih merupakan faktor yang signifikan",
            "Keyakinan saya adalah bahwa aspek biologis antara pria dan wanita dapat mempengaruhi ketertarikan bawaan terhadap bidang spesifik, seperti minat pria pada teknologi dan minat wanita pada bidang kesehatan",
            "Seiring dengan norma-norma sosial yang masih kuat, terlihat kecenderungan bahwa pria lebih suka terlibat dalam bidang yang menekankan keterampilan teknis, sementara wanita cenderung tertarik pada bidang yang membutuhkan kepekaan sosial dan emosional",
            "Pentingnya diakui bahwa pilihan dan ketertarikan dalam memilih jurusan kuliah dapat dipengaruhi oleh pengalaman sosial dan budaya, di mana stereotip gender dapat membentuk pandangan terhadap karier yang diambil",
            "Meskipun bersifat relatif, ada indikasi bahwa pria dan wanita memiliki kecenderungan untuk memilih jurusan yang sejalan dengan peran gender tradisional, seperti minat pria pada ilmu komputer dan minat wanita pada seni atau keperawatan",
            "Faktor-faktor psikologis dan biologis yang berbeda antara pria dan wanita mungkin berkontribusi pada ketertarikan yang berbeda terhadap jenis pekerjaan tertentu dan, oleh karena itu, jurusan kuliah yang dipilih",
            "Pandangan masyarakat terhadap karakteristik tertentu yang dianggap lebih cocok dengan jenis kelamin tertentu juga dapat mempengaruhi minat seseorang dalam memilih jurusan kuliahnya",
            "Sulit diabaikan bahwa norma-norma sosial dan harapan masyarakat terkait peran gender dapat membatasi pilihan jurusan, bahkan jika minat individu mungkin berbeda",
            "Dengan perubahan nilai dan norma sosial seiring waktu, semakin banyak bukti menunjukkan bahwa minat dan pilihan jurusan dapat sangat bervariasi, meskipun pengaruh jenis kelamin tetap relevan",
            "Meskipun perbedaan individu ada, terdapat kecenderungan bahwa pria lebih tertarik pada bidang pekerjaan yang memerlukan logika dan pemecahan masalah teknis, sementara wanita cenderung memilih bidang yang mengandalkan empati dan keterlibatan sosial",
            "Adanya stereotip gender dapat memengaruhi persepsi seseorang terhadap kecocokan dengan bidang studi tertentu, sehingga minat pada jurusan kuliah dapat tercermin dari harapan dan norma-norma gender yang ada",
            "Peran historis dalam pembagian pekerjaan antara pria dan wanita dapat menciptakan predisposisi terhadap pilihan jurusan kuliah, dengan pria lebih tertarik pada bidang-bidang yang dianggap lebih teknis dan wanita pada bidang-bidang yang dianggap lebih terkait dengan kepedulian sosial",
            "Ketertarikan terhadap teknologi dan ilmu komputer yang dominan dalam jurusan teknik informatika lebih umum ditemukan pada mahasiswa pria, sementara wanita sering kali lebih memilih jurusan yang menekankan kreativitas dan interaksi sosial",
            "Perbedaan dalam preferensi kognitif antara pria dan wanita dapat membentuk kecenderungan pada minat terhadap studi tertentu, seperti ketertarikan pria pada pemecahan masalah teknis dan wanita pada kolaborasi interpersonal",
            "Meskipun perkembangan sosial telah memperluas pilihan karier bagi pria dan wanita, norma sosial yang masih ada dapat memberikan tekanan pada individu untuk memilih jurusan yang dianggap sesuai dengan jenis kelamin mereka",
            "Pengaruh budaya dan tradisi dapat menciptakan harapan yang berbeda terkait pilihan karier, dan hal ini tercermin dalam minat seseorang pada jurusan kuliah yang sesuai dengan norma-norma gender yang ada",
            "Dalam mengatasi ketidaksetaraan gender di dunia pekerjaan, penting untuk memahami bagaimana faktor-faktor biologis dan sosial dapat memengaruhi minat dan pilihan jurusan kuliah antara pria dan wanita",
        ],
        [
            "Saya percaya bahwa minat dan bakat seseorang tidak seharusnya dikaitkan dengan jenis kelamin, karena setiap individu memiliki keunikan dan potensi yang tidak dapat diukur oleh parameter gender",
            "Penekanan pada perbedaan jenis kelamin dalam memilih jurusan dapat menciptakan stereotip dan mengabaikan variasi minat yang dapat dimiliki oleh setiap individu, terlepas dari apakah mereka pria atau wanita",
            "Pemikiran bahwa pria lebih cenderung tertarik pada bidang teknis dan wanita pada bidang sosial dapat mengabaikan perkembangan individu yang dinamis dan potensi minat yang berkembang seiring waktu",
            "Mempersempit pilihan jurusan berdasarkan jenis kelamin dapat menghambat perkembangan dan eksplorasi individu terhadap minat dan bakat yang mungkin belum mereka sadari sebelumnya",
            "Melibatkan jenis kelamin sebagai faktor penentu dalam pilihan jurusan dapat menghambat tercapainya kesetaraan gender dan mengukuhkan stereotip yang mungkin telah terbentuk",
            "Menilai minat dan kemampuan berdasarkan jenis kelamin dapat menyamakan individu dalam satu kategori dan mengabaikan keberagaman minat yang dapat ditemui di dalam masyarakat",
            "Pendidikan dan pemilihan jurusan seharusnya memberikan kebebasan kepada setiap individu untuk mengejar minat mereka tanpa harus merasa terikat oleh ekspektasi gender yang ada",
            "Dalam era modern yang semakin inklusif, mengikat minat dan pilihan jurusan pada jenis kelamin terasa ketinggalan zaman dan tidak mencerminkan perkembangan masyarakat yang lebih terbuka dan mendukung",
        ]
    ]
]

def pilihanPositif(tipe) :
    pilihan = kategori[tipe]
    if pilihan[0] != 0 and pilihan[1] != 0 :
        pil = random.choice([0,1])
    elif pilihan[0] != 0 and pilihan[1] == 0 :
        pil = 0
    elif pilihan[0] == 0 and pilihan[1] != 0 :
        pil = 1
    
    return pil

def kirimAlasan(tipe, pilih) :
    result = alasan[tipe][pilih][index]

    return result