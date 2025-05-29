# Import required libraries
import pandas as pd                        # For reading and manipulating tabular data (CSV)
import matplotlib.pyplot as plt            # For plotting graphs and charts
import numpy as np                         # For mathematical operations and linear regression
from datetime import datetime, timedelta   # For handling date and time operations

# This program uses hierarchical inheritance, 
# where multiple child classes (e.g., Temp, Rainfall)
# inherit from a single parent class (WeatherPredictor).

# ------- Class for Weather Prediction --------
class WeatherPredictor:
    
    # Constructor that takes the dataset (DataFrame) as input
    def __init__ (self, data):
        self.data = data  # Store the passed-in data as an instance variable

    # Function to predict the next week's data for a given weather attribute
    def predictor(self, weather):  # 'weather' is the name of the column to analyze
        """
        This function uses the last 7 days of data to fit a linear trend line
        and predicts the next 7 days using that line.
        """
        recent_weather = self.data.tail(7)[weather]  # Extract last 7 values of the specified column
        days = np.arange(1, 8)                       # Create an array [1, 2, 3, 4, 5, 6] for x-axis (days)

        

        # Fit a linear polynomial (y = mx + c) to recent weather data
        slope, intercept = np.polyfit(days, recent_weather, 1)

        # Generate future day numbers [8, 9, ..., 14] for prediction
        future_days = list(range(8, 15))

        # Calculate predictions using the linear model
        predicted_weather = [slope * day + intercept for day in future_days]

        return predicted_weather  # Return the 7 predicted values as a list


# ------- Child classes for specific weather attributes --------

# Class for Temperature predictions and visualizations
class TemperatureTrend(WeatherPredictor):
    def get_prediction(self):
        return self.predictor('Temp3pm')  # Predict using 3PM temperature data
    
    def plot(self):
       # Get the last 14 days of data (assuming 'Date' is a column in your data)
        last_14_days = self.data.tail(14)

        # Plot both 3PM and 9AM temperature data for the last 14 days
        plt.plot(last_14_days['Temp3pm'], label='3PM Temp')  # Plot 3PM temps
        plt.plot(last_14_days['Temp9am'], label='9AM Temp')  # Plot 9AM temps
        plt.title("Temperature Trend (Past 14 Days)")        # Chart title
        plt.xlabel("Days")                                   # X-axis label
        plt.ylabel("Temperature (°C)")                       # Y-axis label
        plt.legend()                                         # Show legend
        plt.grid(True)                                       # Show gridlines
        plt.tight_layout()                                   # Adjust layout
        plt.show()                                           # Display the plot

