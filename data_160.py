import random
import time
import data

# ===================================================================================================

index = 24
times = 8

kategori = [
    7,0,1
]

soal = [20, 16, 9]

def hitungSemester(usia) :
    if usia <= 18 :
        result = random.choice([1,3])
    elif usia <= 20 :
       result = random.choice([3,5])
    else :
       result = random.choice([5,7])
    
    return result

def pilihKategori() :
    if kategori[0] != 0 and kategori[2] != 0 :
        pil = random.choice([0,2])
    elif kategori[0] != 0 and kategori[2] == 0 :
        pil = 0
    elif kategori[0] == 0 and kategori[2] != 0 :
        pil = 2
    
    return pil

def jawab1(samping, tipe) :
    time.sleep(2)
    p = tipe if tipe == 0 else tipe + 1
    for i in range(soal[0]) :
        if i == 2:
            s1 = random.choice([12,13,14,15,16,17])
        elif i == 6 :
            s1 = random.choice([36,37,38,39,40,41])
        else:
            s1 = random.choice([p,p+1,p+2])

        samping[s1].click()
        p += 6

def jawab2(samping, tipe, j) :
    time.sleep(2)
    p = tipe
    for i in range(soal[j]) :
        s1 = random.choice([p,p+1,p+1,p+2])
        samping[s1].click()
        p += 5


