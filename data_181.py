import random
import time
import data

# ===================================================================================================

index = 74
times = 26 #100

kategori = [
    [
        88, 12# follow
    ],
]

jawab = [
    [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [3,2,3,2,2,2,2,2,3,2,3,2,2,3,2,2,3,2,2,2,3,2,2,2,3,3,2],
    [5,5,5,5,5,5,5,5,4,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,6,4,5,4,5,6,6,5,6,4,5,5,5,6,6,4,6,6,6,4,5,4,6,4,4,5],
    [5,4,5,4,4,5,5,5,4,5,5,5,4,5,4,5,5,5,4,5,5,5,4,5,5,5,5],
    [2,3,2,3,2,3,2,3,3,4,2,3,2,3,2,2,2,2,3,3,2,3,2,4,2,2,3],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,5,6,6,6,5,5,6,5,5,6,6,6,6,5,5,6,5,5,6,6,6,6,5,6,6,6],
    [5,6,5,6,5,4,5,5,4,5,5,6,5,6,5,5,5,5,6,5,5,6,5,5,5,5,6],
    [6,6,6,5,6,6,5,6,6,6,6,5,6,6,6,5,6,5,6,6,6,5,6,6,6,6,5],
    [5,6,6,5,6,5,6,5,5,5,6,6,5,6,6,6,6,6,6,5,6,6,6,5,6,6,6],
    [6,5,6,6,6,5,6,6,6,5,6,5,6,5,6,6,6,6,5,6,6,5,6,5,6,6,5],
    [6,6,6,4,6,5,6,6,5,5,6,5,6,6,5,6,6,6,6,6,6,5,6,5,6,6,5],
    [5,4,5,4,4,5,5,5,4,5,5,5,4,5,4,5,5,5,4,5,5,5,4,5,5,5,5],
    [4,5,4,5,5,5,5,5,4,5,4,5,6,5,4,5,4,5,5,5,4,5,5,5,4,4,5],
    [5,5,5,5,4,4,5,5,5,5,5,5,6,4,5,5,5,5,5,5,5,5,4,5,5,5,5],
    [6,5,5,5,5,5,5,6,6,5,5,5,4,6,4,5,5,5,5,6,5,5,5,5,5,5,5],
    [5,6,5,6,5,4,5,5,4,5,5,6,5,6,5,5,5,5,6,5,5,6,5,5,5,5,6],
    [4,5,4,5,5,5,5,5,4,5,4,5,6,5,4,5,4,5,5,5,4,5,5,5,4,4,5],
    [6,5,5,4,4,4,4,5,5,5,5,4,5,5,6,4,5,4,5,5,5,4,4,5,5,5,4],
    [6,5,6,6,6,5,6,6,6,5,6,5,6,5,6,6,6,6,5,6,6,5,6,5,6,6,5],
    [6,5,6,5,5,5,6,6,6,6,6,5,6,5,5,6,6,6,5,6,6,5,5,6,6,6,5],
    [5,6,5,6,5,4,5,5,4,5,5,6,5,6,5,5,5,5,6,5,5,6,5,5,5,5,6],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [5,6,6,5,6,5,6,5,5,5,6,6,5,6,6,6,6,6,6,5,6,6,6,5,6,6,6],
    [6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,5,5,5,5,5,5,6,6,5,5,5,4,6,4,5,5,5,5,6,5,5,5,5,5,5,5],
    [6,5,5,5,5,5,5,6,6,5,5,5,4,6,4,5,5,5,5,6,5,5,5,5,5,5,5],
    [5,4,5,4,4,5,5,5,4,5,5,5,4,5,4,5,5,5,4,5,5,5,4,5,5,5,5],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,5,5,5,5,5,5,5,5,5,5,5,5,5,6,5,5,5,5,5,5,5,5,5,5,5,5],
    [6,5,6,5,5,5,5,5,5,5,6,5,5,6,6,5,6,5,5,5,6,5,5,5,6,6,5],
    [5,5,5,5,5,5,5,5,4,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,4,4,5,5,5,4,5,5,4,5,5,5,5,4,4,4,4,4,5,5,5,5,4,5,4,5],
    [6,6,6,5,6,6,6,6,5,6,6,5,6,6,5,6,6,6,6,6,6,5,6,6,6,6,5],
    [4,5,4,5,5,5,5,5,4,5,4,5,6,5,4,5,4,5,5,5,4,5,5,5,4,4,5],
    [6,5,6,6,6,5,5,6,5,5,6,6,6,6,5,5,6,5,5,6,6,6,6,5,6,6,6],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,5,6,5,6,6,6,5,5,5,6,5,6,6,6,6,6,6,5,5,6,5,6,5,6,6,5],
    [6,6,6,5,6,6,6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,6,6,5,6,6,6],
    [6,6,6,5,6,6,6,6,5,6,6,5,6,6,5,6,6,6,6,6,6,5,6,6,6,6,5],
    [6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,6,6,5,5,6,6,5,4,6,6,5,5,6,5,6,6,6,6,5,6,5,5,6,6,6,5],
    [5,4,4,5,5,5,4,5,5,4,5,5,5,5,4,4,4,4,4,5,5,5,5,4,5,4,5],
    [2,3,2,3,2,3,2,3,3,4,2,3,2,3,2,2,2,2,3,3,2,3,2,4,2,2,3],
    [5,6,6,5,5,6,6,5,4,6,6,5,5,6,5,6,6,6,6,5,6,5,5,6,6,6,5],
    [6,6,6,5,6,6,6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,6,6,5,6,6,6],
    [5,5,5,5,4,4,5,5,5,5,5,5,6,4,5,5,5,5,5,5,5,5,4,5,5,5,5],
    [5,5,5,5,4,4,5,5,5,5,5,5,6,4,5,5,5,5,5,5,5,5,4,5,5,5,5],
    [6,5,6,5,5,5,5,5,5,5,6,5,5,6,6,5,6,5,5,5,6,5,5,5,6,6,5],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [5,6,6,5,5,6,6,5,4,6,6,5,5,6,5,6,6,6,6,5,6,5,5,6,6,6,5],
    [5,4,5,5,5,4,5,5,4,5,4,5,4,5,4,5,5,5,4,5,4,5,5,5,4,5,5],
    [5,4,4,5,5,5,4,5,5,4,5,5,5,5,4,4,4,4,4,5,5,5,5,4,5,4,5],
    [5,6,5,6,5,4,5,5,4,5,5,6,5,6,5,5,5,5,6,5,5,6,5,5,5,5,6],
    [5,5,5,5,5,5,5,5,4,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [6,6,6,5,6,6,5,6,6,6,6,5,6,6,6,5,6,5,6,6,6,5,6,6,6,6,5],
    [5,6,4,5,4,5,6,6,5,6,4,5,5,5,6,6,4,6,6,6,4,5,4,6,4,4,5],
    [6,5,6,5,6,6,6,5,5,5,6,5,6,6,6,6,6,6,5,5,6,5,6,5,6,6,5],
    [5,5,6,6,5,5,5,5,5,5,6,6,4,6,5,5,6,5,5,5,6,6,5,5,6,6,6],
    [3,2,3,2,2,2,2,2,3,2,3,2,2,3,2,2,3,2,2,2,3,2,2,2,3,3,2],
    [6,5,6,5,5,5,6,6,6,6,6,5,6,5,5,6,6,6,5,6,6,5,5,6,6,6,5],
    [6,6,6,4,6,5,6,6,5,5,6,5,6,6,5,6,6,6,6,6,6,5,6,5,6,6,5],
    [4,5,4,5,5,5,5,5,4,5,4,5,6,5,4,5,4,5,5,5,4,5,5,5,4,4,5],
    [5,6,6,5,6,5,6,5,5,5,6,6,5,6,6,6,6,6,6,5,6,6,6,5,6,6,6],
    [6,5,5,5,5,5,5,5,5,5,5,5,5,5,6,5,5,5,5,5,5,5,5,5,5,5,5],
    [6,5,6,6,6,5,6,6,6,5,6,5,6,5,6,6,6,6,5,6,6,5,6,5,6,6,5],
    [5,5,6,6,5,5,5,5,5,5,6,6,4,6,5,5,6,5,5,5,6,6,5,5,6,6,6],
    [6,5,6,5,6,6,6,5,5,5,6,5,6,6,6,6,6,6,5,5,6,5,6,5,6,6,5],
    [6,5,6,6,6,5,5,6,5,5,6,6,6,6,5,5,6,5,5,6,6,6,6,5,6,6,6],
    [5,5,6,6,5,5,5,5,5,5,6,6,4,6,5,5,6,5,5,5,6,6,5,5,6,6,6],
    [6,6,6,5,6,6,6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,6,6,5,6,6,6],
    [6,6,6,5,6,6,6,6,5,6,6,5,6,6,5,6,6,6,6,6,6,5,6,6,6,6,5],
    [5,6,4,5,4,5,6,6,5,6,4,5,5,5,6,6,4,6,6,6,4,5,4,6,4,4,5],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,5,6,6,6,5,6,6,6,5,6,5,6,5,6,6,6,6,5,6,6,5,6,5,6,6,5],
    [6,6,6,4,6,5,6,6,5,5,6,5,6,6,5,6,6,6,6,6,6,5,6,5,6,6,5],
    [5,6,6,5,5,6,6,5,4,6,6,5,5,6,5,6,6,6,6,5,6,5,5,6,6,6,5],
    [5,4,5,5,5,4,5,5,4,5,4,5,4,5,4,5,5,5,4,5,4,5,5,5,4,5,5],
    [2,3,2,3,2,3,2,3,3,4,2,3,2,3,2,2,2,2,3,3,2,3,2,4,2,2,3],
    [6,5,5,5,5,5,5,5,5,5,5,5,5,5,6,5,5,5,5,5,5,5,5,5,5,5,5],
    [3,2,3,2,2,2,2,2,3,2,3,2,2,3,2,2,3,2,2,2,3,2,2,2,3,3,2],
    [5,5,5,5,5,5,5,5,4,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [5,4,4,5,5,5,4,5,5,4,5,5,5,5,4,4,4,4,4,5,5,5,5,4,5,4,5],
    [6,5,5,4,4,4,4,5,5,5,5,4,5,5,6,4,5,4,5,5,5,4,4,5,5,5,4],
    [6,5,6,5,5,5,6,6,6,6,6,5,6,5,5,6,6,6,5,6,6,5,5,6,6,6,5],
    [2,3,2,3,2,3,2,3,3,4,2,3,2,3,2,2,2,2,3,3,2,3,2,4,2,2,3],
    [5,4,5,5,5,4,5,5,4,5,4,5,4,5,4,5,5,5,4,5,4,5,5,5,4,5,5],
    [5,6,6,5,6,5,6,5,5,5,6,6,5,6,6,6,6,6,6,5,6,6,6,5,6,6,6],
    [5,4,5,4,4,5,5,5,4,5,5,5,4,5,4,5,5,5,4,5,5,5,4,5,5,5,5],
    [5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,5,5,4,4,4,4,5,5,5,5,4,5,5,6,4,5,4,5,5,5,4,4,5,5,5,4],
    [3,2,3,2,2,2,2,2,3,2,3,2,2,3,2,2,3,2,2,2,3,2,2,2,3,3,2],
    [6,5,5,4,4,4,4,5,5,5,5,4,5,5,6,4,5,4,5,5,5,4,4,5,5,5,4],
    [6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [5,5,5,5,4,4,5,5,5,5,5,5,6,4,5,5,5,5,5,5,5,5,4,5,5,5,5],
]

domisiliList = [
    "Bogor", "Depok", "Tangerang", "Bekasi", 
    "Cikarang", "Karawang", "Serang", "Cilegon", 
    "Sukabumi", "Purwakarta", "Tangerang Selatan", 
    "Bekasi Selatan", "Bekasi Barat", "Bekasi Timur", 
    "Bekasi Utara",
]

def domisili() :
    return random.choice(domisiliList)

def pendidikan(usia) :
    if usia == 2 :
        result = random.choice([7,7,7,8])
    elif usia == 3 :
        result = random.choice([7,8,8])
    else :
        result = random.choice([7,7,7,8,8,8,8,8,9])

    return result

def pekerjaan(kelamin, pendidikan, usia) :
    if kelamin == 1 :
        if pendidikan == 7 :
            if usia == 2 :
                result = 15
            else :
                result = random.choice([16,18,19,20])
        elif pendidikan == 8 :
            if usia == 2 :
                result = random.choice([15,16,18,19])
            else :
                result = random.choice([16,17,18,19,20])
        else :
            result = random.choice([16,17,18,19,20])

    else :
        if pendidikan == 7 :
            if usia == 2 :
                result = 15
            else :
                result = random.choice([16,18,19])
        elif pendidikan == 8 :
            if usia == 2 :
                result = random.choice([15,16,18,19])
            else :
                result = random.choice([16,17,18,19])
        else :
            result = random.choice([16,17,18,19])

    return result

def pengeluaran(pekerjaan) :
    if pekerjaan == 15 :
        result = 11
    else :
        result = random.choice([11,11,11,12,12,12,13,14])
    
    return result

