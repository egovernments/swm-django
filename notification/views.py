from django.shortcuts import render
#from weather import Weather, Unit
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import requests
import json
from decimal import Decimal
import time
from datetime import timedelta
import dateutil.parser
import datetime

# Create your views here.
def ind(request):
    r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAErtMcrKRMr_l5ICtZnx3mmk27MvDdyWY")
    j = r.json()
    lat = j['location']['lat']
    lon = j['location']['lng']
    l_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(lat) + "," + str(lon) + "&key=AIzaSyAErtMcrKRMr_l5ICtZnx3mmk27MvDdyWY"
    print(l_url)
    l_request = requests.get(l_url)
    l_json = l_request.json()

    full_name = l_json['results'][0]['address_components'][3]['long_name']
    return render(request, 'notification/weather.html', {'lat': lat, 'lon': lon, 'name': full_name})
def index(request):
    # r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAErtMcrKRMr_l5ICtZnx3mmk27MvDdyWY")
    # j = r.json()
    # lat = j['location']['lat']
    # lon = j['location']['lng']
    #
    # f_url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + key + apistring + "details=true"
    # print(f_url)
    # f_request = requests.get(f_url)
    # f_json = f_request.json()
    #
    # h_url = "http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/" + key + apistring + "details=true"
    # print(h_url)
    # h_request = requests.get(h_url)
    # h_json = h_request.json()

    # s1 = "api.openweathermap.org/data/2.5/weather?lat="
    # s2 = str(lat)
    # s3 = "&lon="
    # s4 = str(lon)
    # s5 = "&appid="
    # s6 = "22633ebfc9373698feb160284f68cbbb"
    # final = s1+s2+s3+s4+s5+s6
    # s0 = "http://"
    # final = s0+final
    # r = requests.get(final)
    # x = r.json()
    # am = Decimal(x['main']['temp_max']-273)
    # pm = Decimal(x['main']['temp_min']-273)
    # r1 = round(am,1)
    # r2 = round(pm,1)
    # print(x['name'])
    # context = {
    #  'temp_max': r1,
    #             'temp_min': r2,
    #             'am' : time.strftime('%H:%M', time.gmtime(x['sys']['sunrise'])),
    #             'pm' : time.strftime('%H:%M', time.gmtime(x['sys']['sunset'])),
    #             'name' : x['name'],
    #             'condition' : x['weather'][0]['description']
    #            }
    # s1 = "http://api.openweathermap.org/data/2.5/forecast?lat="
    # s2 = str(lat)
    # print(s2)
    # s3 = "&lon="
    # s4 = str(lon)
    # print(s4)
    # s5 = "&appid="
    # s6 = "22633ebfc9373698feb160284f68cbbb"
    # final = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/2875040?apikey=q8s7DARezTl9xhNbQ0VahwhH7gyXKhDO&details=true"
    # r = requests.get(final)
    # x = r.json()
    # if x['DailyForecasts'][0]['Day']['Icon'] < 10 :
    #     icon0 = "<img src=https://developer.accuweather.com/sites/default/files/0"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # else :
    #     icon0 = "<img src=https://developer.accuweather.com/sites/default/files/"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # if x['DailyForecasts'][1]['Day']['Icon'] < 10 :
    #     icon1 = "<img src=https://developer.accuweather.com/sites/default/files/0"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # else :
    #     icon1 = "<img src=https://developer.accuweather.com/sites/default/files/"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # if x['DailyForecasts'][2]['Day']['Icon'] < 10 :
    #     icon2 = "<img src=https://developer.accuweather.com/sites/default/files/0"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # else :
    #     icon2 = "<img src=https://developer.accuweather.com/sites/default/files/"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # if x['DailyForecasts'][3]['Day']['Icon'] < 10 :
    #     icon3 = "<img src=https://developer.accuweather.com/sites/default/files/0"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # else :
    #     icon3 = "<img src=https://developer.accuweather.com/sites/default/files/"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # if x['DailyForecasts'][4]['Day']['Icon'] < 10 :
    #     icon4 = "<img src=https://developer.accuweather.com/sites/default/files/0"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # else :
    #     icon4 = "<img src=https://developer.accuweather.com/sites/default/files/"+str(x['DailyForecasts'][0]['Day']['Icon'])+"-s.png style='widht:29px;float:right;'>"
    # x = datetime.datetime.now()
    # days = ["mon","tue","wed","thu","fri","sat","sun"]
    # daysdisp = []
    # datedisp = []
    # for ab in range(0,5):
    #     datedisp.append( str(dateutil.parser.parse(str(x-timedelta(days=-ab))).date()))
    #     daysdisp.append( days[(x-timedelta(days=-ab)).weekday()] )
    # print(daysdisp)
    # print(datedisp)
    # dict2 = {'icon0': icon0, 'icon1': icon1, 'icon2': icon2, 'icon3': icon3, 'icon4':icon4, 'days': daysdisp, 'dates':datedisp}
    return HttpResponse("Hi")