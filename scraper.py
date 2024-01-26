import requests
import json
import string
from bs4 import BeautifulSoup



url = "https://www.poetryfoundation.org/poems/poem-of-the-day"

r = requests.get(url)

if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    poems = soup.find_all('a')
    print(poems)