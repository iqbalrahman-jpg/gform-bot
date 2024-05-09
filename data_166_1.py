import random
import time
import data

# ===================================================================================================

index = 32
times = 18

kategori = [
    [
        6,12 #usia
    ],
    [
        6,12 #pekerjaan
    ],
    [
        16,2 #pendidikan
    ],
    [
        18,0 #rata
    ]
]

nama = [
    "Ali Hasanudin",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Yudi Pradanawan",
    "Bayu Danang Merta",
    "Budi Suryanto",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Attaka Majid",
    "Fabian Nadeo Putra",
    "Bayu Dwiganara",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Angga Siregar Putra",
    "Raja Putra Wardanawan",
    "Shaka Kurnia Wijaya",
    "Cynara Nafisah",
    "Mahendra Rhejaa Fadilah",
    "Yanuar Suryadi",
    "Rayhan Adi Wicasa",
    "M. Putra Susanto",
    "Ardyanto Rizki Putra",
    "Putra Wirawan",
    "Agung Nugroho",
    "Dani Ramadhan",
    "Dimas Purbo",
    "Rio Fajar Pratama",
    "Agung Kusuma Jaya",
    "Rizki Pratama Nugraha",
    "Dwi Prasetya Utama",
    "Arif Rahman Hakim",
    "Ananda Dwi Wicaksono",
    "Rama Aditya Wardhana",
    "Cinta Ayu Dewanti",
    "Ade Kurniawan Saputra",
    "Budi Santoso Putra",
    "Ahmad Fauzi Akbar",
    "Rizky Ananda Pratama",
    "Dwi Kusuma Jaya",
    "Agung Santosa Nugroho",
    "Andi Muhammad Rizal",
    "Budi Santoso",
    "Rudi Setiawan",
    "Andi Prasetyo",
    "Rizky Ramadhan",
]

kelamin = [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]

def pekerjaan(usia, kelamin) :
    if usia == 0 :
        result = random.choice([11,15,16])
    elif usia == 1 and kelamin == 4 :
        result = random.choice([11,11,11,13,14,14,15,16])
    elif usia == 1 :
        result = random.choice([11,11,11,14,14,15,16])
    elif kelamin == 4 :
        result = random.choice([11,11,11,13,14,14,15,16])
    else:
        result = random.choice([11,11,11,14,14,15,16])

    return result

def pendidikan(pekerjaan, usia, batas) :
    if batas != 0 :
        if usia == 0 :
            if pekerjaan == 11 :
                result = random.choice([19,20,20,20,20])
            elif pekerjaan == 12 :
                result = random.choice([19,20,20,20,20])
            elif pekerjaan == 15 :
                result = random.choice([20,21])
            else :
                result = random.choice([19,20,20,20,20])
        elif usia == 1 :
            if pekerjaan == 11 :
                result = random.choice([20,21])
            elif pekerjaan == 12 :
                result = random.choice([20,21])
            elif pekerjaan == 13 :
                result = random.choice([20,21])
            elif pekerjaan == 14 :
                result = random.choice([20,21,23])
            elif pekerjaan == 15 :
                result = random.choice([21,23])
            else :
                result = random.choice([20,21,23])
        else :
            if pekerjaan == 11 :
                result = random.choice([20,21])
            elif pekerjaan == 14 :
                result = random.choice([20,21,23])
            elif pekerjaan == 15 :
                result = random.choice([21,23])
            else :
                result = random.choice([20,21,23])
    else :
        result = 22
    return result

def pernah() :
    result = random.choice([26,26,27])
    return result

def lainnya(pernah) :
    if pernah == 26 :
        temp = random.randint(1,3)
        result = random.sample([1,2,3,4], temp)
    else:
        result = [0]
    
    return result

def terakhir(rata) :
    if rata == 29 : 
        result = random.choice([32,33,34])
    elif rata == 30 :
        result = random.choice([32,33,33,33,34])
    else :
        result = random.choice([32,32,33])

    return result

        


