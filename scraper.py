import requests
import json
import string
from bs4 import BeautifulSoup



url = "https://www.poetryfoundation.org/poems/poem-of-the-day"

r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    poems = soup.find_all("ul" , {"class" : "c-vList c-vList_bordered c-vList_bordered_anomaly"})
    for index, poem in enumerate(poems):
        title = poem.find('h2')
        links = poem.find("a", href=True)["href"]
        x = requests.get(links)
        content = BeautifulSoup(x.content, 'html.parser').text
        content_encode = bytes(content.encode())
        file = open(f" poem {index}", "wb")
        file.write(content_encode)
        file.close()
    