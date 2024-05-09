import random
import time

from selenium.webdriver.remote.webelement import WebElement

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data.enumList import dataPilihan as pil

class dataQualtrics :
    driver: webdriver.Firefox

    def __init__(self, driver) :
        self.driver = driver

    def pindahHalaman(self) :
        time.sleep(3)
        submit_button = self.driver.find_elements("css selector", ".NextButton")
        submit_button[0].click()

    def kirim(self) :
        time.sleep(3)
        submit_button = self.driver.find_elements(By.XPATH, "//span[contains(text(), 'Kirim')]")

        submit_button[0].click()

    def kirimJawaban(self) :
        time.sleep(2)
        submit_button = self.driver.find_elements(By.XPATH, "//a[contains(text(), 'Kirim')]")

        submit_button[0].click()

    def tombol(self, pilihan: pil) -> list[WebElement]:
        match pilihan :
            case pil.ISIANPENDEK :
                return self.driver.find_elements("css selector", ".")#isian
            case pil.ISIANPANJANG :
                return self.driver.find_elements("css selector", ".")#texarea
            case pil.KEBAWAH :
                return self.driver.find_elements("css selector", ".SingleAnswer")#kebawah
            case pil.KESAMPING :
                return self.driver.find_elements("css selector", ".")#kesamping
            case pil.CHECKBOX :
                return self.driver.find_elements("css selector", ".")#checkbox
            case pil.LAINNYA :
                return self.driver.find_elements("css selector", ".")#texarea
            case pil.DROPDOWN :
                return self.driver.find_elements("css selector", ".")#dropdown
            case pil.BUBBLE :
                return self.driver.find_elements("css selector", ".q-radio")#soal di dalam soal

    def pilihDropdown(self, pilihan) :
        time.sleep(2)
        option = self.driver.find_elements(By.XPATH, "//span[contains(text(), '"+pilihan+"')]")
        option[len(option) - 1].click()

    # ===================================================================================================

    def hitungUsia(self, batasAwal: int, batasAkhir: int) -> int :
        result = random.randint(batasAwal, batasAkhir)
        return result

    def pilihTipe(self, jenis: list[int]) -> int :
        data: list[int] = []
        for i in range(len(jenis)) :
            if jenis[i] != 0 :
                data.append(i)

        result = random.sample(data, 1)
        return result[0]

    def pilihanCheckbox(self, awal: int, akhir: int, banyakData: int) -> list[int] :
        temp = random.randint(1, banyakData)

        listData: list[int] = []
        i = awal
        while i <= akhir :
            listData.append(i)
            i += 1

        result = random.sample(listData, temp)
        return result

    def polaJawab1(self, pola: int, awal: int, banyakSoal: int, kelipatan: int, jawab: list[WebElement]) :
        p = awal
        for i in range(banyakSoal) :
            s1 = p

            jawab[s1].click()
            p += kelipatan

    def polaJawab2(self, pola: int, awal: int, banyakSoal: int, kelipatan: int, jawab: list[WebElement]) :
        p = awal
        for i in range(banyakSoal) :
            if pola == 0 :
                s1 = random.choice([p,p+1])
            elif pola == 1 :
                s1 = random.choice([p,p+1,p+1])
            elif pola == 2 :
                s1 = random.choice([p,p+1,p+1,p+1])
            elif pola == 3 :
                s1 = random.choice([p,p,p+1])
            elif pola == 4 :
                s1 = random.choice([p,p,p,p+1])
            else :
                s1 = random.choice([p,p+1])

            jawab[s1].click()
            p += kelipatan

    def polaJawab3(self, pola: int, awal: int, banyakSoal: int, kelipatan: int, jawab: list[WebElement]) :
        p = awal
        for i in range(banyakSoal) :
            if pola == 0 :
                s1 = random.choice([p,p+1,p+2])
            elif pola == 1 :
                s1 = random.choice([p,p+1,p+1,p+2,p+2])
            elif pola == 2 :
                s1 = random.choice([p,p+1,p+1,p+1,p+2,p+2,p+2])
            elif pola == 3 :
                s1 = random.choice([p,p,p+1,p+1,p+2])
            elif pola == 4 :
                s1 = random.choice([p,p,p,p+1,p+1,p+1,p+2])
            elif pola == 5 :
                s1 = random.choice([p,p,p+1,p+1,p+1,p+2])
            else :
                s1 = random.choice([p,p+1,p+2])

            jawab[s1].click()
            p += kelipatan

    def polaJawab4(self, pola: int, awal: int, banyakSoal: int, kelipatan: int, jawab: list[WebElement]) :
        p = awal
        for i in range(banyakSoal) :
            if pola == 0 :
                s1 = random.choice([p,p+1,p+2,p+3])
            elif pola == 1 :
                s1 = random.choice([p,p+1,p+1,p+2,p+2,p+3,p+3])
            elif pola == 2 :
                s1 = random.choice([p,p+1,p+1,p+1,p+2,p+2,p+2,p+3,p+3,p+3])
            elif pola == 3 :
                s1 = random.choice([p,p,p+1,p+1,p+2,p+2,p+3])
            elif pola == 4 :
                s1 = random.choice([p,p,p,p+1,p+1,p+1,p+2,p+2,p+2,p+3])
            else :
                s1 = random.choice([p,p+1,p+2,p+3])

            jawab[s1].click()
            p += kelipatan

    def polaJawabCustom(self, awal: int, soal: list[int], kelipatan: int, jawab: list[WebElement]) :
        p = awal

        for i in range(len(soal)) :
            s1 = soal[i] + p

            jawab[s1].click()
            p += kelipatan
