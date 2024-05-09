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

chrome_options = Options()
profil = "Profile 11"

chrome_options.add_argument("user-data-dir=C:\\Users\\ACER\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("profile-directory="+profil)

driver = webdriver.Chrome(executable_path=r'C:\\1.KERJOAN\\bot\\chromedriver\\chromedriver.exe', options=chrome_options)
driver.get("https://forms.gle/D2tRgWhzwkizJduMA")


email = [
    "ekawahy0099@gmail.com",
"yulisetiawan746@gmail.com",
"ekow05047@gmail.com",
"yuninafisah9@gmail.com",
"agustinaprita304@gmail.com",
"naufalardiansyah651@gmail.com",
"bagusrahmad262@gmail.com",
"hanaanissa33@gmail.com",
"heraldygunawan@gmail.com",
"budisantos0@gmail.com",

"bagushari931@gmail.com",
"dwipancaa65@gmail.com",
"oktonadevi@gmail.com",
"ooliviya96@gmail.com",
"yahhszid@gmail.com",
"f.ninadilaa@gmail.com",
"shabirmaulana23@gmail.com",
"srhhusaini@gmail.com",
"jose.anindya@gmail.com",
"erfinpp34@gmail.com",

"argopraz@gmail.com",
"azizahsalma237@gmail.com",
"faradillaaulia62@gmail.com",
"dimaswahyu4769@gmail.com",
"aprilregina663@gmail.com",
"agisprasetya171@gmail.com",
"arddyriski@gmail.com",
"fadlaanm24@gmail.com",
"kurniaseptinia@gmail.com",
"damarek099@gmail.com",

"freddinan35@gmail.com",
"manndabeel99@gmail.com",
"bambang.suhatmoyo@gmail.com",
"aliesakairaini@gmail.com",
"lika.arletta@gmail.com",
"arjuna.gh9@gmail.com",
"dhafidzuann@gmail.com",
"listakamila299@gmail.com",
"sadivapratiwi0@gmail.com",
"hermantocaisar@gmail.com",

"windycantika13@gmail.com",
"stephaniamanda67@gmail.com",
"ardyantoputra43@gmail.com",
"carolineerindra@gmail.com",
"saputranabil157@gmail.com",
"azzahrakhansa006@gmail.com",
"naufalazwin85@gmail.com",
"riskarahmawati400@gmail.com",
"rohmatubaidillah3@gmail.com",
"setiawannugraha372@gmail.com",
# 50 (bawah e  ini 51-60)
"lesmanadewa831@gmail.com",
"muhammadwawan727@gmail.com",
"putri.bella.14.06.06@gmail.com",
"meydianamargaretha@gmail.com",
"bellindainggridina@gmail.com",
"raishaanastasya003@gmail.com",
"bumirakha35@gmail.com",
"ilyasafadil23@gmail.com",
"fikkydevano119@gmail.com",
"budimanyahya71@gmail.com",

"siscapratiwii62@gmail.com",
"fiorenahmad4@gmail.com",
"farhannurrahman92@gmail.com",
"yahyabudiman72@gmail.com",
"putrisasya55@gmail.com",
"anggadewangga089@gmail.com",
"divanipermatasari@gmail.com",
"aliframadhan5098@gmail.com",
"selmanabila30@gmail.com",
"iwansetyawann4@gmail.com",
]

# laki 0 perempuan 1
kelamin = [1,1,0,1,1,0,0,1,0,0,
            0,0,0,1,0,1,0,1,1,1,
            0,1,1,0,1,0,0,0,1,0,
            0,1,0,1,1,0,0,1,1,0,
            1,1,0,1,0,1,0,1,0,0,
            
            0,0,1,1,1,1,0,0,0,0,
            1,0,0,0,1,0,1,0,1,0, 
]
# tasik 8
# cirebon 9
domisili = [
4,5,6,7,8,9,5,4,7,6,5,4,4,5,6,7,7,4,5,7,8,9,9,5,7,4,5,5,5,7,7,6,5,7,5,5,7,5,4,7,6,8,9,4,5,5,5,5,4,5,7,6,5,5,5,7,6,6,6,7,4,5,5,7,5,7,5,7,5,6,8,5,7,4,4,5,5,7,6,5,4,5,7,5,5,5,5,4,6,7,7,7,5,5,7,5,7,6,5,5,5,4,7,9,9,6,7,5,5,7,6,7,7,5,5,5,5,7,5,6,6,7,5,5,4,7,5,7,5,5,7,9,4,5,5,7,5,7,5,6,7,5,5,5,5,7,7,5,7
]

kategori = [
9,10,11,9,11,10,10,9,11,11,10,9,9,10,11,11,10,10,10,9,9,9,11,11,9,11,10,11,9,9,10,9,10,11,10,9,11,11,10,9,10,9,11,
11,10,9,10,9,9,9,10,9,10,9,10,9,10,9,10,10,10,9,11,9,9,10,9,10,11,10,9,10,9,9,9,10,9,10,9,9,10,11,10,9,11,9,9,10,
10,10,9,10,9,10,9,9,10,9,10,9,9,9,9,10,11,10,9,11,10,9,10,11,10,9,10,9,9,9,9,10,9,10,9,10,9,11,9,10,9,10,9,10,9,9,
9,10,9,10,11,9,10,10,9,9,10,9,11,9,9
]

s1n1 = [
5,5,5,4,4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5,4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5,4,5,4,4,4,5,4,3,5,5,5,4,4,5,4,4,3,5,4,5,5,5,4,2,5,5,5,5,4,5,4,4,4,5,4,3,5,5,4,4,5,4,4,3,4,4,2,5,5,5,4,5,4,3,2,1,2,2,3,4,3,2,4,3,4,2,3,4,5,3,4,5,1,1,2,2,3,2,1,2,3,4,5,2,2
]

s1n2 = [
4,5,5,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,5,5,5,3,4,4,4,4,4,5,4,3,2,3,4,3,5,5,4,4,4,5,5,4,3,4,5,3,4,5,2,2,1,1,1,2,2,3,2,4,5,5,4,3,4,5,3,4,5,4,3,2,3,3
]

s1n3 = [
4,5,5,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,4,3,5,5,4,4,4,5,4,3,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,3,4,5,4,3,5,4,4,4,5,4,3,3,4,5,2,5,5,5,4,5,4,5,4,5,3,4,5,5,4,3,2,1,2,3,4,5,2,3,4,5,3,3,2,4,5,4,5,4,5,3,4,5,3
]

s1n4 = [
4,5,5,5,4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4,4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4,4,4,4,5,4,4,4,4,4,5,3,4,4,5,4,4,2,4,3,4,4,4,5,3,4,5,3,5,4,4,4,4,5,4,4,4,5,4,4,4,5,4,4,2,3,5,3,4,4,5,4,2,2,3,4,5,4,3,4,5,2,2,1,1,4,5,5,4,3,2,3,4,5,3,4,3,4,3,4,4,5,3,4,5,3
]

s2n1 = [
4,5,5,5,4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,4,4,3,5,3,4,4,3,4,4,5,4,4,2,4,4,3,5,4,4,3,4,5,4,5,4,5,4,3,2,1,2,3,4,5,5,4,3,4,4,5,3,4,5,3,4,5,3,4,5,4,3,2,3,3 
]

s2n2 = [
4,5,5,5,4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,4,5,4,3,5,5,3,4,5,4,3,4,4,5,4,4,2,5,4,4,4,4,4,3,5,5,4,4,3,4,4,4,3,5,3,4,4,3,4,4,5,4,4,2,4,4,3,5,4,4,3,4,5,4,5,4,5,4,3,2,1,2,3,4,5,5,4,3,4,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,5
]

s2n3 = [
3,5,4,3,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,2,3,4,5,5,5,4,3,4,3,4,2,1,1,2,3,4,3,4,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,5
]

s2n4 = [
3,5,4,4,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,4,3,2,3,4,5,4,3,2,1,2,2,2,3,3,4,5,5,4,3,4,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5
]

s3n1 = [
3,5,4,5,4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5,4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5,4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,4,4,4,5,5,4,4,4,5,4,4,5,4,5,5,4,4,4,4,4,4,4,5,4,3,2,5,4,4,4,1,2,2,1,2,1,2,1,2,1,2,1,2,3,3,3,3,4,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4
]

s3n2 = [
4,5,4,4,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,4,5,4,5,2,5,5,5,5,4,5,5,5,3,4,5,5,3,3,5,5,4,4,4,5,4,4,3,5,4,5,2,3,4,5,2,4,3,4,3,5,3,2,1,1,1,2,3,2,4,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,5
]

s3n3 = [
4,5,4,5,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,4,4,4,5,3,5,5,4,4,4,4,5,4,4,5,4,4,4,4,5,5,3,4,4,5,4,4,2,4,4,5,3,2,3,4,5,3,5,2,1,2,4,3,2,1,1,1,1,2,3,2,4,4,5,4,4,4,3,5,5,5,5,4,5,4,5
]

s4n1 = [
4,5,5,5,4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5,4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5,4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,4,4,3,2,5,5,5,5,5,5,4,5,4,4,4,5,3,5,5,5,4,4,3,5,4,4,2,5,3,3,2,4,5,4,5,4,5,3,4,5,5,4,3,3,4,5,5,4,3,4,5,3,4,5,4,5,4,5,5,5,5,4,5,4,5
]

s4n2 = [
4,5,4,5,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,5,4,5,3,5,5,5,4,3,4,5,5,4,5,5,5,4,4,5,5,4,4,4,5,4,4,3,5,4,5,3,4,3,5,4,3,5,4,3,2,2,2,3,4,4,4,5,5,3,4,5,5,4,5,4,5,5,5,5,4,5,4,5,3,2
]

s4n3 = [
3,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,3,5,5,4,2,5,5,4,5,4,4,5,5,5,4,4,4,3,3,5,4,5,4,4,5,4,3,2,5,3,4,2,4,5,4,5,4,5,3,2,3,4,5,4,5,4,5,4,5,3,4,5,5,4,5,4,5,5,5,5,4,5,4,5,3,2
]

s4n4 = [
3,5,5,4,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,2,2,1,1,2,3,3,2,2,3,4,2,3,2,1,3,4,5,3,4,5,5,4,5,4,5,5,5,5,4,5,4,5,3,2
]

s5n1 = [
3,5,4,3,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,4,4,4,2,5,5,5,5,4,5,5,5,5,4,5,5,4,4,5,4,3,4,4,5,4,3,2,4,4,4,2,4,5,4,5,4,5,4,5,4,5,3,3,3,3,3,4,5,3,4,5,5,4,5,4,5,5,5,5,4,5,4,5,3,2
]

s5n2 = [
3,5,3,5,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,4,4,4,3,5,5,5,4,4,4,5,4,5,5,5,5,3,4,5,4,4,4,4,5,4,3,2,5,3,4,3,3,4,5,5,4,3,2,3,4,5,4,3,5,5,4,3,4,5,5,4,4,4,3,5,4,5,4,3,4,5,5,4,4,3
]

s5n3 = [
3,5,4,4,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,5,4,4,4,3,5,5,5,5,4,5,4,4,5,4,4,5,4,4,5,5,4,4,4,5,4,4,2,5,4,4,3,4,5,4,5,4,5,4,5,4,5,3,4,5,4,3,4,5,4,3,4,5,4,3,2,3,4,5,5,5,4,5,4,4,5
]




times = 10
index = 70
idx = 1
idxx = 1
genz = 40
geny = 20
genx = 20
        


try:
    while times:
        time.sleep(2)
        if idx == 10:
            idx = 0

        option = driver.find_elements("css selector", ".jZZ5Nd")#ganti akun

        option[0].click()

        time.sleep(20)
        driver.switch_to.window(driver.window_handles[idxx])
        time.sleep(2)

        radiobuttons = driver.find_elements("css selector", ".JDAKTe")#pilih akun google
        radiobuttons[idx].click()

        time.sleep(20)
        #Hardcoded logic
        test = 0
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
        pilihan = driver.find_elements("css selector", ".Hvn9fb")#pilihan

        checkboxes[0].click()
        
        if genz != 0 and geny != 0 and genx != 0:
            generasi = random.choice([0,1,2])
            if generasi == 0:
                genz -= 1
            elif generasi == 1:
                geny -= 1
            elif generasi == 2:
                genx -= 1
        elif genz == 0 and geny != 0 and genx != 0:
            generasi = random.choice([1,2])
            if generasi == 1:
                geny -= 1
            elif generasi == 2:
                genx -= 1
        elif genz != 0 and geny == 0 and genx != 0:
            generasi = random.choice([0,2])
            if generasi == 0:
                genz -= 1
            elif generasi == 2:
                genx -= 1
        elif genz != 0 and geny != 0 and genx == 0:
            generasi = random.choice([0,1])
            if generasi == 0:
                genz -= 1
            elif generasi == 1:
                geny -= 1
        elif genz == 0 and geny == 0 and genx != 0:
            generasi = 2
            genx -= 1
        elif genz != 0 and geny == 0 and genx == 0:
            generasi = 0
            genz -= 1
        elif genz == 0 and geny != 0 and genx == 0:
            generasi = 1
            geny -= 1

        radiobuttons[generasi].click()
        
        
        if domisili[index] == 8:
            pilihan[1].send_keys("Tasikmalaya")
        elif domisili[index] == 9:
            pilihan[1].send_keys("Cirebon")
        else:
            radiobuttons[domisili[index]].click()


        radiobuttons[kategori[index]].click()

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

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        textboxes[0].send_keys(email[index])
        radiobuttons[kelamin[index]].click()
        time.sleep(2)
        pendidikan = random.choice([2,3,3,4,4,4,5])
        radiobuttons[pendidikan].click()
        income = random.choice([7,8,9,10])
        radiobuttons[income].click()
        time.sleep(2)
        radiobuttons[11].click()






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

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        testcheck[s1n1[index]-1].click()
        testcheck[s1n2[index]+4].click()
        testcheck[s1n3[index]+9].click()
        testcheck[s1n4[index]+14].click()

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

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        testcheck[s2n1[index]-1].click()
        testcheck[s2n2[index]+4].click()
        testcheck[s2n3[index]+9].click()
        testcheck[s2n4[index]+14].click()

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

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        testcheck[s3n1[index]-1].click()
        testcheck[s3n2[index]+4].click()
        testcheck[s3n3[index]+9].click()

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

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        testcheck[s4n1[index]-1].click()
        testcheck[s4n2[index]+4].click()
        testcheck[s4n3[index]+9].click()
        testcheck[s4n4[index]+14].click()

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

        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
        textarea = driver.find_elements("css selector", ".KHxj8b")#texarea
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian
        
        testcheck[s5n1[index]-1].click()
        testcheck[s5n2[index]+4].click()
        testcheck[s5n3[index]+9].click()

        time.sleep(3)
        kirims1 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")
        kirims2 = driver.find_elements(By.XPATH, "//span[contains(text(), 'Submit')]")

        if len(kirims1) != 0 :
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
            )
        else:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]"))
            )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/D2tRgWhzwkizJduMA")

        index+=1
        idx += 1
        idxx += 1
        print("==================")
        print("index : " + str(index))
        print("idx   : " + str(idx))
        print("idxx  : " + str(idxx))

        times-=1
        print("times : " + str(times))
        print("genz : " + str(genz))
        print("geny : " + str(geny))
        print("genx : " + str(genx))
        
finally:
	# driver.quit()
    print("berhasil")

    # radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
    # textboxes = driver.find_elements("css selector", ".whsOnd")#isian
    # testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
    # checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox