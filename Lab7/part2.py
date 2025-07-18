from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, features='html.parser')

images = bsObj.find_all("img", {"src": re.compile(r"\.\./img/gifts/img3.*\.jpg")
})

for image in images:
    print(image["src"])
