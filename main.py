import json
import requests
from bs4 import BeautifulSoup

def scrape_google_news():
    keyword = "merawat+menanam"
    url = f"https://news.google.com/search?q={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all("article", class_="IFHyqb DeXSAc")
    for result in results:
        source = result.find("div", class_="vr1PYe").text
        title = result.find("a", class_="JtKRv").text
        link = result.find("a")['href'].replace("./", "https://news.google.com/")
        
        print(f"{title}\n{source}\n{link}\n\n")

if __name__ == "__main__":
    scrape_google_news()
