import random
import time
import data

# ===================================================================================================

index = 99
times = 1
idxIsian = 29

kategori = [
    [
        1,0
    ],
    [
        1,0
    ]
]

isian = [
    "Mempunyai fitur pencatat pertemuan atau diskusi kinerja sebagai referensi ke depan",
        # "Menyediakan sistem pemantauan proyek atau tugas sebagai penilaian terhadap kontribusi karyawan",
    "Notifikasi otomatis untuk memperingatkan tentang tenggat waktu atau pencapaian target",
        # "Sistem penilaian yang dapat disesuaikan dengan tujuan dan KPI individu",
        # "Menyusun sistem penilaian yang dapat disesuaikan dengan tujuan dan KPI individu",
        # "Mengoperasikan sistem pemantauan proyek atau tugas sebagai alat penilaian kontribusi karyawan",
        # "Fitur identifikasi kebutuhan pelatihan berdasarkan hasil penilaian kinerja",
    "Menyajikan fitur identifikasi kebutuhan pelatihan berdasarkan hasil penilaian kinerja",
        # "Menggunakan analisis kesenjangan keterampilan sebagai landasan pengembangan karyawan",
    "Melakukan identifikasi gap keterampilan untuk merencanakan pengembangan karyawan",
    "Pengukuran produktivitas dan efisiensi dengan metrik yang dapat diukur",
        # "Mendorong interaksi antara atasan dan bawahan melalui fitur komunikasi yang terintegrasi",
    "Memberikan peringatan secara otomatis terkait batas waktu atau pencapaian target",
    "Mengirimkan notifikasi otomatis untuk mengingatkan tentang batas waktu atau pencapaian target",
    "Terintegrasi dengan alat kolaborasi untuk mendukung kerja tim dan proyek",
        # "Kuesioner penilaian diri untuk memberikan pandangan dari perspektif karyawan",
        # "Fitur pencatat pertemuan atau diskusi kinerja untuk referensi masa depan",
    "Sistem pemantauan proyek atau tugas untuk menilai kontribusi karyawan",
    "Integrasi dengan alat kolaborasi untuk mendukung kerja tim dan proyek",
    "Menyediakan fasilitas penyimpanan dan manajemen dokumen kinerja, termasuk portofolio pencapaian",
    "Memiliki fitur analisis data prediktif guna meramalkan tren kinerja di masa depan",
    "Menyediakan sistem peringkat atau skala penilaian yang mudah dimengerti",
        # "Memberikan penghargaan atau pengakuan atas pencapaian kinerja tertentu",
        # "Kemampuan untuk memberikan umpan balik secara langsung dan terstruktur",
    "Mengirimkan notifikasi otomatis untuk mengingatkan tentang batas waktu atau pencapaian target",
    "Analisis gap keterampilan untuk merencanakan pengembangan karyawan",
        # "Pengelolaan tujuan karyawan yang dapat diakses dan diperbarui secara fleksibel",
    "Grafik dan laporan kinerja untuk melihat perkembangan sepanjang waktu",
    "Mendorong dialog antara atasan dan bawahan melalui fitur komunikasi terintegrasi",
        # "Memberikan peringatan secara otomatis terkait batas waktu atau pencapaian target",
        # "Melakukan identifikasi gap keterampilan sebagai dasar untuk perencanaan pengembangan karyawan",
    "Fitur pemberian penghargaan atau pengakuan untuk pencapaian kinerja tertentu",
    "Integrasi dengan sistem manajemen sumber daya manusia (HRM) untuk data yang lebih terpadu",
        # "Memiliki kemampuan untuk memberikan umpan balik secara langsung dan terstruktur",
        # "Fitur analisis data prediktif untuk meramalkan tren kinerja masa depan",
    "Fitur pelacakan kinerja real-time untuk memonitor pencapaian tujuan karyawan",
    "Mengelola tujuan karyawan dengan fleksibilitas yang memungkinkan akses dan pembaruan",
    "Fitur benchmarking untuk membandingkan kinerja karyawan dengan rekan sejawat",
        # "Menghadirkan fitur identifikasi kebutuhan pelatihan berdasarkan hasil penilaian kinerja",
    "Melakukan pengukuran produktivitas dan efisiensi dengan metrik yang dapat diukur",
        # "Terintegrasi dengan sistem manajemen sumber daya manusia (HRM) untuk data yang lebih terpadu",
    "Mengirimkan notifikasi otomatis untuk memberi peringatan terkait tenggat waktu atau pencapaian target",
        # "Melakukan identifikasi gap keterampilan untuk merencanakan pengembangan karyawan",
        # "Menganalisis kebutuhan pelatihan berdasarkan hasil penilaian kinerja",
        # "Fasilitas untuk menyimpan dan mengelola dokumen-dokumen kinerja, seperti portofolio pencapaian",
    "Sistem peringkat atau skala penilaian yang jelas dan mudah dimengerti",
    "Melibatkan sistem pemantauan proyek atau tugas sebagai penilaian kontribusi karyawan",
    "Memberikan penghargaan atau pengakuan atas pencapaian kinerja tertentu",
        # "Menyusun skala penilaian atau sistem peringkat yang jelas dan mudah dimengerti",
    "Fitur komunikasi terintegrasi untuk mendukung dialog antara atasan dan bawahan",
    "Menyajikan fitur komunikasi terintegrasi guna memfasilitasi dialog antara atasan dan bawahan",
]

def sistem() :
    result = random.choice([4,4,4,4,5,6,7])
    return result