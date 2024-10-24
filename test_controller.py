import unittest
from controller import WeatherController
from model import store_weather_data

class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = WeatherController()

    def test_get_cities(self):
        # Test that get_cities returns the correct city list
        cities = self.controller.get_cities()
        self.assertIn('Delhi', cities)
        self.assertIn('Mumbai', cities)

    def test_fetch_and_display_weather(self):
        # Test fetching weather and ensure it's stored correctly
        self.controller.fetch_and_display_weather('Delhi')
        data = self.controller.get_avg_temp('Delhi')
        self.assertGreater(data, 0)  # Check if some data is returned

    def test_get_min_temp(self):
        # Test fetching minimum temperature
        store_weather_data('Delhi', 30, 25, 35, 'Clouds')  # Store sample data
        min_temp = self.controller.get_min_temp('Delhi')
        self.assertEqual(min_temp, 25)

    def test_get_max_temp(self):
        # Test fetching maximum temperature
        store_weather_data('Delhi', 30, 25, 35, 'Clouds')  # Store sample data
        max_temp = self.controller.get_max_temp('Delhi')
        self.assertEqual(max_temp, 35)
        
def test_get_avg_temp(self):
    # Test fetching average temperature
    store_weather_data('Delhi', 30, 25, 35, 'Clouds')  # Store sample data
    avg_temp = self.controller.get_avg_temp('Delhi')
    self.assertAlmostEqual(avg_temp, 30, places=2)  # Use assertAlmostEqual to allow for floating-point differences


if __name__ == '__main__':
    unittest.main()
