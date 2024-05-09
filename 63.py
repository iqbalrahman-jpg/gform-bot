from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfWt-293AdvzdB__rF_kjVf9_niUqF2ASo2_zLhpo-Z7wweUg/viewform?usp=sharing")

nama = [
    "Mutia Ayu Nur",
    "Ali Hasanudin",
    "Riskia Ayu Febrianti",
    "Budi Prasetyo Wibowo",
    "Aryo Nugraha",
    "Nana Annisa",
    "Yahya Nugraha",
    "Putri Kirana Dewi",
    "Nanda Marsa Ayunda",
    "Yudi Pradanawan",
    "Yuli Ayunda Dewi",
    "Bayu Danang Merta",
    "Bellanda Clara Ayunda", 
    "Budi Suryanto",
    "Miranda Nella",
    "Sadewa Lingga Budiantoro",
    "Alffianto Kuntoro",
    "Annisa Chania",
    "Fattahilah Sadewa",
    "Diah Ayu Cindy",
    "Attaka Majid",
    "Azzarin Ristia Nabila",
    "Fabian Nadeo Putra",
    "Nia EKa Yuliana",
    "Bayu Dwiganara",
    "Syifa Radifah",
    "Aditya Derdinand",
    "Siti Fauziyah",
    "Reyhan Utomowa",
    "Salma Arowaya",
    "Angga Siregar Putra",
    "Putri Keancana",
    "Raja Putra Wardanawan",
    "Affifah Rahman Nabila",
    "Shaka Kurnia Wijaya",
    "Cynara Nafisah",
    "Mona Hadfinna",
    "Mahendra Rhejaa Fadilah",
    "Fryshta Eka Nabilla",
    "Yanuar Suryadi",
    "Rayhan Adi Wicasa",
    "Sutisna Ayuni",
    "Ayu Yulistya Ningsih",
    "M. Putra Susanto",
    "Ardyanto Rizki Putra",
    "Putra Wirawan",
    "Agung Nugroho",
    "Dani Ramadhan",
    "Dimas Purbo",
    "Nabilla Syaqila Qolbi",

]

# laki 0 perempuan 1
kelamin = [1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,]

telp = [
    "084624253733",
    "088565440513",
    "083626799003",
    "088070442682",
    "083435047182",
    "089579629094",
    "080103002233",
    "086659262105",
    "087136378661",
    "080640301967",
    "083806763847",
    "088509885576",
    "084985961237",
    "086137328130",
    "089843988039",
    "086738422620",
    "089045039379",
    "087788078906",
    "088159431881",
    "089474988296",
    "088530547344",
    "085109243357",
    "080470592685",
    "083273198985",
    "081850592479",
    "081211906212",
    "081212784008",
    "081250284950",
    "081264718461",
    "081280281529",
    "081290475868",
    "081270348686",
    "082132447386",
    "087886158249",
    "081278010606",
    "087778433058",
    "085956060930",
    "087848003451",
    "0882008113306",
    "083838919000",
    "081511323691",
    "088294743163",
    "083181803358",
    "081331973192",
    "0895609625455",
    "085729979914",
    "085156051463",
    "085729213992",
    "087780590374",
    "081720592854",
]

