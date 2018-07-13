from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'nearby/index.html', {})
def type(request, type):
    api_key = 'AIzaSyDxAcd3yEl62iecQKuiDVJpgf6L_tS-nzU'
    geolocation_request = requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key=' + api_key)
    geolocation_json = geolocation_request.json()
    lat = geolocation_json['location']['lat']
    lng = geolocation_json['location']['lng']
    return render(request, 'nearby/type.html', {'type': type, 'lat': lat, 'lng': lng, 'YOUR_API_KEY' : api_key})

def maps(request, type):
	return render(request, 'nearby/maps.html', {'type': type})