from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from profil_data import username, password

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
url = "https://www.instagram.com/"

go_link = driver.get(url)
time.sleep(3)

write_username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
write_username.send_keys(username)
time.sleep(3)

write_password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
write_password.send_keys(password)
time.sleep(3)

click_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
click_login.send_keys(Keys.ENTER)
time.sleep(10)

profil_url = "https://www.instagram.com/e_lv_n/?next=%2F"
go_profil = driver.get(profil_url)
time.sleep(3)