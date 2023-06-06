import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# OpenWeatherMap API key
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

# Home route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Weather route
@app.route('/weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(url).json()
    
    if response['cod'] == 200:
        weather_data = {
            'location': response['name'],
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'humidity': response['main']['humidity'],
            'wind_speed': response['wind']['speed'],
        }
        return render_template('index.html', weather=weather_data)
    else:
        error_message = f"Error: {response['message']}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
