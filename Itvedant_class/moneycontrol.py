import  requests
from bs4 import BeautifulSoup

url = "https://www.moneycontrol.com/commodity/"
headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"

res = requests.get(url,{'headers':headers})
# print(res.text)

bs = BeautifulSoup(res.text, 'html5lib')
formated_text = bs.prettify()
# print(formated_text)

tbs = bs.findAll('table',attr={'class':'mctable1'})


print(len(tbs))