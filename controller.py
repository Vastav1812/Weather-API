import model
import view

class WeatherController:
    def __init__(self):
        self.cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

    def get_cities(self):
        return self.cities

    def fetch_and_display_weather(self, city):
        weather_data = model.fetch_weather_data(city)
        if weather_data:
            model.store_weather_data(city, weather_data['temp'], weather_data['temp'], weather_data['temp'], weather_data['condition'])
            view.display_weather_ui(self, weather_data)

    # Methods to get weather data from model
    def get_min_temp(self, city):
        data = model.get_weather_summary(city)
        if data:
            return data[0][4]  # Min temperature
        return 0

    def get_max_temp(self, city):
        data = model.get_weather_summary(city)
        if data:
            return data[0][3]  # Max temperature
        return 0

    def get_avg_temp(self, city):
        data = model.get_weather_summary(city)
        if data:
            return data[0][2]  # Avg temperature
        return 0