# Class for Rainfall predictions and visualizations
class RainfallTrend(WeatherPredictor):
    def get_prediction(self):
        return self.predictor('Rainfall')  # Predict using rainfall data
    
    def plot(self):
        # Get the last 14 days of data
        last_14_days = self.data.tail(14)

        # Plot rainfall data over time
        plt.plot(last_14_days['Rainfall'], label='Rainfall (mm)', color='blue')
        plt.title("Rainfall Trend (Past 14 Days)")
        plt.xlabel("Days")
        plt.ylabel("Rainfall (mm)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Class for Humidity predictions and visualizations
class HumidityTrend(WeatherPredictor):
    def get_prediction(self):
        return self.predictor('Humidity3pm')  # Predict using 3PM humidity data
    
    def plot(self):
        # Get the last 14 days of data
        last_14_days = self.data.tail(14)

        # Plot both 9AM and 3PM humidity levels
        plt.plot(last_14_days['Humidity9am'], label='9AM Humidity', color='green')
        plt.plot(last_14_days['Humidity3pm'], label='3PM Humidity', color='lime')
        plt.title("Humidity Trend (Past 14 Days)")
        plt.xlabel("Days")
        plt.ylabel("Humidity (%)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()    

# Class for Wind Speed predictions and visualizations
class WindSpeedTrend(WeatherPredictor):
    def get_prediction(self):
        return self.predictor('WindSpeed3pm')  # Predict using 3PM wind speed data

    def plot(self):
        # Get the last 14 days of data
        last_14_days = self.data.tail(14)

        # Plot wind speed at 9AM and 3PM
        plt.plot(last_14_days['WindSpeed9am'], label='9AM Wind Speed', color='purple')
        plt.plot(last_14_days['WindSpeed3pm'], label='3PM Wind Speed', color='violet')
        plt.title("Wind Speed Trend (Past 14 Days)")
        plt.xlabel("Days")
        plt.ylabel("Wind Speed (km/h)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Class for Atmospheric Pressure predictions and visualizations
class PressureTrend(WeatherPredictor):
    def get_prediction(self):
        return self.predictor('Pressure3pm')  # Predict using 3PM pressure data
    
    def plot(self):
        # Get the last 14 days of data
        last_14_days = self.data.tail(14)

        # Plot atmospheric pressure at 9AM and 3PM
        plt.plot(last_14_days['Pressure9am'], label='9AM Pressure', color='orange')
        plt.plot(last_14_days['Pressure3pm'], label='3PM Pressure', color='darkorange')
        plt.title("Atmospheric Pressure Trend (Past 14 Days)")
        plt.xlabel("Days")
        plt.ylabel("Pressure (hPa)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# ------- WeatherApp class: User interface & controller --------
class WeatherApp:
    def __init__(self, data):
        WeatherPredictor.__init__(self, data)  # Initialize base class with data

    def predict_next_week(self):
        """
        Uses each weather trend class to get 7-day predictions
        and prints the forecast in a readable format
        """
        today = datetime.today()  # Get current date

        # Create instances of each trend class and get their predictions
        temp_pred = TemperatureTrend(self.data).get_prediction()
        rain_pred = RainfallTrend(self.data).get_prediction()
        hum_pred = HumidityTrend(self.data).get_prediction()
        wind_pred = WindSpeedTrend(self.data).get_prediction()
        press_pred = PressureTrend(self.data).get_prediction()

        print("\n--- Weather Forecast for Next Week ---\n")
        for i in range(7):  # Loop through each day of the week
            day = today + timedelta(days=i+1)  # Calculate the date
            day_name = "Tomorrow" if i == 0 else day.strftime('%A')  # Label for the day

            # Print the forecast values for each parameter
            print(f"{day_name} ({day.strftime('%d-%m-%Y')}):")
            print(f"  Temperature: {temp_pred[i]:.1f}°C" if temp_pred[i] is not None else "  Temperature: N/A")
            print(f"  Rainfall: {rain_pred[i]:.1f} mm" if rain_pred[i] is not None else "  Rainfall: N/A")
            print(f"  Humidity: {hum_pred[i]:.1f}%" if hum_pred[i] is not None else "  Humidity: N/A")
            print(f"  Wind Speed: {wind_pred[i]:.1f} km/h" if wind_pred[i] is not None else "  Wind Speed: N/A")
            print(f"  Pressure: {press_pred[i]:.1f} hPa\n" if press_pred[i] is not None else "  Pressure: N/A\n")

    # Menu to interact with the user
    def menu(self):
        while True:
            # Display the main menu
            print("\nWelcome to WeatherCheck!")
            print("Weather App Menu")
            print("1. Next Week's Weather")
            print("2. Show Temperature Trend")
            print("3. Show Rainfall Trend")
            print("4. Show Humidity Trend")
            print("5. Show Wind Speed Trend")
            print("6. Show Pressure Trend")
            print("7. Show Basic Statistics")
            print("8. Exit")

            choice = input("Enter your choice: ")  # Take user input

            # Call appropriate method based on user choice
            if choice == '1':
                self.predict_next_week()
            elif choice == '2':
                print("Generating Temperature Trend...")
                TemperatureTrend(self.data).plot()
            elif choice == '3':
                print("Generating RainFall Trend...")
                RainfallTrend(self.data).plot()
            elif choice == '4':
                print("Generating Humidity Trend...")
                HumidityTrend(self.data).plot()
            elif choice == '5':
                print("Generating Wind Speed Trend...")
                WindSpeedTrend(self.data).plot()
            elif choice == '6':
                print("Generating Pressure Trend...")
                PressureTrend(self.data).plot()
            elif choice == '7':
                # Show descriptive statistics (mean, std, min, max, etc.)
                print("\nBasic Weather Statistics:")
                print(self.data.describe())
            elif choice == '8':
                print("Exiting Weather App. Stay cozy! 🌦️")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")


# ------- Load CSV and Launch the App --------

# Specify path to the CSV file
file_path = r'sample_weather.csv'

# Read the CSV into a pandas DataFrame
df = pd.read_csv(file_path)

# Create WeatherApp instance with the loaded data
app = WeatherApp(df)

app.menu()
