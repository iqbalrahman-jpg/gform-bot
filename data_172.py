import random
import time
import data

# ===================================================================================================

index = 0
times = 25

def domisili() :
    result = random.choice(["Jakarta", "jakarta"])
    return result

def profesi(usia) :
    if usia <= 25 :
        result = random.choice([0,0,0,2,3])
    elif usia <= 30 :
        result = random.choice([0,1,2,2,3,3])
    else :
        result = random.choice([1,2,2,2,3])

    return result