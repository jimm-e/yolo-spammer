from selenium import webdriver
import time
import string
import random
import os
from random import randint
go = 0
#Yolo Spammer
#Version 1.0
#Created by jimmyshadow1
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
print("\nYolo Spammer")
print("Made by jimmyshadow1\n")
while go == 0:
    url = input("Enter Yolo url: ")
    messageType = input("0 for random letters, 1 for custom message: ")
    if (messageType is "0") or (messageType is ""):
        letters = string.ascii_lowercase
        message = ''.join(random.choice(letters) for i in range(10))
        print(message)
    elif messageType is "1":
        message = input("Custom message: ")
    proxys = input("Use a proxy? (Must have proxies saved in proxies.txt) y/N: ")
    if proxys is "y":
        try:
            proxyFile = open("proxies.txt", "r")
            proxies = proxyFile.read().split(',')
            proxy = proxies[randint(0,len(proxies)-1)]
            print(proxy)
            proxyFile.close()
            driver_options = webdriver.ChromeOptions()
            driver_options.add_argument('--proxy-server=%s' % proxy)
            driver = webdriver.Chrome(executable_path=(resource_path("chromedriver.exe")),options=driver_options)
        except:
            print("Make sure you have proxies in proxies.txt in the same folder as spammer.exe")
    elif (proxys is "n") or (proxys is ""):           
            driver = webdriver.Chrome(executable_path=(resource_path("chromedriver.exe")),)
    try:
        while go == 0:                
            driver.get(url)
            messageToSend = driver.find_element_by_xpath('//*[@id="text"]')
            messageToSend.send_keys(message)
            driver.find_element_by_xpath('//*[@id="send-button"]').click()
            time.sleep(.300)
    except Exception as err:
        if "Message: invalid argument" in str(err):
            print("\n\nPlease enter a vaild Yolo url.\n\n")
        print("Reloading spammer...\n\n")
        driver.quit()


