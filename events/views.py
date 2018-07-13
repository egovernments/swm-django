from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Event, Attended
from django.contrib.auth.decorators import login_required
from accounts.models import Ward

# Create your views here.
def index(request):
    user = request.user
    ward = Ward.objects.all().filter(user = user)[0]
    events = Event.objects.all().filter(publishing_location__in = ward.wards.all()).distinct()
    return render(request, 'events/index.html', {'events': events})
def detail(request, event_id):
    user = request.user
    ward = Ward.objects.all().filter(user = user)[0]
    events = Event.objects.all().filter(publishing_location__in = ward.wards.all()).distinct()
    event = get_object_or_404(Event, pk=event_id)
    message = "w3-green"
    return render(request, 'events/detail.html', {'event': event, 'events': events, 'messange' : message})

@login_required
def attend(request, event_id):
    events = Event.objects.all()
    event = get_object_or_404(Event, pk=event_id)
    user = request.user
    eid = event.id
    uid = user.id
    try:
        x = Attended.objects.filter(user__id=uid).filter(event__id=eid)[0]
        message = "w3-blue"
    except:
        obj = Attended()
        obj.user = request.user
        obj.event = event
        obj.save()
        message = "w3-blue"
    return render(request, 'events/detail.html', {'event': event, 'message': message, 'events': events})