saranfitur = [
    "Fitur-fiturnya sudah memadai, tetapi masih perlu dikembangkan dan dipertahankan.",
    "Semua fitur yang ada sudah cukup, namun perlu terus diperbarui dan ditingkatkan.",
    "Fitur-fiturnya sudah memenuhi kebutuhan, namun tetap perlu dikembangkan lebih lanjut.",
    "Seluruh fitur yang tersedia sudah cukup, namun perlu diperbaiki dan ditingkatkan.",
    "Fitur-fiturnya sudah mencukupi, namun harus terus diperbarui agar tetap relevan.",
    "Semua fitur yang sudah ada sudah cukup, tapi perlu dijaga agar tetap bermanfaat.",
    "Fitur-fiturnya sudah memadai, tetapi perlu dipelihara dan ditingkatkan agar lebih baik lagi.",
    "Semua fitur yang telah tersedia sudah cukup, namun perlu ditingkatkan fungsionalitasnya.",
    "Fitur-fitur yang ada sudah mencukupi, tetapi harus terus disempurnakan.",
    "Fitur-fitur yang sudah ada sudah cukup, namun perlu diuji kembali untuk meningkatkan performanya.",
    "Seluruh fitur yang telah disediakan sudah memenuhi kebutuhan, namun perlu ditingkatkan keandalannya.",
    "Fitur-fitur yang tersedia sudah mencukupi, tetapi perlu diperluas untuk mengakomodasi kebutuhan baru.",
    "Semua fitur yang ada sudah cukup, namun harus diperbaharui secara berkala agar tetap relevan.",
    "Fitur-fitur yang tersedia sudah memadai, tetapi perlu dievaluasi dan ditingkatkan berdasarkan umpan balik pengguna.",
    "Semua fitur yang telah tersedia sudah cukup, tetapi harus terus ditingkatkan agar lebih user-friendly.",
    "Fitur-fiturnya sudah mencukupi, tetapi perlu ada pembaruan secara berkala untuk menjaga keamanan.",
    "Seluruh fitur yang ada sudah memenuhi harapan, namun perlu dikembangkan untuk meningkatkan pengalaman pengguna.",
    "Fitur-fitur yang tersedia sudah cukup, tetapi harus dipelajari dan dimanfaatkan dengan baik oleh pengguna.",
    "Semua fitur yang telah disediakan sudah cukup, tetapi perlu diperhatikan untuk meningkatkan kinerjanya.",
    "Fitur-fitur yang sudah ada sudah mencukupi, tetapi perlu diperbarui agar tetap kompatibel dengan teknologi terbaru.",
    "Seluruh fitur yang tersedia sudah memadai, tetapi perlu dikembangkan lebih lanjut untuk meningkatkan kepuasan pengguna.",
    "Fitur-fitur yang ada sudah mencukupi, tetapi harus terus ditingkatkan agar lebih intuitif dan mudah digunakan.",
    "Semua fitur yang telah tersedia sudah cukup, namun harus terus dijaga dan ditingkatkan sesuai dengan perkembangan teknologi.",
    "Fitur-fitur yang tersedia sudah memadai, tetapi perlu dikembangkan lebih lanjut untuk menghadapi tantangan masa depan.",
    "Seluruh fitur yang ada sudah cukup, namun harus dipertahankan dan ditingkatkan dalam hal perform",
    "Fitur-fitur yang telah disediakan sudah mencukupi, tetapi harus tetap dioptimalkan untuk memberikan pengalaman terbaik kepada pengguna.",
    "Semua fitur yang ada sudah cukup, namun perlu dilakukan evaluasi secara berkala guna meningkatkan efisiensi.",
    "Fitur-fitur yang tersedia sudah memadai, namun perlu ditingkatkan agar dapat bersaing dengan produk sejenis di pasaran.",
    "Seluruh fitur yang telah disiapkan sudah cukup, tetapi perlu terus ditambahkan fitur baru sesuai dengan kebutuhan pengguna.",
    "Fitur-fitur yang ada sudah mencukupi, tetapi harus tetap fleksibel untuk mengakomodasi perubahan kebutuhan pengguna.",
    "Semua fitur yang telah disediakan sudah cukup, tetapi perlu terus diuji coba dan diperbaiki agar sesuai dengan harapan pengguna.",
    "Fitur-fitur yang tersedia sudah memadai, namun perlu ada mekanisme umpan balik pengguna untuk terus memperbaiki dan mengembangkan.",
    "Seluruh fitur yang ada sudah cukup, tetapi perlu diberikan panduan penggunaan yang jelas agar pengguna dapat memanfaatkannya dengan baik.",
    "Fitur-fitur yang telah disediakan sudah mencukupi, tetapi perlu ditingkatkan dalam hal kecepatan dan responsivitas.",
    "Semua fitur yang ada sudah cukup, namun harus tetap disesuaikan dengan kebutuhan dan keinginan pengguna.",
    "Fitur-fitur yang ada sudah mencukupi.",
    "Fitur-fitur yang tersedia sudah memadai, tetapi perlu diupayakan untuk tetap mengikuti perkembangan teknologi terkini.",
    "Seluruh fitur yang telah disediakan sudah cukup, tetapi perlu diberikan pembaruan rutin agar tetap relevan dan bermanfaat.",
    "Fitur-fitur yang ada sudah mencukupi, tetapi perlu diperhatikan keamanannya untuk melindungi data pengguna.",
    "Semua fitur yang telah disediakan sudah cukup, namun perlu dilakukan pengujian secara menyeluruh sebelum dirilis ke publik.",
    "Fitur-fitur yang tersedia sudah memadai, tetapi perlu dilakukan evaluasi kepuasan pengguna secara berkala untuk meningkatkan kualitasnya.",
    "Seluruh fitur yang ada sudah cukup, namun harus terus ditingkatkan agar dapat memberikan solusi yang lebih baik kepada pengguna.",
    "Fitur-fitur yang telah disediakan sudah mencukupi, tetapi perlu dibuat lebih intuitif agar mudah dipahami oleh pengguna.",
    "Semua fitur yang ada sudah cukup, namun perlu dilakukan pengoptimalan performa agar dapat berjalan lebih efisien.",
    "Fitur-fitur yang tersedia sudah memadai, tetapi perlu diberikan dukungan teknis yang baik agar pengguna dapat menggunakannya dengan lancar.",
    "Seluruh fitur yang telah disiapkan sudah cukup, tetapi perlu diberikan panduan dan tutorial yang lengkap agar pengguna dapat memanfaatkannya dengan maksimal.",
    "Semua fitur yang ada sudah cukup, namun perlu dilakukan peningkatan user interface agar lebih menarik dan mudah digunakan.",
    "Fitur-fitur yang tersedia sudah memadai, tetapi perlu dijaga keberlanjutannya dengan melakukan pemeliharaan rutin.",
    "Seluruh fitur yang telah disediakan sudah cukup, namun perlu dipublikasikan informasi terkait pembaruan fitur kepada pengguna.",
    "Fitur-fitur yang ada sudah mencukupi, tetapi perlu dilakukan pengoptimalan untuk mengurangi waktu respons yang lebih cepat.",
]

