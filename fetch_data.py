import requests
import os
from dotenv import load_dotenv
from database import init_db, get_session
from models import EconomicData

# Load FRED API key from .env
load_dotenv()
API_KEY = os.getenv('FRED_API_KEY')

# FRED datasets to store
SERIES = {
    # Original 4
    'UNRATE': 'Unemployment Rate',
    'CPIAUCSL': 'Consumer Price Index (Inflation)',
    'MORTGAGE30US': '30-Year Fixed Mortgage Rate',
    'MSPUS': 'Median Sales Price of Houses',

    # Labor Market
    'JTSJOL': 'Job Openings',
    'CIVPART': 'Labor Force Participation Rate',
    'CES0500000003': 'Average Hourly Earnings',
    'ICSA': 'Initial Jobless Claims',

    # Finance & Markets
    'FEDFUNDS': 'Federal Funds Rate',
    'DGS10': '10-Year Treasury Yield',
    'DGS2': '2-Year Treasury Yield',
    'SP500': 'S&P 500',
    'UMCSENT': 'University of Michigan Consumer Sentiment',

    # Housing
    'HOUST': 'Housing Starts',
    'RHORUSQ156N': 'Home Ownership Rate',
    'CUSR0000SEHA': 'Rent Index',
    'HSN1F': 'New Home Sales',

    # Macro
    'A191RL1Q225SBEA': 'GDP Growth Rate',
    'DSPIC96': 'Real Disposable Personal Income',
    'PSAVERT': 'Personal Savings Rate'
}

def fetch_and_store():
    """Fetches data from FRED API and stores it in the database."""
    
    # Make sure the database and tables exist
    init_db()
    session = get_session()

    for series_id, series_name in SERIES.items():
        print(f"Fetching {series_name}...")

        # Call FRED API
        url = f"https://api.stlouisfed.org/fred/series/observations"
        params = {
            'series_id': series_id,
            'api_key': API_KEY,
            'file_type': 'json',
            'observation_start': '1947-01-01'
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Store each data point in the database
        count = 0
        for obs in data['observations']:
            # Skip missing values
            if obs['value'] == '.':
                continue

            record = EconomicData(
                series_id=series_id,
                series_name=series_name,
                date=obs['date'],
                value=float(obs['value'])
            )
            session.add(record)
            count += 1

        session.commit()
        print(f"  ✓ Stored {count} records for {series_name}")

    session.close()
    print("\nAll data fetched and stored successfully!")

if __name__ == '__main__':
    fetch_and_store()