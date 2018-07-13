from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
import datetime
from request.models import RequestForm, Request, Requested, Point, PointForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json

r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAErtMcrKRMr_l5ICtZnx3mmk27MvDdyWY")
j = r.json()
lat = j['location']['lat']
lon = j['location']['lng']

def home(request):
    return render(request, 'request/home.html', {})

def index(request):
    requests = Point.objects.all()
    return render(request, 'request/index.html', {'requests': requests, 'lat':lat, 'lng':lon})
def detail(request, request_id):
    event = get_object_or_404(Point, pk=request_id)
    return render(request, 'request/detail.html', {'event': event})
@login_required
def create(request, point_id):
    p = Point.objects.all().filter(id=point_id)[0]
    if request.method == "POST":
        form = PointForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('date') < datetime.date.today():
                return render(request, 'request/create.html', {'form': form, 'message': 'date is in past'})
            else:
                post = form.save(commit=False)
                p.source = request.user.first_name
                p.date = datetime.datetime.combine(post.date,post.time)
                p.on = True
                p.save()
                return redirect('/request/index')
    else:
        form = PointForm()
    return render(request, 'request/create.html', {'form': form})
@login_required
def attend(request, event_id):
    event = get_object_or_404(Request, pk=event_id)
    user = request.user
    eid = event.id
    uid = user.id
    try:
        x = Requested.objects.filter(user__id=uid).filter(event__id=eid)[0]
        return render(request, 'request/detail.html', {'event': event, 'message': 'Already Done'})
    except:
        obj = Requested()
        obj.user = request.user
        obj.event = event
        obj.save()
        return render(request, 'request/detail.html', {'event': event, 'message': 'You are attending the event'})