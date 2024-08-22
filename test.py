from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_argument("--start-maximized")
#options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
driver.get("https://play.google.com/store/apps/details?id=com.whatsapp")
time.sleep(5)
element = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/c-wiz[5]/section/header/div/div[2]/button")
element.click()
time.sleep(5)
review = driver.find_elements(By.CLASS_NAME, "RHo1pe")
for review in review:
    print(review.text)
driver.close()