# weather_api/api.py
import os
import requests
from datetime import datetime 
import getpass
import subprocess

def update_api_key(api_name: str) -> str:
    """Prompt the user for the API key if it's not set in the environment."""
    api_key=getpass.getpass(f"Please enter your {api_name}: ")
    subprocess.run(['setx', api_name, api_key], check=True)
    print(f"Your {api_name} has been stored in the environment variable.")
    return api_key

def get_api_key(api_name: str) -> str:
    """Prompt the user for the API key if it's not set in the environment."""
    api_key = os.getenv(api_name)
    if not api_key:
        api_key=getpass.getpass(f"Please enter your {api_name}: ")
        subprocess.run(['setx', api_name, api_key], check=True)
        print(f"Your {api_name} has been stored in the environment variable.")
        print("restart the command prompt to use these environment variables")
    return api_key

# Get API keys for OpenWeather and Google Maps
OPENWEATHER_API_KEY = get_api_key("OPENWEATHERMAPAPIKEY")
GOOGLE_GEOCODE_API_KEY = get_api_key("GEOCODEAPIKEY")

def get_lat_lon(zip_code: str) -> tuple:
    """Fetch latitude and longitude for a given zip code using Google Geocoding API."""
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={zip_code}&key={GOOGLE_GEOCODE_API_KEY}"
    geocode_response = requests.get(geocode_url)
    if geocode_response.status_code != 200:
        print("Possible reasons for the error: 1. Incorrect API Key. 2. API request limit exceeded. 3. Invalid ZipCode.")
        raise Exception(f"Error fetching geocode for {zip_code}: {geocode_response.text}")
    geocode_data = geocode_response.json()
    if geocode_data['status'] != "OK":
        print("Possible reasons for the error: 1. Incorrect API Key. 2. API request limit exceeded. 3. Invalid ZipCode.")
        raise Exception(f"Error in geocode response: {geocode_data['status']}")

    # Extract latitude and longitude
    location = geocode_data['results'][0]['geometry']['location']
    return location['lat'], location['lng']

def get_weather(zip_code: str) -> dict:
    """ Fetch weather data using the latitude and longitude obtained from Google Geocoding API."""
    lat, lon = get_lat_lon(zip_code)
    
    # Fetch weather data using lat and long
     
    # Get today's date in YYYY-MM-DD format
    date = datetime.now().strftime('%Y-%m-%d')

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=imperial"
    weather_response = requests.get(weather_url)
    if weather_response.status_code != 200:
        print("Possible reasons for the error: 1. Incorrect API Key. 2. API request limit exceeded.")
        raise Exception(f"Error fetching weather data: {weather_response.text}")
    
    return weather_response.json()

# Example usage
if __name__ == "__main__":
    zip_code = input("Enter the zip code: ")
    try:
        weather_data = get_weather(zip_code)
        print(weather_data)
    except Exception as e:
        print(e)
