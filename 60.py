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
driver.get("https://forms.gle/R2ab1YjpaS2nbE1H8")

page1 = [
    [1,5,5,4,5,4,5,5,6,5,3,5,5,6,5,6,4,5,4,5,5,5,6,6,4,4,5,4,6,3,5,4,3,5,4,6,5,6,6,4,4,1,4,6,6,4,2,4,6,4,5,6,3,5,6,6,4,5,4,6,2,3,4,6,3,5,6,6,6,4,5,6,5,1,5,4,2,6,5,5,6,2,3,2,1,2,3,2,3,2,1,2,3,2,1,2,3,1,3,2,1,1,1,3,2,1,2,2,2,5,3,3,1,1,3,3,2,1,2,3,3,1,4,2,3,3,3,5,2,1,2,4,4,3,4,2,5,5,6,5,4,3,3,3,6,2,2,6,3,4,5,4,5,4,4,6,2,1,2,3,6,2,4,5,4,6,5,6,5,6,4,5,4,4,1,6,4,5,3,5,5,6,5,4,4,6,4,3,5,5,4,6,6,5,5,5,5,5,5,5,5,4,3,2],
    [6,4,4,2,6,5,6,5,6,2,4,6,6,5,4,5,5,5,4,2,4,6,5,5,5,5,4,6,6,3,4,6,4,2,6,1,5,1,5,1,5,5,4,6,2,4,5,6,5,5,6,6,4,6,4,4,3,6,1,6,6,6,4,4,2,4,1,4,5,5,4,2,5,4,5,4,5,5,5,4,4,2,3,1,3,2,2,1,1,3,2,1,2,3,1,3,2,3,3,1,2,3,1,1,3,1,1,2,3,5,3,1,1,2,3,5,3,1,1,1,4,3,5,4,3,1,3,2,3,3,3,4,5,5,6,3,6,6,5,6,2,5,6,5,4,3,2,3,4,6,3,2,3,4,3,5,5,6,5,5,4,3,4,4,5,5,4,5,5,5,6,6,4,6,5,6,1,5,2,6,5,2,2,2,5,5,5,4,5,4,6,6,5,4,6,4,2,4,1,6,3,1,5,2],
    [4,4,1,5,1,5,6,5,6,4,6,5,6,6,4,6,1,1,4,4,4,4,6,6,4,4,6,1,2,4,4,6,1,4,4,6,4,5,4,4,1,5,1,1,5,5,5,6,5,4,5,4,5,4,5,4,6,5,4,6,5,5,4,5,4,3,4,5,5,6,6,5,6,6,6,5,6,6,6,5,6,1,3,3,3,2,2,2,2,4,2,3,1,3,2,3,1,2,3,5,3,3,3,2,2,1,1,1,2,6,1,1,1,3,2,6,2,3,2,3,3,2,5,5,3,2,2,3,3,2,1,5,5,5,3,2,3,4,5,6,4,2,4,3,4,5,2,5,4,2,6,3,5,6,3,6,4,6,4,5,5,3,2,4,4,4,6,1,5,5,6,4,4,6,5,4,1,6,5,6,1,1,4,2,4,1,4,6,4,1,4,4,5,5,1,2,4,4,6,4,4,1,6,2],
    [5,4,6,5,4,4,1,6,4,4,1,4,4,1,6,6,6,4,6,4,6,6,6,1,4,2,4,4,2,2,4,6,6,5,4,4,6,4,5,5,4,4,6,5,6,5,4,6,5,2,5,5,5,5,5,6,6,5,5,3,5,6,6,5,5,5,3,4,3,3,3,6,5,4,4,6,4,6,5,5,5,1,3,2,3,1,3,2,2,5,2,1,2,3,2,5,2,5,3,5,4,4,3,2,4,3,4,3,3,5,1,1,2,1,3,4,4,3,5,2,5,4,4,6,2,2,1,4,2,2,2,3,4,5,6,4,5,2,6,3,3,5,6,5,2,4,3,5,4,6,3,5,2,4,5,2,3,4,2,3,5,4,5,4,6,6,4,6,6,1,5,6,3,6,4,4,4,5,1,1,2,4,4,1,5,4,6,1,4,4,2,4,4,4,6,5,2,4,2,4,2,2,5,3],
    [5,1,1,6,4,1,4,6,1,5,5,1,1,4,4,6,6,4,4,4,5,4,6,6,5,5,4,6,5,2,2,2,4,5,2,4,2,4,5,4,5,4,5,5,4,6,4,5,6,5,3,3,6,6,6,2,6,3,6,4,3,6,6,6,5,6,4,5,6,4,5,6,5,4,4,5,5,5,6,6,4,5,3,3,2,3,1,3,3,6,1,2,2,1,3,2,1,2,4,2,2,1,2,3,3,1,2,4,2,6,3,1,3,1,3,2,3,2,3,1,5,3,5,6,4,4,2,3,3,2,1,4,5,3,4,5,6,2,4,3,5,6,4,6,4,6,5,6,6,5,4,3,4,2,2,4,5,4,3,2,3,4,3,4,6,4,4,6,4,2,2,2,1,5,1,4,4,4,4,5,5,2,6,1,5,1,5,4,1,5,1,5,4,5,1,5,3,4,5,4,4,3,6,2],
    [4,4,4,4,1,4,5,4,4,5,4,6,5,6,4,1,1,1,1,6,5,6,6,5,6,4,4,6,6,2,4,5,6,5,5,4,1,5,4,4,6,2,6,2,5,5,4,4,5,4,4,5,5,5,5,6,6,2,6,2,2,5,4,4,1,5,1,1,4,1,4,5,4,6,6,6,5,6,6,5,5,2,3,2,2,3,3,2,3,6,1,1,3,2,3,1,1,2,4,2,2,3,3,1,3,3,1,5,2,6,3,3,3,1,1,2,1,2,3,3,2,3,6,3,2,2,3,1,1,2,2,2,6,5,6,6,6,5,4,5,3,6,4,6,5,2,4,3,2,5,4,3,3,4,5,5,2,5,2,5,6,5,6,4,4,4,5,1,5,6,2,1,4,4,4,4,6,6,1,5,5,4,4,2,4,6,1,1,5,6,2,4,6,4,6,4,2,5,6,6,2,2,4,2],
    [4,4,4,4,1,1,5,4,1,5,6,5,4,6,5,6,5,6,5,6,4,6,4,5,6,6,5,6,4,5,5,6,4,6,4,5,3,3,1,4,6,1,4,6,4,5,5,5,1,4,1,6,6,1,4,4,1,5,4,5,4,5,3,5,6,4,6,4,5,2,4,6,1,6,6,1,4,6,4,6,5,1,3,2,1,2,2,2,2,5,1,3,2,3,2,2,1,6,5,6,2,2,2,2,3,2,2,3,1,4,3,3,3,1,2,3,3,3,3,2,2,3,3,4,3,2,3,5,3,1,2,3,3,4,5,4,2,4,3,5,6,4,3,5,1,5,6,4,2,5,4,6,2,5,6,2,6,5,4,5,5,5,5,4,3,4,4,4,6,4,6,5,5,5,5,4,4,6,6,1,5,6,4,3,4,5,1,3,5,1,6,6,5,6,5,6,4,1,5,1,4,2,4,2],
    [4,6,4,5,4,5,4,4,4,6,6,4,5,6,6,5,4,5,5,6,5,5,5,6,4,6,6,6,6,2,5,4,4,6,3,4,5,5,5,6,5,4,3,5,4,2,6,6,6,6,3,5,5,2,4,2,2,4,3,5,5,6,5,6,5,5,2,3,2,3,2,5,4,6,3,4,4,4,3,4,6,1,3,3,1,3,1,3,2,3,1,1,2,2,1,1,2,6,5,4,1,2,2,1,2,3,1,6,1,3,3,3,2,3,2,4,3,3,3,1,1,1,4,5,3,1,1,5,3,3,2,5,3,5,5,4,4,3,3,2,4,5,4,5,5,4,2,2,5,3,5,6,3,4,2,5,6,1,3,5,3,2,3,6,6,6,4,5,5,4,4,5,2,4,6,5,5,5,6,4,6,5,4,2,4,6,6,5,5,5,5,5,4,4,6,4,3,2,5,6,5,2,4,6],
    [4,4,6,5,6,6,5,5,5,5,6,6,4,4,5,6,4,5,6,6,4,2,6,5,5,4,6,4,6,1,4,4,4,4,4,4,4,4,5,6,5,5,4,5,6,3,5,6,6,5,6,6,5,4,6,4,1,3,3,5,6,5,5,3,4,3,6,4,1,5,4,5,6,5,1,4,4,4,4,4,5,3,2,1,1,2,2,3,1,4,1,2,3,2,6,3,1,5,1,6,3,3,2,3,6,1,2,2,1,4,2,3,1,6,2,2,5,3,3,6,4,3,5,5,1,1,2,3,2,3,2,3,2,2,1,4,6,5,2,5,6,5,6,4,5,2,6,3,4,5,6,5,2,3,3,4,5,4,2,4,4,5,5,6,4,5,6,6,4,5,6,4,3,5,5,5,4,4,6,6,6,4,4,4,4,5,1,5,4,4,4,5,6,5,4,5,3,4,4,4,3,4,6,2],
    [5,4,1,6,4,1,4,1,6,1,5,1,4,5,5,6,5,6,6,5,5,4,4,5,6,6,4,6,5,1,4,4,6,4,5,5,5,4,5,6,5,4,4,4,6,6,4,4,4,6,6,1,5,5,5,6,2,1,6,2,4,6,6,2,5,2,6,4,4,5,6,4,6,5,2,4,6,5,5,5,4,2,3,3,1,3,2,3,2,4,1,3,1,2,2,1,1,6,3,2,3,1,3,2,2,3,2,1,2,5,2,3,2,3,1,4,3,3,2,3,5,3,5,6,2,1,1,3,1,1,3,6,4,4,2,6,5,2,1,5,5,5,4,5,6,2,4,3,6,2,6,2,2,5,3,5,5,4,3,3,5,2,6,4,1,1,1,5,4,5,1,5,1,5,6,6,4,6,5,5,5,5,5,6,4,6,1,4,4,4,5,4,6,5,5,4,4,4,4,6,2,3,6,4],
    [4,4,4,4,5,4,4,5,5,5,4,6,4,6,5,5,5,5,6,5,5,6,6,4,6,6,4,2,4,4,4,4,4,6,6,5,4,5,6,6,5,6,6,6,4,6,6,6,4,2,5,4,5,4,2,5,5,6,4,4,5,4,6,5,6,5,5,1,3,5,3,1,3,1,1,3,2,2,3,5,4,1,2,3,1,2,3,2,2,1,2,2,2,1,3,1,1,2,2,5,3,2,1,3,3,1,2,3,2,1,1,2,1,3,1,4,3,1,4,2,2,1,3,1,2,2,3,2,3,3,3,2,6,2,4,5,2,3,5,2,1,2,4,5,2,3,2,3,1,3,2,3,5,3,2,2,2,2,6,3,1,6,2,5,5,4,4,4,6,5,4,5,6,6,5,4,6,4,6,4,4,5,6,4,5,5,5,5,4,2,4,6,4,5,5,4,6,6,6,4,6,4,3,4],
    [5,4,4,6,4,1,5,2,6,6,4,2,3,5,6,4,5,6,4,4,6,3,5,2,6,4,5,3,6,2,4,6,2,5,5,6,5,5,6,4,5,4,5,5,5,4,6,4,5,3,6,4,5,4,2,4,4,5,6,6,6,4,4,6,4,5,2,2,1,3,2,3,3,3,2,3,1,3,2,2,1,2,3,1,3,3,1,3,1,2,1,3,3,1,2,3,3,3,1,1,3,3,2,1,1,2,1,1,1,2,2,1,3,2,2,2,1,2,3,2,1,2,2,2,2,2,2,2,3,3,1,4,5,1,4,4,3,4,6,3,2,2,4,4,2,4,3,4,2,2,2,4,4,3,3,2,5,1,5,4,2,5,2,5,2,4,6,6,4,3,5,6,4,2,6,5,6,5,4,5,4,4,6,5,6,5,6,5,2,4,6,6,5,4,4,4,4,1,3,6,5,5,3,6],
    [4,6,4,4,6,4,4,6,6,5,6,1,6,4,6,4,6,5,3,5,4,4,4,4,5,5,6,5,5,6,4,6,5,6,6,6,5,5,2,2,4,4,6,6,4,5,4,3,6,2,6,6,6,5,3,4,5,4,4,5,6,5,5,4,4,5,4,1,2,1,3,3,3,3,3,2,6,3,2,1,2,3,1,1,3,5,2,3,3,1,2,1,2,1,1,1,2,2,3,2,2,3,2,2,2,1,1,3,1,3,2,2,1,3,3,3,2,1,3,3,2,1,3,2,3,3,1,1,2,3,1,2,6,4,5,5,2,5,5,2,1,3,3,3,3,3,5,5,2,2,1,3,5,3,2,3,4,3,4,2,2,6,4,6,4,3,5,5,6,4,4,6,4,4,6,6,6,6,4,2,4,5,6,6,5,4,5,6,5,6,2,4,4,4,5,1,4,5,5,6,6,5,4,6],
    [6,6,6,5,5,4,4,5,6,6,4,3,2,5,4,6,6,5,2,4,5,4,5,4,5,4,5,4,6,4,4,6,6,5,4,4,5,5,3,2,4,5,6,6,6,4,5,4,4,2,6,6,4,6,2,6,6,5,6,6,5,5,6,5,6,5,5,2,1,1,1,2,2,1,3,3,5,3,1,1,5,2,1,3,2,6,2,1,1,1,1,2,3,3,2,2,1,3,4,1,2,1,2,3,3,2,1,1,3,1,2,2,3,3,3,3,3,6,2,3,3,2,2,3,2,1,2,3,1,2,2,4,4,4,6,3,4,6,4,3,1,2,3,2,5,3,5,5,3,3,2,4,3,5,4,5,3,5,5,2,3,5,3,5,5,5,4,5,5,6,4,4,4,2,6,6,5,4,4,4,2,5,5,4,4,6,2,6,4,6,4,4,5,3,6,6,3,6,4,5,4,5,5,6],
    [6,6,4,4,5,6,4,5,6,6,5,2,6,6,5,4,5,4,2,4,6,6,5,4,6,4,5,6,5,3,4,4,4,2,5,4,6,6,2,5,5,5,5,6,6,5,6,5,5,4,4,5,4,6,2,5,5,5,5,5,6,6,6,4,6,4,6,2,3,2,3,2,1,2,1,2,4,1,2,2,5,2,3,3,3,1,3,3,2,3,3,2,1,3,1,3,1,3,5,2,1,1,3,3,3,1,1,3,2,3,3,1,1,1,1,5,5,5,6,1,1,2,1,2,1,3,2,4,1,3,2,5,5,2,5,4,5,4,5,3,4,3,2,2,1,5,4,2,5,5,1,2,4,2,5,1,3,4,4,4,5,5,1,4,4,4,5,6,2,4,6,6,6,5,5,6,5,6,6,4,4,3,4,4,4,4,2,5,4,6,5,6,5,4,2,5,6,5,6,5,6,5,3,4],
    [4,4,5,4,5,4,6,4,4,3,6,4,5,5,5,4,6,6,1,5,4,5,6,4,4,2,6,4,6,3,6,5,6,4,6,5,5,4,2,6,4,6,4,4,6,6,5,6,5,4,6,5,5,6,4,5,6,4,4,6,5,6,5,4,5,4,5,2,2,1,3,1,3,3,2,1,3,1,2,3,1,3,1,3,2,3,2,1,1,2,2,3,3,1,2,2,1,2,6,2,1,3,3,3,1,3,2,2,2,3,2,6,3,2,1,6,5,4,2,1,1,2,3,3,1,2,2,2,1,3,2,3,5,2,2,4,2,4,5,3,5,4,4,1,2,4,3,2,4,2,2,3,6,3,3,2,2,6,5,3,4,6,1,6,5,4,4,4,5,4,6,4,5,3,4,4,4,4,6,5,4,6,5,5,4,6,4,2,3,6,5,2,5,4,5,4,6,5,6,1,6,6,4,6],
    [4,5,5,4,6,5,5,6,5,4,6,5,2,4,6,4,4,5,4,6,6,4,6,5,4,2,5,2,5,4,5,6,1,3,5,6,6,4,3,3,3,5,5,6,4,4,4,3,6,4,4,6,5,5,6,6,6,5,6,5,6,5,5,6,6,6,4,2,3,2,2,1,2,2,1,1,4,1,1,3,3,1,3,1,2,5,2,3,2,2,3,1,1,2,3,1,3,2,3,1,2,1,2,2,2,3,1,1,3,1,3,5,1,3,1,5,3,3,6,1,3,2,2,2,3,2,1,3,3,1,3,1,5,4,6,4,1,5,3,4,3,2,2,3,1,1,2,3,3,1,4,3,5,3,4,1,3,3,6,2,3,4,3,3,3,5,5,4,4,5,4,6,5,5,2,4,4,6,5,4,6,4,6,6,2,3,6,3,4,6,5,2,6,5,5,4,5,5,5,1,4,4,2,6],
    [5,5,5,4,4,6,4,6,5,4,5,4,3,4,5,4,5,4,3,4,5,6,6,5,4,1,1,1,2,3,6,4,3,3,4,4,5,6,6,3,3,5,5,4,6,4,6,5,4,5,6,6,5,5,3,5,5,4,5,4,5,4,4,5,5,4,5,2,2,2,3,3,1,3,3,1,3,3,1,3,1,2,2,2,2,5,3,1,2,1,3,3,2,2,1,2,1,1,3,2,3,2,3,1,2,3,1,3,2,2,2,4,1,3,3,2,1,2,2,2,1,2,3,1,2,2,2,4,2,1,3,2,3,3,5,5,3,4,4,2,6,1,3,2,1,2,2,5,2,2,5,3,4,2,2,1,2,2,5,1,2,5,5,3,6,3,1,5,5,1,4,4,3,4,4,4,4,6,4,6,4,6,3,3,5,4,4,5,3,2,4,3,6,5,4,5,5,1,5,4,6,5,5,6],
    [6,4,6,5,4,5,6,6,4,3,6,4,3,4,6,5,6,6,5,4,5,5,4,6,5,2,6,5,5,6,4,5,5,1,5,6,5,4,4,4,6,4,4,5,4,5,6,4,5,3,6,4,6,6,3,5,5,6,4,6,4,6,6,4,5,6,3,3,1,4,2,2,3,1,1,1,5,2,3,1,4,3,2,1,2,5,1,3,3,3,3,1,3,2,3,2,3,3,5,1,2,1,3,2,2,1,2,2,1,1,3,3,1,2,2,6,3,2,2,1,2,3,3,1,3,2,3,1,2,2,2,2,3,4,6,6,5,5,5,3,5,4,1,4,2,6,3,1,1,1,2,4,5,3,1,2,1,2,6,5,1,4,3,5,6,5,6,4,4,5,6,3,5,5,4,4,4,5,5,6,5,5,6,5,6,5,6,6,5,4,3,6,1,6,4,6,4,2,6,6,5,4,2,4],
    [5,5,4,5,6,6,5,6,4,2,5,6,6,5,4,6,5,6,4,5,5,5,3,6,6,4,4,6,5,5,6,6,6,2,4,4,6,6,4,4,5,6,5,6,6,5,5,5,5,6,4,4,6,4,5,5,5,6,4,4,4,4,5,6,5,4,2,4,1,4,1,2,2,3,3,2,2,3,2,2,5,3,2,3,3,3,1,1,3,3,1,2,1,1,3,1,1,1,1,3,3,2,1,2,2,3,2,1,1,2,2,2,1,3,1,3,6,1,5,2,1,2,3,2,3,2,1,4,2,2,2,3,4,3,5,6,4,4,3,5,2,5,1,3,3,5,4,2,3,3,3,5,4,5,2,3,2,1,4,4,3,5,4,4,5,4,6,4,6,6,6,4,5,4,5,5,5,6,6,4,4,4,6,6,5,6,5,4,5,4,5,5,6,6,2,2,5,6,5,6,6,6,3,5],
]

