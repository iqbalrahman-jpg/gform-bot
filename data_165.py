import random
import time
import data

# ===================================================================================================

index = 2
times = 98

def pilihPekerjaan(usia, kelamin) :
    if usia == 2 :
        result = random.choice([9,11,11])
    elif usia == 3 and kelamin == 0:
        result = random.choice([8,9,10,11])
    elif usia == 3:
        result = random.choice([8,9,11])
    elif kelamin == 0 :
        result = random.choice([8,9,9,10])
    else:
        result = random.choice([8,9,9,9])

    return result

def hitungSering() :
    result = random.choice([13,14,14,14,15,16])
    return result


