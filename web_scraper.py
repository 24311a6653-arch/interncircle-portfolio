import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")

    data = []

    for quote in quotes:
        data.append({
            "quote": quote.get_text(strip=True)
        })

    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Scraping completed successfully!")
    print("Quotes saved to quotes.json")

else:
    print("Failed to access the website.")