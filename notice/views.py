from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Notice
from accounts.models import Ward

def index(request):
	user = request.user
	ward = Ward.objects.all().filter(user=user)[0]
	events = Notice.objects.all().filter(publishing_location__in = ward.wards.all()).distinct()
	return render(request, 'notice/index.html', {'events': events})

def detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    user = request.user
    ward = Ward.objects.all().filter(user=user)[0]
    events = Notice.objects.all().filter(publishing_location__in = ward.wards.all()).distinct()
    return render(request, 'notice/detail.html', {'event': notice, 'events': events})