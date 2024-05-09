from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Axioo\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("profile-directory=Profile 9")

driver = webdriver.Chrome(executable_path=r'C:\\iqbal\\bisnis\\1\\bot\\Autofill-Google-Form\\chromedriver\\chromedriver.exe', options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe4Egonc8MY8VTIesvCr0UfP34XfY-ZFBbLEEJT45S_oRCjkg/viewform")


try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        






        

        # time.sleep(3)
        # submit_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]"))
        # )

        # submit_button.click()

        # driver.implicitly_wait(4)
        # driver.get("https://forms.gle/dLN8EfqDnaUkuPfj6")

        index+=1
        print("==================")
        print("index : " + str(index))
        print("")

        times-=1
        print("times : " + str(times))
finally:
    # driver.quit()
    print("berhasil")