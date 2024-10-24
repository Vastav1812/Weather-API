# Weather Monitoring System with Real-Time Data Processing

## Overview

This project implements a weather monitoring system using the OpenWeatherMap API to collect weather data for major cities in India. The system collects real-time weather information and provides insights through rollups and aggregates. It also includes alerting features based on user-defined thresholds.

## Features

- **Real-time Data Collection**: Continuously retrieves weather data for cities (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) at configurable intervals.
- **Daily Weather Summary**: Calculates daily aggregates like average, maximum, and minimum temperatures, along with the dominant weather condition.
- **Alerts**: User-configurable thresholds for temperature or specific weather conditions.
- **Data Visualization**: Displays weather trends with temperature graphs and UI components.

## API Integration

- **Data Source**: The system uses the OpenWeatherMap API. You will need an API key to access the data, which can be obtained for free by signing up on OpenWeatherMap.

### Parameters Collected:
- Main Weather Condition (e.g., Rain, Clear)
- Current Temperature (in °C)
- Perceived Temperature (in °C)
- Wind Speed, Humidity, and Pressure

## User Interface

The UI is built using Tkinter, featuring:
- A side panel for selecting cities to view detailed weather information.
- Weather details like temperature, condition, humidity, pressure, and wind speed.
- A graphical bar chart that visualizes minimum, average, and maximum temperatures for the selected city.

## System Architecture (MVC)

- **Model**: Handles data retrieval, processing, and database operations.
- **View**: Implements the user interface using Tkinter to display weather details and graphs.
- **Controller**: Manages the interaction between the view and model, including retrieving data from the model and updating the view.

## Rollups and Aggregates

- **Daily Weather Summary**:
  - Computes average, maximum, and minimum temperatures.
  - Determines the dominant weather condition for each day.
  - Stores daily summaries for further analysis.
  
- **Alerting System**:
  - Supports alert thresholds for temperature or specific weather conditions (e.g., alert if temperature exceeds 35°C).
  - Alerts can be displayed in the UI or integrated with an email notification system (optional).

## Running the Project

### Clone the Repository

```bash
git clone <[repository_url](https://github.com/Vastav1812/Weather-API---CONVIN/tree/main)>
cd Weather-API
```
### **Install Dependencies**
The project uses Python libraries including requests, Tkinter, and matplotlib. Install them using the requirements file:
```
bash
pip install -r requirements.txt
```
--- 

## **Example Usage**
-Display Weather for a City: Select a city from the left panel to display the current weather details, including conditions, temperature, humidity, etc.
-Alerts: Alerts can be configured for temperature exceeding user-specified values.

## **Directory Structure**
```
plaintext
Weather-API/
  ├── app.py                # Main application
  ├── model.py              # Model containing database interaction and data logic
  ├── view.py               # View for UI using Tkinter
  ├── controller.py         # Controller logic to manage interaction
  ├── config.json           # Configuration file (API key and thresholds)
  ├── requirements.txt      # Python dependencies
  ├── test_cases/           # Unit test files
  │   ├── test_model.py     # Tests for model
  │   ├── test_controller.py # Tests for controller
  └── daily_weather_log.txt  # Weather log with daily summaries
```
