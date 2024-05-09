import random
import time
import data

# ===================================================================================================

soal = [5, 5, 5, 5, 5, 5]

positif = 12
negatif = 3

times = 15
index = 10

def countUsia() :
    usia = random.choice([2,3,4,5,6])
    return usia

def countPekerjaan(usia) :
    if usia == 2 :
        pekerjaan = random.choice([8,11])
    elif usia == 3 :
        pekerjaan = random.choice([7,8,9,10,11])
    else :
        pekerjaan = random.choice([7,8,9,10])
    
    return pekerjaan

def countPendapatan(pekerjaan) :
    if pekerjaan == 11 :
        pendapatan = random.choice([13,14])
    elif pekerjaan == 12 :
        pendapatan = random.choice([13,14,15,16])
    else :
        pendapatan = random.choice([16,17,18])
    
    return pendapatan

def pilihJawab() :
    if positif != 0 and negatif != 0 :
        pil = random.choice([0,2])
    elif positif != 0 and negatif == 0 :
        pil = 2
    elif positif == 0 and negatif != 0 :
        pil = 0
    
    return pil

def jawab1(pil, banyakSoal, samping) :
    p = pil
    for i in range(banyakSoal) :
        if pil == 0 :
            s1 = random.choice([p, p, p+1, p+1, p+2])
        else :
            s1 = random.choice([p, p+1, p+1, p+2, p+2])
        
        samping[s1].click()
        p += 5