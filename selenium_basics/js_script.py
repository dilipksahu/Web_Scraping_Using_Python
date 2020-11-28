import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# url = "https://www.chrisburkard.com/"
url = "https://curiositystream.com/categories"

web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text,'html.parser')

print(len(web_soup.findAll("img")))

driver = webdriver.Chrome()
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html,'html.parser')
print(len(sel_soup.findAll("img")))

images = []
for i in sel_soup.findAll("div"):
    print(i)
    src = i["style"]
    images.append(src)

print(images)
