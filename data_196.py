import random
import time
import data

# ===================================================================================================

index = 0
times = 100

soal = [25]

def pekerjaan(usia) :
    if usia == 6 :
        result = random.choice([9,9,9,9,9,9,9,9,10,11,12])
    elif usia == 7 :
        result = random.choice([9,10,11,11,11,11,12])
    else :
        result = random.choice([10,10,10,10,11,11,11,11,12])
    
    return result

def penghasilan(pekerjaan) :
    if pekerjaan == 9 :
        result = random.choice([16,16,16,16,17])
    else :
        result = random.choice([16,17,17,17,18,18,18,18])
    
    return result