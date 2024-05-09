import random
import time
import data

# ===================================================================================================

index = 0
times = 1

jawaban = [
    8,0,42
]

pendidikan = [
    "SMA/SMK Sederajat",
    "D3",
    "S1",
    "S2",
    "S3",
]

pekerjaan = [
    "Pelajar/Mahasiswa",
    "Bekerja",
    "Belum Bekerja",
    "Tidak Bekerja"
]

soal = [28,9,16,15,20,18,15]

def pendidikan() :
    pil = random.choice([0,1,2,2,2,2,2,2,2,2,2,2,2,3,4])
    return pendidikan[pil]

def pekerjaan() :
    pil = random.choice([0,1,1,1,2,3])
    return pekerjaan[pil]