page2 = [
    [2,1,2,3,3,3,3,2,3,2,1,3,2,2,3,3,1,2,1,1,1,3,1,2,1,2,2,1,3,2,3,1,2,1,1,2,1,3,2,3,1,2,3,1,2,2,2,1,1,1,1,2,1,1,5,2,3,3,3,2,3,2,3,3,3,3,6,4,6,5,5,5,4,4,5,4,4,6,4,6,4,6,5,5,4,6,5,4,5,4,5,5,5,5,5,6,4,6,5,6,4,4,4,5,4,5,6,4,6,4,6,6,5,6,6,6,4,5,4,6,4,6,4,6,4,5,4,6,5,6,5,4,2,4,2,5,5,5,2,6,2,4,5,6,5,2,3,4,5,6,4,4,2,5,3,5,5,6,2,4,6,2,5,2,1,1,3,2,1,1,2,3,2,3,2,2,1,3,1,2,1,2,3,1,2,3,3,3,3,3,4,1,2,2,1,3,2,3,1,4,2,1,4,3],
    [3,3,3,1,3,1,3,2,3,3,3,2,1,2,1,2,1,2,3,2,3,1,2,1,3,2,1,1,1,1,1,2,1,3,2,3,2,3,3,3,3,3,1,2,2,1,2,1,2,2,1,5,3,2,5,2,1,2,2,3,3,1,1,1,1,3,5,4,6,5,6,5,5,4,5,6,5,5,6,6,4,6,4,6,4,6,4,5,6,5,6,4,4,4,5,5,6,4,5,4,4,5,4,4,4,4,6,5,6,5,6,6,5,5,5,5,5,5,6,5,6,4,6,4,4,6,5,4,6,6,6,4,1,5,3,4,5,5,4,5,1,5,6,4,4,3,4,5,6,4,3,4,4,6,4,4,6,5,3,5,3,3,3,2,3,3,2,3,2,1,2,1,2,3,3,3,1,1,3,1,1,1,1,2,3,2,1,2,3,2,1,3,2,3,1,3,3,3,3,4,1,2,4,3],
    [3,4,3,2,2,3,3,2,3,2,2,2,3,1,3,2,3,2,2,3,3,1,3,2,2,3,2,2,1,2,2,2,1,1,1,1,3,2,3,3,3,1,3,1,3,2,3,1,3,1,1,6,1,1,4,1,2,2,1,2,3,3,1,1,1,1,5,6,4,6,6,5,6,5,6,4,6,5,6,4,5,5,4,5,6,6,6,6,5,5,6,5,6,6,6,6,6,6,6,5,4,4,6,4,4,5,5,5,4,4,4,4,6,4,4,6,5,4,5,4,4,5,4,5,4,5,6,4,4,5,5,5,4,4,1,6,6,3,2,6,4,3,6,5,5,2,5,3,6,5,4,5,3,4,2,5,6,6,1,5,4,1,5,2,3,3,2,3,3,2,2,2,2,1,3,1,2,3,2,1,2,2,3,4,4,1,3,4,3,3,3,2,3,2,2,2,3,1,3,2,2,2,3,3],
    [1,4,1,3,2,1,3,2,2,1,1,2,3,3,1,3,1,1,2,2,2,3,2,2,1,3,3,2,1,3,1,3,3,2,3,1,3,3,3,1,1,1,3,1,2,1,2,2,3,3,3,3,1,3,3,2,3,2,2,1,2,3,2,1,2,1,6,6,5,6,6,5,6,4,6,4,5,4,5,6,4,6,6,5,5,6,5,4,5,4,6,6,5,6,6,4,4,4,5,4,5,6,5,6,4,4,5,6,5,5,5,6,4,5,5,4,4,5,4,6,4,6,6,5,4,4,4,4,4,5,6,6,4,4,2,4,5,2,4,4,4,4,6,3,3,4,6,4,6,3,4,5,2,5,4,2,6,6,4,3,5,2,4,1,1,2,3,3,1,3,1,3,3,2,1,1,1,4,3,3,4,3,2,2,4,2,2,3,4,3,5,1,2,2,1,2,3,3,3,1,3,3,3,1],
    [1,4,2,3,3,1,3,2,3,1,3,1,1,2,2,2,1,3,2,1,2,3,2,3,2,3,1,1,3,1,3,3,1,2,2,2,2,1,3,3,3,3,1,2,1,1,1,3,1,2,1,4,1,3,4,2,2,2,3,2,3,2,2,3,1,2,6,5,6,6,5,5,4,4,5,5,4,5,6,6,4,5,5,6,6,4,6,5,6,4,6,4,6,6,6,4,5,4,5,5,6,6,6,6,5,4,5,4,4,5,4,5,5,5,4,4,5,4,4,4,5,6,4,5,4,6,4,6,6,6,4,5,3,4,2,5,4,3,5,5,2,5,5,5,4,5,4,5,5,5,5,6,3,3,3,3,5,3,5,6,4,3,4,3,4,3,1,1,1,2,2,3,3,3,1,1,2,5,2,3,1,1,1,1,5,2,3,2,5,3,6,2,3,2,3,2,1,2,3,3,3,2,5,4],
    [2,3,3,1,2,3,2,3,3,3,2,2,2,2,1,1,1,3,2,1,1,3,3,1,3,3,2,2,3,1,3,3,2,1,2,3,2,2,2,1,1,1,1,3,2,3,1,2,3,3,3,5,1,1,4,2,3,3,2,2,1,2,1,1,1,2,5,5,4,5,4,4,6,4,5,6,6,4,5,6,6,6,4,4,4,4,5,4,6,5,5,6,5,5,6,5,5,4,5,5,5,5,6,6,6,6,6,6,6,5,5,5,5,6,4,4,4,5,5,6,5,4,4,4,4,6,4,6,6,4,6,3,6,5,3,3,3,4,3,5,6,4,4,5,4,6,4,4,4,5,3,5,1,4,5,4,4,4,3,4,6,2,6,2,1,3,2,2,1,1,3,3,4,2,1,3,3,5,2,2,2,1,3,2,4,4,2,3,6,1,2,1,2,3,3,3,1,2,2,3,3,2,6,2],
    [1,1,1,1,1,2,1,1,1,3,1,2,1,3,2,2,2,1,2,2,1,2,2,3,2,3,3,2,1,2,1,2,3,2,2,3,1,3,3,1,1,2,2,3,3,3,1,3,1,2,3,6,3,3,5,1,2,1,1,2,3,1,1,3,2,3,6,5,6,6,4,4,4,5,4,6,4,6,4,4,5,5,5,5,6,5,5,6,6,6,4,5,4,6,4,6,4,6,5,4,5,5,6,6,4,6,5,5,5,6,4,6,4,4,6,5,5,6,4,4,4,5,6,4,4,5,4,4,5,6,4,6,4,5,4,4,4,5,1,5,4,5,3,3,4,4,5,5,3,3,2,6,2,5,5,5,5,4,2,4,5,1,6,1,3,1,1,3,2,1,2,1,1,1,1,3,2,3,1,1,2,2,1,3,2,4,4,2,4,1,3,2,1,4,3,1,2,2,3,2,1,1,5,2],
    [5,2,1,2,3,2,1,2,1,3,1,2,1,3,3,1,1,1,3,3,2,3,1,2,2,3,3,1,3,2,2,2,2,1,3,3,2,3,2,1,2,2,1,1,2,1,3,1,1,1,3,3,2,3,5,2,3,1,3,2,3,3,3,1,3,2,5,4,4,4,4,5,6,5,6,6,6,4,6,6,5,4,4,6,4,5,5,6,5,5,4,5,6,4,5,6,5,6,4,5,5,4,4,6,4,6,4,4,4,4,4,6,6,5,5,4,6,5,5,6,6,4,6,5,6,6,4,5,6,6,5,5,3,6,5,5,5,5,2,3,3,6,4,4,5,3,4,6,4,4,5,3,5,4,5,5,6,5,6,6,4,4,5,1,5,2,2,2,2,2,3,1,2,3,3,3,2,3,3,3,1,1,1,2,4,4,4,3,3,1,4,2,2,4,1,2,2,3,1,2,1,3,5,2],
    [5,3,3,2,3,3,1,3,3,3,1,1,2,1,3,2,2,2,1,1,2,3,2,1,2,3,3,2,3,2,3,1,3,1,1,3,1,3,1,2,2,2,3,2,3,1,1,2,1,3,2,3,3,3,6,1,2,2,2,1,2,1,1,3,2,1,4,5,5,5,6,5,4,4,4,4,6,5,6,4,6,6,6,4,4,5,4,6,5,4,5,5,6,4,6,6,5,5,6,6,4,4,4,4,6,5,6,5,5,5,6,6,4,4,6,4,6,5,5,6,4,5,6,4,4,5,5,5,5,6,5,6,4,3,1,5,6,6,2,3,4,2,5,5,6,5,5,2,5,5,4,5,2,5,5,6,4,6,3,6,5,2,5,1,1,3,2,2,3,3,3,3,2,3,3,3,2,1,2,1,1,3,1,2,4,5,2,3,3,1,2,1,3,3,2,2,1,2,1,5,3,3,5,4],
    [3,3,1,3,1,2,3,2,3,1,1,3,3,2,3,3,1,1,3,3,1,3,3,1,2,3,2,3,2,1,1,2,3,2,1,2,2,3,2,2,1,2,2,2,1,3,2,2,1,1,3,5,1,3,5,1,3,3,2,1,2,2,2,1,1,2,6,4,4,5,5,4,6,4,6,4,4,5,4,5,4,4,6,4,4,4,5,6,4,4,5,4,5,5,4,6,5,6,5,6,5,4,5,5,4,6,6,5,6,5,6,5,5,6,4,6,6,6,6,6,6,6,6,4,4,6,5,5,5,5,5,5,3,4,2,4,3,6,3,4,3,1,5,6,6,4,4,4,5,6,5,6,2,6,5,6,5,6,2,3,6,1,5,2,1,1,3,1,3,1,2,1,2,3,2,3,3,2,3,1,1,1,3,2,4,4,3,3,2,1,3,1,3,2,3,3,2,2,1,2,3,3,3,3],
    [5,5,5,5,4,4,5,6,4,6,6,5,4,5,5,5,5,5,6,4,5,5,4,6,4,5,5,4,4,6,4,4,4,4,4,4,6,5,6,6,6,5,6,4,4,6,5,6,6,6,4,6,6,5,3,5,4,6,6,6,4,5,5,4,5,6,2,3,3,1,1,1,3,2,2,2,2,3,3,2,3,1,1,1,5,2,2,1,1,2,3,3,3,3,1,1,1,2,2,2,1,1,1,2,3,1,3,1,2,3,3,3,2,3,2,3,2,2,1,2,2,3,3,1,1,5,3,2,1,3,1,3,5,6,5,4,2,4,4,2,5,3,2,5,3,2,4,1,4,3,3,2,4,3,2,4,5,4,4,4,3,5,1,5,6,4,4,4,4,5,6,5,4,6,4,4,4,5,5,5,4,4,4,6,5,5,6,6,4,5,4,5,6,5,5,4,6,6,5,4,5,5,2,5],
    [5,6,4,4,5,4,4,4,5,5,6,5,6,4,6,5,5,4,5,5,6,6,6,6,6,5,6,4,6,4,5,6,4,5,5,4,4,4,6,4,4,5,4,6,6,5,6,5,4,6,5,4,6,5,4,4,6,5,5,5,6,5,6,3,6,4,3,1,2,1,2,1,3,2,3,2,3,3,1,3,3,3,2,2,3,3,3,1,3,3,3,1,1,2,3,3,3,2,3,3,2,2,1,2,1,1,1,2,2,1,3,1,2,2,1,2,1,4,3,1,2,1,2,2,3,3,1,1,1,3,2,5,6,5,6,4,3,3,5,3,6,4,2,6,2,3,5,1,3,4,2,3,5,2,3,5,4,3,5,3,3,6,2,4,6,4,6,5,6,4,5,4,5,4,5,4,6,4,6,4,4,5,4,4,6,6,6,5,4,4,5,3,6,6,4,5,6,4,5,5,5,6,3,6],
    [6,5,4,6,6,4,6,4,5,4,6,5,5,6,5,4,4,4,6,4,5,5,4,5,4,5,5,6,5,5,4,5,4,5,6,5,5,5,4,4,6,6,6,4,6,4,4,4,6,5,4,5,6,4,3,6,6,6,6,6,4,5,4,5,5,6,2,1,2,2,2,3,2,2,3,3,3,2,3,2,3,1,2,2,5,2,1,2,2,1,1,3,3,3,2,3,2,2,3,4,3,2,2,1,1,1,1,1,3,3,1,1,2,3,1,1,2,5,1,3,3,1,1,1,3,6,1,3,3,3,2,6,6,6,5,5,2,2,6,4,4,3,3,4,3,2,4,2,1,3,4,2,6,3,2,4,3,4,6,4,2,4,3,4,4,6,5,6,3,5,5,5,2,6,4,5,4,5,3,4,5,6,4,4,6,6,4,5,3,4,5,3,5,6,4,3,5,5,6,3,6,3,2,4],
    [4,6,6,5,4,4,5,5,5,5,4,6,4,4,5,4,5,4,4,6,5,6,6,4,4,5,6,5,4,4,4,6,6,6,4,5,4,5,4,6,4,6,4,6,5,6,5,4,4,5,6,5,5,5,2,5,3,6,5,4,5,6,5,4,5,6,1,3,3,3,3,3,1,1,3,2,3,2,2,2,2,3,2,2,4,3,3,2,2,3,3,1,1,1,1,2,2,3,2,4,3,2,1,1,2,1,1,3,3,1,1,3,3,4,2,1,3,1,1,3,1,3,1,2,4,2,2,1,1,3,2,5,5,4,4,6,2,2,4,3,3,3,4,2,3,1,2,3,1,2,3,1,3,3,1,2,3,3,3,3,1,5,2,5,4,5,5,4,3,6,5,5,4,6,5,4,4,3,5,2,1,4,2,4,4,6,6,6,2,4,5,4,4,6,4,5,5,4,6,3,6,3,4,5],
    [6,4,6,4,5,6,4,5,5,6,4,4,6,6,6,6,6,4,6,5,6,4,6,4,5,5,6,4,4,5,6,5,5,5,5,6,4,6,5,5,5,6,5,5,5,4,6,5,5,4,6,5,4,4,4,6,4,5,6,5,4,5,4,3,6,4,1,1,2,1,1,3,2,2,2,2,1,1,2,3,2,1,1,3,6,3,1,2,3,2,2,3,1,1,1,3,1,1,3,2,2,3,2,2,2,1,3,3,1,3,3,2,2,5,3,3,4,5,1,1,1,2,2,2,4,2,3,2,2,2,3,2,2,5,5,5,1,3,4,2,4,2,3,2,4,2,3,4,4,2,2,2,4,4,2,3,2,2,4,1,1,5,2,4,5,5,6,6,5,2,2,2,5,4,6,5,6,3,2,3,2,3,5,3,6,4,6,6,3,2,6,2,5,6,2,6,6,6,5,2,6,2,2,5],
    [4,4,6,2,6,4,3,5,5,4,4,5,4,6,5,5,6,4,6,5,5,6,4,2,4,5,5,1,6,5,4,4,2,5,4,5,6,3,4,4,5,5,4,4,5,6,4,6,6,6,6,4,6,6,3,5,2,6,4,6,4,6,5,5,5,6,3,2,3,4,3,5,2,5,3,6,3,6,3,6,4,3,1,3,4,3,2,1,4,2,1,3,4,3,4,4,3,1,1,2,1,2,4,4,6,6,6,3,1,2,3,1,6,1,3,1,5,6,2,5,2,3,5,4,2,3,3,6,2,1,2,4,3,5,5,3,4,3,3,3,5,3,4,2,2,3,1,5,5,3,3,3,5,2,3,1,4,1,3,2,3,5,2,5,4,6,5,5,5,2,6,3,4,4,4,5,5,3,4,4,6,3,3,6,5,5,4,6,3,4,4,6,5,4,6,4,4,4,5,2,6,6,4,3],
    [6,4,6,5,4,5,6,4,4,6,5,5,5,4,4,6,5,6,5,6,4,4,6,4,6,4,6,6,6,5,5,4,4,4,6,5,5,5,6,5,6,4,5,4,6,6,5,6,6,4,5,4,6,4,4,6,4,4,5,5,6,6,6,5,5,5,1,1,3,4,1,2,1,3,3,3,2,1,3,1,2,1,2,2,3,2,3,3,1,2,2,2,1,2,2,1,2,3,3,3,3,1,3,1,1,1,3,3,1,2,1,2,4,3,4,3,6,1,3,2,3,2,1,4,2,3,2,1,2,1,2,5,5,5,3,6,1,4,4,3,3,1,4,3,2,4,2,4,3,1,5,2,4,2,4,2,2,1,2,1,2,6,2,5,4,6,6,4,5,3,5,4,4,5,4,6,5,6,5,5,4,4,3,5,2,4,2,6,5,5,5,6,6,5,5,6,6,6,4,3,4,4,4,4],
    [5,5,6,6,6,5,4,6,6,5,6,5,4,4,5,5,4,4,6,4,4,6,5,5,5,6,5,6,5,5,4,5,4,6,5,6,6,4,4,4,4,4,4,5,4,4,6,4,4,6,6,5,6,6,3,5,5,5,6,5,5,6,5,6,4,5,3,2,1,3,2,1,1,1,3,1,3,1,2,3,2,1,2,1,4,2,1,3,3,3,3,1,1,1,2,1,2,1,1,1,2,1,3,1,3,3,1,2,2,1,1,3,5,3,4,2,1,2,2,3,3,1,5,2,2,3,2,3,3,1,2,2,1,3,4,5,2,3,4,2,5,2,2,2,1,2,1,3,6,2,4,3,4,1,2,1,3,2,2,1,2,5,2,5,6,6,4,5,3,4,4,6,3,5,6,6,4,5,5,4,5,5,5,4,4,6,5,4,5,6,4,5,4,4,5,3,4,3,5,4,6,4,5,4],
    [5,4,4,5,4,6,4,6,6,5,6,6,6,4,6,6,6,5,5,6,4,5,4,5,4,5,4,4,5,4,5,6,5,6,4,5,5,5,4,5,5,6,5,4,4,5,5,6,6,6,5,4,5,4,1,6,3,6,6,5,6,4,4,6,6,6,3,2,2,3,1,1,2,2,2,3,1,2,2,1,3,1,2,3,4,1,1,2,2,3,2,2,3,1,3,3,1,2,1,3,2,2,1,3,3,1,1,1,2,1,3,3,1,1,2,3,1,3,1,1,3,3,3,1,3,3,2,2,3,3,1,5,4,3,5,6,5,2,5,2,5,3,1,1,2,3,1,2,5,3,3,2,5,2,3,1,2,1,5,6,3,6,6,5,5,4,4,4,6,4,6,6,6,5,6,5,5,6,5,4,5,5,4,4,5,4,4,5,5,6,6,6,6,4,5,5,5,6,5,6,4,5,2,5],
    [5,6,6,6,6,5,5,4,4,5,4,6,5,4,5,5,4,5,6,5,5,4,4,4,6,6,6,4,6,5,5,6,4,6,4,5,4,6,4,5,5,5,6,4,4,4,4,6,5,6,5,5,4,4,1,6,3,6,5,4,6,5,5,4,6,6,2,3,2,2,1,1,2,3,3,3,3,2,2,1,1,1,1,2,2,1,2,2,1,2,2,3,1,1,1,1,1,2,2,3,1,1,2,2,3,3,3,3,2,3,3,1,3,3,3,3,1,3,3,2,2,1,3,2,1,4,3,1,1,3,1,5,5,4,3,5,3,3,5,1,5,2,1,3,4,2,2,2,2,2,2,1,6,4,2,2,2,1,6,3,2,6,2,5,4,4,4,5,4,6,6,6,5,6,5,6,6,5,6,5,5,4,2,4,4,5,6,6,4,6,5,5,5,4,5,6,4,5,4,5,4,6,1,6],
]

