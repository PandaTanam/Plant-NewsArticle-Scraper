import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import firestore
from datetime import datetime

firebase_admin.initialize_app()
db = firestore.client()

def scrape_google_news():
    keyword = "merawat+menanam"
    url = f"https://news.google.com/search?q={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all("article", class_="IFHyqb DeXSAc")

    news_collection_ref = db.collection('news')
    docs = news_collection_ref.stream()
    for doc in docs:
        doc.reference.delete()

    for result in results:
        source = result.find("div", class_="vr1PYe").text
        title = result.find("a", class_="JtKRv").text
        link = result.find("a")['href'].replace("./", "https://news.google.com/")
        image = "https://news.google.com" + result.find("img", class_="Quavad")['src']
        
        news_data = {
            'title': title,
            'source': source,
            'link': link,
            'image': image,
            'timestamp': datetime.now().strftime('%Y/%m/%d - %H:%M')
        }

        news_collection_ref.add(news_data)
        print(f"Saved: {title} from {source} - {link} - {image}")

if __name__ == "__main__":
    scrape_google_news()
