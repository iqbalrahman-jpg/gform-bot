import random
import time

# ===================================================================================================

jawabanIsi = [
    [
        [
            "isi 1, tipe 1",
        ],
        [
            "isi 2, tipe 1",
        ]
    ],
    [
        [
            "isi 1, tipe 2",
        ],
        [
            "isi 2, tipe 2",
        ]
    ],
    [
        [
            "isi 1, tipe 3",
        ],
        [
            "isi 2, tipe 3",
        ]
    ]
]

universitas = [
    "Univ Katolik Atma jaya",
    "Politeknik Kesehatan Surakarta",
    "Universitas Diponegoro",
    "Institut Teknologi Sepuluh Nopember",
    "Universitas Islam Negeri Sunan Kalijaga Yogyakarta",
    "universitas katolik atma jaya",
    "Univ Katolik Atma jaya",
    "Politeknik Negeri Malang",
    "Universitas katolik atma jaya",
    "Universitas Trunojoyo Madura",
    "Universitas Katolik Atma Jaya",
    "Politeknik Negeri Media Kreatif",
    "Universitas Islam Negeri Maulana Malik Ibrahim",
    "Politeknik Kelautan dan Perikanan Pangandaran",
    "Politeknik STMI Jakarta",
    "Politeknik Perkapalan Negeri Surabaya",
    "Universitas Katolik Atma Jaya",
    "Universitas Indonesia",
    "Institut Seni Indonesia Surakarta",
    "Universitas Katolik Atma Jaya",
    "universitas katolik atma jaya",
    "Univ Katolik Atma jaya",
    "Politeknik Kesehatan Banten",
    "Universitas Sultan Ageng Tirtayasa",
    "universitas katolik atma jaya",
    "Univ Katolik Atma jaya",
    "Universitas Veteran Jawa Timur",
    "Universitas Katolik Atma Jaya",
    "Universitas katolik atma jaya",
    "Universitas Veteran Yogyakarta",
    "Universitas katolik atma jaya",
    "universitas katolik atma jaya",
    "Universitas katolik atma jaya",
    "Universitas Katolik Atma Jaya",
    "Universitas katolik atma jaya",
    "Univ Katolik Atma jaya",
    "Universitas Katolik Atma Jaya",
    "Universitas Negeri Jakarta",
    "Universitas katolik atma jaya",
    "Politeknik APP Jakarta",
    "Politeknik Negeri Media Kreatif",
    "Univ Katolik Atma jaya",
    "Univ Katolik Atma jaya",
    "Universitas katolik atma jaya",
    "Universitas katolik atma jaya",
    "Universitas Trunojoyo Madura",
    "Universitas Terbuka",
    "Universitas Katolik Atma Jaya",
    "universitas katolik atma jaya",
    "Politeknik Manufaktur Bandung",
    "Institut Pertanian Bogor",
    "Univ Katolik Atma jaya",
    "Politeknik Pelayaran Banten",
    "Univ Katolik Atma jaya",
    "Politeknik Pelayaran Banten",
    "Politeknik Kesehatan Semarang",
    "universitas katolik atma jaya",
    "Universitas Trunojoyo Madura",
    "Universitas Indonesia",
    "Universitas katolik atma jaya",
    "Politeknik Kesehatan Semarang",
    "Institut Teknologi Sepuluh Nopember",
    "Universitas Islam Negeri Maulana Malik Ibrahim",
    "Politeknik Negeri Semarang",
    "Univ Katolik Atma jaya",
    "Universitas Islam Negeri Syarif Hidayatullah Jakarta",
    "Universitas katolik atma jaya",
    "Universitas Diponegoro",
    "Politeknik Kelautan dan Perikanan Pangandaran",
    "Universitas Negeri Yogyakarta",
    "Universitas Katolik Atma Jaya",
    "Universitas Katolik Atma Jaya",
    "Universitas Katolik Atma Jaya",
    "Universitas Islam Negeri Salatiga",
    "Politeknik Penerbangan Indonesia Curug",
    "Institut Pertanian Bogor",
    "Universitas Katolik Atma Jaya",
    "Universitas Terbuka",
    "Politeknik Manufaktur Bandung",
    "Politeknik Kesehatan Semarang",
    "Politeknik Pelayaran Banten",
    "Institut Teknologi Sepuluh Nopember",
    "Politeknik Penerbangan Surabaya",
    "Universitas Katolik Atma Jaya",
    "Universitas Veteran Jawa Timur",
    "Univ Katolik Atma jaya",
    "Universitas Trunojoyo Madura",
    "Politeknik Kesehatan Banten",
    "Universitas Negeri Yogyakarta",
    "Universitas Islam Internasional Indonesia",
    "Universitas Siliwangi",
    "Univ Katolik Atma jaya",
    "Universitas Trunojoyo Madura",
    "Politeknik Perkapalan Negeri Surabaya",
    "universitas katolik atma jaya",
    "Universitas Islam Negeri Maulana Malik Ibrahim",
    "Universitas Tidar",
    "Universitas Katolik Atma Jaya",
    "universitas katolik atma jaya",
    "universitas katolik atma jaya",
    "Politeknik Ilmu Pelayaran Semarang",
    "universitas katolik atma jaya",
    "universitas katolik atma jaya",
    "Universitas Trunojoyo Madura",
    "Universitas Indonesia",
    "Universitas Negeri Yogyakarta",
    "Univ Katolik Atma jaya",
    "Universitas Islam Internasional Indonesia",
    "Universitas katolik atma jaya",
    "Politeknik STMI Jakarta",
    "Universitas katolik atma jaya",
    "Politeknik Ilmu Pelayaran Semarang",
    "Universitas Katolik Atma Jaya",
    "Politeknik Pelayaran Banten",
    "Universitas Islam Negeri Raden Mas Said",
    "universitas katolik atma jaya",
    "Politeknik Negeri Malang",
    "Univ Katolik Atma jaya",
    "Politeknik Penerbangan Surabaya",
    "universitas katolik atma jaya",
]

