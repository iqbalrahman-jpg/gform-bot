from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import random
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfzgQoO9VEH4x8TD29dAiy-rejg6NqV9ydL0VioFuEn0HTWXw/viewform")

email = [
    "mtianur001@gmail.com",
    "alihasn.01.10@gmail.com",
    "risfebri11@gmail.com",
    "budprasety@gmail.com",
    "aryonugh@gmail.com",
    "nanissa0110@gmail.com",
    "yahnugrah@gmail.com",
    "putriptr0110@gmail.com",
    "nandayundaa1@gmail.com",
    "yudipradan01@gmail.com",
    "yulayund1@gmail.com",
    "byumerta1@gmail.com",
    "Bellandayu01@gmail.com",
    "budsuryant01@gmail.com",
    "nela.mirra@gmail.com",
    "dwa.lingga10@gmail.com",
    "alffiantoro@gmail.com",
    "annicsaa@gmail.com",
    "fataahxdewa@gmail.com",
    "diahcindy03@gmail.com",
    "attakmajid@gmail.com",
    "azzarinrst@gmail.com",
    "fabiannadeo@gmail.com",
    "niaejuliana@gmail.com",
    "bayudwiganara@gmail.com",
    "syifaradifah@gmail.com",
    "aditferdinanda@gmail.com",
    "sitifauziyyahh@gmail.com",
    "reyhanutomowa@gmail.com",
    "salmaarowaya@gmail.com",
    "anggasiregarp@gmail.com",
    "putrikeancana@gmail.com",
    "rajawardanawan@gmail.com",
    "affifahh7@gmail.com",
    "shakapwijaya@gmail.com",
    "cynnarafisa@gmail.com",
    "monahfnna87@gmail.com",
    "mahendrejaa@gmail.com",
    "fryshta.eka823@gmail.com",
    "yanrasuryad@gmail.com",
    "rahannadi1@gmail.com",
    "sutisnayun@gmail.com",
    "ayulistyaan@gmail.com",
    "muhh.santosoo@gmail.com",
    "rudinurbaktii01@gmail.com",
    "ptrawiraw.an@gmail.com",
    "agungnugh@gmail.com",
    "dn.ramadhan@gmail.com",
    "dimas.purbo07@gmail.com",
    "nabilla.s.qolbi@gmail.com",
]

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

domisili = [
    "jogja", "Jogja", "jogjakarta", "Yogyakarta", "Jogjakarta", "yogyakarta", "DIY", "DI Yogyakarta"
]

