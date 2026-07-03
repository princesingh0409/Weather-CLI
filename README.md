# Weather CLI Application

A simple Command Line Interface (CLI) Weather Application built using Python and the OpenWeather API.

## Features

- Get real-time weather information
- Search weather by city name
- Displays:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Pressure
  - Wind Speed
  - Weather Description
- Handles invalid city names
- Simple and user-friendly CLI

## Technologies Used

- Python
- Requests Library
- OpenWeather API

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/princesingh0409/Weather-CLI.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open `weather.py` and replace:

   ```python
   API_KEY = "YOUR_API_KEY"
   ```

   with your own OpenWeather API key.

4. Run the application:

   ```bash
   python weather.py
   ```

## Project Structure

```
Weather-CLI/
│── weather.py
│── requirements.txt
└── README.md
```

## Author

**Priyanshu Singh**