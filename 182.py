from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import random

def pilihTipe(jenis) :
    data = []
    for i in range(len(jenis)) : 
        if jenis[i] != 0 :
            data.append(i)
    
    result = random.sample(data, 1)
    return result[0]

link = "https://docs.google.com/forms/d/e/1FAIpQLSfkWq9_UzflcT3QzLAhfRYzAGNzrPklOFNzi8xM4T-brpuqVQ/viewform"

profil = ["Default"]

isianJawab = [
    [
        [
            "Selama saya di kampus, saya mengamati bahwa kebijakan kesetaraan gender diimplementasikan dengan baik",
            "Pengalaman saya di kampus menciptakan lingkungan yang mendukung kesetaraan gender",
            "Kampus ini mempromosikan kesetaraan gender melalui berbagai kegiatan dan acara yang diselenggarakan",
            "Saya melihat banyak inisiatif untuk meningkatkan kesadaran akan isu-isu kesetaraan gender di lingkungan kampus",
            "Dalam kelas, saya merasa bahwa semua siswa mendapatkan perlakuan yang sama tanpa memandang jenis kelamin",
            "Kampus ini memiliki fasilitas yang mendukung keseimbangan kehidupan kerja dan keluarga bagi semua anggota kampus",
            "Saya berpartisipasi dalam kelompok atau organisasi yang memperjuangkan kesetaraan gender di kampus",
            "Selama wawancara dan interaksi dengan staf akademis, saya merasa adanya penghargaan terhadap ide-ide dan kontribusi dari semua mahasiswa tanpa pandang gender",
            "Saya senang melihat perwakilan gender yang seimbang dalam berbagai kegiatan ekstrakurikuler",
            "Program pelatihan yang diselenggarakan kampus membantu dalam meningkatkan pemahaman mengenai isu-isu kesetaraan gender",
            "Saya pernah terlibat dalam proyek atau penelitian yang mendukung kesetaraan gender di komunitas kampus",
            "Kampus ini memberikan dukungan aktif untuk kelompok-kelompok yang fokus pada isu kesetaraan gender",
            "Saya merasa bahwa penilaian dan penilaian di kampus ini didasarkan pada prestasi dan kemampuan tanpa adanya diskriminasi gender",
            "Sistem mentorship di kampus ini mendukung pertumbuhan karier tanpa memandang jenis kelamin",
            "Saya pernah menghadiri seminar atau lokakarya yang membahas isu-isu kesetaraan gender di dunia akademis",
            "Kampus ini memiliki kebijakan anti-pelecehan dan diskriminasi gender yang ketat",
            "Saya merasa nyaman dan didukung oleh kampus ini untuk mengejar minat dan aspirasi saya, tanpa adanya hambatan berdasarkan gender",
            "Mahasiswa dan staf kampus ini berkomitmen untuk menciptakan lingkungan yang inklusif dan setara bagi semua",
            "Saya melihat adanya kebijakan yang mendukung cuti hamil dan cuti orang tua di lingkungan kampus",
            "Kampus ini aktif dalam menggalang dukungan untuk kampanye dan kegiatan yang mempromosikan kesetaraan gender di masyarakat",
            "Ketika menghadiri pertemuan atau forum mahasiswa, saya melihat partisipasi aktif dari semua jenis kelamin, mencerminkan kesetaraan dalam ekspresi ide dan pandangan",
            "Saya pernah terlibat dalam proyek kolaboratif di kampus yang menekankan pentingnya peran setiap individu tanpa memandang jenis kelamin",
            "Dalam kegiatan pengembangan diri, saya merasa bahwa semua mahasiswa diberikan kesempatan yang sama untuk mengasah keterampilan dan bakat mereka, tanpa adanya stereotip gender",
            "Kampus ini memiliki kelompok atau inisiatif yang mendukung kesejahteraan dan kesetaraan gender, menyediakan sumber daya dan dukungan bagi semua mahasiswa",
            "Saat mengikuti kuliah atau lokakarya, saya mengamati adanya kepedulian terhadap isu-isu gender dan upaya untuk membangun pemahaman yang lebih baik",
            "Pengalaman saya dengan staf administratif menunjukkan bahwa kebijakan dan prosedur kampus ini dirancang untuk menghindari diskriminasi berbasis gender",
            "Saya terlibat dalam kegiatan sukarela yang bertujuan mendukung perempuan dalam mencapai kesetaraan dan keadilan di luar kampus",
            "Kampus ini memiliki pusat sumber daya yang menyediakan informasi dan dukungan terkait isu-isu kesetaraan gender",
            "Saya menyadari adanya program beasiswa atau insentif khusus yang ditujukan untuk mendukung mahasiswa perempuan dalam pengembangan akademis mereka",
            "Saya senang melihat representasi yang seimbang dari berbagai jenis kelamin dalam dewan mahasiswa atau organisasi utama di kampus",
            "Pada saat acara-acara besar seperti peringatan hari-hari penting, kampus ini menyelenggarakan kegiatan yang mengedepankan kesetaraan gender",
            "Saya pernah terlibat dalam pengembangan kebijakan kampus yang berfokus pada mewujudkan lingkungan yang lebih inklusif dan setara",
            "Selama magang atau pengalaman kerja di kampus, saya melihat bahwa perempuan dan laki-laki memiliki kesempatan yang setara untuk mendapatkan pengalaman dan pembelajaran",
            "Saya memiliki mentor atau pembimbing yang mendukung dan memotivasi saya, tanpa memandang perbedaan jenis kelamin",
            "Kampus ini memberikan ruang bagi diskusi terbuka mengenai isu-isu kesetaraan gender, menciptakan kesadaran dan pemahaman yang lebih baik di kalangan mahasiswa dan staf",
        ],
        [
            "Saya merasa bahwa ada kesenjangan dalam representasi gender di beberapa kepengurusan atau organisasi kampus",
            "Terkadang, saya melihat bahwa pengambilan keputusan di kampus cenderung didominasi oleh satu jenis kelamin",
            "Beberapa pengalaman saya menunjukkan bahwa perempuan mungkin kurang terlibat dalam diskusi atau kegiatan akademis yang penting",
            "Kampus ini belum sepenuhnya menghilangkan stereotip gender dalam pemilihan program studi atau jurusan tertentu",
            "Saya menyadari adanya perbedaan dalam pendekatan dan ekspektasi terhadap mahasiswa berdasarkan jenis kelamin di beberapa kelas",
            "Beberapa inisiatif atau program pengembangan karier mungkin lebih terfokus pada satu jenis kelamin daripada yang lain",
            "Saat berpartisipasi dalam proyek kelompok, terkadang saya melihat dominasi suara dari satu jenis kelamin",
            "Perbedaan gaji atau tunjangan antara staf atau dosen berdasarkan jenis kelamin masih menjadi isu yang perlu diperhatikan",
            "Ada situasi di mana perempuan mungkin merasa kurang nyaman atau tidak didukung untuk mengejar karier di bidang-bidang tertentu",
            "Saya merasa bahwa isu-isu kesetaraan gender mungkin tidak mendapatkan perhatian yang cukup dalam kurikulum atau program pendidikan kampus",
            "Saat berinteraksi dengan beberapa dosen atau staf, terkadang saya merasakan adanya prasangka atau stereotip gender",
            "Perempuan mungkin menghadapi tantangan lebih besar dalam mendapatkan dukungan untuk mengambil peran kepemimpinan di beberapa organisasi mahasiswa",
            "Ada kasus di mana komentar atau perlakuan seksual tidak pantas mungkin terjadi tanpa penanganan serius dari pihak kampus",
            "Saya pernah menyaksikan adanya ketidaksetaraan dalam alokasi sumber daya atau dukungan finansial untuk proyek-proyek mahasiswa berbasis gender",
            "Beberapa peraturan atau kebijakan kampus mungkin tidak cukup melindungi mahasiswa dari diskriminasi atau pelecehan berbasis gender",
        ]
    ],
    [
        [

        ],
        [
            "Tidak ada mata kuliah khusus yang membahas isu-isu gender di dalam kurikulum.",
            "Kampus ini tidak menawarkan studi atau mata kuliah yang fokus pada sosiologi gender.",
            "Sayangnya, tidak ada kursus di bidang psikologi yang secara eksplisit mengajarkan tentang gender.",
            "Mata kuliah sastra di sini tidak memiliki fokus khusus pada perspektif feminis.",
            "Tidak ada program hukum dan gender yang tersedia dalam penawaran kuliah kampus.",
            "Mata kuliah ekonomi yang membahas isu-isu feminis tidak termasuk dalam daftar program studi.",
            "Kesehatan reproduksi dan gender bukan bagian dari mata kuliah yang ditawarkan di jurusan kesehatan.",
            "Mata kuliah seni di sini tidak mencakup aspek-aspek feminisme atau isu-isu gender.",
            "Tidak ada mata kuliah khusus yang membahas hak reproduksi dan gender dalam kurikulum.",
            "Pendidikan inklusif gender bukan bagian dari kurikulum pendidikan di kampus ini.",
            "Mata kuliah politik yang mencakup aspek gender tidak tersedia dalam program studi.",
            "Sayangnya, tidak ada kursus yang secara eksplisit mengajarkan tentang politik gender.",
            "Program pendidikan di sini tidak mencakup mata kuliah tertentu tentang kesetaraan gender.",
            "Mata kuliah yang fokus pada ekonomi feminis tidak termasuk dalam daftar opsi.",
            "Tidak ada program studi khusus yang mengeksplorasi hubungan antara seni dan feminisme.",
            "Mata kuliah yang membahas isu-isu gender dalam hukum tidak termasuk dalam program ini.",
        ],
        [
            "-",
            "Saya tidak yakin apakah ada mata kuliah dengan nama tersebut di kurikulum",
            "tidak tahu",
            "Saya belum mengetahui apakah ada kelas tersebut di penawaran program studi",
            "-",
            "-",
            "Belum ada informasi yang saya dapatkan mengenai keberadaan mata kuliah tersebut",
            "Tidak ada kabar mengenai mata kuliah itu dalam daftar kuliah yang saya terima",
            "Tidak Tahu",
            "Saat ini, saya belum memiliki pengetahuan apakah mata kuliah itu masih ada atau tidak",
            "-",
            "Belum ada konfirmasi apakah mata kuliah tersebut masih ditawarkan",
            "Saya tidak dapat memastikan apakah mata kuliah tersebut termasuk dalam kurikulum",
            "-",
            "Belum ada petunjuk mengenai keberadaan mata kuliah tersebut di katalog akademik",
            "tidak tahu",
            "Saya tidak mengetahui apakah mata kuliah itu masih aktif atau sudah dihapus",
            "Saat ini, saya belum bisa memberikan informasi apakah mata kuliah itu ada",
            "Belum ada pemberitahuan resmi apakah mata kuliah tersebut masih dipertahankan",
            "-",
            "Saya belum tahu apakah mata kuliah tersebut masih tersedia di semester ini",
            "Tidak ada kepastian mengenai keberadaan mata kuliah tersebut dalam penawaran akademik",
            "-",
            "Tidak tahu",
            "Tidak tahu akan hal tersebut",
            "Saat ini, saya belum mendapat informasi apakah mata kuliah tersebut masih tersedia",
            "-",
            "Belum ada penjelasan mengenai status terbaru dari mata kuliah tersebut",
            "Saya tidak memiliki informasi yang memadai untuk menyatakan keberadaan mata kuliah itu",
            "Saat ini, saya belum mengetahui apakah mata kuliah tersebut dihapus atau masih ada",
            "-",
            "Tidak ada konfirmasi yang saya terima terkait ketersediaan mata kuliah tersebut",
            "Saya tidak yakin apakah mata kuliah tersebut masih termasuk dalam kurikulum",
            "Belum ada klarifikasi mengenai apakah mata kuliah tersebut masih diajarkan atau tidak",
        ]
    ],
]

