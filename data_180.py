import random
import time
import data

# ===================================================================================================

index = 99
times = 1

kategori = [
    [
        1,0
    ],
]

def pendidikan(usia) :
    if usia < 19 :
        result = 2
    elif usia < 25 :
        result = random.choice([2,3,4])
    else :
        result = random.choice([2,3,3,4,4,4,4,4,4,5])
    
    return result

def pekerjaan(kelamin, usia, pendidikan) :
    if kelamin == 1 :
        if pekerjaan == 2 and usia < 25 :
            result = 12
        elif pekerjaan == 2 :
            result = random.choice([9,10,14])
        elif pekerjaan == 3 :
            result = random.choice([8,9,9,9,10,14,15])
        else :
            result = random.choice([8,8,8,8,9,10,11,14,15])
    else :
        if pekerjaan == 2 and usia < 25 :
            result = 12
        elif pekerjaan == 2 :
            result = random.choice([9,10,14])
        elif pekerjaan == 3 :
            result = random.choice([8,9,9,9,10,15])
        else :
            result = random.choice([8,8,8,8,9,10,11,15])

    return result

def pengeluaran(pekerjaan) :
    if pekerjaan == 8 :
        result = random.choice([19,20,21])
    elif pekerjaan < 11 :
        result = random.choice([18,19,20,21])
    elif pekerjaan == 11 :
        result = random.choice([19,20,21])
    elif pekerjaan == 12 :
        result = random.choice([17,17,18,18,18,19])
    else :
        result = random.choice([18,19,20,21])
    
    return result

def domisili(tipeDom) :
    listKota = [
        [
            "Yogyakarta", "Surabaya", "Bandung", "Jakarta"
        ],
        [
            "Semarang", "Medan", "Makassar", "Denpasar", "Palembang", 
            "Manado", "Malang", "Solo", "Balikpapan", "Samarinda", "Pontianak", 
            "Banjarmasin", "Padang", "Ambon", "Pekanbaru", "Jambi", "Mataram", 
            "Palu", "Bengkulu", "Gorontalo",
        ],
    ]

    return random.choice(listKota[tipeDom])