#coding=utf-8
from selenium import webdriver
import time
import os
os.environ["webdriver.firefox.driver"]="C:\\Program Files\\Mozilla Firefox\\firefox.exe"

driver=webdriver.Firefox(executable_path='D:\\PycharmProjects\\heei3k\\venv\\geckodriver')


class cnitt():
    def __init__(self):
        driver.get("http://www.cnitt.net/forum-44-1.html")
        time.sleep(60)

    def sendwater(self):
        driver.get("http://www.cnitt.net/forum-44-1.html")

        driver.find_element_by_id('subject').clear()
        driver.find_element_by_id('subject').send_keys("为了世界和平与爱")
        driver.find_element_by_id('fastpostmessage').clear()
        driver.find_element_by_id('fastpostmessage').send_keys("为了世界和平与爱")
        driver.find_element_by_id('fastpostsubmit').click()

    def sendresponse(self):
        driver.get("http://www.cnitt.net/thread-11562-1-1.html")

        driver.find_element_by_id('fastpostmessage').clear()
        driver.find_element_by_id('fastpostmessage').send_keys("为了世界和平与爱")
        driver.find_element_by_id('fastpostsubmit').click()



Cnitt=cnitt()

for x in range(500):
    Cnitt.sendresponse()
    time.sleep(15)


driver.quit()