from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from constants import username, password, ignore_name
from base_url import url

chromedriver_autoinstaller.install()

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self. driver = webdriver.Chrome()
        
    def open_link(self):
        go_link = self.driver.get(url)
        time.sleep(3)
        return go_link
    
    def login(self, username, password):
        write_username = self.driver.find_element(
        By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input'
        ).send_keys(username)
        write_password = self.driver.find_element(
        By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input'
        ).send_keys(password)
        return write_username, write_password
        
    def click_login_button(self):
        click_login = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button')
        click_login.send_keys(Keys.ENTER)
        time.sleep(7)
        return click_login
        
    def not_now(self):
       paSs = self.driver.find_element(By.CSS_SELECTOR, "div[role = button]").click()
       time.sleep(3)
       return paSs
    
    def click_search(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "svg[aria-label = Ara]").click()
        time.sleep(5)
        return button
    
    def write_name(self):
        """bu hisseni gptden komek aldm"""
        search_input = self.driver.find_element(By.CSS_SELECTOR, "input[autocapitalize='none']")
        search_input.send_keys(ignore_name)
        time.sleep(3)
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        time.sleep(5)
        profil_link = self.driver.find_element(By.CSS_SELECTOR, "a[href*='/" + ignore_name + "/']")
        profil_link.click()
        time.sleep(5)
        return profil_link
    
    def ignore_user(self):
        more = self.driver.find_element(By.CSS_SELECTOR, "div[role = button]").click()
        time.sleep(3)
        return more
    
    def ignore(self):
        ignore = self.driver.find_element(By.XPATH, "//button[normalize-space()='Engelle']").click()
        time.sleep(3)
        return ignore
    
    def is_sure(self):
        sure = self.driver.find_element(By.XPATH, "//div[@class='x78zum5 xdt5ytf x1crbq5u xvrdyt3 x179zr98']//button[@class='xjbqb8w x1qhh985 xcfux6l xm0m39n x1yvgwvq x13fuv20 x178xt8z x1ypdohk xvs91rp x1evy7pa xdj266r x11i5rnm xat24cr x1mh8g0r x1wxaq2x x1iorvi4 x1sxyh0 xjkvuk6 xurb0ha x2b8uid x87ps6o xxymvpz xh8yej3 x52vrxo x4gyw5p xkmlbd1 x1xlr1w8'][normalize-space()='Engelle']").click()
        time.sleep(5)
        return sure
        





