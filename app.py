from flask import Flask, render_template, request
import requests
from weather_service import WeatherService

app = Flask(__name__)
weather_service = WeatherService()

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/weather')
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    weather_data = weather_service.fetch_weather(lat, lon)
    return weather_data

if __name__ == '__main__':
    app.run(debug=True)
