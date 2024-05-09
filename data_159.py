import random
import time
import data

# ===================================================================================================

index = 0
times = 10

kategori = [
    2,0,8
]

alasan = [
    "Saya sangat menyukai kemudahan menggunakan QRIS. Transaksi menjadi lebih cepat dan praktis. Tidak perlu membawa uang tunai atau kartu kredit. Cukup dengan ponsel saya, semua pembayaran dapat dilakukan dengan mudah.",
    "Pernah mengalami kesulitan saat transaksi menggunakan QRIS karena konektivitas internet yang buruk. Terkadang, transaksi tidak dapat segera diproses, menyebabkan sedikit ketidaknyamanan.",
    "QRIS membuat hidup saya lebih sederhana. Sekarang, saya tidak perlu repot membawa dompet penuh uang tunai. Cukup dengan mengambil ponsel, semuanya selesai.",
    "Beberapa pedagang belum benar-benar terbiasa dengan QRIS, dan kadang-kadang mereka kesulitan mengelola transaksi. Ada beberapa kali di mana mereka lupa meminta pembayaran QRIS.",
    "Keamanan adalah salah satu aspek terbaik dari QRIS. Saya merasa nyaman karena tidak perlu khawatir tentang kehilangan kartu kredit atau uang tunai. Semua informasi transaksi disimpan dengan aman di ponsel saya.",
    "Saya menemukan bahwa beberapa aplikasi QRIS memiliki antarmuka yang rumit dan sulit digunakan, terutama bagi pengguna yang tidak terlalu familiar dengan teknologi.",
    "QRIS memberi saya fleksibilitas untuk memilih berbagai metode pembayaran, termasuk transfer bank dan dompet digital, semua dalam satu kode QR. Sangat nyaman!",
    "Terkadang, transaksi QRIS membutuhkan waktu lebih lama daripada metode pembayaran lainnya, terutama ketika pedagang tidak memiliki peralatan yang memadai atau ketika sistem mereka mengalami gangguan.",
    "Pengalaman menggunakan QRIS memberikan saya lebih banyak diskon dan cashback dibandingkan dengan metode pembayaran konvensional. Saya merasa dihargai sebagai pengguna yang setia.",
    "Saya pernah mengalami situasi di mana transaksi QRIS saya gagal dan dana saya terpotong, namun, sulit untuk menghubungi pusat bantuan dan menyelesaikan masalah tersebut dengan cepat.",
]

def pilihKategori() :
    if kategori[0] != 0 and kategori[2] != 0 :
        pil = random.choice([0,2])
    elif kategori[0] != 0 and kategori[2] == 0 :
        pil = 0
    elif kategori[0] == 0 and kategori[2] != 0 :
        pil = 2
    
    return pil

def jawab1(samping, banyakSoal, kategori) :
    p = kategori
    for i in range(banyakSoal) :
        s1 = random.choice([p,p+1,p+2])
        samping[s1].click()
        p += 5

def hitungPegawai() :
    result = random.randint(5,20)
    return result

def jenisQris() :
    samples = [
        "Bank Indoensia", "BCA", "Bank Cental Asia", "Bank Mandiri", "Ovo", "Gopay", "Dana", "LinkAja", "BNI", "BRI", 
        "Bank Republik Indoensia", "Jenius"
    ]
    temp = random.randint(1,3)
    result = random.sample(samples, temp)
    kata = ""
    for i in range(len(result)) :
        if i == len(result) - 1 :
            kata += result[i]
        else:
            kata += result[i] + ", "

    return kata

def lamaPakai() :
    result = random.randint(3,12)
    return result

def jumlahTransaksi() :
    result = random.randint(17, 199)

    kata = str(result) + ".000"
    return kata

def hitungRandint(awal, akhir) :
    result = random.randint(awal, akhir)
    return result
