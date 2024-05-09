import random
import time
import data

# ===================================================================================================

index = 0
times = 150

def countUsia() :
    result = random.randint(24,50)

    return result

def countPekerjaan(usia) :
    if usia <= 26 :
        result = random.choice(["Mahasiswa", "mahasiswa", "Mahasiswa", "mahasiswa", "Pegawai Swasta", "Karyawan"])
    else :
        result = random.choice(["Pegawai Swasta", "Karyawan", "Pegawai Negeri", "PNS", "Pengusaha", "Bussnisman", "Pengusaha"
                                , "pengusaha ritel", "Pengusaha ritel", "Pemilik restaurant", "Pemilik Resto", "Pengusaha properti", "Pemilik bisnis kecantikan"
                                , "Pemilik Perusahaan Kesehatan", "Pemilik Bisnis Logistik dan Pengiriman"])
    
    return result

def jawab(samping) :
    p = 1
    for i in range(11) :
        s1 = random.choice([p,p+1,p+2,p+3])
        samping[s1].click()
        p += 5

