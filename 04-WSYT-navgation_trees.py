from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html, "lxml")

for child in bsobj.find("table",{"id":"giftList"}).children:
    print(child)