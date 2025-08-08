🎓 IMDb Movie Insights Project – Professional Case Study
🎯 Objective
To design a robust data pipeline that scrapes, enriches, and analyzes IMDb’s Top 250 Movies, culminating in an interactive Power BI dashboard for uncovering actionable insights about movie performance.

🛠️ Tech Stack
Python (Requests, BeautifulSoup, Pandas)

OMDb API

Power BI Desktop

Git / GitHub for version control

🧩 Process Overview
1️⃣ Data Collection
Initial Web Scraping

Extracted movie titles, descriptions, and URLs from IMDb’s Top 250 page.

Addressed challenges:

Dynamic content requiring precise HTML selectors.

Special character encoding issues.

Detailed Scraping

For each movie URL, parsed additional metadata: runtime, genre, director, top cast, and gross worldwide revenue.

Where scraping did not yield reliable results (e.g., missing runtime), used OMDb API for consistent enrichment.

2️⃣ Data Cleaning & Preparation
Normalized numeric fields (box office, ratings, votes).

Split multi-genre strings into separate records (many-to-many relationships).

Created derived fields:

BoxOffice_Million

BoxOffice_Label (for formatting)

Verified data integrity and handled missing values.

3️⃣ Data Modeling in Power BI
Imported cleaned datasets.

Established relationships:

One-to-many between Movies and Genres.

Calendar table linked to Release Year.

Additional Budget table joined by IMDb ID.

Defined calculated columns and measures using DAX.

4️⃣ Dashboard Design
Created a two-page dashboard focusing on business-relevant KPIs:

Page 1: Overview

Cards:

Total Movies

Total Box Office Revenue

Average IMDb Rating

Total Budget

Charts:

Top 10 Grossing Movies

Top 10 Rated Movies

Top 10 Movies by Genre

Genres by both Critically and Financially

Page 2: Trend Analysis

Charts:

Number of Movies Released by Year

Top 10 Genre by AVG Ratings

Total Gross by Genre

Table

Interactive Slicers:

Year Range

Genre

Title

5️⃣ Additional Enhancements
Uploaded project files to GitHub with clear folder structure and README.

💡 Key Learnings
Combining scraping with API enrichment dramatically improves data quality.

Thoughtful data modeling prevents duplication issues in Power BI.

Simplicity and clarity in visuals yield more actionable insights than overcrowding dashboards.

📂 Repository
GitHub – IMDb Movie Insights

🏆 Outcome
A fully documented, end-to-end data project demonstrating:

Web scraping proficiency

Data cleaning and enrichment

Relational modeling

Business-focused reporting

This project can be adapted to similar scenarios in retail analytics, product performance tracking, or media analysis.
