import random
import time
import data

# ===================================================================================================

index = 0
times = 75

kategori = [
    11, # negatif
    0,
    64
]

soal = [10, 20]

def sejak(usia) :
    if usia <= 21 :
        sejak = random.choice(["smp", "SMP", "SMA", "sma", "Smp", "Sma", "Sekolah", "sekolah", "4 tahun lalu", "3 tahun lalu", "2 tahun lalu", "1 tahun lalu", "baru", "baru baru ini", "akhir akhir ini", "beberapa bulan lalu", "2021", "2020", "2022", "2023"])
    elif usia <= 24 :
        sejak = random.choice(["smp", "SMP", "SMA", "sma", "Smp", "Sma", "Kuliah", "kuliah", "5 tahun lalu", "4 tahun lalu", "3 tahun lalu", "2 tahun lalu", "1 tahun lalu", "baru", "baru baru ini", "akhir akhir ini", "beberapa bulan lalu", "2021", "2020", "2022", "2023", "2020 awal"])
    else :
        sejak = random.choice(["SMP", "SMA", "sma", "Smp", "Sma", "Kuliah", "kuliah", "5 tahun lalu", "4 tahun lalu", "3 tahun lalu", "2 tahun lalu", "1 tahun lalu", "baru", "baru baru ini", "akhir akhir ini", "beberapa bulan lalu", "2021", "2020", "2022", "2023", "2020 awal"])

    return sejak

def pekerjaan(usia) :
    if usia <= 19 :
        pekerjaan = random.choice(["siswi", "Siswi", "SISWI", "Pelajar", "pelajar"])
    elif usia <= 21 :
        pekerjaan = random.choice(["siswi", "Siswi", "SISWI", "Pelajar", "pelajar", "Mahasiswi", "mahasiswi"])
    elif usia <= 24 :
        pekerjaan = random.choice(["Mahasiswi", "mahasiswi", "pegawai", "Pegawai", "Pekerja", "Karyawan", "Buruh", "karyawan", "karyawan swasta"])
    else :
        pekerjaan = random.choice(["mahasiswi", "pegawai", "Pegawai", "Pekerja", "Karyawan", "Buruh", "karyawan", "karyawan swasta", "Pegawai Negeri", "Staff"])

    return pekerjaan
