import requests
import sqlite3
from datetime import datetime
import json

# Load configuration from config.json
with open("config.json", "r") as f:
    config = json.load(f)

API_KEY = config['api_key']

# SQLite database setup
conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Create a table to store daily summaries if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS daily_weather_summary (
    city TEXT,
    date TEXT,
    avg_temp REAL,
    max_temp REAL,
    min_temp REAL,
    dominant_condition TEXT
)
''')
conn.commit()

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': city,
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind': data['wind']['speed'],
            'condition': data['weather'][0]['main'],
            'timestamp': data['dt']
        }
        return weather_data
    else:
        return None

# Function to store data in the SQLite database
def store_weather_data(city, temp, min_temp, max_temp, condition):
    today = datetime.now().strftime('%Y-%m-%d')

    c.execute('SELECT * FROM daily_weather_summary WHERE city = ? AND date = ?', (city, today))
    record = c.fetchone()

    if record:
        current_avg_temp = record[2]
        current_max_temp = record[3]
        current_min_temp = record[4]

        new_avg_temp = (current_avg_temp + temp) / 2
        new_max_temp = max(current_max_temp, max_temp)
        new_min_temp = min(current_min_temp, min_temp)

        c.execute('''
            UPDATE daily_weather_summary
            SET avg_temp = ?, max_temp = ?, min_temp = ?
            WHERE city = ? AND date = ?
        ''', (new_avg_temp, new_max_temp, new_min_temp, city, today))
    else:
        c.execute('''
            INSERT INTO daily_weather_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (city, today, temp, max_temp, min_temp, condition))

    conn.commit()

# Function to get the daily weather summary from the database
def get_weather_summary(city):
    c.execute('SELECT * FROM daily_weather_summary WHERE city = ?', (city,))
    return c.fetchall()
