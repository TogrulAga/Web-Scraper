import requests

from bs4 import BeautifulSoup


response = requests.get(input())

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    filtered_links = list(filter(lambda x: len(x.text) > 1 and x.text.startswith("S") and (("entity" in x.get("href") or "topic" in x.get("href")) if x.get("href") is not None else True), links))
    print(list(map(lambda x: x.text, filtered_links)))
else:
    print("Error")
