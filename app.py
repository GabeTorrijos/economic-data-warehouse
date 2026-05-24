import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from database import init_db, get_session
from models import EconomicData
from sqlalchemy import text

load_dotenv()

app = Flask(__name__)

# Initialize database on startup
init_db()

@app.route('/')
def index():
    """Home page — shows overview of what's in the database."""
    session = get_session()
    
    # Get list of all unique series in the database
    series = session.query(
        EconomicData.series_id,
        EconomicData.series_name
    ).distinct().all()
    
    # Get total record count
    total_records = session.query(EconomicData).count()
    
    session.close()
    return render_template('index.html', series=series, total_records=total_records)

@app.route('/query', methods=['GET', 'POST'])
def query():
    """SQL query interface page."""
    session = get_session()
    results = None
    columns = None
    error = None
    user_query = ''

    if request.method == 'POST':
        user_query = request.form.get('sql_query', '')
        try:
            result = session.execute(text(user_query))
            columns = list(result.keys())
            results = [list(row) for row in result.fetchall()]
        except Exception as e:
            error = str(e)

    session.close()
    return render_template('query.html', 
                         results=results, 
                         columns=columns, 
                         error=error,
                         user_query=user_query)

@app.route('/api/series/<series_id>')
def api_series(series_id):
    """API endpoint — returns data for a specific series as JSON."""
    session = get_session()
    
    records = session.query(EconomicData)\
        .filter(EconomicData.series_id == series_id)\
        .order_by(EconomicData.date)\
        .all()
    
    data = [{'date': r.date, 'value': r.value} for r in records]
    session.close()
    
    return jsonify({'series_id': series_id, 'data': data})

@app.route('/visualize')
def visualize():
    """Visualization page — charts for any series."""
    session = get_session()
    series = session.query(
        EconomicData.series_id,
        EconomicData.series_name
    ).distinct().all()
    session.close()
    return render_template('visualize.html', series=series)

if __name__ == '__main__':
    app.run(debug=True)