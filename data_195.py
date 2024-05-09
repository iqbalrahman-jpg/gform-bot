import random
import time
import data

# ===================================================================================================

index = 17
times = 3

kategori = [
    [
        0,0,3
    ],
    [
        4,0,13
    ],
]

jawabIsian = [
    [
        [
            # negatif
            "Konten yang diberikan oleh akun Instagram Kokufootwear terasa monoton dan kurang inovatif, tidak memberikan variasi atau kejutan yang memikat pengikutnya",
            "Saya merasa kecewa dengan kualitas visual dari konten Kokufootwear, terlihat kurang profesional dan kurang menarik perhatian",
            "Isi dari postingan Kokufootwear cenderung klise dan tidak memberikan nilai tambah, membuat saya kehilangan minat untuk terus mengikuti akun tersebut",
            "Penggunaan caption dan deskripsi pada setiap postingan Kokufootwear terasa dangkal dan tidak informatif, tidak memberikan wawasan atau cerita menarik di balik produk mere",
        ],
        [

        ],
        [
            # positif
            "Menurut saya, konten yang disajikan oleh akun Instagram Kokufootwear sangat inspiratif",
            "Saya sangat menghargai variasi produk sepatu yang ditampilkan dalam konten Kokufootwear",
            "Konten Kokufootwear selalu menampilkan gaya yang trendi dan sesuai dengan perkembangan mode",
            "Saya merasa terhubung dengan merek ini karena kontennya mencerminkan nilai-nilai positif",
            "Kokufootwear berhasil menampilkan keunikan dan keberagaman dalam setiap postingan mereka",
            "Konten yang kreatif dan inovatif dari Kokufootwear selalu membuat saya tertarik",
            "Akun ini memberikan inspirasi fashion yang dapat diaplikasikan dalam gaya sehari-hari",
            "Saya menyukai bagaimana Kokufootwear mempromosikan keberlanjutan dan etika dalam industri fashion",
            "Konten mereka memberikan pandangan menyeluruh tentang produk, termasuk kualitas dan desainnya",
            "Kokufootwear secara konsisten memberikan tips gaya dan ide kombinasi yang sangat membantu",
            "Saya merasa senang karena Kokufootwear turut serta dalam kampanye positif dan mendukung masyarakat",
            "Konten yang dipublikasikan selalu memberikan energi positif dan semangat untuk menciptakan gaya unik",
            "Saya menyukai cara Kokufootwear berinteraksi dengan pengikutnya, menciptakan atmosfer ramah dan inklusif",
            "Konten Kokufootwear memberikan gambaran yang jelas tentang kenyamanan sepatu mereka",
            "Saya merasa bahwa akun ini tidak hanya tentang produk, tetapi juga tentang gaya hidup dan ekspresi diri",
            "Kokufootwear berhasil membangun komunitas online yang positif dan bersemangat",
        ],
    ],
    [
        [
            # negatif
            "Saya tertarik dengan konten yang memberikan informasi baru dan bermanfaat, sehingga saya dapat terus mengembangkan pengetahuan saya",
            "Konten yang menginspirasi dan memotivasi saya untuk mencapai tujuan hidup menjadi daya tarik utama, membuat saya ingin terus memerhatikannya",
            "Kreativitas dan inovasi dalam penyampaian konten juga membuat saya terpikat, karena hal ini memberikan pengalaman yang segar dan menarik",
            "Saya cenderung tertarik pada konten yang menghibur dan memberikan keceriaan, sehingga dapat menjadi pelarian yang menyenangkan dari rutinitas sehari-hari",
        ],
        [

        ],
        [
            # positif
            "Saya sangat tertarik dengan konten yang memberikan wawasan mendalam tentang topik yang saya gemari",
            "Konten yang menginspirasi dan memotivasi selalu membuat saya ingin terus menonton",
            "Saya suka konten yang mengajarkan hal-hal baru dan memberikan pengetahuan tambahan",
            "Keseruan dan kreativitas dalam suatu konten selalu berhasil menarik perhatian saya",
            "Konten yang memberikan hiburan positif dan membuat saya tertawa selalu saya cari",
            "Saya senang dengan konten yang membahas tren terkini dan berita positif",
            "Kualitas produksi yang baik dan tata visual yang menarik membuat saya betah menonton lebih lama",
            "Saya tertarik dengan konten yang mendukung nilai-nilai positif dan semangat optimisme",
            "Konten yang membangun komunitas dan interaksi positif antara penonton selalu menarik perhatian saya",
            "Saya suka konten yang memberikan solusi praktis untuk masalah sehari-hari",
            "Keberagaman dalam konten, baik dari segi topik maupun narasumber, selalu membuat saya penasaran",
            "Saya tertarik dengan konten yang menggabungkan pendekatan edukatif dengan hiburan",
            "Kualitas narasi yang baik dan kemampuan narator untuk menjaga ketertarikan saya sangat penting",
            "Konten yang menyajikan cerita inspiratif dan pengalaman positif selalu membuat saya ingin tahu lebih banyak",
            "Saya suka konten yang memberikan tips praktis untuk meningkatkan kualitas hidup",
            "Keaslian dan kejujuran dalam penyampaian konten membuat saya merasa terhubung dan ingin terus mengikuti perkembangannya",
        ],
    ]
]

soal = [18,4]