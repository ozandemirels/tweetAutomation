# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:51:58 2022

@author: ozan.demirel
"""
import driver as driver
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://twitter.com/')
driver.maximize_window()
driver.implicitly_wait(10)

loginButton = driver.find_element(By.XPATH, '//span[contains(text(),"Sign in")]')
loginButton.click()

time.sleep(3)
userName = driver.find_element(By.XPATH, '//input')
userName.send_keys('ozandemirel.93@gmail.com')

nextButtons = driver.find_elements(By.XPATH, '//div[@role="button"]')

for nextButton in nextButtons:
    if nextButton.text == 'Next':
        nextButton.click()
        break

try:
    userName2 = driver.find_element(By.XPATH, '//input')
    userName2.send_keys('ozandemirel93')
    nextButtons2 = driver.find_elements(By.XPATH, '//div[@dir="auto"]')
    for nextButton in nextButtons2:
        if nextButton.text == 'Next':
            nextButton.click()
except:
    pass

passElement = driver.find_element(By.XPATH, '//input[@type="password"]')
passElement.send_keys('****************')

loginButtons = driver.find_elements(By.XPATH, '//div[@dir="auto"]')
for loginButton in loginButtons:
    if loginButton.text == 'Log in':
        loginButton.click()
        break

for i in range(1, 101):
    tweetElement = driver.find_element(By.XPATH, '//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]')
    tweetElement.send_keys('This is robot talking - ' + str(i))

    sendTweet = driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
    sendTweet.click()
    time.sleep(0.5)


