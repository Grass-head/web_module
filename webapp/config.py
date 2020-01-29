from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "d24e065bedb248e580195527190512"
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db') 

SECRET_KEY = "kefyhrehvn%kfcpseur67ewqe76sdoiwyed52"
REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False
