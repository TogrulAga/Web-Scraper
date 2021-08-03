import requests

from bs4 import BeautifulSoup


act_number = int(input())
response = requests.get(input())

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.find_all("a")[act_number - 1].get("href"))
else:
    print("Error")
