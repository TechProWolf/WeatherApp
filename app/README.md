# WeatherApp

WeatherApp is a weather application that provides real-time weather updates for a given location.

## Features

- Get real-time weather updates for any location
- Display current temperature, weather conditions, humidity, wind speed, and more
- Option to view hourly and daily forecasts
- Search for a specific location or use the user's current location
- Option to save favorite locations for quick access
- Responsive design for optimal user experience on different devices

## Installation

1. Clone the project repository:

 $ git clone https://github.com/TechProWolf/WeatherApp.git

2. Navigate to the project directory:
 
 $ cd WeatherApp

3. Install the required dependencies:

 $ pip install -r requirements.txt

4. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) by creating an account and generating an API key.

5. Rename the `.env.example` file to `.env` and replace `YOUR_API_KEY` with your OpenWeatherMap API key.

## Usage

1. Start the Flask development server:
 
 $ flask run
 
2. Open a web browser and visit `http://localhost:5000` to access the WeatherApp.

3. Enter a location in the search bar or use the "Use My Location" button to get weather updates for that location.

4. Explore the different sections of the application to view current weather conditions, hourly and daily forecasts, and save favorite locations.

## Contributing

Contributions to the WeatherApp project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the project repository on GitHub.

2. Create a new branch from the main branch:
 
  $ git checkout -b feature/my-feature

3. Make your changes and commit them following the Udacity Commit Message Style Guide.

4. Push your changes to your forked repository.

5. Create a pull request to the main repository, providing a clear description of the changes you've made.
