import requests

from bs4 import BeautifulSoup

word = input()
response = requests.get(input())

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    for p in soup.find_all("p"):
        if word in p.text:
            print(p.text)
            break