essai = [
    [
        "iya, karena efek suara yang santai bisa membantu saya rileks saat akan memulai pertandingan",
        "Menggunakan musik latar yang sesuai dapat memberikan perasaan harmoni saat bermain Mobile Legends",
        "bagi saya iya, karena musik latar yang epik bisa meningkatkan motivasi saya dalam bermain",
        "iya, musik yang santai bisa membantu saya rileks saat pertandingan yang intens",
        "Tentu, mengapa tidak? Musik latar yang sesuai bisa menciptakan suasana yang menyenangkan bagi saya",
        "iya tentu, suara-suara kemenangan dapat memberikan penghargaan yang memuaskan sehingga dapat lebih menikmato permainan",
        "Suara-suara detail dalam permainan Mobile Legends meningkatkan kepuasan bermain",
        "Mengapa tidak menggabungkan efek suara dan musik latar yang sesuai untuk pengalaman bermain yang lebih lengkap?",
        "Musik latar yang mendalam menciptakan suasana epik dalam pertandingan Mobile Legends",
        "iya karena bisa meningkatkan tingkat imersi antar pemain dalam game",
        "iya karena musik dan efek suara dapat mengurangi keheningan saat bermain, membuatnya lebih menarik dan jauh lebih nyaman",
        "Suara-suara karakter dalam permainan memberi mereka identitas yang unik dan membuatnya lebih menarik",
        "Musik latar yang cocok membuat setiap momen dalam permainan menjadi lebih dramatis dan berkesan",
        "Efek suara seperti suara tembakan dan ledakan menambah ketegangan dan intensitas dalam permainan",
        "iya, karena musik latar juga dapat menunjukkan bahwa kita sedang bermain, tanpa musik rasanya akan hampa dan membosankan",
        "iya, efek suara bisa memberikan petunjuk audio penting dalam match",
        "Efek suara yang tenang bisa membantu saya merasa lebih nyaman saat memulai pertandingan baru",
        "Musik latar yang dinamis mempertahankan motivasi saya selama bermain Mobile Legends",
        "Suara-suara kemenangan dan pencapaian membuat perasaan puas setelah memenangkan pertandingan",
        "Suara-suara perintah tim dan komunikasi dengan rekan satu tim sangat penting untuk kerja sama yang efektif",
        "Musik latar yang tidak terlalu mendalam membuat permainan terasa lebih santai dan menyenangkan",
        "tidak karena saya lebih sering bermain tanpa musik dan efek suara",
        "tidak, karena efek suara yang ada sama saja dengan tidak menggunakan",
        "Menghidupkan efek suara dan musik latar adalah cara bagus untuk merayakan kemenangan dalam permainan",
        "Efek suara yang realistis membuat setiap situasi dalam permainan terasa lebih nyata",
        "Penggunaan efek suara yang tepat meningkatkan pengalaman bermain Mobile Legends secara keseluruhan",
        "iya, karena suara-suara lingkungan dapat membantu saya dalam kenyamanan mengidentifikasi situasi dalam game",
        "Ya, efek suara dalam Mobile Legends tidak hanya menyenangkan tetapi juga membantu saya terlibat dalam permainan",
        "iya karena musik yang enak didengar dapat meningkatkan kesenangan bermain",
        "tidak, menurut saya adanya musik atau tidak tidak mempengaruhi tingkat kenyamanan bermain",
        "suara karakter dapat membuat kenyamanan tersendiri bagi saya dalam bermain",
        "iya, karna musik latar juga dapat mendukung cerita sehingga dapat kenyamanan saat bermain",
        "Musik latar yang dipilih dengan baik bisa membuat permainan semakin menarik dan menambah keasyikan saat bermain",
        "Dengan musik latar yang pas, saya merasa lebih terhubung dengan karakter dalam Mobile Legends",
        "tidak, saya terbiasa main tanpa musik dan efek suara juga sudah tidak apa apa",
        "Musik latar yang santai sangat membantu saya merasa lebih rileks saat menjalani pertandingan panjang",
        "iya, karena fek suara bisa membantu saya dalam kanyamanan bermain",
        "Iya, karena suara dan musik latar dapat menciptakan atmosfer yang lebih mendalam dalam permainan",
        "tentu iya, karena suara dan musik bisa memicu emosi pemain, seperti kegembiraan atau ketegangan akhirnya gamenya akan menjadi lebih seru dan nyaman",
        "Efek suara yang kuat dan realistis selalu membuat pengalaman bermain Mobile Legends menjadi lebih mendalam",
        "Efek suara yang realistis membantu saya merasakan adrenalin permainan dengan lebih intens",
        "Musik latar yang menyenangkan bisa membuat saya tetap termotivasi bahkan saat pertandingan berlangsung sulit",
        "iya, karena suara-suara komunikasi dalam permainan juga dapat meningkatkan interaksi sosial dengan pemain lain",
        "iya, karena efek suara dapat meningkatkan keterlibatan saya ke dalam oermainan",
        "tidak, karena efek dari musik latar tidak terlalu berpengaruh terhadap tingkat kenyamanan bermaiin",
        "tentu, karena musik latar yang cocok dapat membantu saya tetap nyaman",
        "Efek suara yang detail membantu saya memahami peristiwa dalam permainan dengan lebih baik",
        "iya karena terkadang musik latar yang mendalam dapat meningkatkan perasaan prestasi setelah menang",
        "Penggunaan musik latar yang bijaksana membantu menjaga tingkat fokus selama pertandingan",
        "iya, karena Suara-suara positif bisa memberikan penghargaan kepada pemain"
    ],
    [
        "Kehadiran musik dan efek suara adalah kunci untuk menjaga semangat dan kegembiraan selama bermain",
        "Musik adalah elemen yang membangkitkan emosi dalam permainan dan membuatnya lebih mendalam",
        "Efek suara dan musik latar membuat permainan menjadi lebih seru dan semangat",
        "Efek suara dan musik latar menjadikan permainan lebih mendalam dan penuh semangat",
        "Musik dalam permainan adalah seperti pemberi semangat yang terus mendorong saya untuk bermain dengan semangat",
        "Dalam Mobile Legends, musik adalah teman setia yang selalu ada untuk mendukung semangat pemain",
        "Efek suara dan musik latar yang disertakan dalam permainan ini benar-benar meningkatkan aspek keseruan dalam bermain",
        "Penting untuk fokus pada perbaikan keterampilan dan koordinasi tim daripada terlalu memikirkan efek suara atau musik dalam permainan",
        "Efek suara dan musik latar yang digunakan dalam permainan memastikan bahwa setiap momen di dalamnya memiliki rasa semangat yang kuat",
        "Perpaduan musik dan efek suara menciptakan permainan yang lebih menarik dan membuatnya semakin menggugah semangat",
        "Saya sangat setuju, musik dalam permainan benar-benar membantu membangkitkan semangat dan menjaga saya termotivasi",
        "Permainan yang lebih serius mungkin lebih memilih mematikan musik dan efek suara untuk memaksimalkan konsentrasi dan komunikasi tim",
        "Dalam permainan, musik dan efek suara adalah elemen yang tak terpisahkan yang membuatnya semakin menarik",
        "Kehilangan elemen musik dalam permainan bisa membuat pengalaman bermain terasa monoton dan kurang menginspirasi",
        "Musik adalah pengingat konstan akan semangat dan tujuan saya saat bermain Mobile Legends",
        "iya, bermain tanpa musik akan membuat permainan terasa bosan dan mengurangi peluang kemenangan",
        "Efek suara yang mendukung peristiwa-peristiwa dalam permainan membuatnya lebih menarik dan semangat",
        "Efek suara dan musik latar membantu menciptakan pengalaman bermain yang lebih bersemangat dan berkesan",
        "Tanpa musik, permainan menjadi hambar dan kehilangan nuansa yang membuatnya menjadi pengalaman yang lebih khas",
        "Dalam pertandingan yang kompetitif, pemain seringkali memilih untuk mematikan suara dan fokus pada komunikasi tim dan taktik permainan",
        "tentu, dengan musik dan efek suara akan membuat permainan menjadi lebih seru dan semangat",
        "Efek suara yang kuat memicu emosi pemain dan membuat permainan lebih seru",
        "iya, adanya musik dan efek suara game jadi lebih seru dan asik",
        "Tanpa musik dan efek suara, permainan menjadi kurang menarik dan tidak memiliki daya tarik yang sama",
        "Kombinasi musik dan efek suara menciptakan pengalaman bermain yang lebih seru, dan itu adalah hal yang benar-benar saya nikmati",
        "Musik latar dan efek suara membantu menciptakan permainan yang lebih seru dan semangat yang tak terbantahkan",
        "Efek suara dan musik latar menciptakan permainan yang lebih mendalam dan memotivasi pemain untuk terus berusaha",
        "Efek suara dan musik mungkin dapat menghibur, tetapi mereka bukanlah faktor kunci yang memengaruhi hasil permainan",
        "Kemenangan dalam Mobile Legends lebih banyak tentang pengetahuan, kerja sama, dan pengambilan keputusan yang baik daripada musik latar atau efek suara",
        "tidak, karena skill yang akan menjadi penentu skor akhir dan jalannya permainan ",
        "Musik dalam permainan adalah sumber energi yang tak terbantahkan yang terus memompa semangat dalam diri saya",
        "Musik latar adalah pendorong semangat yang membantu saya tetap fokus selama permainan Mobile Legends",
        "iya, adanya musik latar dan efek suara menjadikan permainan lebih seru",
        "Permainan tanpa musik akan kehilangan nuansa semangat yang membuatnya begitu menarik",
        "Dalam permainan, ada daya tarik khusus dalam musik dan efek suara yang membawa semangat dan kegembiraan",
        "Kehadiran musik dan efek suara dalam permainan menjadikan setiap momen lebih bersemangat dan menyenangkan",
        "Tentu, tanpa ragu, musik dalam permainan adalah penyemangat yang kuat yang selalu meningkatkan semangat saya",
        "tidak, karena skill yang akan menjadi penentu skor akhir dan jalannya permainan ",
        "Kehadiran musik dan efek suara dalam permainan adalah seperti sumber daya semangat yang tak terputus",
        "Perpaduan musik dan efek suara dalam Mobile Legends adalah salah satu faktor kunci yang membuat permainan ini begitu seru dan semangat",
        "Efek suara dan musik latar membawa permainan Mobile Legends ke tingkat baru dalam hal keseruan dan antusiasme",
        "Meskipun musik dan efek suara bisa menjadi hiburan, tidak ada yang menggantikan pentingnya strategi dan pelaksanaan dalam permainan ini",
        "Penting untuk diingat bahwa keterampilan, strategi, dan kerjasama tim adalah aspek yang lebih krusial dalam permainan ini daripada musik atau efek suara",
        "Ketika musik dan efek suara berpadu dengan baik, permainan menjadi lebih menarik dan penuh dengan semangat",
        "Saya tidak setuju, karena dalam permainan seperti Mobile Legends, skill pemain yang akan menjadi faktor penentu dalam menentukan skor akhir dan mengendalikan jalannya permainan",
        "Meskipun musik dapat menjadi tambahan yang menyenangkan, kemenangan dalam Mobile Legends lebih tergantung pada kemampuan dan keputusan pemain",
        "Musik adalah bahan bakar emosi yang menjaga semangat selama permainan Mobile Legends",
        "Dalam Mobile Legends, musik dan efek suara adalah sahabat sejati yang selalu hadir untuk menaungi semangat bermain saya",
        "iya, karena dengan adanya musik akan membangkitkan semangat ",
        "Musik dan efek suara membantu menciptakan atmosfer yang benar-benar menghidupkan permainan",
    ],
    [
        "Efek suara dan musik latar mungkin bisa membuat permainan lebih menghibur, tetapi tidak selalu membuatnya lebih mudah",
        "tidak, musik dan efek suara justru akan mempermudah dalam permainan",
        "Efek suara yang berlebihan dalam permainan bisa membuat situasi terasa lebih rumit dan sulit untuk diprediksi",
        "Saya merasa bahwa permainan tanpa musik dan efek suara dapat membantu pemain lebih fokus pada strategi dan taktik",
        "Meskipun musik bisa menjadi tambahan yang menyenangkan, saya merasa bahwa dalam pertandingan yang intens, fokus tanpa gangguan musik adalah kunci",
        "Fokus pada komunikasi dengan tim dan pemahaman taktik lebih penting daripada terlalu khawatir tentang musik dan efek suara",
        "Saya cenderung berpikir bahwa efek suara yang terlalu bising dan musik latar yang intensif dapat mengaburkan detail-detail penting dalam permainan",
        "Mematikan musik dan efek suara adalah pilihan yang banyak pemain pilih untuk meningkatkan fokus dan pengertian situasi permainan",
        "Terlalu banyak suara dalam permainan dapat mengganggu komunikasi tim dan koordinasi taktik",
        "Terkadang, musik dan efek suara dalam permainan malah membuat saya terlalu terobsesi dengan elemen-elemen audio dan kurang memperhatikan permainan itu sendiri",
        "Adanya musik dan efek suara yang berlebihan sering kali mengaburkan suara-suara penting dalam permainan",
        "Saya cenderung bermain lebih baik tanpa musik dan efek suara yang mengalihkan perhatian dari permainan itu sendiri",
        "Kehadiran musik dan efek suara kadang-kadang bisa membingungkan pemain dengan suara-suara yang berlebihan",
        "Saya lebih memilih mematikan musik dan efek suara agar dapat lebih fokus pada koordinasi taktik dalam permainan",
        "Efek suara yang terlalu kuat seringkali membuat saya merasa terlalu tegang, sehingga membuat permainan menjadi lebih sulit",
        "Meskipun musik dapat meningkatkan suasana, mereka tidak selalu membuat permainan menjadi lebih mudah",
        "Terlalu banyak musik dan efek suara dalam permainan seringkali membuat saya merasa lebih tertekan dan kurang leluasa dalam mengambil keputusan",
        "Tidak, dengan adanya musik latar dan efek suara membuat permainan terasa lebih intens dan menantang",
        "Saya percaya bahwa fokus pada permainan, tanpa gangguan musik atau efek suara, adalah kunci untuk meningkatkan kinerja dalam Mobile Legends",
        "Meskipun musik latar bisa menambahkan suasana, mereka tidak selalu memudahkan permainan",
        "iya, dengan adanya musik latar dan efek suara membuat permainan jauh lebih mudah",
        "Saya lebih suka bermain tanpa musik dan efek suara untuk menjaga fokus dan konsentrasi selama permainan",
        "Tidak setuju, efek suara dan musik latar sering kali menjadi gangguan yang menghalangi pemain dalam mengambil keputusan penting",
        "Musik latar yang terlalu intens dan efek suara yang kuat sering membuat permainan terasa lebih sulit daripada seharusnya",
        "Sebaliknya, adanya musik latar dan efek suara bisa meningkatkan tingkat kesulitan permainan dan membuatnya lebih menarik",
        "Sebaliknya, fokus pada strategi dan kerjasama tim adalah kunci kesuksesan dalam permainan Mobile Legends",
        "Saya lebih suka bermain tanpa musik dan efek suara agar dapat lebih fokus pada permainan dan kerjasama tim",
        "Dalam situasi yang memerlukan koordinasi yang ketat, efek suara yang berlebihan bisa membuat permainan menjadi lebih rumit",
        "Saya lebih memilih bermain dengan kesunyian agar dapat lebih fokus pada aspek-aspek permainan yang lebih penting",
        "Mematikan musik dan efek suara dalam permainan adalah salah satu cara saya menjaga fokus dan kinerja selama pertandingan",
        "Musik dan efek suara dalam jumlah yang berlebihan cenderung mengurangi tingkat konsentrasi pemain",
        "Terlalu banyak suara dalam permainan dapat mengganggu komunikasi tim dan mengacaukan strategi",
        "Saya tidak setuju, musik latar dan efek suara cenderung meningkatkan ketegangan dalam permainan daripada membuatnya lebih mudah",
        "Saya percaya bahwa pemain yang berfokus pada strategi dan kerja tim cenderung lebih berhasil daripada yang terlalu memikirkan musik dan efek suara",
        "Tidak, musik dan efek suara sebenarnya bisa mengganggu perhatian dan membuat pemain kurang fokus",
        "Terlalu banyak suara dalam permainan sering kali membuat saya merasa kurang tenang dan kurang dapat berkonsentrasi",
        "Terlalu banyak informasi audio bisa membingungkan pemain dan mengakibatkan kesalahan dalam pengambilan keputusan",
        "Efek suara yang intens dan musik dramatis justru bisa membuat pemain lebih tegang dan meningkatkan intensitas permainan",
        "Sebaliknya, fokus pada musik dan efek suara bisa menghambat kemampuan pemain untuk memahami detail-detail penting dalam permainan",
        "Terlalu banyak informasi audio dalam permainan kadang-kadang membingungkan dan mengganggu pemahaman situasi permainan",
        "Terlalu banyak musik dan efek suara sering kali membuat permainan menjadi lebih sulit diprediksi",
        "tidak, justru adanya musik latar dan efek suara bisa membuat game menjadi intensif dan mudah",
        "Musik latar yang intens dan efek suara yang kuat seringkali mengganggu kemampuan saya untuk berkomunikasi dengan tim",
        "Musik dan efek suara tidak selalu membuat permainan lebih mudah, karena pemain harus tetap beradaptasi dengan perubahan-perubahan dalam permainan",
        "iya, dengan adanya musik dan efek suara akan membuat permainan jauh lebih mudah karena akan membuat detail kecil lebih terlihat",
        "Terlalu banyak informasi audio bisa membuat saya merasa kurang nyaman dan kurang bisa berpikir dengan jernih dalam permainan",
        "Efek suara yang intens dapat membuat saya merasa terlalu tegang, sehingga kurang bisa bermain dengan santai dan efektif",
        "Musis latar dan efek suara membawa elemen kejutan dan ketegangan yang dapat membuat permainan menjadi lebih sulit",
        "Dalam situasi yang memerlukan koordinasi dan kerjasama tim yang baik, terlalu banyak suara bisa membingungkan",
        "Dalam pertandingan kompetitif, pemain sering memilih untuk mematikan musik dan efek suara untuk memaksimalkan kinerja mereka",
    ],
    [
        "Tidak, memahami efek suara dalam permainan lebih terkait dengan teknik desain suara daripada musik.",
        "Iya, mendengarkan musik dalam permainan dapat membantu melatih telinga untuk mendeteksi nuansa musikal.",
        "Iya, mendengarkan musik dalam permainan dapat membantu memahami interaksi antara suara dan gameplay.",
        "Benar, bisa membantu mengenal komposer yang menciptakan musik untuk permainan tersebut.",
        "Tidak, pengetahuan musik lebih baik diperoleh melalui studi dan pengalaman musikal yang lebih mendalam.",
        "Tidak karena ML sering kali mengulang-ulang musik latar yang sama, sehingga variasi musik yang Anda dengar bisa terbatas.",
        "Tidak, karena mendengarkan musik dalam game tidak memberikan wawasan sejati tentang sejarah musik atau aspek-aspek teori musik yang lebih mendalam.",
        "Tidak, untuk meningkatkan pengetahuan musik, lebih baik mendengarkan karya-karya musik klasik atau berbagai genre yang beragam.",
        "Tidak, pemahaman tentang gameplay dalam permainan tidak selalu terkait dengan pengetahuan musik.",
        "Ya, dapat memperluas pengetahuan tentang peran musik dalam hiburan digital.",
        "Tidak, pendengaran musik dalam permainan mungkin tidak mencakup beragam genre atau gaya musik.",
        "Ya, ini dapat membantu memahami bagaimana musik dapat berinteraksi dengan gameplay.",
        "Tidak, karena kualitas suara dalam game tidak selalu setara dengan rekaman musik profesional.",
        "Benar, dapat memberikan pandangan tentang peran musik dalam menciptakan identitas permainan.",
        "Ya, ini bisa membantu memperluas pengetahuan tentang jenis musik yang digunakan dalam permainan.",
        "Tidak, musik dalam permainan mungkin hanya memiliki nilai intrinsik terbatas dalam pengembangan pengetahuan musik.",
        "Iya, mendengarkan musik latar dan efek suara dalam permainan dapat meningkatkan pemahaman tentang penggunaan musik dalam berbagai konteks.",
        "Iya, bisa membantu memahami perbedaan antara musik latar dan musik aksi dalam permainan.",
        "Tidak, pengetahuan musik tidak secara otomatis bertambah hanya dengan mendengarkan musik dalam permainan.",
        "Tidak, pemahaman tentang musik melibatkan aspek yang lebih mendalam daripada sekadar mendengarkan latar musik dalam permainan.",
        "Tidak, karena mendengarkan musik game mungkin tidak memberikan konteks atau pemahaman mendalam tentang komposisi musik yang lebih luas.",
        "Tidak, efek suara dalam permainan tidak berkontribusi pada pengetahuan musik secara signifikan.",
        "Tidak, karena efek suara dalam game lebih ditujukan untuk interaksi gameplay dan tidak selalu mengandung unsur musik yang menonjol.",
        "Benar, bisa membantu memahami bagaimana musik digunakan untuk meningkatkan pengalaman bermain game.",
        "Tidak, memahami efek suara dalam permainan tidak sama dengan memahami musik.",
        "Tidak, memahami musik dalam permainan tidak berkontribusi pada kemampuan bermain atau membuat musik.",
        "Iya, pemahaman tentang dinamika musik dalam permainan dapat bertambah.",
        "Ya, bisa memberikan wawasan tentang peran musik dalam narasi dalam permainan.",
        "Tidak, musik dalam permainan tidak biasanya digunakan untuk pendidikan musik.",
        "Tidak, efek suara dalam permainan cenderung fokus pada aspek gameplay dan tidak terlalu terkait dengan pengetahuan musik.",
        "Benar, memahami alur cerita permainan dapat membantu menginterpretasikan musiknya.",
        "Iya, pemahaman tentang peran audio dalam permainan dapat meningkatkan apresiasi musik.",
        "Tidak, mendengarkan musik dalam permainan tidak mendalami sejarah atau teori musik.",
        "Tidak, musik dalam permainan cenderung sederhana dan repetitif, sehingga tidak banyak yang dapat dipelajari darinya.",
        "Tidak, musik dalam permainan tidak selalu mengikuti prinsip-prinsip musik yang konvensional.",
        "Tidak, musik dalam permainan mobile legend biasanya dirancang untuk pengalaman bermain game, bukan untuk pendidikan musik.",
        "Benar, bisa membantu memahami penggunaan musik dalam permainan kompetitif.",
        "Dengan lagu yang itu-itu saja dan monoton menurut saya itu tidak akan menambah wawasan musik saya.",
        "Tidak, karena sering kali memotong atau mengedit musik latar belakang untuk menyesuaikan dengan aksi dalam permainan, yang bisa merusak pengalaman mendengar musik aslinya.",
        "Ya, ini dapat membantu mengenal genre musik yang digunakan dalam permainan.",
        "Tidak, musik dalam permainan tidak selalu mencerminkan keragaman musik di luar permainan.",
        "Ya, ini dapat memahami cara musik digunakan untuk menandai peristiwa dalam permainan.",
        "Tidak, pemahaman tentang permainan tidak selalu terkait dengan pemahaman musik.",
        "Tidak, mendengarkan musik dalam permainan tidak secara langsung meningkatkan pengetahuan musik.",
        "Tidak, karena menurut saya itu tidak mempengaruhi wawasan saya terhadap musik sama sekali.",
        "Iya, mendengarkan efek suara dalam permainan dapat meningkatkan pemahaman tentang sound design.",
        "Benar, memahami penggunaan musik dalam permainan bisa memberikan wawasan tentang cara menciptakan emosi melalui musik.",
        "Iya, dapat membantu memahami bagaimana musik dapat mempengaruhi suasana dalam permainan.",
        "Tidak, musik dalam game Mobile Legends lebih cenderung menjadi latar belakang untuk meningkatkan pengalaman bermain, bukan fokus utama untuk meningkatkan pengetahuan musik.",
        "Ya, ini dapat memperkaya pengetahuan tentang berbagai instrumen musik yang digunakan."
    ],
    [
        "Tidak, suara-suara karakter hero dapat terasa repetitif setelah beberapa kali bermain",
        "Iya, musik dan suara-suara dalam Mobile Legends membantu mengenali situasi dalam permainan",
        "Tidak, musik latar dan efek suara kadang-kadang terlalu keras dan mengganggu",
        "Iya, musik latar dan efek suara membantu menciptakan dunia yang konsisten dalam permainan",
        "ya, musik permainan sering mengikuti perasaan heroik yang cocok dengan tema permainan",
        "Tidak, beberapa suara efek dalam permainan mungkin tidak realistis",
        "Iya, suara-suara lingkungan dalam game menciptakan suasana yang sesuai dengan alam permainan",
        "Iya, musik dan efek suara menambah variasi dalam permainan",
        "Suara-suara karakter kadang-kadang terasa tidak relevan dengan tindakan mereka",
        "Tidak, karena veberapa efek suara mungkin terlalu mengganggu dan tidak sesuai dengan suasana permainan",
        "Beberapa efek suara dalam game terdengar datar dan kurang bervariasi",
        "Musiknya mungkin tidak selalu mencerminkan karakteristik dari peta tertentu dalam permainan",
        "Iya, efek suara yang digunakan sesuai dengan karakter-karakter hero",
        "Iya, efek suara ketika karakter menggunakan keterampilan atau kemampuan khusus sesuai dengan karakter mereka",
        "Iya, mereka berhasil menciptakan suasana misterius dalam beberapa peta permainan",
        "Beberapa efek suara dalam game tidak selalu sesuai dengan efek visual yang ada",
        "Iya, mereka berhasil menghadirkan kesan epik dalam permainan dengan musik dan suara yang sesuai",
        "Ya, musik latar dan efek suara dalam Mobile Legends seringkali cocok dengan suasana aksi dan pertempuran dalam permainan",
        "Iya, suara-suara dalam game seperti pukulan, serangan, dan keterampilan sesuai dengan tindakan dalam permainan",
        "Iya, suara-suara karakter menambah personalitas kepada masing-masing hero",
        "Iya, musiknya seringkali cocok dengan peta tertentu dalam permainan",
        "Iya, efek suara menambah kejelasan dalam situasi berisik selama pertempuran",
        "Iya, musik dan suara dalam game ini membantu menciptakan identitas unik bagi setiap karakter hero",
        "Iya, musik latar dalam game ini seringkali meningkatkan ketegangan selama pertandingan",
        "Iya, dalam situasi tertentu, musiknya bisa meresapkan rasa tegang saat pertempuran memanas",
        "Terkadang, musik latar tidak sesuai dengan cerita yang sedang berlangsung dalam permainan",
        "Iya, musik latar dalam game ini mencerminkan tema dan cerita yang ada di latar belakang permainan",
        "Tidak, musiknya terlalu repetitif di beberapa peta permainan",
        "Suara-suara dalam permainan bisa terasa terlalu keras atau kurang seimbang",
        "Suara-suara karakter hero bisa terdengar seperti loop yang berulang-ulang",
        "Iya, musik latar dan efek suara menciptakan perasaan kehadiran hero dalam permainan",
        "Iya, musiknya menyatu dengan gaya seni grafis permainan dan karakternya",
        "Iya, soundtrack game ini seringkali memberikan dorongan motivasi selama pertandingan",
        "Iya, mereka menggunakan musik untuk memicu emosi pemain selama pertandingan",
        "Iya, mereka menggunakan musik untuk mempertegas momen penting dalam permainan",
        "Iya, mereka memilih musik yang sesuai dengan genre game",
        "Musiknya mungkin terasa terlalu dramatis dalam situasi yang seharusnya tidak begitu",
        "Iya, musik permainan Mobile Legends dapat menambahkan elemen dramatis selama pertandingan",
        "Iya, musik permainan dapat beradaptasi dengan perubahan situasi dalam pertandingan",
        "Terkadang, musik latar dalam Mobile Legends terlalu monoton selama permainan",
        "Iya, musiknya mengikuti perkembangan permainan dan berubah sesuai dengan situasi",
        "Terkadang, musik latar tidak menggambarkan dengan baik suasana permainan yang sedang berlangsung",
        "Iya, soundtrack dalam permainan ini menggambarkan perbedaan antara tim",
        "Iya, efek suara menambah imersi dalam permainan, seperti suara pedang atau tembakan",
        "Tidak, musik latar tidak selalu berubah sesuai dengan situasi dalam permainan",
        "Iya, musik latar dalam game ini membantu mengidentifikasi jenis permainan yang sedang dimainkan",
        "Musiknya mungkin terasa kurang mendalam atau menarik dalam beberapa situasi",
        "Iya, musiknya dapat menunjukkan perubahan musim atau waktu dalam game",
        "Iya, permainan ini menggunakan musik untuk membimbing pemain dalam menjalani permainan",
        "Tidak semua efek suara cocok dengan karakter hero tertentu",
    ],
    [
        "Tidak, musik yang tidak memiliki dinamika atau variasi yang cukup dapat membuat pemain kehilangan minat dalam permainan",
        "Tidak, suara-suara permainan yang tidak berkualitas dapat mengganggu pendengaran dan mengganggu konsentrasi",
        "Tidak, musik latar yang tidak cocok dengan tema permainan dapat menciptakan ketidakselarasan yang mengganggu konsentrasi",
        "Iya, suara-suara permainan yang memberikan petunjuk atau informasi taktis dapat membantu pemain dalam mengambil keputusan yang tepat",
        "Iya, musik dengan melodi yang kuat dapat meningkatkan motivasi pemain dan membantu mereka fokus",
        "Tidak, musik latar yang monoton atau tidak bervariasi dapat membuat pemain kehilangan minat dalam permainan",
        "Tidak, efek suara yang berlebihan bisa membuat permainan terasa kacau dan sulit untuk fokus",
        "Tidak, musik yang terlalu mendalam atau emosional dapat mengalihkan perhatian dari permainan",
        "Iya, musik dengan dinamika yang sesuai dapat mengikuti perkembangan permainan dan membantu pemain merasa lebih terlibat",
        "Tidak, permainan yang memerlukan pendengaran teliti mungkin lebih baik dimainkan tanpa musik latar",
        "Iya, musik dengan beat yang tepat dapat membantu mempertahankan ritme permainan yang konsisten",
        "Iya, musik latar yang dipilih dengan baik dapat mengurangi gangguan eksternal yang mengganggu konsentrasi",
        "Tidak, terlalu banyak suara dalam permainan bisa mengganggu pemahaman suara-suara penting",
        "Iya, musik dengan tempo yang sesuai dapat membantu menjaga kecepatan permainan yang konsisten",
        "Iya, musik latar yang familiar dapat memberikan kenyamanan dan membuat pemain lebih fokus",
        "Tidak, musik yang tidak sesuai dengan selera pemain dapat membuat mereka kurang terlibat dalam permainan",
        "Tidak, musik latar yang terlalu keras bisa merusak pendengaran pemain dan mengganggu fokus",
        "Tidak, musik latar yang tidak sesuai dengan suasana permainan dapat menciptakan disonansi dan mengalihkan fokus",
        "Tidak, terlalu banyak efek suara dalam permainan bisa membuat permainan terasa bising dan membingungkan",
        "Iya, efek suara yang jelas dalam permainan dapat memberikan umpan balik penting yang memungkinkan pemain tetap fokus",
        "Tidak, musik dengan melodi yang tidak jelas dapat mengganggu pendengaran pemain dan mengurangi fokus",
        "Iya, musik latar yang dirancang secara dinamis dapat menyesuaikan diri dengan situasi dalam permainan dan membantu pemain tetap fokus",
        "Iya, suara-suara yang memberikan petunjuk dalam permainan dapat membantu pemain bergerak dengan tepat dan fokus pada tujuan",
        "Tidak, efek suara yang terlalu sering dan monoton bisa membuat permainan terasa membosankan dan mengurangi fokus",
        "Iya, musik yang berkorelasi dengan tema permainan dapat meningkatkan keterlibatan pemain dan fokus",
        "Iya, musik latar dengan melodi yang menenangkan dapat membantu pemain tetap tenang dalam situasi yang menegangkan",
        "Iya, musik yang dipersonalisasi dalam permainan dapat membantu pemain merasa lebih terlibat dan fokus",
        "Tidak, musik latar yang berulang-ulang dengan pola yang sederhana dapat membuat pemain bosan dan kurang fokus",
        "Iya, musik latar yang cocok dapat menciptakan atmosfer yang mendukung fokus dalam permainan",
        "Iya, musik latar yang menghadirkan suasana permainan dengan baik dapat membantu pemain merasa lebih terhubung dengan permainan",
        "Iya, suara-suara permainan yang memberikan informasi tentang situasi dapat membantu pemain membuat keputusan yang lebih baik",
        "Iya, musik latar yang menggambarkan tema permainan dengan baik dapat meningkatkan keterlibatan dan fokus",
        "Iya, musik dapat menciptakan suasana yang mendukung fokus, seperti ketika musik epik digunakan dalam momen penting dalam permainan",
        "Tidak, musik yang tidak berhubungan dengan tema permainan dapat menciptakan perasaan tidak sesuai dan mengalihkan fokus",
        "Tidak, musik latar yang terlalu keras atau berisik dapat mengganggu konsentrasi pemain",
        "Iya, musik latar yang memberikan energi positif dapat meningkatkan semangat dan fokus pemain",
        "Iya, musik latar yang lembut dan menenangkan dapat membantu meredakan stres dan meningkatkan konsentrasi",
        "Tidak, musik dengan lirik yang dominan dapat mengalihkan perhatian dari permainan",
        "Tidak, efek suara yang tidak berkualitas tinggi dalam permainan dapat mengganggu pendengaran dan konsentrasi",
        "Tidak, musik dengan tempo yang tidak sesuai dengan ritme permainan dapat mengacaukan konsentrasi pemain",
        "Iya, musik latar yang dirancang khusus untuk meningkatkan fokus pemain dapat berdampak positif",
        "Tidak, musik yang tidak sesuai dengan tema permainan dapat mengacaukan fokus",
        "Iya, efek suara yang menggambarkan situasi dengan baik dapat membantu pemain merasa lebih terlibat dalam permainan",
        "Tidak, musik yang terlalu intens atau dramatis bisa mengalihkan fokus pemain dari permainan itu sendiri",
        "Tidak, suara-suara yang terlalu intens dalam permainan dapat membuat pemain merasa stres dan kurang fokus",
        "Iya, musik latar yang memotivasi dapat membantu pemain tetap termotivasi untuk mencapai tujuan dalam permainan",
        "Tidak, musik latar yang terlalu rumit atau terlalu banyak instrumen bisa membingungkan pemain",
        "Iya, suara-suara permainan yang terkait dengan tindakan dalam permainan dapat membantu pemain tetap fokus pada tujuan mereka",
        "Tidak, efek suara yang berlebihan atau tidak realistis dalam permainan bisa mengganggu pemahaman situasi",
        "Iya, efek suara yang realistis dalam permainan dapat memperkuat keterlibatan pemain dan meningkatkan fokus",
    ]
]

