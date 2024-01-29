import requests
import json
import string
from bs4 import BeautifulSoup



url = "https://www.poetryfoundation.org/poems/poem-of-the-day"

r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    poems = soup.findAll('article')

while True:
    for index, poem in enumerate(poems, start=0):
        link = poem.find('h2', {'class':'c-hdgSans c-hdgSans_2'})
        link = link.find('a')['href']
        x = requests.get(link)
        soup_2 = BeautifulSoup(x.content, 'html.parser')
        title = soup_2.find('h1', {'class' : 'c-hdgSans c-hdgSans_2 c-mix-hdgSans_inline'}).text
        content = soup_2.find('div', {'class': 'c-feature-bd'}).text
        content_encode = bytes(content.encode())
        file = open(f" poem {index} {title}", "wb")
        file.write(content_encode)
        file.close()
        print("Saved")
      