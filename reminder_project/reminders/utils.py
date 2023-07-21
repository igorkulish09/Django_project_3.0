import requests
from bs4 import BeautifulSoup


def get_new_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select(".quote")

    new_quotes = []
    for quote in quotes:
        text = quote.select_one(".text").get_text()
        author_name = quote.select_one(".author").get_text()
        author_bio = quote.find_next("span").find_next("span").get_text()
        new_quotes.append({"text": text, "author": author_name, "bio": author_bio})

    return new_quotes
