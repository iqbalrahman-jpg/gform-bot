from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening GUI)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open a website
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe4Egonc8MY8VTIesvCr0UfP34XfY-ZFBbLEEJT45S_oRCjkg/viewform")

email = "mtianur001@gmail.com",
passs = "081331973192"

times = 1

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

		option = driver.find_elements(By.XPATH, "//span[contains(text(), 'login')]")
		option[1].click()

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



		# radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah
		# textboxes = driver.find_elements("css selector", ".whsOnd")#isian
		# testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping
		# checkboxes = driver.find_elements("css selector", ".uHMk6b")#checkbox
		# pilihan = driver.find_elements("css selector", ".AB7Lab")#soal di dalam soal

		# dropdown = driver.find_elements("css selector", ".ry3kXd")#dropdown
		# option = driver.find_elements(By.XPATH, "//span[contains(text(), '"+domisili+"')]")

		# time.sleep(3)
		# submit_button = WebDriverWait(driver, 10).until(
		#     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
		# )

		# submit_button.click()