sarandesign = [
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit sentuhan warna akan membuatnya lebih menonjol.",
    "Desainnya sudah cukup menarik, namun beberapa efek animasi dapat ditambahkan untuk membuatnya lebih dinamis.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada ukuran font akan membuatnya lebih enak dibaca.",
    "Desainnya sudah cukup menarik, tapi beberapa elemen grafis tambahan dapat memberikan sentuhan yang lebih menarik.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit perubahan layout akan membuatnya terlihat lebih segar.",
    "Desainnya sudah cukup menarik, namun beberapa ikon yang relevan dapat ditambahkan untuk meningkatkan kesan visual.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada margin dan padding akan memberikan kesan yang lebih rapi.",
    "Desainnya sudah cukup menarik, namun beberapa transisi halus antara halaman dapat memberikan pengalaman yang lebih mulus.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit efek parallax dapat memberikan dimensi yang lebih menarik.",
    "Desainnya sudah cukup menarik, namun beberapa gambar latar belakang dapat ditambahkan untuk menciptakan suasana yang lebih kaya.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit variasi pada tipografi akan memberikan tampilan yang lebih menarik.",
    "Desainnya sudah cukup menarik, namun beberapa filter gambar atau efek pencahayaan dapat memberikan suasana yang lebih dramatis.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada proporsi elemen akan memberikan keseimbangan yang lebih baik.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada skema warna dapat memberikan kontras yang lebih menarik.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit perubahan pada komposisi elemen akan memberikan tampilan yang lebih dinamis.",
    "Desainnya sudah cukup menarik, namun beberapa ilustrasi atau grafis kustom dapat menambahkan elemen visual yang unik.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada properti animasi akan memberikan sentuhan yang lebih halus.",
    "Desainnya sudah cukup menarik, namun beberapa elemen berbasis vektor dapat memberikan kesan modern yang lebih menonjol.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada tata letak konten akan memberikan pengalaman yang lebih intuitif.",
    "Desainnya sudah cukup menarik, namun beberapa efek hover pada tombol atau link dapat memberikan interaksi yang lebih menarik.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit variasi pada jenis font akan memberikan kesan yang lebih kreatif.",
    "Desainnya sudah cukup menarik, namun beberapa animasi mikro pada elemen dapat memberikan kehidupan.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penggunaan whitespace yang strategis akan memberikan tampilan yang lebih lega.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada efek transparansi dapat memberikan tampilan yang lebih modern.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit variasi pada tipe penggunaan font akan memberikan nuansa yang lebih beragam.",
    "Desainnya sudah cukup menarik, namun beberapa elemen animasi yang interaktif dapat meningkatkan keterlibatan pengguna.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penggunaan elemen geometris akan memberikan tampilan yang lebih futuristik.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada ukuran dan warna ikon akan memberikan visibilitas yang lebih baik.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada penggunaan gradient dapat memberikan tampilan yang lebih kaya.",
    "Desainnya sudah cukup menarik, namun beberapa efek transisi halus antara halaman dapat memberikan pengalaman yang lebih seamless.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada penggunaan elemen tipografi yang menonjolkan pesan utama akan memberikan efek yang lebih kuat.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada tata letak elemen akan memberikan keteraturan yang lebih jelas.",
    "Tampilan desainnya sudah cukup menarik, namun beberapa penggunaan efek paralaks dapat memberikan dimensi yang lebih dalam.",
    "Desainnya sudah cukup menarik, namun penambahan sedikit animasi mikro pada elemen interaktif dapat memberikan efek yang lebih menarik.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada penggunaan warna yang lebih kontras akan memberikan tampilan yang lebih mencolok.",
    "Desainnya sudah cukup menarik, namun beberapa variasi pada penggunaan grid layout dapat memberikan tampilan yang lebih dinamis.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada ukuran dan posisi elemen teks akan memberikan keseimbangan yang lebih baik.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada jenis animasi yang digunakan dapat memberikan tampilan yang lebih interaktif.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penggunaan elemen ilustrasi yang konsisten akan memberikan kesan yang lebih seragam.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada pemilihan gambar yang lebih relevan dengan konten akan meningkatkan daya tarik visual.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada ukuran font akan memperbaiki keterbacaan.",
    "Desainnya sudah cukup menarik, namun penambahan sedikit efek hover pada tombol dapat memberikan responsivitas yang lebih baik.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada ruang putih antar elemen akan memberikan tampilan yang lebih teratur.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada tata letak navigasi akan meningkatkan keterjangkauan pengguna.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada skema warna untuk menciptakan kontras yang lebih baik.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada pemilihan font yang lebih sesuai dengan tema akan meningkatkan kesesuaian visual.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penyesuaian pada pemilihan ikon yang lebih konsisten akan memberikan tampilan yang lebih harmonis.",
    "Desainnya sudah cukup menarik, namun beberapa variasi pada penggunaan tipografi akan memberikan tampilan yang lebih menarik secara visual.",
    "Tampilan desainnya sudah cukup menarik, tetapi sedikit penambahan efek transisi yang halus akan memberikan pengalaman pengguna yang lebih lancar.",
    "Desainnya sudah cukup menarik, namun beberapa perubahan pada tata letak konten untuk meningkatkan fokus pada elemen kunci akan memberikan tampilan yang lebih efektif.",
]

