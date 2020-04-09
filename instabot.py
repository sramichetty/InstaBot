from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

class Instagrambot:

    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
        self.login()

    def login(self):
        self.driver.get('https://instagram.com/accounts/login')
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)

    def nav_user(self,user):
        self.driver.get('https://instagram.com/' + user)
    
    def like_user_post(self,user,limit = 3):
        self.nav_user(user)
        photo = self.driver.find_element_by_class_name('eLPA')
        photo.click()
        sleep(2)
        for i in range (limit):
            like_btn = self.driver.find_element_by_name('afkep')[1]
            like_btn.click()
            next_btn = self.driver.find_element_by_xpath("//a[contains(text() , 'Next')]")
            next_btn.click()
            sleep(1)



bot = Instagrambot('username','password')
bot.like_user_post('the rock')





