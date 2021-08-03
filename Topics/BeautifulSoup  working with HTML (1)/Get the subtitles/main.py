import requests

from bs4 import BeautifulSoup


index = int(input())
content = requests.get(input()).content

soup = BeautifulSoup(content, "html.parser")

print(soup.find_all("h2")[index].text)
