import random
import time
import data

# ===================================================================================================

index = 4
times = 96

nama = [
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Diah Ayu Cindy",
    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Siti Fauziyah",
    "Salma Arowaya",
    "Putri Keancana",
    "Affifah Rahman Nabila",
    "Cynara Nafisah",
    "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
    "Fryshta Eka Nabilla",
    "Rayhan Adi Wicasa",
    "Sutisna Ayuni",
    "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Ardyanto Rizki Putra",
    "Putra Wirawan",
    "Agung Nugroho",
    "Dania Ramadhani",
    "Dimas Purbo",
    "Nabilla Syaqila Qolbi",
    "Maya Dara Putri",
    "Dewi Sari Wijaya",
    "Ratih Suci Lestari",
    "Rizkia Ayu Nugi",
    "Intan Ayu Lestari",
    "Amanda Dewi Talitha",
    "Fira Nur Hidayah",
    "Rama Aditya Wardhana",
    "Cinta Ayu Dewanti",
    "Ade Kurniawan Saputra",
    "Mira Fitriana Wati",
    "Dian Kusuma Wardani",
    "Budi Santoso Putra",
    "Rina Nuraini Sari",
    "Ahmad Fauzi Akbar",
    "Rizky Ananda Pratama",
    "Maya Dewi Sari",
    "Kirana Ayu Dewi",
    "Dila Yuliani Wati",
    "Andi Muhammad Rizal",
    "Budi Santoso",
    "Rina Permata Sari",
    "Dian Nugroho",
    "Maya Putri Lestari",
    "Andi Prasetyo",
    "Sinta Utami Sari",
    "Rizky Putri Ramadhani",
    "Eka Puspita Dewi",
    "Dika Setiawan Pratama",
    "Rani Fitriani",
    "Nisa Indah Sari",
    "Tiara Dewi Puspita",
    "Nina Anggraini",
    "Dini Cahyani",
    "Raka Triyana",
    "Maya Dewi Utami",
    "Devi Puspitasari",
    "Rina Anggraini Sari",
    "Yuli Setiawan",
    "Eka Wahyu",
    "Yuni Nafisah",
    "Prita agustina",
    "Naufal Ardiansyah",
    "Hana Anissa Herian",
    "Heraldy Gunawan",
    "Eko Wijaya",
    "Safira Handesaputri",
    "Dwi Panca",
    "Okto Devano",
    "Olivia Niken",
    "faradilla nina",
    "Shabir Maulana",
    "Sarah Husaini",
    "Anindya Riri",
    "Erfina Pratiwi",
    "Argo Prasetyawan",
    "Salma Azizah",
    "Faradilla Aulia",
    "Regina Cantika Subandini",
    "Ardy Risqiqa",
    "Septinia Kurniawan",
    "Fredinan Puan",
    "Amanda Bella Putri",
    "Kairaini Aliesa",
    "Lika Arletta",
    "Lista Kamilla",
    "Sadiva Pratiwi",
    "Windy Cantika",
    "Stephani Amanda Safitri",
    "Marylda Putri Sentosa",
    "Nabil Saputri",
    "Khansa Azzahra",
    "Naufal Azwin",
    "Riska Rahmawati",
]

kelamin = [
    0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,
]

def jawab1(jaw) :
    pil = random.choice([0,1])

    if pil == 0 :
        temp = random.randint(1,4)
        s1 = random.sample([0,1,2,3], temp)
    else :
        temp = random.randint(1,3)
        s1 = random.sample([0,1,3], temp)
    
    for i in s1 :
        jaw[i].click()