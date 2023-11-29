
# Flask Weather Application

This repository contains a Flask-based web application that provides real-time weather information. It utilizes the OpenWeather API to fetch the current temperature in both Celsius and Fahrenheit, along with the location name based on the user's geographical coordinates.

## Features

- **Geolocation Support**: Automatically fetches the user's current location.
- **Weather Data**: Displays the temperature in Celsius and Fahrenheit and the name of the location.
- **Responsive Design**: Simple and responsive user interface.

## Installation

To run this application, you'll need Python and Flask installed on your machine.

1. **Clone the Repository**

   ```bash
   git clone [repository URL]
   cd [repository folder]
   ```

2. **Install Dependencies**

   This application requires Flask and requests. You can install them using pip:

   ```bash
   pip install Flask requests python-dotenv
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your OpenWeather API key:

   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

4. **Run the Application**

   ```bash
   python app.py
   ```

   The application will start running on `http://localhost:5000`.

## Usage

Navigate to `http://localhost:5000` in your web browser. The application will automatically request your location and display the current weather data.

## File Structure

- `app.py`: Main application file where Flask routes are defined.
- `weather_service.py`: Contains the `WeatherService` class that handles API requests.
- `templates/`: Folder containing HTML templates.
  - `index.html`: Front-end HTML structure.

## Contributing

Feel free to fork this project, make changes, and open a pull request to contribute. Contributions, issues, and feature requests are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
