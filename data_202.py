import random
import time
import data

# ===================================================================================================

index = 0
times = 100

soal = [13,11]

listUniv = [
    "Universitas Atma Jaya Yogyakarta",
    "Universitas Islam Indonesia",
    "Universitas Gadjah Mada",
    "Universitas Gadjah Mada",
    "UGM",
    "UGM",
    "Universitas Sarjanawiyata",
    "Universitas Respati Yogyakarta",
    "Universitas Ahmad Dahlan",
    "UAD",
    "Universitas Alma Ata",
    "Politeknik API Yogyakarta",
    "Sekolah Tinggi Pertanahan Nasional",
    "Sekolah Tinggi Ilmu Ekonomi YKPN",
    "Universitas Negeri Yogyakarta",
    "UNY",
    "Akademi Akuntansi YKPN",
    "UPN Veteran Yogyakarta",
    "Universitas Cokroaminoto",
    "Akademi Maritim Yogyakarta",
    "Sekolah Tinggi Ilmu Kesehatan Panti Rapih",
    "Sekolah Tinggi Teknologi Nasional",
    "Sekolah Tinggi Bahasa Asing LIA Yogyakarta",
    "Sekolah Tinggi Ilmu Kesehatan Akbidyo",
    "Sekolah Tinggi Multi Media (MMTC)",
    "Sekolah Tinggi Manajemen ",
    "Universitas Proklamasi 45",
    "Poltekkes Kemenkes Yogyakarta",
    "Sekolah Tinggi Teknologi Nuklir Yogyakarta",
    "Akademi Komunikasi Indonesia YPK",
    "Politeknik LPP Yogyakarta",
    "Institut Teknologi Yogyakarta",
    "Universitas Muhammadiyah",
    "Sekolah Tinggi Ilmu Ekonomi Widya Wiwaha",
    "Sekolah Tinggi Pembangunan",
    "Universitas Janabadra",
    "Akademi Teknologi Kulit Yogyakarta",
    "Universitas AMIKOM Yogyakarta",
    "Sekolah Tinggi Teknologi Kedirgantaraan",
    "Institut Sains dan Teknologi Akprind",
    "Universitas Islam Negeri Sunan Kalijaga",
    "Institut Seni Indonesia Yogyakarta",
    "Akademi Manajemen Administrasi Yogyakarta",
    "Universitas Sanata Dharma",
    "Institut Pertanian Stiper",
    "Instiper",
]

listDesa = [
    "Desa Gamping Tengah",
    "Jalan Malioboro Utara",
    "Daerah Sleman Barat",
    "Desa Banguntapan Selatan",
    "Jalan Magelang Timur",
    "Daerah Bantul Selatan",
    "Desa Sewon Kulon",
    "Jalan Solo Barat",
    "Daerah Kota Gede Prawirotaman",
    "Desa Kalasan Timur",
    "Jalan Parangtritis Pantai Selatan",
    "Daerah Prambanan Tengah",
    "Desa Pleret Kidul",
    "Jalan Sudirman Utara",
    "Daerah Ngaglik Selatan",
    "Desa Sentolo Barat",
    "Jalan Kaliurang Utara",
    "Daerah Imogiri Timur",
    "Desa Berbah Lor",
    "Jalan Palagan Selatan",
    "Daerah Prawirotaman Kulon",
    "Desa Pandak Lor",
    "Jalan Wates Selatan",
    "Daerah Kotagede Timur",
    "Desa Mlati Kidul",
    "Jalan Tugu Barat",
    "Daerah Tirtodipuran Timur",
    "Desa Cangkringan Barat",
    "Jalan Gejayan Selatan",
    "Daerah Gunungkidul Pesisir",
    "Desa Seyegan Utara",
    "Jalan Prawirotaman Tengah",
    "Daerah Tamansari Kidul",
    "Desa Turi Timur",
    "Jalan Kusumanegara Barat",
    "Daerah Sedayu Selatan",
    "Desa Moyudan Lor",
    "Jalan Gedongkuning Puspa",
    "Daerah Plered Timur",
    "Desa Pakem Selatan",
    "Jalan Margo Utomo Permai",
    "Daerah Mergangsan Kulon",
    "Desa Kaliurang Timur",
    "Jalan Selokan Mataram Indah",
    "Daerah Ngemplak Kidul",
    "Desa Minggir Barat",
    "Jalan Ki Ageng Gribig Timur",
    "Daerah Bangunjiwo Kulon",
    "Desa Kalitirto Selatan",
    "Jalan Parangtritis Pantai Barat",
]

def univ() :
    return random.choice(listUniv)

def desa() :
    return random.choice(listDesa)

def penghasilan(usia) :
    if usia == 2 :
        return 6
    elif usia == 3 :
        return data.hitungUsia(6,7)
    else :
        return random.choice([6,6,7,7,7,7,8,9])