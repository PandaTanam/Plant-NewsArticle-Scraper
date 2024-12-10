# News Scraper

This project is designed to scrape the latest news articles related to plant care and management from Google News. The scraper is implemented as a Google Cloud Function that is triggered by Pub/Sub messages. The scraped data is stored in a Firestore database for easy access and retrieval.

## Features

- Scrapes the latest news articles based on a specified keyword.
- Stores the news articles in a Firestore database.
- Automatically deletes old news articles before adding new ones to keep the database updated.
- Triggered by Google Cloud Pub/Sub for automated scraping.

## Technologies Used

- Python: The programming language used for the scraper.
- Requests: For making HTTP requests to fetch web pages.
- BeautifulSoup: For parsing HTML and extracting data from web pages.
- Firebase Admin SDK: For interacting with Firestore to store news articles.
- Google Cloud Firestore: A NoSQL document database for storing news data.
- Google Cloud Functions: For deploying the scraper as a serverless function.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Google Cloud account with Firestore and Cloud Functions enabled
- Firebase Admin SDK credentials
- Google Cloud SDK (for local testing and deployment)

### Usage

Once deployed, the function will automatically scrape the latest news articles related to "merawat menanam" (plant care and management) whenever it is triggered by a Pub/Sub message.

### Deployment

To deploy the scraper as a Google Cloud Function, follow these steps:

1. **Deploy the Function:**
   Use the Google Cloud SDK to deploy the function:
    ```bash
    gcloud functions deploy news_pubsub
        --runtime python39
        --trigger-topic YOUR_PUBSUB_TOPIC_NAME
        --entry-point news_pubsub
        --project YOUR_PROJECT_ID
        --region YOUR_REGION
    ```
                                                   
2. **Set Up Pub/Sub Trigger:**
   Create a Pub/Sub topic that will trigger the function. You can publish messages to this topic to invoke the scraper.

### Scraping Logic

- The scraper fetches news articles from Google News using the specified keyword.
- It parses the HTML to extract the title, source, link, and image of each article.
- Before adding new articles, it deletes any existing articles in the Firestore collection to ensure the database is up-to-date.

## Firestore Structure

The scraped news articles are stored in a Firestore collection named `news`. Each document in this collection contains the following fields:
- `title`: The title of the news article.
- `source`: The source of the news article.
- `link`: The URL link to the news article.
- `image`: The URL of the article's image.
- `timestamp`: The time when the article was scraped.
