import random
import time
import data

# ===================================================================================================

soal = []

usia = [0, 15, 16, 7, 3]
kat1 = [[1, 40], [2, 39], [17, 24]]
kat2 = [4, 13]

index = 9
times = 41

def hitungCheck1() :
    result = []

    s45 = random.choice([0,1,1,1])
    s3 = random.choice([0,1])
    s12 = random.choice([0,0,0,1])

    if s45 == 1 :
        temp = random.choice([1,2,2])
        res = random.sample([3,4], temp)
        for i in res :
            result.append(i)

    if s3 == 1 :
        result.append(2)

    if s12 == 1 :
        temp = random.choice([1,1,1,2])
        res = random.sample([0,1], temp)
        for i in res :
            result.append(i)

    return result

def hitungCheck2() :
    result = []

    s1 = random.choice([0,1,1,1])
    s23 = random.choice([0,1])
    s4 = random.choice([0,0,0,0,0,1])

    if s1 == 1 :
        result.append(6)

    if s23 == 1 :
        temp = random.choice([1,1,2])
        res = random.sample([7,8], temp)
        for i in res :
            result.append(i)

    if s4 == 1 :
        result.append(9)

    return result

def hitungCheckNo() :
    result = []

    s14 = random.choice([0,1,1,1])
    s23 = random.choice([0,1,1,1,1,1,1,1])
    s45 = random.choice([0,0,0,0,1])

    if s14 == 1 :
        temp = random.choice([1,1,1,1,1,1,2])
        res = random.sample([0,3], temp)
        for i in res :
            result.append(i)

    if s23 == 1 :
        temp = random.choice([1,2,2,2])
        res = random.sample([1,2], temp)
        for i in res :
            result.append(i)

    if s45 == 1 :
        temp = random.choice([1,1,1,1,1,2])
        res = random.sample([3,4], temp)
        for i in res :
            result.append(i)

    return result
