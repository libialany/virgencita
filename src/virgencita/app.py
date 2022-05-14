from flask import Flask, render_template, request, url_for
import sys
import requests
import requests_cache
import logging
import random
import os
from geopy.geocoders import Nominatim
requests_cache.install_cache('virgencita', expire_after=1800)

def getLocation(client_ip):
    try:
        API_KEY_LOCATION=os.getenv('FORECAST_API_KEY_LOCATION')
        url=f'http://api.ipstack.com/{client_ip}?access_key={API_KEY_LOCATION}'
        headers={
        'accept':"application/json",
        'content-type':"application/json"
        }
        response= requests.request("GET",url,headers=headers)
        respond= response.json()     
        lat = round(respond['latitude']*1000+0.5)/1000
        lon = round(respond['longitude']*1000+0.5)/1000        


    except BaseException:
        lat = '-34.6037'
        lon = '-58.3816'
        pass
    print('Lat/Lon: ' + str(lat) + ', ' + str(lon), file=sys.stdout)
    sys.stdout.flush()
    return(lat, lon)


def getCity(coords):
    try:
        geolocator = Nominatim(user_agent="getcoldinLaPaz")
        location = geolocator.reverse(f"{coords[0]}, {coords[1]}")
        info=location.raw['address']
        city = info['city']
        district= info['city_district']  
    except BaseException:
        city = 'Buenos Aires'
        pass
    print('City: ' + city, file=sys.stdout)
    sys.stdout.flush()
    return(city)




def getForecast(coords):
    API_KEY_WEATHER=os.getenv('FORECAST_API_KEY_WEATHER')
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&appid={API_KEY_WEATHER}')
    #print('Is cached: ' + str(r.from_cache) + '\n', file=sys.stdout)
    sys.stdout.flush()
    data = r.json()
    return(data)


def getHumidity(forecast):
    humidity = forecast['main']['humidity']
    # OpenWeather free has no Precipitation
    return humidity


def createApp():
    app = Flask(__name__)
    app.logger.disabled = False
    log = logging.getLogger('werkzeug')
    log.disabled = True
    @app.route('/')
    def show_index():
        client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        print('Client IP: ' + str(client_ip), file=sys.stdout)
        sys.stdout.flush()
        coords = getLocation(client_ip)
        forecast = getForecast(coords)
        return render_template("index.html",probability=getHumidity(forecast),geocity=getCity(coords))
    return app