telp = [
    "089659093492",
    "082311661975",
    "085743134600",
    "081284035792",
    "08990800373",
    "087881565603",
    "08561457366",
    "081284080605",
    "081260703421",
    "089635900280",
    "087881635223",
    "088901737453",
    "085777443837",
    "08811140623",
    "081370723719",
    "083899373966",
    "085710926144",
    "087889550897",
    "087885059708",
    "085714379318",
    "082111009923",
    "085669700058",
    "08578637894",
    "021-85349217",
    "081284919966",
    "081287411419",
    "089617684368",
    "081282688353",
    "081295256880",
    "081322403694",
    "081911262963",
    "081213985046",
    "089653230390",
    "083871144619",
    "087887973908",
    "081288992581",
    "081318514000",
    "082244366663",
    "087883374245",
    "083865512841",
    "089640073450",
    "085715423173",
    "081291418889",
    "082292936439",
    "089610811380",
    "081290294579",
    "089694687073",
    "081136394026",
    "082298008074",
    "081310331261",
    "081284784532",
    "085688010365",
    "089899070533",
    "081219104910",
    "085695844860",
    "082111963635",
    "087780916507",
    "085727593784",
    "085725305214",
    "088114604436",
    "083808659612",
    "089864549742",
    "089993632434",
    "081289151142",
    "083874075494",
    "085795211785",
    "081293688414",
    "085725895185",
    "083807329320",
    "089509345589",
    "087877940982",
    "082298397212",
    "083806942220",
    "085716230518",
    "085683450901",
    "081310955800",
    "081310560465",
    "081284181960",
    "085688010836",
    "081293361994",
    "081287584914",
    "085774757200",
    "089683382470",
    "081290576448",
    "089661984316",
    "083890997737",
    "083876748742",
    "081213699191",
    "089635497654",
    "083891250852",
    "081289435934",
    "089656683141",
    "083898044725",
    "085773211130",
    "085712484121",
    "085647228125",
    "081908482555",
    "087785218346",
    "085776316880",
    "087887988079",
    "081295793652",
    "081297694007",
    "081905847362",
    "081210455651",
    "085861858596",
    "085697724020",
    "088886467433",
    "085693956596",
    "081310177330",
    "081318671715",
    "089690188018",
    "087887684865",
    "081210971780",
    "081288333474",
    "089620577769",
    "087771777990",
    "085715888054",
    "089658372715",
    "081315002381",
    "089997325833",
    "082298516567",
    "081280558090",
    "087721069098",
    "083815054203",
    "089601760956",
    "083870298534",
    "081294000097",
    "089977213512",
    "085774460379",
    "083872678527",
    "088895091215",
    "087771238776",
    "085697365253",
    "083873632436",
    "083892992457",
    "081395420704",
    "089988870029",
    "081318761259",
    "085714646514",
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
    "08118887755",
    "0818790679",
    "081919898900",
    "081393566446",
    "082110058977",
    "087775926467",
    "081281206074",
    "081399741974",
    "081317526565",
    "087876555253",
    "082125250353",
    "08568683354",
    "083878700800",
    "081280136486",
    "08561003778",
    "081298216070",
    "081332007865",
    "081316206977",
    "081391544451",
    "08112508699",
    "081217879043",
    "08211320123",
    "08176414926",
    "08212602273",
    "082123847472",
    "081314828465",
    "081383190190",
    "081398524121",
    "081510055825",
    "085608584007",
]

