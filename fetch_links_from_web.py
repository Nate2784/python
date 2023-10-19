import urllib.request as req, urllib.parse as parse, urllib.error as error
from bs4 import BeautifulSoup as bs

url = input('Enter url -')
html = req.urlopen(url).read()
soup =bs(html, 'html.parser')
# retrieve all https and save them in an md file
tags = soup('a')
with open('links fetched.md', "w") as file:

    for tag in tags:
        link = tag.get('href', None)
        if link and link.startswith('https://'):
            file.write(link + '\n')
file.close()
