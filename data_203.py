import random
import time
import data

# ===================================================================================================

index = 90
times = 10

soal = [15,9]

listUniv = [
    "UPN Veteran Yogyakarta",
    "Universitas Atma Jaya Yogyakarta",
    "Universitas Mercu Buana Yogyakarta",
    "Sekolah Tinggi Ilmu Ekonomi YKPN",
    "Akademi Akuntansi YKPN",
    "Universitas Sanata Dharma",
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
    if usia == 0 :
        return 4
    elif usia == 1 :
        return data.hitungUsia(4,5)
    else :
        return random.choice([4,4,5,5,5,5,6,7])