cowo = 184
cewe = 18

times = 202
index = 2

try:
    while times:
        time.sleep(5)
        #Hardcoded logic
        test = 0

        if cowo != 0 and cewe != 0:
            kelamin = random.choice([0,1])
        elif cowo != 0 and cewe == 0:
            kelamin = 0
        elif cowo == 0 and cewe != 0:
            kelamin = 1

        time.sleep(2)
        if kelamin == 0:
            cowo -= 1
        else:
            cewe -= 1

        usia = random.choice([2,3,4,5,2,3,4,5,2,3,4,5,6])
        pendidikan = random.choice([9,10,11,9,10,11,9,10,11,9,10,11,12,13])

        time.sleep(2)
        radiobuttons = driver.find_elements("css selector", ".nWQGrd")#kebawah

        radiobuttons[kelamin].click()
        radiobuttons[usia].click()
        radiobuttons[pendidikan].click()

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = -1
        for i in range(20):
            s1 = page1[i][index] + p
            testcheck[s1].click()
            p += 6

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        testcheck = driver.find_elements("css selector", ".T5pZmf")#kesamping

        p = -1
        for i in range(20):
            s1 = page2[i][index] + p
            testcheck[s1].click()
            p += 6

        time.sleep(3)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]"))
        )

        submit_button.click()

        time.sleep(2)
        textboxes = driver.find_elements("css selector", ".whsOnd")#isian

        textboxes[0].send_keys(telp[index])

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
        driver.get("https://forms.gle/R2ab1YjpaS2nbE1H8")

        index+=1
        print("==================")
        print("cowo : " + str(cowo))
        print("cewe : " + str(cewe))
        print("")
        
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