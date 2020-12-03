import  requests
from bs4 import BeautifulSoup

url = "https://www.itvedant.com/"


headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
res = requests.get(url,{'headers':headers})
# print(res.text)

bs = BeautifulSoup(res.text, 'html5lib')
formated_text = bs.prettify()
# print(formated_text)

htmlfile = 'abc.html'

# f = open(htmlfile,'w')
# f.write(f)
# f.close()

img_list = bs.find_all('a')
for i in img_list:
    print(i)
    print("----------------------------------")
print(len(img_list))

print("success")