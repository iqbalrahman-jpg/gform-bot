import random
import time
import data

# ===================================================================================================

index = 14
times = 1

nama = [
	"Mutia Ayu Nur",
    "Riskia Ayu Febrianti",
    "Nana Annisa",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yuli Ayunda Dewi",
    "Bellanda Clara Ayunda", 
    "Miranda Nella",
    "Annisa Chania",
    "Diah Ayu Cindy",
    "Azzarin Ristia Nabila",
    "Nia EKa Yuliana",
    "Syifa Radifah",
    "Siti Fauziyah",
    "Salma Arowaya",
]

isian = [
    [
        "Sekitar 1 bulan an",
        "1 bulan",
        "Seminggu ini",
        "baru baru ini",
        "2 bulan lalu",
        "sebulan lalu",
        "1 bulanna",
        "2 mingguan",
        "seminggu lalu",
        "hampir sebulan",

        "sebulanan",
        "Hampir 3 bulanan",
        "seminggu",
        "satu minggu",
        "Hampir sebulan",
    ],
    [
        "tiktok",
        "tiktok",
        "tiktok, ig",
        "Tiktok",
        "tiktok dan instagram",
        "internet",
        "Tiktok",
        "tiktok",
        "teman",
        "Tiktok",

        "Tiktok, instagram, twitter",
        "instagram, tiktok",
        "Tiktok",
        "tiktok",
        "tiktok dan teman",
    ],
    [
        "Menurut pandangan saya, keunggulan utama produk skincare merek Somethinc adalah formulanya yang dirancang untuk semua jenis kulit",
        "Saya percaya keunggulan produk Somethinc terletak pada kombinasi bahan alami yang mereka gunakan untuk memberikan manfaat optimal pada kulit",
        "Salah satu keunggulan yang menonjol dari produk Somethinc adalah kandungan antioksidan tinggi yang dapat melindungi kulit dari kerusakan radikal bebas",
        "Menurut saya, kualitas formulasi produk Somethinc menciptakan pengalaman skincare yang menyeluruh dan memuaskan",
        "Keunggulan produk Somethinc dapat dilihat dari kemampuannya memberikan hidrasi intensif tanpa meninggalkan rasa lengket",
        "Saya yakin keunggulan utama Somethinc adalah kesesuaian produk dengan berbagai masalah kulit, membuatnya cocok untuk berbagai jenis pengguna",
        "Kelebihan produk Somethinc mungkin terletak pada kemampuannya mengatasi permasalahan kulit tertentu, seperti jerawat atau penuaan dini",
        "Saya melihat keunggulan produk Somethinc dalam inovasi formulanya yang terus menerus mengikuti perkembangan terkini dalam perawatan kulit",
        "Salah satu hal yang membuat produk Somethinc menonjol adalah komitmennya terhadap bahan-bahan berkualitas dan tidak mengandung bahan berbahaya",
        "Menurut saya, keunggulan produk Somethinc dapat dirasakan melalui hasil positif yang diberikan pada tekstur dan tampilan kulit pengguna setelah penggunaan rutin",

        "Salah satu keunggulan utama produk skincare merek Somethinc adalah formulanya yang kaya akan bahan alami, memberikan nutrisi maksimal pada kulit",
        "Menurut saya, keunggulan terbesar produk Somethinc terletak pada kemampuannya mengatasi masalah kulit khusus, seperti jerawat atau kekeringan",
        "Keunggulan produk Somethinc dapat dilihat dari hasilnya yang terlihat efektif, memberikan kulit tampak lebih sehat dan bercahaya",
        "Saya yakin bahwa keunggulan produk Somethinc terletak pada keselarasan formula yang dapat digunakan oleh berbagai jenis kulit tanpa menyebabkan iritasi",
        "Kelebihan menonjol dari produk Somethinc adalah kandungan antioksidannya yang tinggi, membantu melawan radikal bebas dan menjaga kulit dari penuaan dini",
    ],
    [
        "Tidak ada",
        "Meskipun banyak yang menyukai produk Somethinc, beberapa orang mungkin merasa bahwa harganya cukup tinggi dibandingkan dengan merek skincare sejenis di pasaran",
        "menurut saya tidak ada",
        "tidak saya rasa",
        "tidak ada",
        "Beberapa konsumen mungkin mencatat bahwa produk Somethinc memiliki aroma yang cukup kuat, yang mungkin tidak disukai oleh mereka yang sensitif terhadap wewangian",
        "Kekurangan potensial lainnya mungkin terletak pada ketersediaan produk, di mana beberapa varian atau ukuran produk tertentu mungkin sulit ditemukan di beberapa toko atau wilayah",
        "saya rasa tidak ada",
        "Ada kemungkinan bahwa sebagian orang mengalami reaksi kulit tertentu terhadap beberapa bahan yang digunakan dalam produk Somethinc, yang dapat menjadi kekurangan bagi pengguna dengan kulit yang sangat sensitif",
        "-",

        "tidak saya rasa",
        "Tidak ada",
        "Beberapa pengguna mungkin menganggap kekurangan produk skincare merek Somethinc terletak pada harganya yang relatif tinggi dibandingkan dengan merek sejenis di pasaran",
        "Ada kemungkinan bahwa sebagian orang dengan kulit sangat sensitif dapat mengalami reaksi negatif terhadap beberapa bahan yang terdapat dalam produk Somethinc, menjadi satu kekurangan potensial",
        "tidak ada",
    ],
    [
        "Dua minggu",
        "Sekitar setengah tahun",
        "Lebih dari satu tahun yang lalu",
        "Sebulan",
        "Hampir dua tahun",
        "Sejak sekitar satu setengah tahun yang lalu",
        "Beberapa bulan lalu",
        "Hampir dua tahun",
        "Sebulan an",
        "Sekitar setahun yang lalu",

        "Hampir dua tahun",
        "Sekitar setengah tahun",
        "Sebulanan",
        "baru baru ini saja",
        "setahun belakangan",
    ]
]

def pendidikan(pekerjaan) :
    if pekerjaan == 4 :
        result = 10
    elif pekerjaan == 5 :
        result = 11
    else :
        result = data.hitungUsia(12,13)
    
    return result