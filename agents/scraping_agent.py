# agents/scraping_agent.py

import requests
from bs4 import BeautifulSoup

def get_earnings_news(ticker):
    """
    Scrapes Yahoo Finance for recent news headlines and filters those about earnings.
    Returns top 3 relevant headlines.
    """
    url = f"https://finance.yahoo.com/quote/{ticker}/news?p={ticker}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all links with headline text
    headlines = []
    for a_tag in soup.find_all("a", href=True):
        title = a_tag.get_text().strip()
        if "earnings" in title.lower() and len(title) > 10:
            headlines.append(title)
        if len(headlines) >= 3:
            break

    return headlines
