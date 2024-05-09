import random
import time
import data

# ===================================================================================================

index = 0
times = 10

listSemester = [
    0,0,2,3,2,3
]

kategori = [
    2,0,8
]

soal = [5,5,5,5,5]

def pilihanSemester() :
    data = []
    for i in range(len(listSemester)) : 
        if listSemester[i] != 0 :
            data.append(i)
    
    result = random.sample(data, 1)
    return result[0]

def pilihTipe() :
    data = []
    for i in range(len(kategori)) : 
        if kategori[i] != 0 :
            data.append(i)
    
    result = random.sample(data, 1)
    return result[0]

