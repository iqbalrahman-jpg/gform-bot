import random
import time
import data

# ===================================================================================================

index = 0
times = 30

listInstansi = [
    "SMAN 1 Rumbia", 
    "⁠SMA Bangun Cipta Rumbia",
    "⁠SMK Muhammadiyah 1 Rumbia",
    "⁠SMPN 1 Rumbia",
    "⁠SMK Al Falah",
    "⁠SMAN 1 Seputih Surabaya",
]

soal = [2,5,5,2,5,2,2,2,5,2,5,2,5,2,5,2,5,2,5,2,0]

def pilihanInstansi() :
    result = random.randint(0, len(listInstansi)-1)
    return listInstansi[result]