positif = 44
negatif = 6

times = 50
index = 0

try:
    while times:
        time.sleep(2)
        #Hardcoded logic
        test = 0

        usia = random.randint(16,25)
        domisiliIndx = random.randint(0, len(domisili) - 1)

        if positif != 0 and negatif != 0:
            pil = random.choice([0,2])
        elif positif != 0 and negatif == 0:
            pil = 0
        elif positif == 0 and negatif != 0:
            pil = 2

        time.sleep(3)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        textboxes[0].send_keys(email[index])
        textboxes[1].send_keys(nama[index])
        textboxes[2].send_keys(usia)
        textboxes[3].send_keys(domisili[domisiliIndx])

        time.sleep(2)
        if pil == 0:
            positif -= 1
        else:
            negatif -= 1

        p = pil
        for i in range(18) :
            s1 = random.choice([p,p+1])
            checkboxes[s1].click()
            p += 4
        
        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea

        for j in range(len(essai)) :
            textarea[j].send_keys(essai[j][index])

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfzgQoO9VEH4x8TD29dAiy-rejg6NqV9ydL0VioFuEn0HTWXw/viewform")

        index+=1
        print("==================")
        print("positif = " + str(positif))
        print("negatif = " + str(negatif))
        print("")
        
        times-=1
        print("index  = " + str(index))
        print("times  = " + str(times))
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
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        # )

        # submit_button.click()