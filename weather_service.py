import os
from dotenv import load_dotenv
import requests

load_dotenv()

class WeatherService:

    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
    
    def fetch_weather(self, lat, lon):
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        temp_c = data['main']['temp']
        temp_f = temp_c * 9/5 + 32
        location_name = data['name'] 
        return {'temperature_c': temp_c, 'temperature_f': temp_f, 'location': location_name}