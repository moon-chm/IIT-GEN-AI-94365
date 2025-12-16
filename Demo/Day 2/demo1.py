from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
time.sleep(2)

driver.get("https://duckduckgo.com/")
print("Initial Page Title",driver.title)
driver.implicitly_wait(5)
time.sleep(2)
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("What is python")
search_box.send_keys(Keys.RETURN)
print("later page title",driver.title)  
time.sleep(6)
driver.quit()
