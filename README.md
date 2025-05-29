# Weather Prediction App 🌦️📊

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python-based weather forecasting application that uses linear regression to predict temperature, rainfall, humidity, wind speed, and atmospheric pressure trends.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Format](#data-format)

## Features ✨
- **7-Day Weather Forecast** for:
  - Temperature (°C)
  - Rainfall (mm)
  - Humidity (%)
  - Wind Speed (km/h)
  - Atmospheric Pressure (hPa)
- **Interactive Command Line Interface**
- **Data Visualization** (14-day historical trends)
- **Statistical Analysis** (mean, min, max, std. deviation)
- **CSV Data Support**

## Installation 💻

1. Clone the repository:
bash
git clone https://github.com/yourusername/WeatherPredictionApp.git
cd WeatherPredictionApp
2. Install dependencies:
bash
pip install -r requirements.txt


## Usage 🚀

Run the application:
bash
python weather_app.py


**Menu Options**:
1. Next Week's Weather Forecast
2. Show Temperature Trend
3. Show Rainfall Trend
4. Show Humidity Trend
5. Show Wind Speed Trend
6. Show Pressure Trend
7. Show Basic Statistics
8. Exit


## Data Format 📋
The application expects a CSV file with these columns (sample provided):
csv
Temp9am,Temp3pm,Rainfall,Humidity9am,Humidity3pm,WindSpeed9am,WindSpeed3pm,Pressure9am,Pressure3pm
22.1,24.5,0.0,68,65,12,15,1015,1013

## How It Works ⚙️
1. Uses **linear regression** on last 7 days' data
2. Implements **hierarchical inheritance**:
   - Parent class: `WeatherPredictor` (base logic)
   - Child classes: `TemperatureTrend`, `RainfallTrend`, etc.
3. Visualizations using `matplotlib`

