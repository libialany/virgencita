# Virgencita del tiempo climático

[![Build Status](https://travis-ci.org/reynico/virgencita.svg?branch=master)](https://travis-ci.org/reynico/virgencita)

__Note__  I just made some modifications to make it work.

### Setup
- <del> Download [GeoIP city location database](https://dev.maxmind.com/geoip/geoip2/geolite2/)</del>
- <del>Uncompress and rename to `geo.mmdb`</del>
### Manually

- Set in terminal with  `export FORECAST_API_KEY_LOCATION
=...`

- Set in terminal with `export FORECAST_API_KEY_LOCATION
=...`


- Install the Python requirements `make install`
- Run with `python3 ./src/main.py`

### Dockerfile

- Set your `FORECAST_API_KEY_WEATHER`. Create an .env file.
- Set your `FORECAST_API_KEY_LOCATION`. Create an .env file.

## How to test locally

<del> Requires 18.02.0+</del>
 
`docker-compose up` 

<h2> Running unit tests </h2>

- <del> Run `make test`</del>

<h2> Run lint </h2>

- <del> Run `make lint` </del>


