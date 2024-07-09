import requests
import json
import string
from bs4 import BeautifulSoup
from datetime import date
import datetime

today = str(date.today())

url = "https://www.poetryfoundation.org/poems/poem-of-the-day"


def get_poem():
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        poems = soup.findAll('article')

        for poem in poems:
            link = poem.find('h2', {'class': 'c-hdgSans c-hdgSans_2'})
            link = link.find('a')['href']
            x = requests.get(link)
            soup_2 = BeautifulSoup(x.content, 'html.parser')
            title = soup_2.find('h1', {'class': 'c-hdgSans c-hdgSans_2 c-mix-hdgSans_inline'}).string
            print(title.text)
            content = soup_2.find('div', {'class': 'c-feature'}).text
            content_encode = bytes(content.encode())
            file = open(f"{today}", "wb")
            file.write(content_encode)
            file.close()
            print("Saved")


if __name__ == "__main__":
    get_poem()
