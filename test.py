nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo",
    "Aryo Nugraha",
    "Nana Clara Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Yuli Ayunda Dewi",
    "Bayu Danang Merta"
]

email = [
    "mtianur001@gmail.com",
    "@alihasn",
    "risfebri11@gmail.com",
    "budprasety@gmail.com",
    "@aryonugh",
    "nannaanisa97",
    "yahnugrah@gmail.com",
    "ptrkrna",
    "nandayundaa1@gmail.com",
    "yudipradan01@gmail.com",
    "yuli.ayunda",
    "byumerta1@gmail.com"
]

kelamin = [1,0,1,0,0,1,0,1,1,0,1,0]

masalah =[
    "Mungkin sering terlambat dalam menghadiri acara karena lalu lintas",
    "Transportasi umum yang tidak dapat diandalkan",
    "Kesulitan mencari tempat parkir",
    "Kehilangan tiket atau akses masuk, lupa membawa tiket atau tidak dapat menemukan pintu masuk yang tepat",
    "Kerusuhan atau keamanan yang buruk, terkadang keamanan di acara tidak terjamin, yang bisa memicu kerusuhan atau bahaya bagi para pengunjung",
    "Masalah teknis acara yang sering bergantung pada teknologi, jadi masalah teknis seperti masalah audio atau video bisa terjadi dan mengganggu pengalaman acara",
    "Ketidaknyamanan tempat duduk merasa tidak nyaman dengan posisi duduk selama acara berlangsung, terutama jika tempat tersebut terlalu penuh atau tidak cukup lega",
    "Antrian yang panjang terutama jika event populer atau hanya ada sedikit pintu masuk",
    "Cuaca yang buruk bisa mengganggu acara yang dilakukan di luar ruangan, sseperti tiba-tiba turun hujan",
    "Terkadang informasi tentang acara bisa salah atau tidak jelas",
    "Kehabisan tempat parkir, hingga harus berjalan jauh",
    "Terlambat datang"
]

saran = [
    "pastikan aplikasinya mudah digunakan dan dapat diakses dengan mudah",
    "data pengguna harus aman dan terlindungi",
    "untuk pembayaran agar mudah",
    "",
    "Hadirkan banyak promo dan diskon yang menarik",
    "Tampilan yang menarik",
    "Keamanan, tampilan, dan kemudahan untuk pengguna",
    "",
    "",
    "Tampilan aplikasinya dibuat agar menarik dan bagus",
    "keamanan dan kemudahan akses oleh user",
    ""
]

for i in range(len(nama)) :
    if kelamin[i] == 0:
        temp = " laki laki"
    else:
        temp = " perempuan"
    print(nama[i] + email[i] + temp + masalah[i])
