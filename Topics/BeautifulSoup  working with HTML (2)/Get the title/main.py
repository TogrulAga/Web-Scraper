import requests

from bs4 import BeautifulSoup


response = requests.get(input())

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.find("h1").text)
else:
    print("Error")
