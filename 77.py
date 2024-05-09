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
driver.get("https://forms.gle/ewmgWRyVrNzot6aW8")

s1 = [
    [2,3,4],
    [3,4],
    [1,2],
    [2,3,4,5],
    [1,3,4],
    [2,3,5],
    [1,2,3,4],
    [3,5],
    [1,2,3,5],
    [1,3,5],
    [1,2,3,5],
    [2,3,4,5],
    [2,3],
    [1,2,3,4],
    [1,2,4,5],
    [1],
    [2,3,5],
    [1,2,3,5],
    [4],
    [1,2,3,4,5],
    [2,4],
    [1,2,3,4],
    [1,4],
    [2,3],
    [1,2,3,5],
    [2,3,5],
    [1,2,3,4,5],
    [1,2,3],
    [1,2,5],
    [1,2,3],
    [2,4],
    [1,3],
    [1,2,4,5],
    [1,2,3,4,5],
    [1,2,3,5],
    [2],
    [2,4],
    [2,3,4],
    [3,5],
    [3],
]

s2 = [
    [3,4,5,7],
    [5,6,7,8],
    [3,7,8],
    [3,6,7,9],
    [1,2,3,4,5,8],
    [2,3,4,5,6,7],
    [2,3,4,6],
    [3,4,5,7,9],
    [1,4,5,6,7],
    [2,3,4,6,7,8],
    [3,4,5,6,8],
    [2,3,4,5,6],
    [3,8,9],
    [2,3,5,7,8],
    [1,2,3,5,7,8,9],
    [2,4,6,7],
    [2,3,8],
    [1,2,3,4,6,7],
    [3,5,6,7],
    [1,4,7,8],
    [2,3,4,6,7],
    [3,4,6],
    [3,7,8],
    [3,7,8],
    [2,3,4,5,7],
    [1,3,4,6,7],
    [1,2,3,4,6],
    [3,4,5,6,8],
    [5,8],
    [4,8],
    [1,3,6,8],
    [4,5,8],
    [1,2,4,5,7,8],
    [2,4,6,7],
    [4,5,8],
    [1,2,4,5,7,8,9],
    [2,4,6],
    [2,4,5],
    [2,5,6,7,9],
    [4,5,6,7],
]

s3 = [
    [1,3,7,8,9,11],
    [1,3,4,5,7,8,11],
    [1,8,9,11,13],
    [4,5,8,9],
    [1,2,3,6,9,11],
    [2,3,4,11],
    [1,4,5,8,9,12],
    [2,3,4,7,8],
    [3,5,8,12],
    [2,4,7,11],
    [2,3,4,6,7,11],
    [2,3,5,7,8,9,11],
    [2,3,7,8],
    [1,3,4,5,6,7,8,10,11],
    [1,2,3,4,7,8,10],
    [1,3,4,6,7,11],
    [7,9],
    [2,3,7],
    [2,3,4,6,7,8,11],
    [11,13],
    [3,4,5,8],
    [1,4,5,8,9],
    [2,8,9],
    [2,3,4,8,11],
    [4,7,11,12],
    [3,4,5,7,8,10],
    [1,2,3,4,8,9],
    [2,3,4,7,8],
    [2,3,4,8,11],
    [3,4,5,6,7,8],
    [2,3,5,7,11],
    [2,3,7,8],
    [1,3,4,7,9,13],
    [2,3,7,9,11],
    [3,4],
    [1,2,4,5,7,8],
    [1,2,4,6,8,9],
    [1,2,4,5,7,8],
    [1,2,3,7,8,11,12],
    [2,3,5,7],
]

p1 = [
    [3,4,4,4,4,4,4,4,3,4,4,3,3,4,3,4,4,3,4,4,4,4,4,4,2,3,4,4,4,3,4,2,3,4,4,4,3,4,2,3],
    [3,3,3,4,2,4,4,4,2,3,3,3,3,4,3,4,2,3,3,4,2,4,4,4,2,3,4,4,2,2,3,2,3,4,4,4,2,4,2,3],
    [1,2,2,2,2,3,3,4,0,2,1,3,3,3,2,1,2,3,2,4,2,2,2,1,1,1,4,1,2,1,3,2,2,4,4,2,1,2,2,3],
    [3,2,0,0,3,3,4,1,0,1,1,1,1,1,2,0,2,1,2,1,2,1,0,0,0,3,4,1,2,2,0,1,2,4,4,0,1,0,1,1],
    [3,2,0,2,3,3,3,1,2,4,0,2,2,1,2,0,2,1,4,1,2,1,2,0,1,3,4,1,2,2,3,1,1,4,4,2,2,2,1,1],
    [1,2,0,0,3,3,2,1,0,1,0,1,1,1,2,0,2,1,4,1,2,1,0,0,0,0,2,1,2,1,0,1,2,2,0,0,1,0,1,1],
    [1,3,1,0,3,3,2,4,0,3,2,1,1,3,3,1,2,3,2,4,2,4,0,1,0,2,2,1,2,1,2,1,2,2,0,4,1,0,1,3],
]

