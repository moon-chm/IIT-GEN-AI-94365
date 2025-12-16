from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
time.sleep(5)
driver.get("https://www.google.com/?zx=1765856273996&no_sw_cr=1")
driver.implicitly_wait(5)
time.sleep(5)
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("What is Oneplus latest OS")
search_box.send_keys(Keys.RETURN)
time.sleep(10)
driver.quit()

