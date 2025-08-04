import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = "https://www.imdb.com/chart/top"
headers = {
    "User-Agent": "Mozilla/5.0",
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


json_ld_tag = soup.find("script", type="application/ld+json")
json_data = json.loads(json_ld_tag.string)


movies_raw = json_data["itemListElement"]
movies = []

for item in movies_raw:
    movie = item["item"]
    movies.append({
        "Title": movie.get("name"),
        "Alternate Title": movie.get("alternateName"),
        "Description": movie.get("description"),
        "URL": movie.get("url")
    })


df = pd.DataFrame(movies)
df.to_csv("top_250_simple.csv", index=False)

print(f"✅ Scraped {len(df)} movies and saved to top_250_simple.csv")