kategori = [
    [
        35,15
    ],
    [
        0,16,34
    ],
]

indexIsian = [
    [
        0,0
    ],
    [
        0,0,0
    ]
]

index = 0
        
try:
    for i in range(len(profil)):
        time.sleep(2)
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
        chrome_options.add_argument("profile-directory="+profil[i])

        driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)
        driver.get(link)

        times = 1
        idx = 1
        idxx = 1

        while times:
            time.sleep(2)

            if idx == 10:
                idx = 0

            option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

            option[0].click()

            time.sleep(10)
            driver.switch_to.window(driver.window_handles[idxx])
            time.sleep(2)

            radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
            radiobuttons[idx].click()

            time.sleep(10)
            # ================================================================================

            tipeKesetaraan = pilihTipe(kategori[0])
            kategori[0][tipeKesetaraan] -= 1
            kesetaraan = random.choice([0,0,0,1,1,1,2]) if tipeKesetaraan == 0 else random.choice([2,3,3,3,4,4,4])

            isianKesetraan = isianJawab[0][tipeKesetaraan][indexIsian[tipeKesetaraan]]
            indexIsian[0][tipeKesetaraan] += 1

            tipeMatkul = pilihTipe(kategori[1])
            kategori[1][tipeMatkul] -= 1
            matkul = tipeMatkul

            isianMatkul = isianJawab[1][tipeMatkul][indexIsian[tipeMatkul]]
            indexIsian[1][tipeMatkul] += 1



            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

            checkboxes[0].click()

            time.sleep(2)
            radiobuttons[0].click()

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

            radiobuttons[kesetaraan].click()

            time.sleep(2)
            textarea[0].send_keys(isianKesetraan)

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            
            radiobuttons[random.choice([1,2])].click()
            radiobuttons[random.choice([6,7])].click()

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(3)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

            radiobuttons[matkul].click()

            time.sleep(2)
            textarea[0].send_keys(isianMatkul)

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            radiobuttons[random.choice([1,2])].click()
            
            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            radiobuttons[random.choice([1,2])].click()
            radiobuttons[random.choice([6,7])].click()
            
            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(3)
            kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            if len(kirims1) != 0 :
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
                )
            else:
                submit_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
                )

            submit_button.click()

            time.sleep(2)
            radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

            radiobuttons[1].click()

            # time.sleep(3)
            # kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
            # kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

            # if len(kirims1) != 0 :
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
            #     )
            # else:
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
            #     )

            # submit_button.click()

            # driver.implicitly_wait(4)
            # driver.get(link)

            index += 1
            idx += 1
            idxx += 1
            times -= 1
            print("==================")
            print("times : " + str(times))
            print("index : " + str(index))
            print("idx  : " + str(idx))
            print("idxx : " + str(idxx))
            print("")
            print("kategori = " + str(kategori[0]))
            print("         = " + str(kategori[1]))
            print("indexisian = " + str(indexIsian[0]))
            print("           = " + str(indexIsian[1]))

        driver.quit()
        
finally:
    # driver.quit()
    print("berhasil")

            # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
            # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
            # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
            # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
            # textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
            # pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

            # dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
            # option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

            # time.sleep(3)
            # kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Berikutnya')]")
            # kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Next')]")

            # if len(kirims1) != 0 :
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
            #     )
            # else:
            #     submit_button = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next')]"))
            #     )

            # submit_button.click()
