import random
import time
import data

# ===================================================================================================

index = 9
times = 71

kategori = [
    [
        13,0,58
    ],
]

soal = [5,10,8,7,4]

def pekerjaan(usia) :
    if usia == 2 :
        result = random.choice([5,6,6,6,8])
    elif usia == 3 :
        result = random.choice([5,6,7,8,8,8,8])
    else :
        result = random.choice([5,7,8,8,8,8])
    
    return result

def penghasilan(pekerjaan) :
    if pekerjaan == 5 :
        result = random.choice([14,15])
    elif pekerjaan == 6 :
        result = random.choice([13,14])
    elif pekerjaan == 7 :
        result = random.choice([14,15,15,16,16,16])
    else :
        result = random.choice([14,15,15,15,16,16,16])

    return result