p2 = [
    [3,2,2,3,3,4,3,1,2,3,2,2,2,3,3,2,2,1,3,3,2,3,2,4,2,3,2,3,3,3,3,1,2,3,3,2,4,2,3,3],
    [3,2,2,3,2,2,3,1,2,3,3,2,2,2,2,2,3,1,3,2,3,3,3,2,3,3,3,3,2,3,3,3,1,2,2,2,2,3,3,3],
    [3,2,2,3,2,3,2,1,2,3,2,2,2,2,2,2,3,1,2,2,3,3,3,3,3,3,3,3,2,3,3,3,1,2,2,2,3,2,3,2],
]

p3 = [
    [4,2,3,3,2,1,3,3,3,2,2,4,1,2,4,1,3,4,3,4,3,3,3,3,4,3,4,3,3,4,2,2,2,3,4,2,2,4,3,2],
    [4,2,3,2,1,2,3,2,3,2,1,4,2,1,4,1,2,4,3,4,3,3,3,3,4,3,4,3,3,4,2,2,1,3,4,2,4,4,3,2],
    [4,4,3,3,3,2,4,3,3,2,3,4,2,2,4,1,4,4,3,4,3,4,3,2,4,4,4,2,4,4,2,2,3,4,4,2,3,4,3,2],
    [4,3,3,2,2,2,4,4,3,2,2,3,2,2,4,1,4,4,4,4,3,4,3,3,4,4,4,3,4,3,2,2,2,3,4,2,4,4,3,2],
]

p4 = [   
    [4,4,3,4,3,0,3,3,3,2,3,4,0,2,4,1,4,4,3,4,3,2,3,1,4,2,4,2,2,4,2,3,3,2,4,1,4,4,3,2],
    [4,4,3,4,3,0,3,3,3,2,3,4,0,2,4,1,3,4,4,4,3,2,3,2,4,2,4,2,2,4,2,3,3,3,4,1,3,4,3,2],
    [4,3,3,4,3,0,3,4,3,2,3,4,0,1,4,1,3,4,2,4,3,3,3,2,4,3,4,2,3,4,2,3,3,3,4,1,4,4,3,2],
    [4,3,4,4,3,0,4,2,3,2,3,3,0,2,4,1,1,4,2,4,4,3,3,2,4,3,4,1,3,3,2,3,3,2,4,1,4,4,3,2],
]

s4 = [
    [2,3,4],
    [2,3,4],
    [1,2,3,4],
    [1,3,4],
    [2,3,4],
    [1,2,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,3,4],
    [1,3],
    [1,2,4],
    [1,3],
    [1,2,4],
    [1,4],
    [1,4],
    [1,2,3],
    [1,2,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,3,4],
    [1,3,4],
    [1,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,4],
    [2,3],
    [1,3,4],
    [1,2,3,4],
    [2,3],
    [1,2,3,4],
    [1,2,3,4],
    [2,4],
    [1,2,3,4],
    [3,4],
    [2,4],
    [1,2,4],
    [1,2,3,4],
    [1,3,4],
    [3,4],
    [2,3,4],
]

civil = 30
tcivil = 10

years5 = 34
years1 = 6

position = 35
tposition = 5

level1 = 12
level2 = 12
level3 = 13
level4 = 3

replace1 = 9
replace2 = 13
replace3 = 10
replace4 = 8

impact1 = 8
impact2 = 7
impact3 = 14
impact4 = 11

