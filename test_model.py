import unittest
from unittest.mock import patch
import sqlite3
from model import store_weather_data, get_weather_summary

class TestModel(unittest.TestCase):

    def setUp(self):
        # Set up an in-memory SQLite database for testing
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS daily_weather_summary (
                city TEXT,
                date TEXT,
                avg_temp REAL,
                max_temp REAL,
                min_temp REAL,
                dominant_condition TEXT
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    @patch('model.sqlite3.connect')
    def test_store_weather_data(self, mock_connect):
        # Mock the sqlite3 connection to return the in-memory connection
        mock_connect.return_value = self.conn

        # Now call store_weather_data without passing conn explicitly
        store_weather_data('Delhi', 30, 25, 35, 'Clouds')
        
        # Verify that the data was inserted into the in-memory database
        self.c.execute('SELECT * FROM daily_weather_summary WHERE city="Delhi"')
        result = self.c.fetchone()
        self.assertIsNotNone(result)  # Check if data is stored
        self.assertEqual(result[0], 'Delhi')
        self.assertEqual(result[2], 30)  # Check avg temp

    @patch('model.sqlite3.connect')
    def test_get_weather_summary(self, mock_connect):
        # Mock the sqlite3 connection to return the in-memory connection
        mock_connect.return_value = self.conn

        # Insert data first, then retrieve it using get_weather_summary
        store_weather_data('Delhi', 30, 25, 35, 'Clouds')
        result = get_weather_summary('Delhi')
        
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0][0], 'Delhi')

if __name__ == '__main__':
    unittest.main()
