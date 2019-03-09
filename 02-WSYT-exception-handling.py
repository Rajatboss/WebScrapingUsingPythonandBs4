from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

#types of error
'''
try:
    html = urlopen("http://www.psythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
    # return null , break or other
except URLError as e:
    print("The server could not found")
else:
    # conditions
    print("It worked")
'''
# The problem is if we try to access an non-existing tga then it will result in None object which itself is an error but for he program it will not ct as error

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read(), "lxml")
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.psythonscraping.com/pages/page1.html")

if title == None:
    print("title could not be found")
else:
    print(title)