times = 40
index = 0

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        if civil != 0 and tcivil != 0 :
            pil = random.choice([0,1])
            if pil == 0:
                civil -= 1 
            else:
                tcivil -= 1
        elif civil != 0 and tcivil == 0 :
            pil = 0
            civil -= 1
        elif civil == 0 and tcivil != 0 :
            pil = 1 
            tcivil -= 1

        time.sleep(2)
        if years5 != 0 and years1 != 0 :
            pil1 = random.choice([0,1])
            if pil1 == 0:
                years5 -= 1
            else:
                years1 -= 1
        elif years5 != 0 and years1 == 0 :
            pil1 = 0
            years5 -= 1
        elif years5 == 0 and years1 != 0 :
            pil1 = 1 
            years1 -= 1

        time.sleep(2)
        if position != 0 and tposition != 0 :
            pil2 = random.choice([0,1])
            if pil2 == 0:
                position -= 1
            else:
                tposition -= 1
        elif position != 0 and tposition == 0 :
            pil2 = 0 
            position -= 1
        elif position == 0 and tposition != 0 :
            pil2 = 1 
            tposition -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        time.sleep(2)
        if pil == 0 :
            radiobuttons[1].click()
        else:
            radiobuttons[random.choice([0,2,3,4])].click()

        time.sleep(2)
        if pil1 == 0:
            radiobuttons[random.choice([8,9])].click()
        else:
            radiobuttons[7].click()

        time.sleep(2)
        if pil2 == 0:
            radiobuttons[10].click()
        else:
            radiobuttons[random.choice([11,12])].click()

        radiobuttons[14].click()
        driver.implicitly_wait(4)

        textboxes[2].send_keys("IQSI")

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        if level1 != 0 and level2 != 0 and level3 != 0 and level4 != 0:
            level = random.choice([1,2,3,4])
            if level == 1:
                level1 -= 1
            elif level == 2:
                level2 -= 1
            elif level == 3:
                level3 -= 1
            else:
                level4 -= 1
        elif level1 != 0 and level2 != 0 and level3 != 0 and level4 == 0:
            level = random.choice([1,2,3])
            if level == 1:
                level1 -= 1
            elif level == 2:
                level2 -= 1
            else:
                level3 -= 1
        elif level1 != 0 and level2 != 0 and level3 == 0 and level4 != 0:
            level = random.choice([1,2,4])
            if level == 1:
                level1 -= 1
            elif level == 2:
                level2 -= 1
            else:
                level4 -= 1
        elif level1 != 0 and level2 == 0 and level3 != 0 and level4 != 0:
            level = random.choice([1,3,4])
            if level == 1:
                level1 -= 1
            elif level == 3:
                level3 -= 1
            else:
                level4 -= 1
        elif level1 == 0 and level2 != 0 and level3 != 0 and level4 != 0:
            level = random.choice([2,3,4])
            if level == 2:
                level2 -= 1
            elif level == 3:
                level3 -= 1
            else:
                level4 -= 1
        elif level1 != 0 and level2 != 0 and level3 == 0 and level4 == 0:
            level = random.choice([1,2])
            if level == 1:
                level1 -= 1
            else:
                level2 -= 1
        elif level1 != 0 and level2 == 0 and level3 != 0 and level4 == 0:
            level = random.choice([1,3])
            if level == 1:
                level1 -= 1
            else:
                level3 -= 1
        elif level1 == 0 and level2 != 0 and level3 != 0 and level4 == 0:
            level = random.choice([2,3])
            if level == 2:
                level2 -= 1
            else:
                level3 -= 1
        elif level1 != 0 and level2 == 0 and level3 == 0 and level4 != 0:
            level = random.choice([1,4])
            if level == 1:
                level1 -= 1
            else:
                level4 -= 1
        elif level1 == 0 and level2 != 0 and level3 == 0 and level4 != 0:
            level = random.choice([1,2,3,4])
            if level == 1:
                level1 -= 1
            elif level == 2:
                level2 -= 1
            elif level == 3:
                level3 -= 1
            else:
                level4 -= 1
        elif level1 == 0 and level2 == 0 and level3 != 0 and level4 != 0:
            level = random.choice([3,4])
            if level == 3:
                level3 -= 1
            else:
                level4 -= 1
        elif level1 != 0 and level2 == 0 and level3 == 0 and level4 == 0:
            level = 1
            level1 -= 1 
        elif level1 == 0 and level2 != 0 and level3 == 0 and level4 == 0:
            level = 2
            level2 -= 1 
        elif level1 == 0 and level2 == 0 and level3 != 0 and level4 == 0:
            level = 3
            level3 -= 1 
        elif level1 == 0 and level2 == 0 and level3 == 0 and level4 != 0:
            level = 4
            level4 -= 1

        time.sleep(2)
        if replace1 != 0 and replace2 != 0 and replace3 != 0 and replace4 != 0:
            replace = random.choice([1,2,3,4])
            if replace == 1:
                replace1 -= 1
            elif replace == 2:
                replace2 -= 1
            elif replace == 3:
                replace3 -= 1
            else:
                replace4 -= 1
        elif replace1 != 0 and replace2 != 0 and replace3 != 0 and replace4 == 0:
            replace = random.choice([1,2,3])
            if replace == 1:
                replace1 -= 1
            elif replace == 2:
                replace2 -= 1
            else:
                replace3 -= 1
        elif replace1 != 0 and replace2 != 0 and replace3 == 0 and replace4 != 0:
            replace = random.choice([1,2,4])
            if replace == 1:
                replace1 -= 1
            elif replace == 2:
                replace2 -= 1
            else:
                replace4 -= 1
        elif replace1 != 0 and replace2 == 0 and replace3 != 0 and replace4 != 0:
            replace = random.choice([1,3,4])
            if replace == 1:
                replace1 -= 1
            elif replace == 3:
                replace3 -= 1
            else:
                replace4 -= 1
        elif replace1 == 0 and replace2 != 0 and replace3 != 0 and replace4 != 0:
            replace = random.choice([2,3,4])
            if replace == 2:
                replace2 -= 1
            elif replace == 3:
                replace3 -= 1
            else:
                replace4 -= 1
        elif replace1 != 0 and replace2 != 0 and replace3 == 0 and replace4 == 0:
            replace = random.choice([1,2])
            if replace == 1:
                replace1 -= 1
            else:
                replace2 -= 1
        elif replace1 != 0 and replace2 == 0 and replace3 != 0 and replace4 == 0:
            replace = random.choice([1,3])
            if replace == 1:
                replace1 -= 1
            else:
                replace3 -= 1
        elif replace1 == 0 and replace2 != 0 and replace3 != 0 and replace4 == 0:
            replace = random.choice([2,3])
            if replace == 2:
                replace2 -= 1
            else:
                replace3 -= 1
        elif replace1 != 0 and replace2 == 0 and replace3 == 0 and replace4 != 0:
            replace = random.choice([1,4])
            if replace == 1:
                replace1 -= 1
            else:
                replace4 -= 1
        elif replace1 == 0 and replace2 != 0 and replace3 == 0 and replace4 != 0:
            replace = random.choice([1,2,3,4])
            if replace == 1:
                replace1 -= 1
            elif replace == 2:
                replace2 -= 1
            elif replace == 3:
                replace3 -= 1
            else:
                replace4 -= 1
        elif replace1 == 0 and replace2 == 0 and replace3 != 0 and replace4 != 0:
            replace = random.choice([3,4])
            if replace == 3:
                replace3 -= 1
            else:
                replace4 -= 1
        elif replace1 != 0 and replace2 == 0 and replace3 == 0 and replace4 == 0:
            replace = 1
            replace1 -= 1 
        elif replace1 == 0 and replace2 != 0 and replace3 == 0 and replace4 == 0:
            replace = 2
            replace2 -= 1 
        elif replace1 == 0 and replace2 == 0 and replace3 != 0 and replace4 == 0:
            replace = 3
            replace3 -= 1 
        elif replace1 == 0 and replace2 == 0 and replace3 == 0 and replace4 != 0:
            replace = 4
            replace4 -= 1

        time.sleep(2)
        if impact1 != 0 and impact2 != 0 and impact3 != 0 and impact4 != 0:
            impact = random.choice([1,2,3,4])
            if impact == 1:
                impact1 -= 1
            elif impact == 2:
                impact2 -= 1
            elif impact == 3:
                impact3 -= 1
            else:
                impact4 -= 1
        elif impact1 != 0 and impact2 != 0 and impact3 != 0 and impact4 == 0:
            impact = random.choice([1,2,3])
            if impact == 1:
                impact1 -= 1
            elif impact == 2:
                impact2 -= 1
            else:
                impact3 -= 1
        elif impact1 != 0 and impact2 != 0 and impact3 == 0 and impact4 != 0:
            impact = random.choice([1,2,4])
            if impact == 1:
                impact1 -= 1
            elif impact == 2:
                impact2 -= 1
            else:
                impact4 -= 1
        elif impact1 != 0 and impact2 == 0 and impact3 != 0 and impact4 != 0:
            impact = random.choice([1,3,4])
            if impact == 1:
                impact1 -= 1
            elif impact == 3:
                impact3 -= 1
            else:
                impact4 -= 1
        elif impact1 == 0 and impact2 != 0 and impact3 != 0 and impact4 != 0:
            impact = random.choice([2,3,4])
            if impact == 2:
                impact2 -= 1
            elif impact == 3:
                impact3 -= 1
            else:
                impact4 -= 1
        elif impact1 != 0 and impact2 != 0 and impact3 == 0 and impact4 == 0:
            impact = random.choice([1,2])
            if impact == 1:
                impact1 -= 1
            else:
                impact2 -= 1
        elif impact1 != 0 and impact2 == 0 and impact3 != 0 and impact4 == 0:
            impact = random.choice([1,3])
            if impact == 1:
                impact1 -= 1
            else:
                impact3 -= 1
        elif impact1 == 0 and impact2 != 0 and impact3 != 0 and impact4 == 0:
            impact = random.choice([2,3])
            if impact == 2:
                impact2 -= 1
            else:
                impact3 -= 1
        elif impact1 != 0 and impact2 == 0 and impact3 == 0 and impact4 != 0:
            impact = random.choice([1,4])
            if impact == 1:
                impact1 -= 1
            else:
                impact4 -= 1
        elif impact1 == 0 and impact2 != 0 and impact3 == 0 and impact4 != 0:
            impact = random.choice([1,2,3,4])
            if impact == 1:
                impact1 -= 1
            elif impact == 2:
                impact2 -= 1
            elif impact == 3:
                impact3 -= 1
            else:
                impact4 -= 1
        elif impact1 == 0 and impact2 == 0 and impact3 != 0 and impact4 != 0:
            impact = random.choice([3,4])
            if impact == 3:
                impact3 -= 1
            else:
                impact4 -= 1
        elif impact1 != 0 and impact2 == 0 and impact3 == 0 and impact4 == 0:
            impact = 1
            impact1 -= 1 
        elif impact1 == 0 and impact2 != 0 and impact3 == 0 and impact4 == 0:
            impact = 2
            impact2 -= 1 
        elif impact1 == 0 and impact2 == 0 and impact3 != 0 and impact4 == 0:
            impact = 3
            impact3 -= 1 
        elif impact1 == 0 and impact2 == 0 and impact3 == 0 and impact4 != 0:
            impact = 4
            impact4 -= 1

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        for i in s1[index]:
            checkboxes[i-1].click()

        time.sleep(2)
        for i in s2[index]:
            checkboxes[i+4].click()

        time.sleep(2)
        for i in s3[index]:
            checkboxes[i+13].click()

        time.sleep(2)
        radiobuttons[level].click()
        radiobuttons[replace+4].click()
        radiobuttons[impact+10].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
        testcheck = driver.find_elements("css selector", ".AB7Lab")#kesamping
        checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox

        p = 0
        for i in range(7):
            jawab1 = p1[i][index] + p
            testcheck[jawab1].click()
            p += 5

        p = 70 
        for i in range(3):
            jawab1 = p2[i][index] + p
            testcheck[jawab1].click()
            p += 5

        p = 85
        for i in range(4):
            jawab1 = p3[i][index] + p
            testcheck[jawab1].click()
            p += 5

        p = 125
        for i in range(4):
            jawab1 = p4[i][index] + p
            testcheck[jawab1].click()
            p += 5

        p = -1
        for i in s4[index]:
            jawab2 = i + p
            checkboxes[jawab2].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        )

        submit_button.click()

        driver.implicitly_wait(4)
        driver.get("https://forms.gle/ewmgWRyVrNzot6aW8")

        print("==================")
        print("civil  : " + str(civil))
        print("tcivil : " + str(tcivil))
        print("")
        print("years5 : " + str(years5))
        print("years1 : " + str(years1))
        print("")
        print("position  : " + str(position))
        print("tposition : " + str(tposition))
        print("")
        print("level1 : " + str(level1))
        print("level2 : " + str(level2))
        print("level3 : " + str(level3))
        print("level4 : " + str(level4))
        print("")
        print("replace1 : " + str(replace1))
        print("replace2 : " + str(replace2))
        print("replace3 : " + str(replace3))
        print("replace4 : " + str(replace4))
        print("")
        print("impact1 : " + str(impact1))
        print("impact2 : " + str(impact2))
        print("impact3 : " + str(impact3))
        print("impact4 : " + str(impact4))
        print("")
        # print("  : " + str())
        # print("")
        
        index+=1
        times-=1
        print("index  : " + str(index))
        print("times  : " + str(times))
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