from flask import Flask, render_template, request, url_for
from forecastiopy import *
import geoip2.database
import os

app = Flask(__name__)
reader = geoip2.database.Reader('geo.mmdb')

@app.route('/')
def show_index():
    client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    client_response = reader.city(client_ip)
    apiKey = os.environ['FORECAST_API_KEY']
    lat = str(client_response.location.latitude)
    lon = str(client_response.location.longitude)
    fio = ForecastIO.ForecastIO(apiKey, latitude=lat, longitude=lon)
    current = FIOCurrently.FIOCurrently(fio)
    return render_template("index.html", probabilidad = int(current.precipProbability*100))

if __name__ == '__main__':
    app.run()
