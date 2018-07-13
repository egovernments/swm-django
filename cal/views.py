from django.shortcuts import render
import calendar
import datetime, requests,json
from datetime import timedelta
import dateutil.parser

# Create your views here.
def index(request):
    return render(request, 'cal/index.html', {})

def wcal(request):
        send_url = 'http://freegeoip.net/json'
        r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAErtMcrKRMr_l5ICtZnx3mmk27MvDdyWY")
        j = r.json()
        lat = j['location']['lat']
        lon = j['location']['lng']
        s1 = "http://api.openweathermap.org/data/2.5/forecast?lat="
        s2 = str(lat)
        s3 = "&lon="
        s4 = str(lon)
        s5 = "&appid="
        s6 = "22633ebfc9373698feb160284f68cbbb"
        final = s1+s2+s3+s4+s5+s6
        r = requests.get(final)
        x = r.json()
        htmlcal = calendar.HTMLCalendar(calendar.MONDAY)
        month = datetime.datetime.now().strftime("%m")
        year = datetime.datetime.now().strftime("%y")
        day = datetime.datetime.now().strftime("%d")
        d = int(day)
        m = int(month)
        y = 2000+int(year)
        hcal = htmlcal.formatmonth(y, m)
        for ab in range(0,5):
            day = str(d)
            hcal = hcal.replace(">"+day+"<",">"+" <img src=http://openweathermap.org/img/w/"+x['list'][ab]['weather'][0]['icon']+".png style='widht:29px'><br></br>"+day+"<")
            d = d+1
        icon0 = "<img src=http://openweathermap.org/img/w/"+x['list'][0]['weather'][0]['icon']+".png style='widht:29px'>"
        icon1 = "<img src=http://openweathermap.org/img/w/"+x['list'][1]['weather'][0]['icon']+".png style='widht:29px'>"
        icon2 = "<img src=http://openweathermap.org/img/w/"+x['list'][2]['weather'][0]['icon']+".png style='widht:29px'>"
        icon3 = "<img src=http://openweathermap.org/img/w/"+x['list'][3]['weather'][0]['icon']+".png style='widht:29px'>"
        icon4 = "<img src=http://openweathermap.org/img/w/"+x['list'][4]['weather'][0]['icon']+".png style='widht:29px'>"
        x = datetime.datetime.now()
        days = ["mon","tue","wed","thu","fri","sat","sun"]
        daysdisp = []
        datedisp = []
        for ab in range(0,5):
            datedisp.append( str(dateutil.parser.parse(str(x-timedelta(days=-ab))).date()))
            daysdisp.append( days[(x-timedelta(days=-ab)).weekday()] )
        print(daysdisp)
        print(datedisp)
        return render(request, 'cal/wcal.html', { 'cal' : hcal , 'icon0': icon0, 'icon1': icon1, 'icon2': icon2, 'icon3': icon3, 'icon4':icon4, 'days': daysdisp, 'dates':datedisp})
