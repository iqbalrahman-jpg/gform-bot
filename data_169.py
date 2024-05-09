import random
import time
import data

# ===================================================================================================

index = 256
times = 1
# 10
indexTelp = 137

jawaban = [
    2,2,2,2,0,0,2,0,0,2,2,0,2,2,2,2,3,0,0,2,3,2,3,2
]

def pekerjaan(usia) :
    if usia <= 25 : 
        result = random.choice(["Freelance", "Freelancer", "Karyawan Swasta", "Pegawai"])
    else :
        result = random.choice(["Karyawan Swasta", "Pegawai Negeri", "pegawai negri", "Pegawai kantor", "karyawan", "pegawai swasta", "karyawan swasta", "buruh pabrik"])
    
    return result

def jawab(jawab) :
    p = 0
    for i in range(24) :
        j = p + jawaban[i]
        s1 = j - 1 if jawaban[i] == 3 else random.choice([j, j+1])
        jawab[s1].click()

        p += 4

nama = [
    "Kairaini Aliesa",
    "Naufal Azwin",
    "Shaka Kurnia Wijaya",
    "Prita agustina",
    "Dwi Kusuma Jaya",
    "Eko Wijaya",
    "Devi Puspitasari",
    "Rsi",
    "Maya Dara Putri",
    "MDu",

    "Rina Permata Sari",
    "Lika Arletta",
    "ADW",
    "Bagus Hariawan",
    "Nanda Marsa Ayunda",
    "Yuli Ayunda Dewi",
    "Sadiva Pratiwi",
    "AMK",
    "BSR",
    "Septinia Kurniawan",

    "Rfa",
    "Dimas Purbo",
    "Budi Santoso Putra",
    "Rani Fitriani",
    "Yanuar Suryadi",
    "Andi Muhammad Rizal",
    "RFA",
    "Hermanto Caisar",
    "Erfina Pratiwi",
    "Rohmat Ubaidillah",

    "Mutia Ayu Nur",
    "Cynara Nafisah",
    "Fredinan Puan",
    "Attaka Majid",
    "BDP",
    "YSL",
    "Dini Cahyani",
    "ACP",
    "Agis Prasetya",
    "Arn",

    "Affifah Rahman Nabila",
    "nsp",
    "Nma",
    "Damar Eka",
    "Olivia Niken",
    "anp",
    "Budi Suryanto",
    "RAP",
    "AKK",
    "Windy Cantika",

    "Faradilla Aulia",
    "dsd",
    "Add",
    "Dpw",
    "FNP",
    "NIS",
    "Rt",
    "Fs",
    "MFW",
    "IK",

    "Maya Dewi Utami",
    "AD",
    "Reyhan Utomowa",
    "NSQ",
    "AM",
    "Rina Anggraini Sari",
    "DKW",
    "Dian Nugroho",
    "Bayu Dwiganara",
    "Dian Kusuma Wardani",

    "EP",
    "Anindya Riri",
    "Dani Ramadhan",
    "Rio Fajar Pratama",
    "Nabilla Syaqila Qolbi",
    "Eka Wahyu",
    "Indra Kusuma",
    "Aditya Derdinand",
    "Intan Ayu Lestari",
    "Marylda Putri Sentosa",

    "NEY",
    "Salma Arowaya",
    "Amanda Bella Putri",
    "RPW",
    "DSW",
    "PKW",
    "Setiawan Nugraha",
    "Naufal Ardiansyah",
    "RAS",
    "Angga Siregar Putra",

    "Yanto Wibowo",
    "Yahya Nugraha",
    "DAC",
    "Cinta Ayu Dewanti",
    "RA",
    "Bagus Rahmad",
    "PS",
    "Ananda Dwi Wicaksono",
    "Ali Hasanudin",
    "Agung Nugroho",

    "Lista Kamilla",
    "NA",
    "Riskia Ayu Febrianti",
    "Khansa Azzahra",
    "DRA",
    "RNS",
    "YWOP",
    "App",
    "TDS",
    "YPW",

    "Sus",
    "FN",
    "Agung Santosa Nugroho",
    "Rina Nuraini Sari",
    "Mona Hadfinna",
    "Nana Annisa",
    "Bambang Suhatmoyo",
    "BAN",
    "Yudi Pradanawan",
    "MPL",

    "Eka Puspita Dewi",
    "ASP",
    "Yuni Nafisah",
    "Hana Anissa Herian",
    "afr",
    "Dito Prasetya",
    "Ardyanto Putra Wardhana",
    "Bellanda Clara Ayunda", 
    "Dcb",
    "DYA",

    "Bayu Danang Merta",
    "Rizal Pratama",
    "Muhammad Fadlan",
    "Dewi Sari Wijaya",
    "DKA",
    "DPP",
    "Sarah Husaini",
    "Nisa Indah Sari",
    "snd",
    "RP",

    "BDM",
    "Riska Rahmawati",
    "Andi Prasetyo",
    "YAD",
    "Ade Kurniawan Saputra",
    "KA",
    "AR",
    "SKW",
    "ANP",
    "Arif Rahman Hakim",

    "WC",
    "Nina Anggraini",
    "mhj",
    "Aryo Nugraha",
    "MRF",
    "Sinta Utami Sari",
    "Budi Prasetyo Wibowo",
    "Ratih Suci Lestari",
    "BSP",
    "ARS",

    "SR",
    "IAD",
    "MTAP",
    "Heraldy Gunawan",
    "Budi Santoso",
    "Yoga Putra Wijaya",
    "Diah Ayu Cindy",
    "Rizki Pratama Nugraha",
    "Raja Putra Wardanawan",
    "MDI",

    "Mira Fitriana Wati",
    "MDP",
    "Ahmad Fauzi Akbar",
    "FEN",
    "Arjuna Ghafur",
    "SLB",
    "Fattahilah Sadewa",
    "Yazid Hasbilluh Kurniawan",
    "asn",
    "Nia EKa Yuliana",

    "CP",
    "YNN",
    "Syifa Radifah",
    "Salma Azizah",
    "SAS",
    "RAw",
    "Dpp",
    "Dika Setiawan Pratama",
    "Dwi Prasetya Utama",
    "Ardy Riski",

    "Dila Yuliani Wati",
    "DNW",
    "BS",
    "YPA",
    "BPW",
    "DPL",
    "Tiara Dewi Puspita",
    "Rudi Setiawan",
    "Shabir Maulana",
    "PW",

    "SA",
    "CAD",
    "Maya Dewi Sari",
    "Nabil Saputra",
    "RN",
    "Budi Santoso",
    "Maya Putri Lestari",
    "Fira Nur Hidayah",
    "Dwi Panca",
    "Okto Devano",

    "RPS",
    "AN",
    "Fabian Nadeo Putra",
    "Yuli Setiawan",
    "Fryshta Eka Nabilla",
    "Alffianto Kuntoro",
    "Putri Kirana Dewi",
    "Ardyanto Rizki Putra",
    "RL",
    "Putri Keancana",

    "Rama Aditya Wardhana",
    "CN",
    "RU",
    "Regina Cantika Subandini",
    "Annisa Chania",
    "AH",
    "Mahendra Rhejaa Fadilah",
    "Agung Kusuma Jaya",
    "Damar Hafidzhuan",
    "NA",

    "AKJ",
    "SF",
    "Dimas Wahyu",
    "Azzarin Ristia Nabila",
    "Argo Prasetyawan",
    "Miranda Nella",
    "SAS",
    "ARN",
    "Putra Wirawan",
    "BCA", 

    "Mn",
    "Rizky Ramadhan",
    "APW",
    "Stephani Amanda Safitri",
    "Bima Aditya Nugraha",
    "Rizky Ananda Pratama",
    "Raka Triyana",
    "RRP",
    "RR",
    "Sadewa Lingga Budiantoro",

    "PK",
    "NAP",
    "faradilla nina",
    "rud",
    "RA",
    "Siti Fauziyah",
]

kelamin = [
    1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1
]