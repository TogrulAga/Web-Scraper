import json
import string
import os
import requests

from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self):
        self.save_articles()

    @staticmethod
    def get_url():
        url = input("Input the URL:\n")
        response = requests.get(url)
        print()
        if response.status_code == 200:
            quote = json.loads(response.content)
            if "content" in quote.keys():
                print(quote["content"])
            else:
                print("Invalid quote resource!")
        else:
            print("Invalid quote resource!")

    @staticmethod
    def get_movie_url():
        url = input("Input the URL:\n")

        if "imdb" not in url or "title" not in url:
            print("Invalid movie page!")
            return

        response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        result = {}
        print()
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            result["title"] = soup.find("h1").text
            for meta in soup.find_all("meta"):
                if meta.get("name") == "description":
                    result["description"] = meta.get("content")

            if result == {}:
                print("Invalid movie page!")
            else:
                print(result)
        else:
            print("Invalid movie page!")

    @staticmethod
    def save_html():
        url = input("Input the URL:\n")
        response = requests.get(url)
        print()
        if response.status_code == 200:
            with open("source.html", "wb") as file:
                file.write(response.content)

            print("Content saved.")
        else:
            print(f"The URL returned {response.status_code }!")

    @staticmethod
    def save_articles():
        num_pages = int(input())
        type_of_articles = input()
        url = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page="
        for i in range(1, num_pages + 1):
            response = requests.get(f"{url}{i}")
            os.mkdir(f"Page_{i}")
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                articles = soup.find_all("article")
                for article in articles:
                    article_type = article.find("span", {"class": "c-meta__type"})
                    if article_type.text == type_of_articles:
                        article_url = article.find("a").get("href")
                        article_page = requests.get("https://www.nature.com" + article_url)
                        if article_page.status_code == 200:
                            article_content = BeautifulSoup(article_page.content, "html.parser")
                            if "News" in article_type.text:
                                body = article_content.find("div", {"class": "c-article-body"}).text.strip()
                                title = article_content.find("h1", {"class": "c-article-magazine-title"}).text.strip()
                            elif article_type.text == "Research Highlight":
                                body = article_content.find("div", {"class": "article-item__body"}).text.strip()
                                title = article_content.find("h1", {"class": "article-item__title"}).text.strip()

                            title = "".join(list(filter(lambda x: x not in string.punctuation, title))).replace(" ", "_")
                            print(title, body)
                            with open(f"Page_{i}/{title}.txt", "w", encoding="utf-8") as file:
                                file.write(body)
                        else:
                            print("No response")
                    else:
                        print(f"Wrong article type: {article_type.text}")


_ = WebScraper()
