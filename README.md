# 🎬 IMDb Movie Performance Insights

A Python-powered project to extract, enrich, and analyze IMDb's Top 250 Movies. This workflow combines web scraping, API integration, and data transformation to build a clean dataset ready for business intelligence and KPI generation.

---

## 🔄 Project Workflow

### 1. Web Scraping (IMDb Website)
- **`scraper.py`**  
  → Scrapes the IMDb Top 250 page for titles, years, and movie URLs.
  
- **`movie_details_scraper.py`**  
  → Scrapes each movie’s page for genre, director, top cast, and runtime.

### 2. API Enrichment (OMDb)
- **`omdb_enricher.py`**  
  → Enriches movie data using the OMDb API: 
    - Runtime (clean format)
    - Box Office Gross
    - IMDb Rating
    - IMDb Votes
    - Standardized director, cast, genre fields

### 3. Data Cleaning & Type Handling
- **`check_data_types.ipynb`**  
  → Ensures proper data types (`int`, `float`, `object`)  
  → Adds derived fields:
    - `BoxOffice_Million` — numeric for KPIs
    - `BoxOffice_Label` — formatted for readability
    - `BoxOffice_Missing` — flag for missing gross data

---

## 📁 Folder Structure

IMDb-Movie-Insights/
├── data/
│ ├── top_250_simple.csv # Raw scraped titles + URLs
│ ├── movie_genres.csv 
│ ├── top_250_budget.csv
│ └── top_250_final.csv # ✅ Cleaned & transformed dataset
│
├── src/
│ ├── scraper.py
│ ├── movie_details_scraper.py
│ ├── omdb_enricher.py
│ └── check_data_types.ipynb # Data validation & transformation
│
├── Power BI/
│ └── imdb.pbix - KPI visualizations
│
├── README.md
