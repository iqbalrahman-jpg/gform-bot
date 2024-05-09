import random
import time
import data

# ===================================================================================================

index = 19
times = 56

kategori = [
    [
        33,12,11
    ],
]

soal = []

def pendidikan(usia) :
    if usia <= 1 :
        result = random.choice([16,17,17,17,17])
    elif usia <= 3 :
        result = 17
    else :
        result = random.choice([18,19])
    
    return result

def agama(etnis) :
    if etnis == 21 :
        result = random.choice([33,33,33,33,33,33,34,35,36,37,38])
    elif etnis == 22 :
        result = random.choice([33,34,34,34,34,34,35,35,35,35,35,36,37,38])
    else :
        result = random.choice([33,34,35, 33,34,35, 33,34,35, 36,37,38])
    
    return result

def pekerjaan(usia) :
    if usia <= 5 :
        result = random.choice([41,41,41,41,41,41,41,42,44,45,47])
    else :
        result = random.choice([41,41,42,42,43,44,45,47])
    
    return result

