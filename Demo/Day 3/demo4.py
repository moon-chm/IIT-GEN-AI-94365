from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
time.sleep(5)
driver.get("https://www.sunbeaminfo.in/index")
driver.implicitly_wait(5)
time.sleep(5)
search_box=driver.find_element(By.LINK_TEXT,"INTERNSHIP")
time.sleep(10)
driver.quit()

