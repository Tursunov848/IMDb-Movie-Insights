import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time


INPUT_FILE = "imdb_scraper/top_250_simple.csv"
OUTPUT_FILE = "top_250_detailed.csv"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_movie_details(url):
    response = requests.get(url, headers=HEADERS)
    response.encoding = response.apparent_encoding  
    soup = BeautifulSoup(response.text, "html.parser")

   
    json_tag = soup.find("script", type="application/ld+json")
    if not json_tag:
        raise ValueError("No JSON-LD found")
    data = json.loads(json_tag.string)

    
    title = data.get("name")
    year = data.get("datePublished", "")[:4]
    rating = data.get("aggregateRating", {}).get("ratingValue")
    votes = data.get("aggregateRating", {}).get("ratingCount")

    genres = data.get("genre", [])
    if isinstance(genres, str): genres = [genres]

    directors = []
    if isinstance(data.get("director"), list):
        directors = [d.get("name") for d in data.get("director")]
    elif isinstance(data.get("director"), dict):
        directors = [data["director"].get("name")]

    actors = [a.get("name") for a in data.get("actor", [])][:3]

    runtime_minutes = None
    duration_str = data.get("duration", "")
    if "PT" in duration_str:
        try:
            hours = 0
            minutes = 0
            if "H" in duration_str:
                hours = int(duration_str.split("H")[0].replace("PT", ""))
            if "M" in duration_str:
                minutes = int(duration_str.split("H")[-1].replace("M", ""))
            runtime_minutes = hours * 60 + minutes
        except:
            pass

    if runtime_minutes is None:
        try:
            runtime_tag = soup.find("li", attrs={"data-testid": "title-techspec_runtime"})
            runtime_text = runtime_tag.get_text(strip=True)
            runtime_minutes = int(runtime_text.replace("min", "").strip())
        except:
            runtime_minutes = None


    gross = None
    try:
        gross_tag = soup.find("li", attrs={"data-testid": "title-boxoffice-cumulativeworldwidegross"})
        if gross_tag:
            gross_text = gross_tag.find("span").text.replace("$", "").replace(",", "").strip()
            if gross_text.isdigit():
                gross = int(gross_text)
    except:
        gross = None

    return {
        "Title": title,
        "Year": int(year) if year.isdigit() else None,
        "Rating": float(rating) if rating else None,
        "Votes": int(votes) if isinstance(votes, int) else int(votes.replace(",", "")) if votes else None,
        "Genres": genres,
        "Directors": directors,
        "Top_Cast": actors,
        "Runtime_Minutes": runtime_minutes,
        "Gross_Worldwide": gross,
        "URL": url
    }


def main():
    df_input = pd.read_csv(INPUT_FILE)
    results = []

    for idx, row in df_input.iterrows():
        print(f"🔍 Scraping {idx + 1}/{len(df_input)}: {row['Title']}")
        try:
            details = scrape_movie_details(row['URL'])
            results.append(details)
        except Exception as e:
            print(f"⚠️  Failed: {row['Title']} — {e}")
        time.sleep(1.5)

    df_output = pd.DataFrame(results)
    df_output.to_csv(OUTPUT_FILE, index=False)
    print(f"\n✅ Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
