from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
time.sleep(2)

driver.get("https://portfolio-ecru-seven-38.vercel.app/")
driver.implicitly_wait(5)
time.sleep(2)
search_box=driver.find_element(By.NAME,'name')
search_box.send_keys("Darshan")
search_box.send_keys(Keys.RETURN)
time.sleep(7)
driver.quit()