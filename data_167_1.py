import random
import time
import data

# ===================================================================================================

index = 0
times = 100

kategori = [
    [
        42,33,11,14 #pekerjaan
    ],
    [
        71,29 #domisili
    ],
    [
        57,43 #berapakali
    ],
    [
        0,0,10,20,70 #jawaban
    ]
]

def pekerjaan(usia) :
    result = []
    if usia == 0 :
        result = [6,10]
    elif usia == 1 :
        result = [7,11]
    else :
        result.append(data.hitungUsia(8,9))
        result.append(data.hitungUsia(10,11))
    
    return result