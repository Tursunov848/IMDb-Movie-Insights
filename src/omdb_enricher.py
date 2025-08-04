import pandas as pd
import requests
import time
import os

API_KEY = "54f7bef6"  
INPUT_FILE = "imdb_scraper/top_250_simple.csv"
OUTPUT_FILE = "top_250_enriched.csv"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def extract_imdb_id(url):
    return url.split("/")[4]

def fetch_omdb_data(imdb_id):
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={API_KEY}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    
    if data.get("Response") == "False":
        raise Exception(data.get("Error", "Unknown error"))
    
    return {
        "IMDb_ID": imdb_id,
        "Title": data.get("Title"),
        "Year": data.get("Year"),
        "Rated": data.get("Rated"),
        "Released": data.get("Released"),
        "Runtime_Minutes": int(data.get("Runtime", "0 min").replace(" min", "")) if "min" in data.get("Runtime", "") else None,
        "Genre": data.get("Genre"),
        "Director": data.get("Director"),
        "Top_Cast": data.get("Actors"),
        "BoxOffice": data.get("BoxOffice", "").replace("$", "").replace(",", "") if data.get("BoxOffice") != "N/A" else None,
        "IMDb_Rating": float(data.get("imdbRating")) if data.get("imdbRating") != "N/A" else None,
        "IMDb_Votes": int(data.get("imdbVotes", "0").replace(",", "")) if data.get("imdbVotes") != "N/A" else None,
    }

def main():
    df = pd.read_csv(INPUT_FILE)
    enriched_data = []

    for idx, row in df.iterrows():
        imdb_id = extract_imdb_id(row["URL"])
        print(f"🔍 Fetching {idx+1}/{len(df)}: {row['Title']} ({imdb_id})")

        try:
            movie_data = fetch_omdb_data(imdb_id)
            enriched_data.append(movie_data)
        except Exception as e:
            print(f"⚠️  Failed to fetch {row['Title']}: {e}")
        
        time.sleep(0.75)  

    df_enriched = pd.DataFrame(enriched_data)
    df_enriched.to_csv(OUTPUT_FILE, index=False)
    print(f"\n✅ Enriched data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
