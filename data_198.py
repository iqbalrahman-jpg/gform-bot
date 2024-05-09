import random
import time
import data

# ===================================================================================================

index = 15
times = 15

soal = [6,8,4,10]

kategori = [
    [
        8,7 # 3 - 5
    ]
]

def jawab(banyakSoal, kelipatan, jawab) :
    p = 2
    for i in range(banyakSoal) :
        s1 = random.choice([p,p+1,p+1,p+1,p+2,p+2,p+2,p+2])
        
        jawab[s1].click()
        p += kelipatan
