from flask import Flask, request
import requests

app = Flask(__name__)

city_coords = {
    "mexico": {'lat': 19.42847, 'lon': -99.12766},
    "monterrey": {'lat': 25.7714, 'lon': -100.309},
    "guadalajara": {'lat': 20.6736, 'lon': -103.344}
}

def get_lon_lat_weather(lon,lat):
    API_key = "816ea02da816af5fa177ca5ef6321c5c"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"  
    return requests.get(url).json()

def get_city_weather(city):
    city_name_coords = city_coords[city.lower()]
    print(city_name_coords)
    return get_lon_lat_weather(city_name_coords['lon'], city_name_coords['lat'])

@app.route("/weather")
def get_weather():
    city = request.args.get('city_name')
    return get_city_weather(city)

app.run(debug=True)