soal = [3,4,7,8,9,13,14,16]

tipe1 = 14
tipe2 = 0
tipe3 = 0

tipe1Idx = 0
tipe2Idx = 0
tipe3Idx = 0

index = 106
times = 14

def countUsia() :
    usia = random.randint(19,25)
    return usia

def countSemester(usia) :
    if usia <= 22 :
        semester = 0
    else :
        semester = random.choice([0,2,2,2])
    
    return semester

def countStatus(semester) :
    if semester == 0 :
        status = random.choice([0,0,1])
    else :
        status = 0
    
    return status

def cekTipe() :
    if tipe1 != 0 and tipe2 != 0 and tipe3 != 0 :
        pil = random.choice([1,1,1,2,3])
    elif tipe1 != 0 and tipe2 != 0 and tipe3 == 0 :
        pil = random.choice([1,1,2])
    elif tipe1 != 0 and tipe2 == 0 and tipe3 != 0 :
        pil = random.choice([1,1,3])
    elif tipe1 == 0 and tipe2 != 0 and tipe3 != 0 :
        pil = random.choice([2,2,3])
    elif tipe1 != 0 and tipe2 == 0 and tipe3 == 0 :
        pil = 1
    elif tipe1 == 0 and tipe2 != 0 and tipe3 == 0 :
        pil = 2
    elif tipe1 == 0 and tipe2 == 0 and tipe3 != 0 :
        pil = 3
    
    return pil

def jawab1(banyakSoal, radiobuttons) :
    j = 0
    p = 0
    for i in range(banyakSoal) :
        if i+1 == soal[j] :
            s1 = random.choice([p, p+1])
            j +=1 
        else:
            s1 = random.choice([p+2, p+3, p+3, p+3, p+4, p+4, p+4])
        
        radiobuttons[s1].click()
        p += 5 

def jawab2(banyakSoal, radiobuttons) :
    j = 0
    p = 0
    for i in range(banyakSoal) :
        if i+1 == soal[j] :
            s1 = random.choice([p+2, p+3, p+3, p+3, p+4, p+4, p+4])
            j +=1 
        else:
            s1 = random.choice([p, p+1])
        
        radiobuttons[s1].click()
        p += 5 

def jawab3(banyakSoal, radiobuttons) :
    j = 0
    p = 0
    for i in range(banyakSoal) :
        if i+1 == soal[j] :
            s1 = random.choice([p])
            j +=1 
        else:
            s1 = random.choice([p+3, p+4])
        
        radiobuttons[s1].click()
        p += 5 



def jawabx(checkbox, status) :
    if status == 0 :
        pil = random.choice([0,0,1])
        if pil == 0 :
            checkbox[0].click()
    else :
        pil = random.choice([0,0,1])
        if pil == 0 :
            checkbox[1].click()

    temp = random.randint(1,3)
    s2 = random.sample([2,3,4], temp)

    for i in s2 :
        checkbox[i].click()

def jawabx1(testcheck, checkbox, batasx1, batasx2, batasy1, batasy2, status) :
    s1 = random.randint(batasx1,batasx2)
    s2 = random.randint(batasy1,batasy2)

    testcheck[s1].click()
    testcheck[10+s2].click()

    jawabx(checkbox, status)



def halaman5(checkbox, textbox, radio, testcheck, textarea, batas1, batas2, pilihan4, pilihan5, batas3, batas4) :
    temp = random.randint(1,4)

    s1 = random.sample([0,1,2,3,4,5,6,7], temp)
    s2 = random.randint(batas1, batas2)
    bulan = random.choice(["", " bulan", " Bulan", " bln", " Bln", " BLN"])
    s3 = random.choice([0,1,2,3])
    s4 = 5 if pilihan4 == "ya" else 6
    s5 = 11 if pilihan5 == "-" else random.choice([7,8,9,10])
    s6 = random.randint(batas3, batas4)

    for i in s1 :
        checkbox[i].click()
    
    time.sleep(2)
    textbox[0].send_keys(s2)
    textbox[0].send_keys(bulan)

    time.sleep(2)
    radio[s3].click()
    radio[s4].click()
    radio[s5].click()

    time.sleep(2)
    testcheck[s6].click()

    if s5 == 11 :
        textarea[2].send_keys("-")
    
    testcheck[s6].click()

def jawabIsian(tipe, isian) :
    if tipe == 1 :
        s1 = random.choice(["Meditasi", "Santai", "Relax", "Focus", "menerima diri sendiri", "latihan bernapas", "bernapas secara teratur"])
        s2 = random.choice(["Membuka aplikasi mindfulness", "journaling", "meditasi", "bertemu teman", "me time", "refreshing"])
    elif tipe == 2 :
        s1 = random.choice(["tidak tahu", "relax", "tidur", "yoga", "tidak pernah merasakan mindfulness"])
        s2 = random.choice(["merokok", "minum alkohol", "tidur", "bertemu teman", "shopping", "refreshing", "nonton film", "dengerin lagu", "me time"])
    else :
        s1 = random.choice(["Menentukan tujuan", "goal setting", "menenangkan diri", "meditasi", "breathing exercise", "latihan pernapasan"])
        s2 = random.choice(["membuka aplikasi mindfulness", "journaling", "meditasi", "bertemu teman", "me time", "refreshing"])
    
    isian[0].send_keys(s1)
    isian[1].send_keys(s2)

