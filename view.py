import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Function to display the weather data in the UI
def display_weather_ui(controller, weather_data):
    root = tk.Tk()
    root.title(f"Weather Data for {weather_data['city']}")
    root.geometry("600x600")

    # Display the city and current temperature
    city_label = tk.Label(root, text=f"{weather_data['city']}", font=("Arial", 24))
    city_label.pack(pady=10)

    temp_label = tk.Label(root, text=f"{weather_data['temp']}°C", font=("Arial", 32, "bold"))
    temp_label.pack(pady=10)

    condition_label = tk.Label(root, text=f"Condition: {weather_data['condition']}", font=("Arial", 16))
    condition_label.pack(pady=5)

    # Display other data like humidity, pressure, wind speed
    humidity_label = tk.Label(root, text=f"Humidity: {weather_data['humidity']}%", font=("Arial", 12))
    humidity_label.pack(pady=5)

    pressure_label = tk.Label(root, text=f"Pressure: {weather_data['pressure']} mmHg", font=("Arial", 12))
    pressure_label.pack(pady=5)

    wind_label = tk.Label(root, text=f"Wind: {weather_data['wind']} m/s", font=("Arial", 12))
    wind_label.pack(pady=5)

    # Min, Max, Avg temperature display
    min_temp = controller.get_min_temp(weather_data['city'])
    max_temp = controller.get_max_temp(weather_data['city'])
    avg_temp = controller.get_avg_temp(weather_data['city'])

    min_label = tk.Label(root, text=f"Min: {min_temp}°C  Max: {max_temp}°C  Avg: {avg_temp}°C", font=("Arial", 12))
    min_label.pack(pady=10)

    # Create bar chart for temperature overview
    figure = plt.Figure(figsize=(5, 3), dpi=100)
    ax = figure.add_subplot(111)

    temps = [min_temp, avg_temp, max_temp]
    ax.bar(['Min Temp', 'Avg Temp', 'Max Temp'], temps, color=['blue', 'orange', 'red'])

    ax.set_title('Temperature Overview')
    ax.set_ylabel('Temperature (°C)')

    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().pack()

    root.mainloop()

# Function to display the main UI with city selection
def show_main_ui(controller):
    root = tk.Tk()
    root.title("Weather Data")
    root.geometry("300x500")

    label = tk.Label(root, text="Select a city to view weather", font=("Arial", 14))
    label.pack(pady=20)

    city_var = tk.StringVar()
    city_var.set(controller.get_cities()[0])

    city_menu = ttk.OptionMenu(root, city_var, *controller.get_cities())
    city_menu.pack(pady=20)

    def on_city_selected():
        city = city_var.get()
        controller.fetch_and_display_weather(city)

    show_button = tk.Button(root, text="Show Weather", command=on_city_selected)
    show_button.pack(pady=10)

    root.mainloop()