times = 25
index = 25
mudah = 25
susah = 0

# ada kak, request jawaban di page 1
# - Apakah anda sudah mengetahui layanan bank digital: Iya
# - Apakah anda sudah menggunakan layanan bank digital: Tidak

try:
    while times:
        time.sleep(11)
        #Hardcoded logic
        test = 0
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        pilihan = driver.find_elements("css selector", ".Hvn9fb")#pilihan
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        textboxes[0].send_keys(nama[index])
        radiobuttons[kelamin[index]].click()
        textboxes[1].send_keys("Mts Assakinah")
        radiobuttons[2].click()
        textboxes[2].send_keys(telp[index])
        p = 0
        lagi = random.choice([p,p+1,p+2,p+3,p+4,p+3,p+4])
        testcheck[lagi].click()
        p = 5
        if mudah != 0 and susah != 0:
            indikator = random.choice([1,2])
            if indikator == 1:
                jawab = random.choice([p,p+1,p,p+1,p,p+1,p+2])
                mudah -= 1
            else:
                jawab = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
                susah -= 1
        elif mudah == 0:
            jawab = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            susah -= 1
            indikator = 2
        elif susah ==0:
            jawab = random.choice([p,p+1,p,p+1,p,p+1,p+2])
            mudah -= 1
            indikator = 1

        p = 10
        testcheck[jawab].click()
        if jawab >= 3:
            s3 = random.choice([p,p+1,p,p+1,p,p+1,p+2])
        else:
            s3 = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
        
        testcheck[s3].click()
        p = 15
        if jawab >= 3:
            s4 = random.choice([p+1,p+1,p+2,p+3,p+4,p+3,p+4,p+3,p+4])
        else:
            s4 = random.choice([p,p+1,p,p+1,p,p+1,p+2])

        testcheck[s4].click()
        p = 20
        s5 = random.choice([p+1,p+1,p+2,p+3,p+4,p+3,p+4,p+3,p+4])
        testcheck[s5].click()
        p = 25
        s6 = random.choice([p,p,p,p+1,p+1,p+1,p+2,p+3,p+3])
        testcheck[s6].click()
        p = 30
        s7 = random.choice([p+1,p+1,p+2,p+3,p+4,p+3,p+4,p+3,p+4])
        testcheck[s7].click()
        p = 35
        if indikator == 1:
            s8 = random.choice([p,p,p,p+1,p+1,p+1,p+2,p+3,p+3])
            testcheck[s8].click()
        else:
            s8 = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            testcheck[s8].click()
        p = 40
        s9 = random.choice([p+1,p+2,p+3,p+4,p+3,p+4,p+3,p+4])
        testcheck[s9].click()
        p = 45
        if indikator == 1:
            s10 = random.choice([p,p,p,p+1,p+1,p+1,p+2,p+3,p+3])
            testcheck[s10].click()
        else:
            s10 = random.choice([p+2,p+3,p+4,p+3,p+4,p+3,p+4])
            testcheck[s10].click()

        textarea[0].send_keys(saranfitur[index])
        textarea[1].send_keys(sarandesign[index])
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfWt-293AdvzdB__rF_kjVf9_niUqF2ASo2_zLhpo-Z7wweUg/viewform?usp=sharing")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("mudah : " + str(mudah))
        print("susah : " + str(susah))

        times-=1
        print("times : " + str(times))
        
finally:
	# driver.quit()
    print("berhasil")

    # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
    # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
    # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox