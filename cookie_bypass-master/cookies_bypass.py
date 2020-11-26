#selenium libraries
import subprocess
from selenium import webdriver
import os
import time
import getpass

#Shutting dnow all chrome processes before using the program
print("[INFO] Shutting down all chrome processes to use this program.")
subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
#import getpass
options = webdriver.ChromeOptions()
#Find your google cookie directory. I have automated this part, if it doesn't work please refer to my video to find your cookie folder.
path_to_chrome_cookie="user-data-dir=C:\\Users\\Lenovo\\AppData\\Local\\Google\\Chrome\\User Data"
#Path to your chrome profile
options.add_argument(path_to_chrome_cookie) 
try:
    driver = webdriver.Chrome(os.getcwd()+"\\webdriver\\chromedriver.exe", options=options)
except:
    print("[-] 1. Please close all your chrome browser before opening the program")
    print("[-] 2. Please update the chromedriver.exe in the webdriver folder according to your chrome version:https://chromedriver.chromium.org/downloads")
#go to the website that you want to bypass
driver.get("https://main.sci.gov.in/case-status")















