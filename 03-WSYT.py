from urllib.request import urlopen
from bs4 import BeautifulSoup

html  = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html, "lxml")
namelist = bsobj.findAll('span',{'class':'green'})
for name in namelist:
    print(name.get_text())


'''
find (tag, attributes, recursive, text, keywords )
findAll (tag, attributes, recursive, text, keywords )

Tags: .findAll({"h1", "h2", "h3", "h4" })
Attributes: .findAll("sapn", {"class":{"green", "red"}})
Recursive: Boolean
Text: nameList = bsObj.findAll(text="the prince")
                 print(len(nameList))
Limit: =findAll() with a limit 1 
Keyword allText = bsObj.findAll(id="title",class="text")
'''

'''
Types of objects in BeautifulSoup 
> BeautifulSoup objects - bsobj
> Tag objects - bsObj.div.h1
> NavigableString objects - text within tags
> The Comment object - <!-a comment object -->
'''           

