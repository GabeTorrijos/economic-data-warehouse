# Economic Data Warehouse

A SQL-powered web application that stores, queries, and visualizes 47,000+ real economic data points from the Federal Reserve (FRED API).

Built with Python, Flask, SQLAlchemy, and Chart.js.

---

## Live Demo

Coming soon — deploying to Render.

---

## Features

- **SQL Query Interface** — Run real SQL queries against 47,000+ rows of economic data directly from the browser
- **Interactive Charts** — Visualize any of 20 economic series with historical Chart.js line charts
- **Data Pipeline** — Automated Python script fetches and stores data from the FRED API into a SQLite database
- **20 Economic Series** — Covers labor market, inflation, housing, finance, and macroeconomic indicators
- **75+ Years of Data** — Historical data dating back to 1947

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Database | SQLite, SQLAlchemy |
| Data Source | Federal Reserve FRED API |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Deployment | Render |

---

## Database Schema

```sql
CREATE TABLE economic_data (
    id          INTEGER PRIMARY KEY,
    series_id   TEXT NOT NULL,
    series_name TEXT NOT NULL,
    date        TEXT NOT NULL,
    value       REAL
);
```

---

## Economic Series Included

**Labor Market**
- Unemployment Rate (UNRATE)
- Job Openings (JTSJOL)
- Labor Force Participation Rate (CIVPART)
- Average Hourly Earnings (CES0500000003)
- Initial Jobless Claims (ICSA)

**Inflation & Prices**
- Consumer Price Index (CPIAUCSL)
- Rent Index (CUSR0000SEHA)

**Housing**
- 30-Year Fixed Mortgage Rate (MORTGAGE30US)
- Median Sales Price of Houses (MSPUS)
- Housing Starts (HOUST)
- Home Ownership Rate (RHORUSQ156N)
- New Home Sales (HSN1F)

**Financial Markets**
- Federal Funds Rate (FEDFUNDS)
- 10-Year Treasury Yield (DGS10)
- 2-Year Treasury Yield (DGS2)
- S&P 500 (SP500)
- University of Michigan Consumer Sentiment (UMCSENT)

**Macroeconomic**
- GDP Growth Rate (A191RL1Q225SBEA)
- Real Disposable Personal Income (DSPIC96)
- Personal Savings Rate (PSAVERT)

---

## Project Structure

| File | Purpose |
|------|---------|
| `app.py` | Flask application and routes |
| `models.py` | SQLAlchemy database schema |
| `database.py` | Database connection and setup |
| `fetch_data.py` | FRED API data pipeline |
| `requirements.txt` | Python dependencies |
| `templates/index.html` | Home page |
| `templates/query.html` | SQL query interface |
| `templates/visualize.html` | Chart visualizations |
| `static/css/style.css` | Stylesheet |

---

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/GabeTorrijos/economic-data-warehouse.git
cd economic-data-warehouse
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip3 install -r requirements.txt
```

4. Add your FRED API key to a `.env` file

FRED_API_KEY=your_api_key_here

5. Fetch data and populate the database
```bash
python3 fetch_data.py
```

6. Run the app
```bash
python3 app.py
```

7. Open your browser and go to `http://127.0.0.1:5000`

---

## Example SQL Queries

```sql
-- Latest unemployment rate readings
SELECT date, value FROM economic_data
WHERE series_id = 'UNRATE'
ORDER BY date DESC LIMIT 20;

-- Record counts for all series
SELECT series_name, COUNT(*) as total_records,
       MIN(date) as earliest, MAX(date) as latest
FROM economic_data
GROUP BY series_name
ORDER BY total_records DESC;

-- Fed funds rate since 2020
SELECT date, value FROM economic_data
WHERE series_id = 'FEDFUNDS'
AND date >= '2020-01-01'
ORDER BY date;
```

---

## Data Source

All data is sourced from the [Federal Reserve Bank of St. Louis FRED API](https://fred.stlouisfed.org/).

---

## Author

Gabriel Torrijos — [GitHub](https://github.com/GabeTorrijos)